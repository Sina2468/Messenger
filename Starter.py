from Setting import Menu
from Local_IP_finder import Get_local_IP
from os import system


def Starter():
    print(Menu)
    with open("DistIP.txt", "w") as File:
        File.write(str(input("\nDist-IP >>> ")))

    Get_local_IP()

    system("start S_R.bat")
