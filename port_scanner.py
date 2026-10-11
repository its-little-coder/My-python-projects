import socket

target = "github.com" 
port = 80

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(2.0)

try:
    result = s.connect_ex((target, port))
    
    if result == 0:
        print(f"🎉 Port {port} on {target} is OPEN!")
    else:
        print(f"🔒 Port {port} on {target} is closed.")
    s.close()
except Exception as e:
    print(f"Connection failed: {e}")

