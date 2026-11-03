$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$vaultPath = Split-Path -Parent $scriptDir
$deckDir = Join-Path $vaultPath "01-Propuestas-Comerciales\Operations-Driven-by-Intelligence-EN"
$htmlFile = Join-Path $deckDir "index.html"
$outputPdf = Join-Path $deckDir "Operations_Driven_by_Intelligence_Telat.pdf"

Write-Host "Compiling Generic Operations Driven by Intelligence (US English, 8 Slides) to PDF HD..." -ForegroundColor Cyan

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
    Write-Host "PDF generado: $($item.FullName)" -ForegroundColor Green
    Write-Host "Tamaño: $([math]::Round($item.Length / 1KB, 2)) KB" -ForegroundColor Green
} else {
    Write-Host "ERROR: Falló generación de PDF." -ForegroundColor Red
    exit 1
}

