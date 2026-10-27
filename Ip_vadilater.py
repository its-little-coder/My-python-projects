import re
def is_valid_ip(ip):
    parts = ip.split(".")
    for part in parts:
        if int(part) > 255:
            return False
    return True

# Test
ips = input("give you ip: ")

for ip in ips:
    if is_valid_ip(ip):
        print(ip, "-> Valid IP")
    else:
        print(ip, "-> Invalid IP")
