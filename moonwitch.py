import os
import sys
import requests
from colorama import init, Fore, Style

init(autoreset=True)

API_URL = "https://your-api-endpoint.com/api/v1/"
API_KEY = "YOUR_API_KEY_HERE"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    banner = f"""{Fore.MAGENTA}
    __  __                   __        ___ _       _     
   |  \/  | ___  ___  _ __   \ \      / (_) |_ ___| |__  
   | |\/| |/ _ \/ _ \| '_ \   \ \ /\ / /| | __/ __| '_ \ 
   | |  | | (_)| (_) | | | |   \ V  V / | | || (__| | | |
   |_|  |_|\___/\___/|_| |_|    \_/\_/  |_|\__\___|_| |_|
    {Style.RESET_ALL}
            github.com/whosouvikkk
    """
    print(banner)

def print_menu():
    menu = f"""
{Fore.MAGENTA}[H]{Style.RESET_ALL} Help
{Fore.MAGENTA}[V]{Style.RESET_ALL} Version
{Fore.MAGENTA}[S]{Style.RESET_ALL} Settings

{Fore.MAGENTA}[MoonWitch Lookups]{Style.RESET_ALL}

{Fore.MAGENTA}[01]{Style.RESET_ALL} Phone Number Lookup      {Fore.MAGENTA}[05]{Style.RESET_ALL} TG Username Lookup
{Fore.MAGENTA}[02]{Style.RESET_ALL} UPI Lookup               {Fore.MAGENTA}[06]{Style.RESET_ALL} Instagram Lookup
{Fore.MAGENTA}[03]{Style.RESET_ALL} Vehicle Lookup           {Fore.MAGENTA}[07]{Style.RESET_ALL} Aadhaar Lookup
{Fore.MAGENTA}[04]{Style.RESET_ALL} Location/IP Lookup       {Fore.MAGENTA}[08]{Style.RESET_ALL} PAN Lookup

{Fore.MAGENTA}[00]{Style.RESET_ALL} Exit
"""
    print(menu)

def query_api(endpoint, query_param, query_value):
    """
    Handles API requests. Checks if the API is configured first.
    Prints details line by line if successful.
    """
    print(f"\n{Fore.YELLOW}[*] Initializing search for: {query_value}...{Style.RESET_ALL}")
    
    if API_URL == "https://your-api-endpoint.com/api/v1/" or API_KEY == "YOUR_API_KEY_HERE":
        print(f"\n{Fore.RED}[-] API is not provided or configured.{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}[!] Please update API_URL and API_KEY in the source code to view actual details.{Style.RESET_ALL}")
        input(f"\n{Fore.MAGENTA}[Press Enter to return to menu...]{Style.RESET_ALL}")
        return

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    params = {query_param: query_value}
    
    try:
        response = requests.get(f"{API_URL}{endpoint}", headers=headers, params=params)
        
        if response.status_code == 200:
            data = response.json()
            print(f"\n{Fore.GREEN}[+] Results Found:{Style.RESET_ALL}")
            
            for key, value in data.items():
                print(f"    {Fore.MAGENTA}>{Style.RESET_ALL} {key.capitalize()}: {value}")
        else:
            print(f"\n{Fore.RED}[-] Error {response.status_code}: {response.text}{Style.RESET_ALL}")
            
    except Exception as e:
        print(f"\n{Fore.RED}[-] Connection Error: {str(e)}{Style.RESET_ALL}")
        
    input(f"\n{Fore.MAGENTA}[Press Enter to return to menu...]{Style.RESET_ALL}")

def main():
    while True:
        clear_screen()
        print_banner()
        print_menu()
        
        
        choice = input(f"{Fore.MAGENTA}┌──(admin@moonwitch)-[C:\\MoonWitch-Tools]\n└──${Style.RESET_ALL} ").strip()

        if choice == '01':
            target = input(f"{Fore.MAGENTA}[?]{Style.RESET_ALL} Enter Phone Number to search: ")
            query_api("lookup/phone", "number", target)
        elif choice == '02':
            target = input(f"{Fore.MAGENTA}[?]{Style.RESET_ALL} Enter UPI ID to search: ")
            query_api("lookup/upi", "vpa", target)
        elif choice == '03':
            target = input(f"{Fore.MAGENTA}[?]{Style.RESET_ALL} Enter Vehicle Registration to search: ")
            query_api("lookup/vehicle", "reg_no", target)
        elif choice == '04':
            target = input(f"{Fore.MAGENTA}[?]{Style.RESET_ALL} Enter IP Address to search: ")
            query_api("lookup/ip", "address", target)
        elif choice == '05':
            target = input(f"{Fore.MAGENTA}[?]{Style.RESET_ALL} Enter Telegram Username to search: ")
            query_api("lookup/telegram", "username", target)
        elif choice == '06':
            target = input(f"{Fore.MAGENTA}[?]{Style.RESET_ALL} Enter Instagram Handle to search: ")
            query_api("lookup/instagram", "handle", target)
        elif choice == '07':
            target = input(f"{Fore.MAGENTA}[?]{Style.RESET_ALL} Enter Aadhaar Number to search: ")
            query_api("lookup/aadhaar", "uid", target)
        elif choice == '08':
            target = input(f"{Fore.MAGENTA}[?]{Style.RESET_ALL} Enter PAN Number to search: ")
            query_api("lookup/pan", "pan_no", target)
        elif choice.lower() == 'h':
            print(f"\n{Fore.MAGENTA}[Help]{Style.RESET_ALL} Select a number from the menu to perform a lookup. Configure your API keys in the source code.")
            input("\nPress Enter to continue...")
        elif choice.lower() == 'v':
            print(f"\n{Fore.MAGENTA}MoonWitch v1.1.0{Style.RESET_ALL} (Purple Edition)")
            input("\nPress Enter to continue...")
        elif choice in ['00', 'exit', 'quit']:
            print(f"\n{Fore.MAGENTA}[!] Exiting MoonWitch...{Style.RESET_ALL}")
            sys.exit(0)
        else:
            print(f"\n{Fore.RED}[-] Invalid option.{Style.RESET_ALL}")
            import time
            time.sleep(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{Fore.MAGENTA}[!] Session Terminated by User.{Style.RESET_ALL}")
        sys.exit(0)