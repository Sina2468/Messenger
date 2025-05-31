import Setting
from os import system


def Starter():
    print(Setting.Menu)
    Setting.Dist_IP = str(input("\nDist-IP >>> "))

    for name in Setting.Names:
        system(name)
