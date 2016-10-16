macAddr_usrIn = input("Enter the first 3 bytes of the MAC address (ie AB:BC:CD): ")


manuf = open("manuf.txt",encoding="utf-8")


for line in manuf:

    if macAddr_usrIn in line:
        print(line.encode("utf-8"))

