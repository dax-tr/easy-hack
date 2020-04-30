# /usr/bin/env python
# -*- coding : utf-8 -*-
import os
import time
os.system("apt-get install figlet")
os.system("clear")
os.system("figlet Easy-Hack")
ip = input("Target Ip : ")
host = str(input("Target Host : "))
print("""
	1- Easy-Hack V1 
	
	Coder : TheDax
		""")
secenek1 = 1
secenek2 = 2
int(input("Please Choose Your Transaction : "))
if secenek1 == 1:
	os.system("clear")
print("""
	1- Dnsenum
	2- Dnsrecon
	3- Whois
	4- Dmitry
	5- Fierce
	6- Aircrack-ng [Wifi-DDOS]
	7- Uniscan
	8- Nmap
	
		""")
		
info = int(input("Please Choose Your Transaction : "))
if info == 1:
	os.system("clear")
	os.system("dnsenum "+host)
	quit()
if info == 2:
	os.system("clear")
	os.system("dnsrecon -d "+host)
	quit()
if info == 3:
	os.system("clear")
	os.system("whois "+host)
	quit()
if info == 4:
	os.system("clear")
	os.system("dmitry -winsepfb -t 1 "+host)
	quit()
if info == 5:
	os.system("clear")
	os.system("fierce -dns "+host)
	quit()
if info == 6:
	os.system("clear")
	mac = input("Enter MAC Address : ")
	channel = input("Enter the Number of Channels : ")
	os.system("clear")
	os.system("airmon-ng start wlan0")
	os.system("iwconfig wlan0mon channel "+channel)
	os.system("aireplay-ng -0 0 -a "+mac+" wlan0mon")
	
	
if info == 7:
	os.system("clear")
	os.system("uniscan -u "+host+" -qweds")
	quit()
if info == 8:
	os.system("clear")
print("""
	1- Fast Scan
	2- Standart Scan
	3- Full Scan
	4- Anonymous Scan
		""")
nmap = int(input("Please Select Scan Type : "))
if nmap == 1:
	os.system("nmap --mtu 8 -T4 -A -n -Pn "+ip)
	quit()
if nmap == 2:
	os.system("nmap --mtu 8 -sS -sV -Pn "+ip)
	quit()
if nmap == 3:
	os.system("nmap -f 24 -sT -sV  "+ip)
	quit()
if nmap == 4:
	os.system("proxychains nmap -sS -sV --script firewall-bypass -Pn "+ip)
	quit()
