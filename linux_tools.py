# /usr/bin/env python
# -*- coding : utf-8 -*-

import os

print("""
Programs :
	1 - Tor
	2 - Lynis
	3 - Armitage
	4 - Aircrack-ng
	5 - P0f
	6 - Xsser
	7 - ProxyChains
	8 - JoomScan
	9 - Gedit
	10 - Owasp-Zap
	11 - JSQL
	12 - Uniscan
	13 - Leafpad
	14 - Gedit
	15 - Dnsmap
	""")

programlar = input("'\033[92m'Install programs ? [Enter] : ")
if  programlar == "E" or "e":

	os.system("apt-get install tor")
	tor = print("OK")
	os.system("apt-get install lynis")
	lynis = print("OK")
	os.system("apt-get install armitage")
	armitage = print("OK")
	os.system("apt-get install aircrack-ng")
	aircrack = print("OK")
	os.system("apt-get install p0f")
	p0f = print("OK")
	os.system("apt-get install xsser")
	xxser = print("OK")
	os.system("apt-get install proxychains")
	proxy = print("OK")
	os.system("apt-get install joomscan")
	joomscan = print("OK")
	os.system("apt-get install gedit")
	gedit = print("OK")
	os.system("apt-get install owasp-zap")
	owas_pzap = print("OK")
	os.system("apt-get install jsql")
	print("OK")
	os.system("apt-get install uniscan")
	owas_pzap = print("OK")
	os.system("apt-get install leafpad")
	owas_pzap = print("OK")
	os.system("apt-get install gedit")
	owas_pzap = print("OK")
	os.system("apt-get install dnsmap")
	owas_pzap = print("OK")
	os.system("apt-get install figlet")
	os.system("clear")
else:
	exit()
güncelleme = input("'\033[92m'Update your operating system? [Enter] : ")

if güncelleme == "E" or "e":
	os.system("apt-get update && apt-get upgrade")
	
else:
	quit()
	exit()

	

while True:
	os.system("clear")
	os.system("figlet THEDAX")
	print("Programs are loaded successfully.")
	quit()
	
