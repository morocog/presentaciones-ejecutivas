$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$vaultPath = Split-Path -Parent $scriptDir
$esBase = Join-Path $vaultPath "00-Executive-Decks-ES"

$chromePath = "C:\Program Files\Google\Chrome\Application\chrome.exe"
if (-not (Test-Path $chromePath)) {
    $chromePath = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
}

Write-Host "Iniciando compilacion masiva de PDFs vectoriales 16:9 en espanol..." -ForegroundColor Cyan
Write-Host "Navegador de compilacion: $chromePath" -ForegroundColor DarkCyan

$decks = @(
    @{
        Name = "Deck 01 - Soluciones IA Telat"
        Dir = "01-Soluciones-IA-Telat"
        Pdf = "01_Soluciones_IA_Telat.pdf"
    },
    @{
        Name = "Deck 02 - Operaciones Impulsadas por Inteligencia"
        Dir = "02-Operaciones-Impulsadas-por-Inteligencia"
        Pdf = "02_Operaciones_Impulsadas_por_Inteligencia.pdf"
    },
    @{
        Name = "Deck 03 - Diferenciadores Tecnologicos y Operativos"
        Dir = "03-Diferenciadores-Tecnologicos-y-Operativos"
        Pdf = "03_Diferenciadores_Tecnologicos_y_Operativos.pdf"
    },
    @{
        Name = "Deck 04 - Portafolio Capacidades Comerciales"
        Dir = "04-Portafolio-Capacidades-Comerciales"
        Pdf = "04_Portafolio_Capacidades_Comerciales.pdf"
    }
)

foreach ($d in $decks) {
    $deckPath = Join-Path $esBase $d.Dir
    $htmlFile = Join-Path $deckPath "index.html"
    $outputPdf = Join-Path $deckPath $d.Pdf

    Write-Host "`n--- Compilando: $($d.Name) ---" -ForegroundColor Yellow

    if (-not (Test-Path $htmlFile)) {
        Write-Host "ERROR: No existe $htmlFile" -ForegroundColor Red
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
        Write-Host "OK: PDF generado exitosamente: $($item.FullName)" -ForegroundColor Green
        Write-Host "    Tamano: $([math]::Round($item.Length / 1KB, 2)) KB" -ForegroundColor Green
    } else {
        Write-Host "ERROR: Fallo la generacion de $outputPdf" -ForegroundColor Red
    }
}

Write-Host "`nCompilacion masiva finalizada con exito." -ForegroundColor Cyan
