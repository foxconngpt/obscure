@echo off
setlocal

echo 🔄 Ativando ambiente virtual...
call .venv\Scripts\activate

:menu
echo.
echo === MENU - Diagnostico App ===
echo [1] Rodar aplicação Flask
echo [2] Inicializar banco (init_db.py)
echo [3] Testar variáveis do .env (test_env.py)
echo [4] Atualizar dependências (requirements.txt)
echo [0] Sair
set /p opcao=Escolha uma opcao: 

if "%opcao%"=="1" (
    python app.py
) else if "%opcao%"=="2" (
    python init_db.py
) else if "%opcao%"=="3" (
    python test_env.py
) else if "%opcao%"=="4" (
    pip install -r requirements.txt
) else if "%opcao%"=="0" (
    exit
) else (
    echo Opcao invalida!
)

goto menu
