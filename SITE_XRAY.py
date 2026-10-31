#---------import area-----------
import socket as s
import requests as r
import whois

#-----------variables------------
web = input("enter the website name (e.g. google.com): ")
url = "https://" + web

#-----------Functions------------
def get_ip():
    ip = s.gethostbyname(web)
    return ip

def who_is():
    Who = whois.whois(web)
    return Who.creation_date, Who.expiration_date, Who.registrar

def get_headers():
    response = r.get(url)
    return response.headers.get('Server'), response.status_code, response.headers.get('Content-Type')

#---------Banner-----------------
print(r"""
   ____  ___  __________      _  _____   ___  __
  / __/ / _ \/_  __/ __/____ | |/_/ _ \ / _ \/ / 
 _\ \  / // / / / / _/ /___// / / , _// , _/ /__
/___/ /____/ /_/ /___/     /_/ /_/|_|/_/|_/____/

          [ SITE-XRAY v1.0 | By saksham ]
          [ Advanced OSINT Tool ]
""")
print("-" * 50)

#---------print-----------------
print("\n--- SITE-XRAY REPORT ---")

ip = get_ip()
print(f"[+] IP Address: {ip}")

creation, expire, registrar = who_is()
print(f"[+] Registrar: {registrar}")
print(f"[+] Created On: {creation}")
print(f"[+] Expires On: {expire}")

server, status, ctype = get_headers()
print(f"[+] Status Code: {status} (Live)" if status == 200 else f"[+] Status Code: {status}")
print(f"[+] Server: {server}")
print(f"[+] Content-Type: {ctype}")

print("-" * 50)
