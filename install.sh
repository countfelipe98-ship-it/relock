#!/bin/bash

# Cores para o terminal
PURPLE='\033[0;35m'
WHITE='\033[1;37m'
NC='\033[0m' # No Color

clear

# Mostrar ASCII Art
cat << "EOF"
 ▄████▄▓██   ██▓ ▄▄▄▄   ▓█████  ██▀███               
▒██▀ ▀█ ▒██  ██▒▓█████▄ ▓█   ▀ ▓██ ▒ ██▒             
▒▓█    ▄ ▒██ ██░▒██▒ ▄██▒███   ▓██ ░▄█ ▒             
▒▓▓▄ ▄██▒░ ▐██▓░▒██░█▀  ▒▓█  ▄ ▒██▀▀█▄               
▒ ▓███▀ ░░ ██▒▓░░▓█  ▀█▓░▒████▒░██▓ ▒██▒             
░ ░▒ ▒  ░ ██▒▒▒ ░▒▓███▀▒░░ ▒░ ░░ ▒▓ ░▒▓░             
  ░  ▒  ▓██ ░▒░ ▒░▒   ░  ░ ░  ░  ░▒ ░ ▒░             
░       ▒ ▒ ░░   ░    ░    ░     ░░   ░              
░ ░     ░ ░      ░         ░  ░   ░                  
░       ░ ░           ░                              
 ▄▄▄     ▄▄▄█████▓▄▄▄█████▓ ▄▄▄       ▄████▄   ██ ▄█▀
▒████▄   ▓  ██▒ ▓▒▓  ██▒ ▓▒▒████▄    ▒██▀ ▀█   ██▄█▒ 
▒██  ▀█▄ ▒ ▓██░ ▒░▒ ▓██░ ▒░▒██  ▀█▄  ▒▓█    ▄ ▓███▄░ 
░██▄▄▄▄██░ ▓██▓ ░ ░ ▓██▓ ░ ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓██ █▄ 
 ▓█   ▓██▒ ▒██▒ ░   ▒██▒ ░  ▓█   ▓██▒▒ ▓███▀ ░▒██▒ █▄
 ▒▒   ▓▒█░ ▒ ░░     ▒ ░░    ▒▒   ▓▒█░░ ░▒ ▒  ░▒ ▒▒ ▓▒
  ▒   ▒▒ ░   ░        ░      ▒   ▒▒ ░  ░  ▒   ░ ░▒ ▒░
  ░   ▒    ░        ░        ░   ▒   ░        ░ ░░ ░ 
      ░  ░                       ░  ░░ ░      ░  ░   
                                     ░               
EOF

echo -e "${PURPLE}painel 1.2.0 link do site oficial da cyber attack:https://cyber-attack-092.my.canva.site/${NC}"
echo ""
echo -e "${WHITE}Iniciando instalação para Linux/Termux...${NC}"

# Verificar se é Termux ou Linux comum
if [ -d "/data/data/com.termux/files/usr/bin" ]; then
    echo -e "${PURPLE}[Termux]${NC} Atualizando pacotes..."
    pkg update -y && pkg upgrade -y
    echo -e "${PURPLE}[Termux]${NC} Instalando Python e dependências..."
    pkg install python -y
else
    echo -e "${PURPLE}[Linux]${NC} Atualizando pacotes..."
    sudo apt update -y
    echo -e "${PURPLE}[Linux]${NC} Instalando Python e dependências..."
    sudo apt install python3 python3-pip -y
fi

echo -e "${PURPLE}[Geral]${NC} Instalando bibliotecas do bot..."
pip install discord.py colorama

echo ""
echo -e "${WHITE}Instalação concluída!${NC}"
echo -e "Para iniciar o painel, use: ${PURPLE}python main.py${NC}"
