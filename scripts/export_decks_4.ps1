$chromePath = "C:\Program Files\Google\Chrome\Application\chrome.exe"
if (-not (Test-Path $chromePath)) {
    $chromePath = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
}

# 1. Canonical Deck
$canonicalHtml = "C:\Users\SDVP\Documents\GitHub\presentaciones-ejecutivas\00-Executive-Decks-EN\04-Commercial-Capabilities-Deck\index.html"
$canonicalPdf = "C:\Users\SDVP\Documents\GitHub\presentaciones-ejecutivas\00-Executive-Decks-EN\04-Commercial-Capabilities-Deck\04_Commercial_Capabilities_Deck.pdf"
$canonicalUri = "file:///" + ($canonicalHtml -replace '\\', '/')

Write-Host "Compiling Canonical Deck..." -ForegroundColor Cyan
Start-Process -FilePath $chromePath -ArgumentList @(
    "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
    "--run-all-compositor-stages-before-draw", "--virtual-time-budget=5000",
    "--print-to-pdf=$canonicalPdf", $canonicalUri
) -Wait -NoNewWindow
Copy-Item $canonicalPdf "C:\Users\SDVP\Downloads\04_Commercial_Capabilities_Deck.pdf" -Force

# 2. Harry and David Deck
$hdHtml = "C:\Users\SDVP\Documents\GitHub\presentaciones-ejecutivas\00-Executive-Decks-EN\04-Commercial-Capabilities-Deck-Harry-and-David\index.html"
$hdPdf = "C:\Users\SDVP\Documents\GitHub\presentaciones-ejecutivas\00-Executive-Decks-EN\04-Commercial-Capabilities-Deck-Harry-and-David\04_Commercial_Capabilities_Deck_Harry_and_David.pdf"
$hdUri = "file:///" + ($hdHtml -replace '\\', '/')

Write-Host "Compiling Harry & David Deck..." -ForegroundColor Cyan
Start-Process -FilePath $chromePath -ArgumentList @(
    "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
    "--run-all-compositor-stages-before-draw", "--virtual-time-budget=5000",
    "--print-to-pdf=$hdPdf", $hdUri
) -Wait -NoNewWindow
Copy-Item $hdPdf "C:\Users\SDVP\Downloads\04_Commercial_Capabilities_Deck_Harry_and_David.pdf" -Force
Copy-Item $hdPdf "C:\Users\SDVP\Documents\GitHub\presentaciones-ejecutivas\01-Propuestas-Comerciales\Seasonal-Contact-Center\04_Commercial_Capabilities_Deck_Harry_and_David.pdf" -Force

Write-Host "All decks compiled and synced successfully." -ForegroundColor Green
