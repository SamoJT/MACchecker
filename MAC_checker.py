#Please note, i was struggling on how to make python download the text file from either my github or the wireshark source hence the
#need for the user input! Not efficient or smooth but works..

a = input("Is wireshark installed? y or n: ")
print()

if a == ("y"):
    macAddr_usrIn = input("Enter the first 3 bytes of the MAC address (ie AB:BC:CD): ")
    print()
    manuf = open("/usr/share/wireshark/manuf",encoding="utf-8") 
    for line in manuf:
        if macAddr_usrIn in line:
            print(line.encode("utf-8"))

elif a == ("n"): 
    print("Please click this link to download the text file required for the program:")
    print("https://raw.githubusercontent.com/SamoJT/MACchecker/master/manuf.txt")
    print("Ensure it is in the same directory as this program.")
    print("If you're unable to download, copy and paste into a text document and name manuf.txt")
    print()
    b = input("When downloaded and in same directory press y to continue: ")
    if b == ("y"):
        macAddr_usrIn = input("Enter the first 3 bytes of the MAC address (ie AB:BC:CD): ")
        print()
        manuf = open("manuf.txt",encoding="utf-8") 
        for line in manuf:
            if macAddr_usrIn in line:
                print(line.encode("utf-8"))
    else:
        print("Invalid input, please restart program.")
else:
    print("Invalid input, please restart program.")
