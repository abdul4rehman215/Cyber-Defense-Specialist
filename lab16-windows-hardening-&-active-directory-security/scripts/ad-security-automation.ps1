#!/usr/bin/env pwsh

param(
    [string]$ConfigFile = "./configs/ad-config.json",
    [string]$LogFile = "./logs/ad-security.log"
)

function Write-SecurityLog {
    param([string]$Message, [string]$Level = "INFO")

    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    $entry = "[$timestamp] [$Level] $Message"

    Write-Host $entry
    Add-Content -Path $LogFile -Value $entry
}

function Test-PasswordPolicy {
    param($Policy)

    if ($Policy.min_length -lt 8) { return $false }
    if (-not $Policy.complexity) { return $false }
    if ($Policy.max_age -gt 365) { return $false }

    return $true
}

function Test-LockoutPolicy {
    param($Policy)

    if ($Policy.threshold -gt 10) { return $false }
    if ($Policy.duration -lt 15) { return $false }

    return $true
}

function Invoke-UserAudit {
    param($Users)

    $disabled = ($Users | Where-Object { -not $_.enabled }).Count
    $admins = ($Users | Where-Object { $_.role -like "*Admin*" }).Count
    $service = ($Users | Where-Object { $_.role -eq "Service" }).Count

    Write-SecurityLog "Disabled Accounts: $disabled"
    Write-SecurityLog "Admin Accounts: $admins"
    Write-SecurityLog "Service Accounts: $service"

    return @{
        Disabled = $disabled
        Admins = $admins
        ServiceAccounts = $service
    }
}

function New-SecurityRecommendations {
    param($Config)

    $recommendations = @()

    $adminCount = ($Config.users | Where-Object { $_.role -like "*Admin*" }).Count

    if ($adminCount -gt 2) {
        $recommendations += "Reduce excessive admin accounts."
    }

    $disabledAccounts = $Config.users | Where-Object { -not $_.enabled }
    if ($disabledAccounts.Count -gt 0) {
        $recommendations += "Review and remove unnecessary disabled accounts."
    }

    if (-not (Test-PasswordPolicy $Config.security_policies.password_policy)) {
        $recommendations += "Password policy does not meet minimum security standards."
    }

    return $recommendations
}

try {

    if (-not (Test-Path "./logs")) {
        New-Item -ItemType Directory -Path "./logs" | Out-Null
    }

    Write-SecurityLog "Starting AD Security Automation Script"

    $config = Get-Content $ConfigFile | ConvertFrom-Json

    $passwordValid = Test-PasswordPolicy $config.security_policies.password_policy
    $lockoutValid = Test-LockoutPolicy $config.security_policies.lockout_policy

    $userAudit = Invoke-UserAudit $config.users
    $recommendations = New-SecurityRecommendations $config

    $summary = @{
        Domain = $config.domain
        PasswordPolicyCompliant = $passwordValid
        LockoutPolicyCompliant = $lockoutValid
        UserAudit = $userAudit
        Recommendations = $recommendations
        GeneratedAt = Get-Date
    }

    $summary | ConvertTo-Json -Depth 5 | Out-File "./logs/security-summary.json"

    Write-SecurityLog "AD Security Automation completed successfully"

} catch {
    Write-SecurityLog "Error: $($_.Exception.Message)" "ERROR"
    exit 1
}
