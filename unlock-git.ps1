# Script para remover .git/index.lock com segurança

$gitRunning = Get-Process git -ErrorAction SilentlyContinue

if ($gitRunning) {
    Write-Output "⚠️ Existe um processo Git rodando. Espere terminar antes de remover o lock."
    exit 1
}

$lockFile = ".git\index.lock"

if (Test-Path $lockFile) {
    Remove-Item -Force $lockFile
    Write-Output "✅ Lock file removido com sucesso!"
} else {
    Write-Output "ℹ️ Nenhum lock file encontrado."
}
