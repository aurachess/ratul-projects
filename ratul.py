import os
import sys
import time
import random

# ANSI Escape Codes for Colors
RED = "\033[91m"
BOLD = "\033[1m"
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RESET = "\033[0m"

def banner():
    os.system("clear")
    art = f"""{RED}{BOLD}
          ,xHMMMMMMMMHdx,      000\\
        .HMMMMMMMMMMMMMMMh.    00000000
       .MMMMMMMMMMMMMMMMMMM.   / 0000000
       MMMMMMMMMMMMMMMMMMMMM:  / D000000
       MMMMMMMMMMMMMMMMMMMMM:     D0000
       `MMMMMMMMMMMMMMMMMMM:'      D000
        `MMMMMMMMMMMMMMMMM:'       D000
          `*HMMMMMMMMMH*;'         D000
             `'***`''              DOO
                                   DOO
                                   00
                                   00
                                   0
    """
    print(art)
    
    print(f"{RED}{BOLD} ██████╗  █████╗ ████████╗██╗   ██╗██╗     ")
    print(f" ██╔══██╗██╔══██╗╚══██╔══╝██║   ██║██║     ")
    print(f" ██████╔╝███████║   ██║   ██║   ██║██║     ")
    print(f" ██╔══██╗██╔══██║   ██║   ██║   ██║██║     ")
    print(f" ██║  ██║██╔══██║   ██║   ╚██████╔╝███████╗")
    print(f" ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚══════╝")
    
    print(f"   ↓     ↓     ↓     ↓     ↓     ↓     ↓")
    print(f"   🩸    🩸    🩸    🩸    🩸    🩸    🩸")
    print(f"     🩸      🩸      🩸      🩸      🩸\n")
    print(f"{CYAN}========== [ Made by Ratul ] =========={RESET}\n")

def main_menu():
    banner()
    print(f"{YELLOW}[+] Select Target Platform (TEST / PRANK):{RESET}\n")
    print(f"{GREEN}[1]{RESET} Facebook Account Hack")
    print(f"{GREEN}[2]{RESET} Instagram Account Hack")
    print(f"{GREEN}[3]{RESET} TikTok Account Hack")
    print(f"{GREEN}[4]{RESET} YouTube Account Hack")
    print(f"{GREEN}[5]{RESET} WhatsApp Account Hack")
    print(f"{GREEN}[6]{RESET} Messenger Account Hack")
    print(f"{GREEN}[7]{RESET} IMO Account Hack")
    print(f"{RED}[0]{RESET} Exit\n")
    
    choice = input(f"{BOLD}{CY5AN}Ratul@Tool:~# {RESET}")
    
    platforms = {
        "1": "Facebook",
        "2": "Instagram",
        "3": "TikTok",
        "4": "YouTube",
        "5": "WhatsApp",
        "6": "Messenger",
        "7": "IMO"
    }
    
    if choice in platforms:
        p_name = platforms[choice]
        os.system("clear")
        banner()
        print(f"{YELLOW}[*] Target Selected: {p_name}{RESET}")
        phone = input(f"{YELLOW}[?] Enter Target Phone Number / Username: {RESET}")
        
        print(f"\n{RED}[+] Connecting to {p_name} servers...")
        time.sleep(1.5)
        print(f"[+] Bypassing security firewalls...")
        time.sleep(2)
        print(f"[+] Extracting database hashes for {phone}...")
        time.sleep(2)
        
        # কিছু ফানি ফেক পাসওয়ার্ড
        fake_passwords = [
            "P@ssw0rd123", "iloveyou99", "password_kui_bujhsi", 
            "hacker_bhai_maaf_koro", "bhul_bhal_pass_123", "amar_sonar_bangla"
        ]
        hacked_pass = random.choice(fake_passwords)
        
        print(f"\n{GREEN}[SUCCESS] Account Hacked Successfully! 🎉{RESET}")
        print(f"{CYAN}----------------------------------------{RESET}")
        print(f"{BOLD} Target ID  : {phone}")
        print(f"{BOLD} Fake Pass  : {RED}{hacked_pass}{RESET}")
        print(f"{CYAN}----------------------------------------{RESET}")
        print(f"{YELLOW}\n(Disclaimer: This is just a prank tool for fun! 🤣){RESET}\n")
        
        input(f"{GREEN}Press Enter to go back to menu...{RESET}")
        main_menu()
        
    elif choice == "0":
        print(f"\n{RED}Exiting... Bye Bye! 👋{RESET}")
        sys.exit()
    else:
        print(f"\n{RED}[!] Invalid Choice! Try again.{RESET}")
        time.sleep(1.5)
        main_menu()

if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print(f"\n\n{RED}[!] Program Interrupted. Exiting...{RESET}")
        sys.exit()
