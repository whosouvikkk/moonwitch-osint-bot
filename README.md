MoonWitch Tools 🌙
MoonWitch is a streamlined, terminal-based OSINT (Open Source Intelligence) framework designed for rapid data lookups. It provides a clean, purple-themed command-line interface to query external APIs for information gathering.

Preview
Plaintext
    __  __                   __        ___ _       _     
   |  \/  | ___  ___  _ __   \ \      / (_) |_ ___| |__  
   | |\/| |/ _ \/ _ \| '_ \   \ \ /\ / /| | __/ __| '_ \ 
   | |  | | (_)| (_) | | | |   \ V  V / | | || (__| | | |
   |_|  |_|\___/\___/|_| |_|    \_/\_/  |_|\__\___|_| |_|
    
            github.com/who_souvikkk/

[H] Help
[V] Version
[S] Settings

[MoonWitch Lookups]

[01] Phone Number Lookup      [05] TG Username Lookup
[02] UPI Lookup               [06] Instagram Lookup
[03] Vehicle Lookup           [07] [Aadhaar Redacted] Lookup
[04] Location/IP Lookup       [08] PAN Lookup

[00] Exit

┌──(admin@moonwitch)-[C:\MoonWitch-Tools]
└──$ 
Features
Phone Number Lookup

UPI ID Lookup

Vehicle Registration Lookup

Location/IP Tracking

Social Media Lookups (Telegram, Instagram)

Document Verification ([Aadhaar Redacted], PAN)

Prerequisites
Python 3.x

requests library

colorama library

Installation & Configuration
Clone the repository:

Bash
git clone 
cd MoonWitch-Tools
Install the required packages:

Bash
pip install -r requirements.txt
Configure API Access:
To use this tool, you must provide your own API URL and API Key.

Open moonwitch.py in a text editor.

Locate the configuration section at the top:

Python
API_URL = "https://your-api-endpoint.com/api/v1/"
API_KEY = "YOUR_API_KEY_HERE"
If you do not have an API key, you can join and contact me for assistance: https://t.me/moonwitchservices

Usage
Run the script from your terminal:

Bash
python moonwitch.py
Navigate the menu using the numbered options. The tool will prompt you for the specific number or ID required for each lookup.

Disclaimer
This tool is intended for educational and authorized investigative purposes only. The user assumes all responsibility for legal compliance when using this software to query data.