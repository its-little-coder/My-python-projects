import socket
target = "hack.com"
try:                                                  
    for port in [21, 22, 80, 443]:
        s = socket.socket()
        s.settimeout(1)                                  
    if s.connect_ex((target, port)) == 0:
            print(f"{port} OPEN 🎉")
        s.close()
except Exception as e:
    print(e)
