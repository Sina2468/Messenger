from scapy.all import IP, ICMP, send
import Setting
from Cleaner import Cleaner


def Sender():

    while True:
        Setting.Text = str(input("Message >>> "))

        Packet = IP(dst=Setting.Dist_IP, src=Setting.Local_IP) / ICMP() / Setting.Text
        print("------------------------------")
        send(Packet)
        print("------------------------------")
        print()
        print()
        print()


if __name__ == "__main__":
    Cleaner()
    Sender()
