# Script de exportación PDF exclusivo para el Slide de Soluciones BPO Grupo Coppel
$ErrorActionPreference = "Stop"
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$BaseDir = Resolve-Path "$ScriptDir\..\01-Propuestas-Comerciales\Grupo-Coppel"
$HtmlPath = Join-Path $BaseDir "soluciones_bpo_coppel.html"
$OutputPdf = Join-Path $BaseDir "Propuesta_Servicios_BPO_Grupo_Coppel_Telat.pdf"
$DownloadsPdf = Join-Path "$env:USERPROFILE\Downloads" "Propuesta_Servicios_BPO_Grupo_Coppel_Telat.pdf"

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

Write-Host "Compilando slide de Servicios BPO Coppel a PDF..." -ForegroundColor Cyan

$TempDir = Join-Path $env:TEMP ("chrome_coppel_" + [guid]::NewGuid().ToString().Substring(0,8))
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
