#!/bin/bash

echo "~ Starting bluetooth"

sudo systemctl start bluetooth

echo "~ Setting up hictool for beacon"

sudo hciconfig hci0 up
sudo hciconfig hci0 leadv 3

echo "~ starting the ibeacon"
sudo hcitool -i hci0 cmd 0x08 0x0008 15 02 01 06 03 03 aa fe 0d 16 aa fe 10 00 03 67 69 74 68 75 62 00 00 00 00 00 00 00 00 00 00 00
