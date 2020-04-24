import os, sys


# beacon_type = sys.argv[1]
# print(beacon_type)
class PiError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        print("PiError")

        if self.message:
            return "PiError, {0}".format(self.message)
        else:
            return "PiError, unidentified error occures in hci tools up"


def instruction():

    print("open a different terminal and run :")
    print("systemctl start bluetooth (this will acrive bluetooth)")


def ibeacon():
    try:
        os.system("sudo hciconfig hci0 up")
        os.system("sudo hciconfig hci0 leadv 3")
        os.system(
            "sudo hcitool -i hci0 cmd 0x08 0x0008 1E 02 01 1A 1A FF 4C 00 02 15 63 6F 3F 8F 64 91 4B EE 95 F7 D8 CC 64 A8 63 B5 00 00 00 00 C8"
        )

    except Exception as e:
        raise PiError(str(e))


def EddystoneUrl():
    try:
        os.system("sudo hciconfig hci0 up")
        os.system("sudo hciconfig hci0 leadv 3")
        os.system(
            "sudo hcitool -i hci0 cmd 0x08 0x0008 15 02 01 06 03 03 aa fe 0d 16 aa fe 10 00 03 67 69 74 68 75 62 00 00 00 00 00 00 00 00 00 00 00"
        )
    except Exception as e:
        raise PiError(str(e))


if __name__ == "__main__":
    beacon_type = input("enter beacon type (ibeacon or edystone)  : ")

    if beacon_type not in ["ibeacon", "edystone"]:
        print('beacon type is wrong')
        sys.exit()

    if beacon_type == "ibeacon":
        ibeacon()
        sys.exit()

    EddystoneUrl()
