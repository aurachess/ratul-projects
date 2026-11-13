import os
import sys
import time

# ANSI Escape Codes for Colors (Red & Cyan/Blue style)
RED = "\033[91m"
BOLD = "\033[1m"
CYAN = "\033[96m"
RESET = "\033[0m"

def banner():
    os.system("clear")
    # উপরের অ্যাসকি আর্ট বা লোগো অংশ
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
    
    # মূল নাম "RATUL" বড় অক্ষরে দেখানোর জন্য
    print(f"{RED}{BOLD} ██████╗  █████╗ ████████╗██╗   ██╗██╗     ")
    print(f" ██╔══██╗██╔══██╗╚══██╔══╝██║   ██║██║     ")
    print(f" ██████╔╝███████║   ██║   ██║   ██║██║     ")
    print(f" ██╔══██╗██╔══██║   ██║   ██║   ██║██║     ")
    print(f" ██║  ██║██║  ██║   ██║   ╚██████╔╝███████╗")
    print(f" ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚══════╝")
    
    # রক্তের ফোঁটা বা ড্রপ ইফেক্ট
    print(f"   ↓     ↓     ↓     ↓     ↓     ↓     ↓")
    print(f"   🩸    🩸    🩸    🩸    🩸    🩸    🩸")
    print(f"     🩸      🩸      🩸      🩸      🩸\n")
    
    # নিচে ক্রেডিটের লাইন
    print(f"{CYAN}========== [ Made by Ratul ] =========={RESET}\n")

if __name__ == "__main__":
    banner()