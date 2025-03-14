import pyfiglet
import subprocess
import os
import time
import sys
from colorama import init, Fore, Back

init(autoreset=True)

def set_terminal_background():
    sys.stdout.write("\033[47m\033[2J\033[H")
    sys.stdout.flush()

def fade_in_text(text, steps=8, delay=0.015):
    for _ in range(steps + 1):
        sys.stdout.write(f"\033[30;47m{text}\033[0m\r")
        sys.stdout.flush()
        time.sleep(delay)
    print()

def print_banner():
    text = pyfiglet.figlet_format("Pretzel", font="slant")
    for line in text.split("\n"):  
        fade_in_text(line)
    print("\033[30;47m=-=-=-=--=-=-= Made by Astr =-=-=-=--=-=-=\033[0m\n")
    print("\033[30;47mCurrently this is Undetected, Pretzel will continue to update and be Undetected.\033[0m\n")
    print("\033[30;47mPlease use this tool responsibly, Pretzel isn't made for online cheating.\033[0m\n")

def skin_changer():
    dll_path = "Dynamic/Skin.dll"
    hookloader_path = "hookloader.exe"
    
    if not os.path.isfile(dll_path):
        print("\033[30;47m[ Info ] Error: Skin.dll not found in Folder/Dynamic!\033[0m")
        return

    if not os.path.isfile(hookloader_path):
        print("\033[30;47m[ Info ] Error: hookloader.exe not found! Ensure it is in the main directory.\033[0m")
        return

    print("\033[30;47m[ Status ] Initializing Skin Changer...\033[0m")
    print("\033[30;47m[ Info ] Hooks may fail from time to time, if you didn't see a difference in-game retry.\033[0m")
    time.sleep(1)

    try:
        subprocess.run([hookloader_path, dll_path], check=True)
        print("\033[30;47m[ Info ] Skin Changer Loaded!!\033[0m")
    except subprocess.CalledProcessError as e:
        print(f"\033[30;47m[ Info ] Error running hookloader: {e}\033[0m")

def hook_menu():
    while True:
        print("\033[30;47m1 - Skin Changer [ Unlock all in-game skins ]\033[0m")
        print("\033[30;47m2 - Go Back [ Go back to main menu ]\033[0m")
        choice = input("\033[30;47m> \033[0m").strip().lower()

        if choice == "1" or choice == "skin changer":
            skin_changer()
        elif choice == "2" or choice == "go back":
            return
        else:
            print("\033[30;47m[ Info ] Option is invalid, Try another option.\033[0m")

def main():
    set_terminal_background()
    print_banner()

    while True:
        print("\033[30;47m1 - Hook\033[0m")
        print("\033[30;47m2 - Exit and unload\033[0m")
        choice = input("\033[30;47m> \033[0m").strip().lower()

        if choice == "1" or choice == "hook":
            hook_menu()
        elif choice == "2" or choice == "exit":
            print("\033[30;47m[ Info ] Exiting...\033[0m")
            break
        else:
            print("\033[30;47m[ Info ] Option is invalid, Try another option.\033[0m")

if __name__ == "__main__":
    main()
