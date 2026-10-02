<#
.SYNOPSIS
    Script oficial de Telat Group para compilar la Presentación Comercial Ejecutiva en PDF HD (16:9 Panorámica).

.DESCRIPTION
    Utiliza el motor nativo de Google Chrome en modo Headless para compilar un documento PDF vectorial
    de alta fidelidad cromática y tipográfica a partir del archivo index.html.

.EXAMPLE
    .\export_pdf.ps1
#>

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$vaultPath = Split-Path -Parent $scriptDir
$deckDir = Join-Path $vaultPath "02-Direccion-y-Estrategia\Presentacion-Comercial-Telat"
$htmlFile = Join-Path $deckDir "index.html"
$outputPdf = Join-Path $deckDir "Presentacion_Comercial_Telat_Group.pdf"

Write-Host "============================================================" -ForegroundColor Cyan
Write-Host "   TELAT GROUP - COMPILADOR DE PRESENTACIONES EN PDF (16:9)" -ForegroundColor Cyan
Write-Host "============================================================" -ForegroundColor Cyan

if (-not (Test-Path $htmlFile)) {
    Write-Host "ERROR: No se encontró el archivo fuente en '$htmlFile'." -ForegroundColor Red
    exit 1
}

$chromePath = "C:\Program Files\Google\Chrome\Application\chrome.exe"
if (-not (Test-Path $chromePath)) {
    $chromePath = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    if (-not (Test-Path $chromePath)) {
        Write-Host "ERROR: No se encontró Google Chrome ni Microsoft Edge en las rutas estándar." -ForegroundColor Red
        exit 1
    }
}

Write-Host "Fuente: $htmlFile" -ForegroundColor White
Write-Host "Destino: $outputPdf" -ForegroundColor White
Write-Host "Motor: $chromePath" -ForegroundColor White
Write-Host "Compilando PDF en 16:9 panorámico..." -ForegroundColor Yellow

$htmlUri = "file:///" + ($htmlFile -replace '\\', '/')

$chromeArgs = @(
    "--headless=new",
    "--disable-gpu",
    "--no-pdf-header-footer",
    "--run-all-compositor-stages-before-draw",
    "--virtual-time-budget=3000",
    "--print-to-pdf=`"$outputPdf`"",
    "`"$htmlUri`""
)

Start-Process -FilePath $chromePath -ArgumentList $chromeArgs -Wait -NoNewWindow

if (Test-Path $outputPdf) {
    $size = (Get-Item $outputPdf).Length
    $sizeMB = [math]::Round($size / 1MB, 2)
    Write-Host "`n✓ PDF generado exitosamente ($sizeMB MB)" -ForegroundColor Green
    Write-Host "Ubicación: $outputPdf" -ForegroundColor Cyan
} else {
    Write-Host "`nERROR: No se pudo generar el archivo PDF." -ForegroundColor Red
    exit 1
}

Write-Host "============================================================" -ForegroundColor Cyan
