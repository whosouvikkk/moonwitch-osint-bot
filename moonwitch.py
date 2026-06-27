import sys
import httpx
import os
import time
from urllib.parse import quote

API_MAP = {
    "01": ("Phone Number Lookup", "API_URL_NUM_HERE"),
    "02": ("UPI Lookup", "API_URL_UPI_HERE"),
    "03": ("Vehicle Lookup", "API_URL_VEHICLE_HERE"),
    "04": ("TG Username Lookup", "API_URL_TG_HERE"),
    "05": ("Aadhaar Lookup", "API_URL_AADHAAR_HERE")
}

RED = '\033[31m'      
W = '\033[97m'        
R = '\033[0m'         
BR = f"\033[1m{RED}"  

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_ui():
    clear_screen()
    ui = f"""{BR}
 ███╗   ███╗ ██████╗  ██████╗ ███╗   ██╗██╗    ██╗██╗████████╗ ██████╗██╗  ██╗
 ████╗ ████║██╔═══██╗██╔═══██╗████╗  ██║██║    ██║██║╚══██╔══╝██╔════╝██║  ██║
 ██╔████╔██║██║   ██║██║   ██║██╔██╗ ██║██║ █╗ ██║██║   ██║   ██║     ███████║
 ██║╚██╔╝██║██║   ██║██║   ██║██║╚██╗██║██║███╗██║██║   ██║   ██║     ██╔══██║
 ██║ ╚═╝ ██║╚██████╔╝╚██████╔╝██║ ╚████║╚███╔███╔╝██║   ██║   ╚██████╗██║  ██║
 ╚═╝     ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝ ╚══╝╚══╝ ╚═╝   ╚═╝    ╚═════╝╚═╝  ╚═╝
                {W}https://t.me/moonwitchservices{R}

  {RED}[H]{W} Help          {RED}[V]{W} Version          {RED}[C]{W} Contact

  {RED}[Osint Modules]{W}                             {RED}[System & Plugins]{W}

  {RED}[01]{W} Phone Number Lookup                   {RED}[00]{W} Exit System
  {RED}[02]{W} UPI Lookup                            {RED}[..]{W} Update Tool
  {RED}[03]{W} Vehicle Lookup           
  {RED}[04]{W} TG Username Lookup
  {RED}[05]{W} Aadhaar Lookup
{R}"""
    print(ui)

def filter_and_format(data_dict):
    """Filters out API metadata and prints results line by line cleanly."""
    hidden_keys = {
        "powered by", "api info", "key owner", "remaining", 
        "dailyremaining", "limit", "used", "created", "expiry", 
        "status", "success", "developer", "credit"
    }
    
    print(f"\n{BR} ┌── Target Acquired {R}")
    print(f"{BR} │ {R}")
    
    for key, value in data_dict.items():
        clean_key = str(key).replace('_', ' ').strip()
        key_lower = clean_key.lower()
        
        if key_lower in hidden_keys:
            continue
            
        if isinstance(value, dict):
            if key_lower == "api info":
                continue
            for sub_key, sub_val in value.items():
                clean_sub_key = str(sub_key).replace('_', ' ').strip()
                if clean_sub_key.lower() not in hidden_keys:
                    print(f"{BR} ├─ {R}{clean_sub_key.title()}: {sub_val}")
                    
        elif isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    for list_key, list_val in item.items():
                        clean_list_key = str(list_key).replace('_', ' ').strip()
                        if clean_list_key.lower() not in hidden_keys:
                            print(f"{BR} ├─ {R}{clean_list_key.title()}: {list_val}")
                else:
                    print(f"{BR} ├─ {R}{item}")
        else:
            print(f"{BR} ├─ {R}{clean_key.title()}: {value}")
            
    print(f"{BR} │ {R}")
    print(f"{BR} └── End of Report ─────────────────────────────────────────{R}\n")

def run_lookup(api_url, query):
    try:
        print(f"\n{RED}[*] Querying shadows for '{query}'...{R}")
        with httpx.Client(timeout=30.0) as client:
            resp = client.get(f"{api_url}{quote(query)}")
            if resp.status_code == 200:
                time.sleep(0.5) 
                filter_and_format(resp.json())
            else:
                print(f"{BR}[!] Connection Interrupted:{R}{RED} API returned status code {resp.status_code}{R}")
    except Exception as e:
        print(f"{BR}[!] Fatal Error:{R}{RED} {e}{R}")

def show_help():
    print(f"\n{BR} ┌── MoonWitch Documentation {R}")
    print(f"{BR} │ {R}")
    print(f"{BR} ├─ {W}[01] Phone Number Lookup{R}: Enter target 10-digit mobile number.")
    print(f"{BR} ├─ {W}[02] UPI Lookup         {R}: Enter valid UPI ID (e.g., target@bank).")
    print(f"{BR} ├─ {W}[03] Vehicle Lookup     {R}: Enter target vehicle registration.")
    print(f"{BR} ├─ {W}[04] TG Username Lookup {R}: Enter Telegram username (without @).")
    print(f"{BR} ├─ {W}[05] Aadhaar Lookup     {R}: Enter 12-digit Aadhaar number.")
    print(f"{BR} ├─ {W}[00] Exit System        {R}: Safely terminate connection.")
    print(f"{BR} │ {R}")
    print(f"{BR} ├─ {W}If you don't have an API, contact on Telegram:{R}")
    print(f"{BR} ├─ {W}https://t.me/moonwitchservices{R}")
    print(f"{BR} └── ───────────────────────────────────────────────────────{R}\n")

def main():
    display_ui()
    while True:
        prompt_str = f"{RED}┌──(admin@moonwitch)─[C:\\MoonWitch-Tools]\n└──${R} "
        try:
            choice = input(prompt_str).strip()
        except KeyboardInterrupt:
            print(f"\n{RED}[*] Force quitting...{R}")
            sys.exit()
            
        if choice in ["00", "0"]:
            print(f"{RED}[*] Shutting down systems...{R}")
            sys.exit()
            
        elif choice.lower() == 'h':
            show_help()
        elif choice.lower() == 'v':
            print(f"\n{BR}[*] MoonWitch Terminal Version:{R} {W}v2{R}\n")
        elif choice.lower() == 'c':
            print(f"\n{BR}[*] Official Contact:{R} {W}https://t.me/moonwitchservices{R}\n")
            
        elif choice in API_MAP or (choice.startswith('0') and choice in API_MAP):
            key = choice if len(choice) == 2 else f"0{choice}"
            if key in API_MAP:
                api_info = API_MAP[key]
                query = input(f"\n{BR}[?]{R}{RED} Enter target for {api_info[0]}: {R}").strip()
                run_lookup(api_info[1], query)
        else:
            if choice != "":
                print(f"{BR}[!]{R}{RED} Invalid command sequence. Type 'H' for help.{R}")

if __name__ == "__main__":
    main()
