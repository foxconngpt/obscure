# Criar .gitignore se não existir
if (!(Test-Path ".gitignore")) {
    Set-Content .gitignore "`n__pycache__/`n*.pyc"
    git add .gitignore
    Write-Host ".gitignore criado e adicionado ao Git."
}

# Apagar arquivos .pyc locais
Write-Host "Removendo arquivos .pyc locais..."
Get-ChildItem -Recurse -Include *.pyc | Remove-Item -Force

# Remover .pyc versionados do cache do Git
Write-Host "Removendo arquivos .pyc do controle de versão (cached)..."
git rm --cached -r __pycache__ 2>$null

# Adicionar todas as mudanças restantes
git add .

# Commit das alterações
git commit -m "Versão limpa e funcional pronta para produção"

# Push para o repositório remoto
git push origin main
Write-Host "✅ Projeto atualizado com sucesso no GitHub!"
