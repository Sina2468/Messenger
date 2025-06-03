from socket import gethostname, gethostbyname


def Get_local_IP():
    hostname = gethostname()

    with open("localIP.txt", "w") as file:
        file.write(str(gethostbyname(hostname)))
