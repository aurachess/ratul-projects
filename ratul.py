import os
import sys
import time
import random
import socket

# ANSI Escape Codes for Professional Hacker Colors
BLACK = "\033[30m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
WHITE = "\033[97m"
BOLD = "\033[1m"
RESET = "\033[0m"

def clear_screen():
    os.system("clear")

def banner():
    clear_screen()
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
    print(f" ██║  ██║██║  ██║   ██║   ╚██████╔╝███████╗")
    print(f" ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚══════╝")
    print(f"   ↓     ↓     ↓     ↓     ↓     ↓     ↓")
    print(f"   🩸    🩸    🩸    🩸    🩸    🩸    🩸")
    print(f"     🩸      🩸      🩸      🩸      🩸\n")
    
    print(f"{GREEN}┌────────────────────────────────────────┐{RESET}")
    print(f"{GREEN}│{RESET} {BOLD}{CYAN}  [ SYSTEM: EXPLOIT v4.5.1 ]           {RESET}{GREEN}│{RESET}")
    print(f"{GREEN}│{RESET} {BOLD}{WHITE}  [ OPERATOR: RATUL (ELITE) ]          {RESET}{GREEN}│{RESET}")
    print(f"{GREEN}└────────────────────────────────────────┘{RESET}\n")

def matrix_effect():
    print(f"{GREEN}")
    chars = "01010101ABCDEF#@$%&*<>XYZ"
    for _ in range(8):
        line = "".join(random.choice(chars) for _ in range(50))
        print(line)
        time.sleep(0.04)
    print(f"{RESET}")

def progress_bar(description):
    print(f"\n{YELLOW}[*] {description}{RESET}")
    for i in range(101):
        bar = '█' * (i // 2) + '-' * (50 - (i // 2))
        sys.stdout.write(f"\r{GREEN}[{bar}] {i}%{RESET}")
        sys.stdout.flush()
        time.sleep(random.uniform(0.02, 0.06))
    print("\n")

def main_menu():
    banner()
    print(f"{WHITE}  Select Exploit Module:{RESET}\n")
    print(f"{GREEN}  [1]{RESET} {WHITE}Facebook Target Breacher{RESET}")
    print(f"{GREEN}  [2]{RESET} {WHITE}Instagram Session Hijacker{RESET}")
    print(f"{GREEN}  [3]{RESET} {WHITE}TikTok API Injector{RESET}")
    print(f"{GREEN}  [4]{RESET} {WHITE}YouTube Sub-Zero Exploit{RESET}")
    print(f"{GREEN}  [5]{RESET} {WHITE}WhatsApp End-to-End Decryptor{RESET}")
    print(f"{GREEN}  [6]{RESET} {WHITE}Messenger Packet Sniffer{RESET}")
    print(f"{GREEN}  [7]{RESET} {WHITE}IMO Database Extractor{RESET}")
    print(f"{RED}  [0]{RESET} {WHITE}Abort / Exit{RESET}\n")
    
    choice = input(f"{BOLD}{RED}ratul@root-pc:~# {RESET}")
    
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
        clear_screen()
        banner()
        print(f"{CYAN}[+] Selected Module: {p_name} Exploit Framework{RESET}")
        target = input(f"{YELLOW}[?] Enter Target Phone / Username / IP: {WHITE}")
        
        # রিয়েল হ্যাকিংয়ের মতো টার্মিনাল লগ দেখানো
        matrix_effect()
        print(f"{RED}[!] Resolving target host: {target}...{RESET}")
        time.sleep(1)
        print(f"{GREEN}[+] Connection established with remote gateway (Port 443)...{RESET}")
        time.sleep(1.2)
        print(f"{BLUE}[+] Injecting payload into secure socket layer (SSL)...{RESET}")
        time.sleep(1.5)
        
        # প্রোগ্রেস বার
        progress_bar(f"Bypassing {p_name} 2FA & Firewalls")
        
        print(f"{MAGENTA}[*] Dumping memory hashes and session cookies...{RESET}")
        time.sleep(2)
        
        fake_passwords = [
            "Rx9#mK$2026", "Dark_Lord_99", "Shadow_Bypass_X", 
            "Root_Access_Granted", "Cyber_Ghost#1", "NullPointerException",
            "Matrix_Pass_777", "Access_Denied_Lol"
        ]
        hacked_pass = random.choice(fake_passwords)
        fake_ip = f"{random.randint(10,192)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}"
        
        print(f"\n{GREEN}{BOLD}==========================================")
        print(f" [✔] TARGET COMPROMISED SUCCESSFULLY! 🚀")
        print(f"=========================================={RESET}")
        print(f" {CYAN}Target ID/Phone :{RESET} {WHITE}{target}{RESET}")
        print(f" {CYAN}Fake IP Addr    :{RESET} {YELLOW}{fake_ip}{RESET}")
        print(f" {CYAN}Extracted Pass  :{RESET} {RED}{BOLD}{hacked_pass}{RESET}")
        print(f" {CYAN}Session Token   :{RESET} {GREEN}Bearer_eyJhbGciOi...{RESET}")
        print(f"{GREEN}{BOLD}=========================================={RESET}")
        print(f"{YELLOW}\n (Note: Purely a Prank Simulation created by Ratul! 🤣){RESET}\n")
        
        input(f"{MAGENTA}Press [Enter] to return to terminal core...{RESET}")
        main_menu()
        
    elif choice == "0":
        print(f"\n{RED}[!] Terminating session... Goodbye, Commander! 👋{RESET}")
        sys.exit()
    else:
        print(f"\n{RED}[!] Invalid command option! Type a valid choice.{RESET}")
        time.sleep(1.5)
        main_menu()

if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print(f"\n\n{RED}[!] Interrupt signal received. Shutting down safely...{RESET}")
        sys.exit()
