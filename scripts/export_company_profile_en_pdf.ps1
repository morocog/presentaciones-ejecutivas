$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$vaultPath = Split-Path -Parent $scriptDir
$deckDir = Join-Path $vaultPath "02-Direccion-y-Estrategia\Company-Profile-Telat-EN"
$htmlFile = Join-Path $deckDir "index.html"
$outputPdf = Join-Path $deckDir "Company_Profile_Telat_EN.pdf"

Write-Host "Compiling Company Profile Telat (EN) to PDF..." -ForegroundColor Cyan

if (-not (Test-Path $htmlFile)) {
    Write-Host "ERROR: Source not found: $htmlFile" -ForegroundColor Red
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
    "--window-size=1920,1080",
    "--force-device-scale-factor=1",
    "--hide-scrollbars",
    "--no-pdf-header-footer",
    "--run-all-compositor-stages-before-draw",
    "--virtual-time-budget=4000",
    "--print-to-pdf=$outputPdf",
    $htmlUri
)

Start-Process -FilePath $chromePath -ArgumentList $chromeArgs -Wait -NoNewWindow

if (Test-Path $outputPdf) {
    $size = (Get-Item $outputPdf).Length
    $sizeMB = [math]::Round($size / 1MB, 2)
    Write-Host "SUCCESS: PDF generated ($sizeMB MB)" -ForegroundColor Green
    Write-Host "Output: $outputPdf" -ForegroundColor Cyan
} else {
    Write-Host "ERROR: PDF generation failed" -ForegroundColor Red
    exit 1
}
