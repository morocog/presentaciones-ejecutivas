$chromePath = "C:\Program Files\Google\Chrome\Application\chrome.exe"
if (-not (Test-Path $chromePath)) {
    $chromePath = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
}
$dir = "C:\Users\SDVP\Documents\GitHub\presentaciones-ejecutivas\01-Propuestas-Comerciales\Seasonal-Contact-Center"
$htmlFile = Join-Path $dir "Propuesta_Comercial_TELAT_Seasonal_Contact_Center.html"
$outputPdf = Join-Path $dir "Propuesta_Comercial_TELAT_Seasonal_Contact_Center.pdf"
$downloadsPdf = "C:\Users\SDVP\Downloads\Propuesta_Comercial_TELAT_Seasonal_Contact_Center.pdf"

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
    Copy-Item $outputPdf -Destination $downloadsPdf -Force
    Write-Host "PDF generated: $outputPdf" -ForegroundColor Green
    Write-Host "Copied to Downloads: $downloadsPdf" -ForegroundColor Green
} else {
    Write-Host "Failed to generate PDF." -ForegroundColor Red
}
