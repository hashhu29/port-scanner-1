import socket

def scanning(targethost, portrange):
    openports = []
    for ports in portrange:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(3)

        results = sock.connect_ex((targethost, ports))

        if results == 0:
            openports.append(ports)

            sock.close()

            return openports
        scanning()
        
def main(targethost, portrange):
    targethost = "209.27.233.19"
    portrange = range(1, 2001)

    openports = scanning(targethost, portrange)

    if openports:
        print("Open")
        for ports in openports:
            print(ports)
    else:
        print("No ports.")

    if __name__ == "__main__":
        main()

