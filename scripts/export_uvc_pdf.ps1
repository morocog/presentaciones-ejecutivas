$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$vaultPath = Split-Path -Parent $scriptDir
$deckDir = Join-Path $vaultPath "01-Propuestas-Comerciales\UVC-Unlimited-Vacation-Club"
$htmlFile = Join-Path $deckDir "index.html"
$outputPdf = Join-Path $deckDir "Propuesta_Comercial_UVC_Unlimited_Vacation_Club_Telat.pdf"
$downloadsPdf = "$env:USERPROFILE\Downloads\Propuesta_Comercial_UVC_Unlimited_Vacation_Club_Telat.pdf"

Write-Host "Iniciando compilación PDF para Unlimited Vacation Club (UVC)..." -ForegroundColor Cyan

if (-not (Test-Path $htmlFile)) {
    Write-Host "ERROR: No existe $htmlFile" -ForegroundColor Red
    exit 1
}

$chromePath = "C:\Program Files\Google\Chrome\Application\chrome.exe"
if (-not (Test-Path $chromePath)) {
    $chromePath = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
}

$htmlUri = "file:///" + ($htmlFile -replace '\\', '/')

$chromeArgs = @(
    "--headless=new",
    "--disable-gpu",
    "--no-pdf-header-footer",
    "--run-all-compositor-stages-before-draw",
    "--virtual-time-budget=5000",
    "--print-to-pdf=$outputPdf",
    $htmlUri
)

Start-Process -FilePath $chromePath -ArgumentList $chromeArgs -Wait -NoNewWindow

if (Test-Path $outputPdf) {
    $item = Get-Item $outputPdf
    Write-Host "PDF generado exitosamente en repo: $($item.FullName)" -ForegroundColor Green
    Write-Host "Tamaño: $([math]::Round($item.Length / 1KB, 2)) KB" -ForegroundColor Green
    
    # Copia directa a Downloads para acceso inmediato de Ricardo
    Copy-Item -Path $outputPdf -Destination $downloadsPdf -Force
    Write-Host "PDF copiado a Descargas: $downloadsPdf" -ForegroundColor Yellow
} else {
    Write-Host "ERROR: No se encontró el PDF generado." -ForegroundColor Red
    exit 1
}
