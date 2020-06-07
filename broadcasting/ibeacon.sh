#!/bin/bash

echo "~ Starting bluetooth"

sudo systemctl start bluetooth

echo "~ Setting up hictool for beacon"

sudo hciconfig hci0 up
sudo hciconfig hci0 leadv 3

echo "~ starting the ibeacon"
sudo hcitool -i hci0 cmd 0x08 0x0008 1E 02 01 1A 1A FF 4C 00 02 15 63 6F 3F 8F 64 91 4B EE 95 F7 D8 CC 64 A8 63 B5 00 00 00 00 C8
