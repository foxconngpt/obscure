@echo off
setlocal enabledelayedexpansion

echo.
echo === PUBLICAR NOVA VERSAO NO GITHUB ===
echo.

:: Pergunta a versão
set /p versao="Digite a nova versão (ex: 2.0.0): v"

:: Pergunta a mensagem da versão
set /p mensagem="Digite a mensagem desta versão: "

:: Adiciona e commita tudo
git add .
git commit -m "! Versao v%versao% - %mensagem%"

:: Cria tag anotada
git tag -a v%versao% -m "Versão v%versao% - %mensagem%"

:: Faz push do código e da tag
git push
git push origin v%versao%

echo.
echo ✅ Versão v%versao% publicada com sucesso!
pause