from os import system
import psutil
import os
from pypresence import Presence
import time
import sys
import discord
import subprocess
import json
from rich.table import Table
from rich.console import Console
from rich.style import Style
from rich.panel import Panel as RichPanel
from rich.text import Text
import asyncio
import colorama
from colorama import Fore, init, Style
import platform
import inquirer
from cloner import Clone

version = '0.3'
clones = {'Clones_teste_feitos': 0}
versao_python = sys.version.split()[0]

console = Console()


def clearall():
    system('clear')
    print(f"""{Style.BRIGHT}{Fore.RED}

████████████████████████████████████████████████████████████████████████████████████
█░░░░░░████████████░░░░░░░░░░░░░░░░███░░░░░░██████████░░░░░░█░░░░░░██████████░░░░░░█
█░░▄▀░░████████████░░▄▀▄▀▄▀▄▀▄▀▄▀░░███░░▄▀░░░░░░░░░░░░░░▄▀░░█░░▄▀░░░░░░░░░░██░░▄▀░░█
█░░▄▀░░████████████░░▄▀░░░░░░░░▄▀░░███░░▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░██░░▄▀░░█
█░░▄▀░░████████████░░▄▀░░████░░▄▀░░███░░▄▀░░░░░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░▄▀░░██░░▄▀░░█
█░░▄▀░░████████████░░▄▀░░░░░░░░▄▀░░███░░▄▀░░██░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░██░░▄▀░░█
█░░▄▀░░████████████░░▄▀▄▀▄▀▄▀▄▀▄▀░░███░░▄▀░░██░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░██░░▄▀░░█
█░░▄▀░░████████████░░▄▀░░░░░░▄▀░░░░███░░▄▀░░██░░░░░░██░░▄▀░░█░░▄▀░░██░░▄▀░░██░░▄▀░░█
█░░▄▀░░████████████░░▄▀░░██░░▄▀░░█████░░▄▀░░██████████░░▄▀░░█░░▄▀░░██░░▄▀░░░░░░▄▀░░█
█░░▄▀░░░░░░░░░░████░░▄▀░░██░░▄▀░░░░░░█░░▄▀░░██████████░░▄▀░░█░░▄▀░░██░░▄▀▄▀▄▀▄▀▄▀░░█
█░░▄▀▄▀▄▀▄▀▄▀░░████░░▄▀░░██░░▄▀▄▀▄▀░░█░░▄▀░░██████████░░▄▀░░█░░▄▀░░██░░░░░░░░░░▄▀░░█
█░░░░░░░░░░░░░░████░░░░░░██░░░░░░░░░░█░░░░░░██████████░░░░░░█░░░░░░██████████░░░░░░█
████████████████████████████████████████████████████████████████████████████████████

{Style.RESET_ALL}{Fore.MAGENTA}{Fore.RESET}""")


client = discord.Client()
if os == "Windows":
    system("cls")
else:
    print(chr(27) + "[2J")
    clearall()
while True:
    token = input(
        f'{Style.BRIGHT}{Fore.MAGENTA}Masukkan token Anda untuk melanjutkan{Style.RESET_ALL}{Fore.RESET}\n >'
    )
    guild_s = input(
        f'{Style.BRIGHT}{Fore.MAGENTA}Masukkan ID server yang ingin Anda salin{Style.RESET_ALL}{Fore.RESET}\n >'
    )
    guild = input(
        f'{Style.BRIGHT}{Fore.MAGENTA}Masukkan ID server yang ingin anda simpan{Style.RESET_ALL}{Fore.RESET}\n>'
    )
    clearall()
    print(f'{Style.BRIGHT}{Fore.GREEN}ID yang dimasukkan adalah:')
    print(
        f'{Style.BRIGHT}{Fore.GREEN}Token Anda: {Fore.YELLOW}{token}{Style.RESET_ALL}{Fore.RESET}'
    )
    print(
        f'{Style.BRIGHT}{Fore.GREEN}ID Server yang akan di salin: {Fore.YELLOW}{guild_s}{Style.RESET_ALL}{Fore.RESET}'
    )
    print(
        f'{Style.BRIGHT}{Fore.GREEN}ID Server yang di simpan: {Fore.YELLOW}{guild}{Style.RESET_ALL}{Fore.RESET}'
    )
    confirm = input(
        f'{Style.BRIGHT}{Fore.MAGENTA}Silahkan di cek lagi apakah sudah benar? {Fore.YELLOW}(Y/N){Style.RESET_ALL}{Fore.RESET}\n >'
    )
    if confirm.upper() == 'Y':
        if not guild_s.isnumeric():
            clearall()
            print(
                f'{Style.BRIGHT}{Fore.RED}ID server yang akan disalin harus hanya mengandung angka saja.{Style.RESET_ALL}{Fore.RESET}'
            )
            continue
        if not guild.isnumeric():
            clearall()
            print(
                f'{Style.BRIGHT}{Fore.RED}ID server tujuan tempat anda menyimpan hasil salinan harus hanya mengandung angka saja.{Style.RESET_ALL}{Fore.RESET}'
            )
            continue
        if not token.strip() or not guild_s.strip() or not guild.strip():
            clearall()
            print(
                f'{Style.BRIGHT}{Fore.RED}Satu atau lebih field kosong.{Style.RESET_ALL}{Fore.RESET}'
            )
            continue
        if len(token.strip()) < 3 or len(guild_s.strip()) < 3 or len(
                guild.strip()) < 3:
            clearall()
            print(
                f'{Style.BRIGHT}{Fore.RED}Satu atau lebih field memiliki kurang dari 3 karakter.{Style.RESET_ALL}{Fore.RESET}'
            )
            continue
        break

    elif confirm.upper() == 'N':
        clearall()
else:
    clearall()
    print(
        f'{Style.BRIGHT}{Fore.RED}Opsi tidak valid. Harap masukkan Y atau N.{Style.RESET_ALL}{Fore.RESET}'
    )
input_guild_id = guild_s
output_guild_id = guild
token = token
clearall()


@client.event
async def on_ready():
    try:
        start_time = time.time()
        global clones
        table = Table(title="Versi", style="bold magenta")
        table.add_column("Komponen")
        table.add_column("Versi")
        table.add_row("Cloner", str(version), style="cyan")
        table.add_row("Discord.py", str(discord.__version__), style="cyan")
        table.add_row("Python", str(versao_python), style="cyan")
        console.print(RichPanel(table, width=47))
        console.print(
            RichPanel(f" Keautentikan berhasil",
                      style="bold green",
                      width=47))
        console.print(
            RichPanel(
                f" Halo, {client.user.name}! Proses menyalin akan segera dimulai...",
                style="bold blue",
                width=47))
        print(f"\n")
        questions = [
            inquirer.List(
                'clone_emojis',
                message="\033[35mApakah Anda ingin menyalin emoji?\033[0m",
                choices=['\033[32mYa\033[0m', '\033[31mTidak\033[0m'],
            ),
        ]
        answers = inquirer.prompt(questions)
        guild_from = client.get_guild(int(input_guild_id))
        guild_to = client.get_guild(int(output_guild_id))
        await Clone.guild_edit(guild_to, guild_from)
        await Clone.channels_delete(guild_to)
        await Clone.roles_create(guild_to, guild_from)
        await Clone.categories_create(guild_to, guild_from)
        await Clone.channels_create(guild_to, guild_from)
        end_time = time.time()
        duration = end_time - start_time
        duration_str = time.strftime("%M:%S", time.gmtime(duration))
        if answers['clone_emojis'] == '\033[32mYa\033[0m':
            print(
                f"{Style.BRIGHT}{Fore.YELLOW}Proses penyalinan emoji sedang berlangsung. Ini mungkin memakan waktu beberapa saat."
            )
            await asyncio.sleep(20)
            await Clone.emojis_create(guild_to, guild_from)
            print(
                f"{Style.BRIGHT}{Fore.BLUE}Server berhasil disalin dalam {Fore.YELLOW}{duration_str}{Style.RESET_ALL}"
            )
            print(
                f"{Style.BRIGHT}{Fore.BLUE}Kunjungi server Discord kami: {Fore.YELLOW}https://discord.gg/Qvf5NUtqMg{Style.RESET_ALL}"
            )
            clones['Clones_teste_feitos'] += 1
            with open('saves.json', 'w') as f:
                json.dump(clones, f)
            print(
                f"{Style.BRIGHT}{Fore.BLUE}Menyelesaikan proses dan mengakhiri sesi pada akun {Fore.YELLOW}{client.user}"
            )
            await client.close()  # menutup kode
    except discord.LoginFailure:
        print(
            "Tidak dapat mengotentikasi ke akun. Periksa apakah token yang dimasukkan benar."
        )
    except discord.Forbidden:
        print("Tidak dapat menyalin karena keterbatasan izin.")
    except discord.HTTPException:
        print("Terjadi kesalahan dalam berkomunikasi dengan API Discord.")
    except discord.NotFound:
        print(
            "Tidak dapat menemukan salah satu elemen yang disalin (channel, kategori, dll.)."
        )
    except Exception as e:
        print(Fore.RED + "Terjadi kesalahan:", e)


try:
    client.run(token, bot=False)
except discord.LoginFailure:
    print(Fore.RED + "Token yang dimasukkan tidak valid")
    print(
        Fore.YELLOW +
        "\n\nKode akan dijalankan ulang dalam 10 detik. Jika Anda tidak ingin menunggu, segarkan halaman dan mulai kembali."
    )
    print(Style.RESET_ALL)
    time.sleep(10)
    subprocess.Popen(["python", __file__])
    print(Fore.RED + "Mengulang kembali...")
