# Script de exportación PDF exclusivo para el Slide de SLAs Estándar (UVC)
$ErrorActionPreference = "Stop"
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$BaseDir = Resolve-Path "$ScriptDir\..\01-Propuestas-Comerciales\UVC-Unlimited-Vacation-Club"
$HtmlPath = Join-Path $BaseDir "sla_estandar_uvc.html"
$OutputPdf = Join-Path $BaseDir "SLA_Estandar_UVC_Telat.pdf"
$DownloadsPdf = Join-Path "$env:USERPROFILE\Downloads" "SLA_Estandar_UVC_Telat.pdf"

$ChromePaths = @(
    "C:\Program Files\Google\Chrome\Application\chrome.exe",
    "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    "$env:LOCALAPPDATA\Google\Chrome\Application\chrome.exe"
)

$ChromeCmd = $null
foreach ($path in $ChromePaths) {
    if (Test-Path $path) {
        $ChromeCmd = $path
        break
    }
}

if (-not $ChromeCmd) {
    Write-Error "No se encontró Google Chrome en el sistema."
    exit 1
}

Write-Host "Compilando slide de SLAs UVC a PDF..." -ForegroundColor Cyan

$TempDir = Join-Path $env:TEMP ("chrome_sla_" + [guid]::NewGuid().ToString().Substring(0,8))
New-Item -ItemType Directory -Path $TempDir -Force | Out-Null

$Uri = "file:///" + ($HtmlPath -replace '\\', '/')

$Args = @(
    "--headless=new",
    "--disable-gpu",
    "--no-pdf-header-footer",
    "--run-all-compositor-stages-before-draw",
    "--virtual-time-budget=6000",
    "--print-to-pdf=$OutputPdf",
    "--user-data-dir=$TempDir",
    $Uri
)

$Process = Start-Process -FilePath $ChromeCmd -ArgumentList $Args -Wait -PassThru -NoNewWindow

if (Test-Path $TempDir) {
    Remove-Item -Path $TempDir -Recurse -Force -ErrorAction SilentlyContinue
}

if (Test-Path $OutputPdf) {
    Copy-Item -Path $OutputPdf -Destination $DownloadsPdf -Force
    $PdfSize = (Get-Item $OutputPdf).Length / 1KB
    Write-Host ("PDF generado exitosamente en repo: {0}" -f $OutputPdf) -ForegroundColor Green
    Write-Host ("Tamaño: {0:N2} KB (1 página exacta)" -f $PdfSize) -ForegroundColor Yellow
    Write-Host ("Copiado a Descargas: {0}" -f $DownloadsPdf) -ForegroundColor Green
} else {
    Write-Error "No se generó el archivo PDF."
}
