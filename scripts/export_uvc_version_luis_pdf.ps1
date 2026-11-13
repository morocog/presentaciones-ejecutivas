# Script de exportación PDF exclusivo para la Versión Luis (UVC)
# Conserva 100% inalterado el PDF canónico original

$ErrorActionPreference = "Stop"
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$BaseDir = Resolve-Path "$ScriptDir\..\01-Propuestas-Comerciales\UVC-Unlimited-Vacation-Club"
$HtmlPath = Join-Path $BaseDir "index_version_luis.html"
$OutputPdf = Join-Path $BaseDir "Propuesta_Comercial_UVC_Version_Luis.pdf"
$DownloadsPdf = Join-Path "$env:USERPROFILE\Downloads" "Propuesta_Comercial_UVC_Version_Luis.pdf"

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
    Write-Error "No se encontro Google Chrome en el sistema."
    exit 1
}

Write-Host "Iniciando compilacion PDF para la Version Luis (Unlimited Vacation Club)..." -ForegroundColor Cyan

$TempDir = Join-Path $env:TEMP ("chrome_uvc_luis_" + [guid]::NewGuid().ToString().Substring(0,8))
New-Item -ItemType Directory -Path $TempDir -Force | Out-Null

$Uri = "file:///" + ($HtmlPath -replace '\\', '/')

$Args = @(
    "--headless=new",
    "--disable-gpu",
    "--no-pdf-header-footer",
    "--print-to-pdf=$OutputPdf",
    "--user-data-dir=$TempDir",
    $Uri
)

$Process = Start-Process -FilePath $ChromeCmd -ArgumentList $Args -Wait -PassThru -NoNewWindow

if (Test-Path $TempDir) {
    Remove-Item -Path $TempDir -Recurse -Force -ErrorAction SilentlyContinue
}

if (Test-Path $OutputPdf) {
    $PdfSize = (Get-Item $OutputPdf).Length / 1KB
    Write-Host ("PDF generado exitosamente en repo: {0}" -f $OutputPdf) -ForegroundColor Green
    Write-Host ("Tamano: {0:N2} KB" -f $PdfSize) -ForegroundColor Yellow
    
    # Copiar a Descargas de Ricardo
    Copy-Item -Path $OutputPdf -Destination $DownloadsPdf -Force
    Write-Host ("PDF copiado a Descargas: {0}" -f $DownloadsPdf) -ForegroundColor Green
} else {
    Write-Error "Fallo la generacion del PDF Version Luis."
}

