#!/usr/bin/env pwsh

function New-HTMLSecurityReport {

    param(
        [string]$OutputFile = "./logs/security-report.html"
    )

    $ad = Get-Content "./logs/security-summary.json" | ConvertFrom-Json
    $registry = Get-Content "./logs/registry-hardening-report.json" | ConvertFrom-Json
    $monitor = Get-Content "./logs/security-monitor-summary.json" | ConvertFrom-Json

    $overallScore = $monitor.OverallScore

    $scoreClass = if ($overallScore -ge 80) { "compliant" }
                  elseif ($overallScore -ge 60) { "warning" }
                  else { "non-compliant" }

    $alertsHtml = ""
    foreach ($alert in $monitor.Alerts) {
        $alertsHtml += "<li class='non-compliant'>$alert</li>"
    }

    $recommendHtml = ""
    foreach ($rec in $monitor.Recommendations) {
        $recommendHtml += "<li>$rec</li>"
    }

$html = @"
<!DOCTYPE html>
<html>
<head>
<title>Security Hardening Report</title>
<style>
body { font-family: Arial; margin: 20px; }
.header { background-color: #2c3e50; color: white; padding: 20px; }
.section { margin: 20px 0; padding: 15px; border: 1px solid #ddd; }
.compliant { color: green; font-weight: bold; }
.non-compliant { color: red; font-weight: bold; }
.warning { color: orange; font-weight: bold; }
</style>
</head>
<body>

<div class="header">
<h1>Windows Security Hardening Report</h1>
<p>Generated: $(Get-Date -Format "yyyy-MM-dd HH:mm:ss")</p>
</div>

<div class="section">
<h2>Executive Summary</h2>
<p>Overall Security Score: <span class="$scoreClass">$overallScore%</span></p>
</div>

<div class="section">
<h2>Active Directory Security</h2>
<p>Password Policy Compliant: $($ad.PasswordPolicyCompliant)</p>
<p>Lockout Policy Compliant: $($ad.LockoutPolicyCompliant)</p>
</div>

<div class="section">
<h2>Registry Security</h2>
<p>Compliance Percentage: $($registry.CompliancePercent)%</p>
</div>

<div class="section">
<h2>Critical Alerts</h2>
<ul>
$alertsHtml
</ul>
</div>

<div class="section">
<h2>Recommendations</h2>
<ul>
$recommendHtml
</ul>
</div>

</body>
</html>
"@

    $html | Out-File $OutputFile
    Write-Host "Report generated: $OutputFile"
}

New-HTMLSecurityReport
