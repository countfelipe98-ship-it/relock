@echo off
cls
title Instalador Cyber Attack - Painel 1.2.0

echo  ▄████▄▓██   ██▓ ▄▄▄▄   ▓█████  ██▀███               
echo ▒██▀ ▀█ ▒██  ██▒▓█████▄ ▓█   ▀ ▓██ ▒ ██▒             
echo ▒▓█    ▄ ▒██ ██░▒██▒ ▄██▒███   ▓██ ░▄█ ▒             
echo ▒▓▓▄ ▄██▒░ ▐██▓░▒██░█▀  ▒▓█  ▄ ▒██▀▀█▄               
echo ▒ ▓███▀ ░░ ██▒▓░░▓█  ▀█▓░▒████▒░██▓ ▒██▒             
echo ░ ░▒ ▒  ░ ██▒▒▒ ░▒▓███▀▒░░ ▒░ ░░ ▒▓ ░▒▓░             
echo   ░  ▒  ▓██ ░▒░ ▒░▒   ░  ░ ░  ░  ░▒ ░ ▒░             
echo ░       ▒ ▒ ░░   ░    ░    ░     ░░   ░              
echo ░ ░     ░ ░      ░         ░  ░   ░                  
echo ░       ░ ░           ░                              
echo  ▄▄▄     ▄▄▄█████▓▄▄▄█████▓ ▄▄▄       ▄████▄   ██ ▄█▀
echo ▒████▄   ▓  ██▒ ▓▒▓  ██▒ ▓▒▒████▄    ▒██▀ ▀█   ██▄█▒ 
echo ▒██  ▀█▄ ▒ ▓██░ ▒░▒ ▓██░ ▒░▒██  ▀█▄  ▒▓█    ▄ ▓███▄░ 
echo ░██▄▄▄▄██░ ▓██▓ ░ ░ ▓██▓ ░ ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓██ █▄ 
echo  ▓█   ▓██▒ ▒██▒ ░   ▒██▒ ░  ▓█   ▓██▒▒ ▓███▀ ░▒██▒ █▄
echo  ▒▒   ▓▒█░ ▒ ░░     ▒ ░░    ▒▒   ▓▒█░░ ░▒ ▒  ░▒ ▒▒ ▓▒
echo   ▒   ▒▒ ░   ░        ░      ▒   ▒▒ ░  ░  ▒   ░ ░▒ ▒░
echo   ░   ▒    ░        ░        ░   ▒   ░        ░ ░░ ░ 
echo       ░  ░                       ░  ░░ ░      ░  ░   
echo                                      ░               

echo.
echo painel 1.2.0 link do site oficial da cyber attack:https://cyber-attack-092.my.canva.site/
echo.
echo Iniciando instalacao para Windows...

:: Verificar se Python está instalado
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python nao encontrado! Por favor, instale o Python em python.org e marque "Add to PATH".
    pause
    exit
)

echo Instalando bibliotecas necessarias...
pip install discord.py colorama

echo.
echo Instalacao concluida!
echo Para iniciar o painel, use: python main.py
pause
