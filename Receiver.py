from scapy.all import sniff
from Setting import Local_IP, Dist_IP
from Cleaner import Cleaner


def Receiver():

    while True:
        print()
        print("------------------------------")
        print()
        print(
            str(
                sniff(
                    count=1,
                    filter=f"icmp and src host {Dist_IP} and dst host {Local_IP}",
                )[0].load
            )[2:-1]
        )


if __name__ == "__main__":
    Cleaner()
    Receiver()
