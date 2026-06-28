@echo off
cd /d "%~dp0"

if exist ".venv\Scripts\activate.bat" (
    call ".venv\Scripts\activate.bat"
)

set /p DB_PASSWORD=Digite a senha do PostgreSQL: 
set DB_NAME=nexus_erp

python main.py

pause
