import socket

def scan(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((host, port))
        print("Port open: " + str(port))
        s.close()
    except:
        print("Port closed: " + str(port))

host = "34.104.35.123"
for port in [443, 80, 63933]:
    scan(host, port)
