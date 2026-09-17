<#
.SYNOPSIS
    Script oficial de Telat Group para publicar y gestionar micro-sitios públicos efímeros de presentaciones en GitHub.

.DESCRIPTION
    Permite empaquetar una presentación de la Bóveda Privada 'presentaciones-ejecutivas' y desplegarla
    de forma segura y aislada en un repositorio satélite público (ej: tip-direccion, movistar-propuesta),
    o retirarla de la nube pasando el repositorio satélite a privado.

.PARAMETER SourceFolder
    Nombre de la subcarpeta dentro de 'presentaciones-ejecutivas' que se desea publicar.
    Ejemplo: '01-Propuestas-Comerciales\TIP-Mexico'

.PARAMETER TargetRepoName
    Nombre del repositorio satélite en GitHub (ej: 'tip-direccion').

.EXAMPLE
    .\publish_presentation.ps1 -SourceFolder "01-Propuestas-Comerciales\TIP-Mexico" -TargetRepoName "tip-direccion"
#>

param (
    [Parameter(Mandatory=$false)]
    [string]$SourceFolder = "",

    [Parameter(Mandatory=$false)]
    [string]$TargetRepoName = ""
)

$vaultPath = "c:\Users\SDVP\Documents\GitHub\presentaciones-ejecutivas"

Write-Host "============================================================" -ForegroundColor Cyan
Write-Host "   TELAT GROUP - PUBLICADOR DE MICRO-SITIOS EFÍMEROS" -ForegroundColor Cyan
Write-Host "============================================================" -ForegroundColor Cyan

if (-not $SourceFolder) {
    Write-Host "Catálogo de presentaciones disponibles en la Bóveda:" -ForegroundColor Yellow
    $cats = Get-ChildItem -Path $vaultPath -Directory | Where-Object { $_.Name -match '^\d\d-' }
    foreach ($c in $cats) {
        Write-Host "`n[$($c.Name)]" -ForegroundColor Green
        Get-ChildItem -Path $c.FullName -Directory | ForEach-Object {
            Write-Host "  - $($c.Name)\$($_.Name)" -ForegroundColor White
        }
    }
    Write-Host "`nUso: .\publish_presentation.ps1 -SourceFolder '<Carpeta>' -TargetRepoName '<nombre-repo-satelite>'" -ForegroundColor Cyan
    exit
}

$fullSource = Join-Path $vaultPath $SourceFolder
if (-not (Test-Path $fullSource)) {
    Write-Host "ERROR: La carpeta '$fullSource' no existe." -ForegroundColor Red
    exit 1
}

$targetLocal = Join-Path "c:\Users\SDVP\Documents\GitHub" $TargetRepoName
if (-not (Test-Path $targetLocal)) {
    New-Item -ItemType Directory -Path $targetLocal -Force | Out-Null
    Write-Host "Creado directorio satélite local: $targetLocal" -ForegroundColor Green
}

# Copiar archivos
Copy-Item -Path "$fullSource\*" -Destination $targetLocal -Recurse -Force
Write-Host "Archivos copiados desde '$SourceFolder' hacia '$TargetRepoName'." -ForegroundColor Green

# Crear .nojekyll para GitHub Pages
Set-Content -Path (Join-Path $targetLocal ".nojekyll") -Value "" -Force

# Instrucciones de Git
Write-Host "`nPara publicar en GitHub como micro-sitio público efímero:" -ForegroundColor Yellow
Write-Host "1. cd `"$targetLocal`"" -ForegroundColor White
Write-Host "2. git init; git add .; git commit -m `'Deploy publico efimero para cliente`'" -ForegroundColor White
Write-Host "3. git remote add origin https://github.com/morocog/$TargetRepoName.git" -ForegroundColor White
Write-Host "4. git branch -M main; git push -u origin main --force" -ForegroundColor White
Write-Host "5. En GitHub Settings -> Pages: activar 'Deploy from branch: main'." -ForegroundColor White
Write-Host "`nURL resultante: https://morocog.github.io/$TargetRepoName/" -ForegroundColor Cyan
Write-Host "============================================================" -ForegroundColor Cyan
