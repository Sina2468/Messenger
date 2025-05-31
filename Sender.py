from scapy.all import IP, ICMP, send
import Setting


def Sender():

    while True:
        text = str(input("Message >>> "))
        if text == "":
            pass
        else:
            Setting.Text = text

        Packet = IP(dst=Setting.Dist_IP) / ICMP() / Setting.Text
        send(Packet)


if __name__ == "__main__":
    Sender()
