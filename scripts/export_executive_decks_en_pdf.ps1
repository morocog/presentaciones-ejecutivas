$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$vaultPath = Split-Path -Parent $scriptDir
$enBase = Join-Path $vaultPath "00-Executive-Decks-EN"

$chromePath = "C:\Program Files\Google\Chrome\Application\chrome.exe"
if (-not (Test-Path $chromePath)) {
    $chromePath = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
}

Write-Host "Starting batch compilation of 16:9 executive PDFs in English..." -ForegroundColor Cyan
Write-Host "Compiler browser: $chromePath" -ForegroundColor DarkCyan

$decks = @(
    @{
        Name = "Deck 01 - Telat AI Solutions"
        Dir = "01-Telat-AI-Solutions"
        Pdf = "01_Telat_AI_Solutions.pdf"
    },
    @{
        Name = "Deck 02 - Operations Driven by Intelligence"
        Dir = "02-Operations-Driven-by-Intelligence"
        Pdf = "02_Operations_Driven_by_Intelligence.pdf"
    },
    @{
        Name = "Deck 03 - Technology Differentiators"
        Dir = "03-Technology-Differentiators"
        Pdf = "03_Key_Technology_Differentiators.pdf"
    },
    @{
        Name = "Deck 04 - Commercial Capabilities Deck"
        Dir = "04-Commercial-Capabilities-Deck"
        Pdf = "04_Commercial_Capabilities_Deck.pdf"
    }
)

foreach ($d in $decks) {
    $deckPath = Join-Path $enBase $d.Dir
    $htmlFile = Join-Path $deckPath "index.html"
    $outputPdf = Join-Path $deckPath $d.Pdf

    Write-Host "`n--- Compiling: $($d.Name) ---" -ForegroundColor Yellow

    if (-not (Test-Path $htmlFile)) {
        Write-Host "ERROR: $htmlFile does not exist" -ForegroundColor Red
        continue
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
        Write-Host "OK: PDF generated: $($item.FullName)" -ForegroundColor Green
        Write-Host "    Size: $([math]::Round($item.Length / 1KB, 2)) KB" -ForegroundColor Green
    } else {
        Write-Host "ERROR: Failed to generate PDF for $($d.Name)" -ForegroundColor Red
    }
}

Write-Host "`nBatch compilation completed." -ForegroundColor Cyan
