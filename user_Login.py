import socket
def login():
    name = input("Enter your Name: ")
    password = input("Password: ")
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)
    return [name, password, IPAddr, hostname]
