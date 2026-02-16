#!/usr/bin/env pwsh

param(
    [string]$OutputDir = "./logs",
    [string]$ReportFile = "./logs/security-report.html"
)

function Get-ADSecurityStatus {

    $summaryFile = "$OutputDir/security-summary.json"

    if (-not (Test-Path $summaryFile)) {
        throw "AD security summary not found."
    }

    $data = Get-Content $summaryFile | ConvertFrom-Json

    $score = 0

    if ($data.PasswordPolicyCompliant) { $score += 40 }
    if ($data.LockoutPolicyCompliant) { $score += 30 }

    $adminPenalty = if ($data.UserAudit.Admins -gt 2) { 10 } else { 0 }
    $score += (30 - $adminPenalty)

    return @{
        Score = $score
        Details = $data
    }
}

function Get-RegistrySecurityStatus {

    $reportFile = "$OutputDir/registry-hardening-report.json"

    if (-not (Test-Path $reportFile)) {
        throw "Registry report not found."
    }

    $data = Get-Content $reportFile | ConvertFrom-Json

    return @{
        Score = $data.CompliancePercent
        Details = $data
    }
}

function Test-CriticalSecuritySettings {

    $alerts = @()

    $adData = Get-Content "$OutputDir/security-summary.json" | ConvertFrom-Json
    $regData = Get-Content "$OutputDir/registry-hardening-report.json" | ConvertFrom-Json

    if (-not $adData.PasswordPolicyCompliant) {
        $alerts += "Password policy is not compliant."
    }

    if (-not $adData.LockoutPolicyCompliant) {
        $alerts += "Lockout policy is not compliant."
    }

    foreach ($item in $regData.Results) {
        if (-not $item.Compliant) {
            $alerts += "Registry setting non-compliant: $($item.KeyPath)\$($item.ValueName)"
        }
    }

    return $alerts
}

function New-SecurityReport {
    param($ADStatus, $RegistryStatus, $Alerts)

    $overallScore = [math]::Round(($ADStatus.Score + $RegistryStatus.Score) / 2, 2)

    $recommendations = @()

    if ($overallScore -lt 70) {
        $recommendations += "Overall security posture is below acceptable threshold."
    }

    if ($Alerts.Count -gt 0) {
        $recommendations += "Immediate remediation required for critical alerts."
    }

    return @{
        ADScore = $ADStatus.Score
        RegistryScore = $RegistryStatus.Score
        OverallScore = $overallScore
        Alerts = $Alerts
        Recommendations = $recommendations
        GeneratedAt = Get-Date
    }
}

try {

    $adStatus = Get-ADSecurityStatus
    $registryStatus = Get-RegistrySecurityStatus
    $alerts = Test-CriticalSecuritySettings

    $report = New-SecurityReport $adStatus $registryStatus $alerts

    $report | ConvertTo-Json -Depth 6 | Out-File "$OutputDir/security-monitor-summary.json"

    Write-Host "Security monitoring completed successfully."
    Write-Host "Overall Security Score: $($report.OverallScore)%"

} catch {
    Write-Host "Monitor error: $($_.Exception.Message)"
    exit 1
}
