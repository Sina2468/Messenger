Menu: str = """=====================================================

			payam

====================================================="""

Names: list = ["Sender.py", "Receiver.py"]

Text: str = ""

try:
    with open("DistIP.txt", "r") as file:
        Dist_IP: str = str(file.read())
except:
    pass

try:
    with open("localIP.txt", "r") as file:
        Local_IP: str = str(file.read())
except:
    pass

