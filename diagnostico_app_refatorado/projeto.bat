@echo off
setlocal

echo 🔄 Ativando ambiente virtual...
call .venv\Scripts\activate

:menu
echo.
echo === MENU - Diagnóstico App ===
echo [1] Rodar aplicação Flask
echo [2] Inicializar banco de dados
echo [0] Sair
set /p opcao=Escolha uma opcao: 

if "%opcao%"=="1" (
    python app.py
) else if "%opcao%"=="2" (
    python init_db.py
) else if "%opcao%"=="0" (
    exit
) else (
    echo Opcao invalida!
)

goto menu