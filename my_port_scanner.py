
import socket

port = [20, 21 , 22, 23, 42, 43, 53, 67, 69, 80]

host = input("Enter hostname or IP adress:")

for i in port:
	print(str(i))
	try:
		print("one")
		scan = socket.socket()
		print("Scanning " + str(i) + " port on host " + host)
		#scan.settimeout(0.5)
		scan.connect((host, i))
	except scan.error:
		print("Port -- ", port, " -- [CLOSED]")
	else:
		print("Port -- ", port, " -- [OPEN]")