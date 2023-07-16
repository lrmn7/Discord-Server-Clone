import subprocess
import os
from pathlib import Path
import questionary
from rich.console import Console
from rich.panel import Panel
from rich.traceback import install
import colorama
from colorama import Fore, init, Style

colorama.init
install()

console = Console()


def clear_screen():
    os.system('clear')
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


def main():
    clear_screen()
    language = questionary.select("Pilih bahasa:",
                                  choices=["ID", "EN"]).ask()
    if not is_python_installed():
        clear_screen()
        console.print(
            Panel(f"Python tidak terinstal di sistem Anda.",
                  title="[bold red]Error[/bold red]"))
        return
    elif not is_main_script_present(language):
        clear_screen()
        console.print(
            Panel(f"Tidak dapat menemukan file main-{language}.py.",
                  title="[bold red]Error[/bold red]"))
        return
    elif not confirm_execution(language):
        clear_screen()
        console.print(
            Panel("Operasi dibatalkan.",
                  title="[bold yellow]Peringatan[/bold yellow]"))
        return
    try:
        subprocess.run([get_python_interpreter(), f"main-{language}.py"])
        console.log(
            f"Subprocess command: {get_python_interpreter(), f'main-{language}.py'}"
        )
        clear_screen()
        console.print(
            Panel("Script berhasil dijalankan.",
                  title="[bold green]Sukses[/bold green]"))
    except subprocess.CalledProcessError as e:
        clear_screen()
        console.print(
            Panel(f"Terjadi kesalahan saat menjalankan subprocess: {e}",
                  title="[bold red]Error[/bold red]"))


def is_python_installed():
    try:
        subprocess.check_output(["python", "--version"])
        return True
    except subprocess.CalledProcessError:
        return False


def is_main_script_present(language):
    return Path(f"main-{language}.py").is_file()


def confirm_execution(language):
    messages = {
        "ID":
        "Anda akan menjalankan skrip main-id.py. Apakah Anda ingin melanjutkan?",
        "EN":
        "You are about to execute the main-en.py script. Do you want to continue?"
    }
    clear_screen()
    confirmation = questionary.confirm(messages[language]).ask()
    return confirmation


def get_python_interpreter():
    if is_python3_installed():
        return "python3"
    else:
        return "python"


def is_python3_installed():
    try:
        subprocess.check_output(["python3", "--version"])
        return True
    except subprocess.CalledProcessError:
        return False


if __name__ == "__main__":
    main()
