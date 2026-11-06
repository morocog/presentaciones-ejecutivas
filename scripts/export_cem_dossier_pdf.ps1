$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$vaultPath = Split-Path -Parent $scriptDir
$deckDir = Join-Path $vaultPath "01-Propuestas-Comerciales\CEM-Colegio-Estudios-Multidisciplinarios"
$htmlFile = Join-Path $deckDir "dossier-ejecutivo-cem.html"
$outputPdf = Join-Path $deckDir "Dossier_Ejecutivo_CEM_Colegio_Estudios_Multidisciplinarios.pdf"

Write-Host "Iniciando compilación PDF para el Dossier Ejecutivo de CEM..." -ForegroundColor Cyan

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
    "--virtual-time-budget=4000",
    "--print-to-pdf=$outputPdf",
    $htmlUri
)

Start-Process -FilePath $chromePath -ArgumentList $chromeArgs -Wait -NoNewWindow

if (Test-Path $outputPdf) {
    $item = Get-Item $outputPdf
    Write-Host "PDF generado exitosamente: $($item.FullName)" -ForegroundColor Green
    Write-Host "Última Modificación: $($item.LastWriteTime)" -ForegroundColor Yellow
    Write-Host "Tamaño: $([math]::Round($item.Length / 1KB, 2)) KB" -ForegroundColor Green
} else {
    Write-Host "ERROR: No se encontró el PDF generado." -ForegroundColor Red
    exit 1
}
