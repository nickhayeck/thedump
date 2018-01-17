# Weakly Encrypted Chat client using RSA and Diffie-Hellman

import os, socket, random

def isPrime(n):
	n = int(n)
	if n <= 1:
		return False
	elif n<=3:
		return True
	elif n % 2 == 0 or n % 3 == 0:
		return False
	for i in range(5,n):
		if n % i == 0:
			return False
	return True

def GenRandPrime():
	while True:
		rand = int.from_bytes(os.urandom(2),byteorder='little')
		if isPrime(rand) == True:
			return rand


def coda(key, mode, text):
	if mode == 'encode':
		text = '~' + text
		hexstring = hex(int(''.join(str(ord(c)).zfill(3) for c in text))*key*2).replace('0x','')

		return str('%030x' % random.randrange(16**100)) + ''.join(hexstring)
	elif mode == 'decode':
		intJoined = int(int(text[100:], 16)//key//2)
		output = ''.join([chr(int(str(intJoined)[i:i+3])) for i in range(0,len(str(intJoined)),3)])
		return output[1:]

if input('Server or Client?').lower() in ['server','s','serv']:
	g = 0
	p = 0
	x = ord(os.urandom(1))
	secretkey = 1
	#begin server
	TCP_IP = "127.0.0.1"
	TCP_PORT = 888
	BUFFER_SIZE = 1024

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((TCP_IP, TCP_PORT))
	s.listen(1)
	print("start success on {0}:{1}".format(TCP_IP,TCP_PORT))
	conn, addr = s.accept()
	print("Connection address:", addr[0])

	if input('Initiate Diffie-Hellman Handshake?').lower() in ['y','yes','ye','yeah']:
		#assign rand values to g, p
		g = GenRandPrime()
		p = GenRandPrime()

		#output g, p, and x for logging purposes: eliminate later
		#print('g: '+str(g), 'p: '+str(p), 'x: '+str(x))

		#sends g, p and key-x, then waits for key-y: later change to send one single array
		conn.send(str(g).encode())
		ok = conn.recv(BUFFER_SIZE)

		conn.send(str(p).encode())
		ok = conn.recv(BUFFER_SIZE)

		conn.send(str((g**x%p)).encode())
		data = conn.recv(BUFFER_SIZE).decode()

		#shared private key
		secretkey = int(data)**x%p

		print('responding with: \'encryption established\'\n')
		conn.send('encryption established\n'.encode())

	#chat loop: later add in encryption
	inp = ''
	while inp != 'q':
		inp = str(input('-> '))
		if inp != '':
			conn.send(coda(secretkey, 'encode', str(inp)).encode())
	s.shutdown(socket.SHUT_RDWR)
	s.close()

else:
	g = 0
	p = 0
	keyx = 0
	secretkey = 1
	y = ord(os.urandom(1))
	ip = input('Server IP: ')
	port = int(input('Server Port: '))
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
		s.connect((ip,port))
	except KeyboardInterrupt:
	 	s.shutdown()
	 	s.close()
	except:
	 	print('uhhhh error')
	 	s.close()
	g = int(s.recv(1024).decode())
	s.send(str(g).encode())
	p= int(s.recv(1024).decode())
	s.send(str(p).encode())
	keyx= int(s.recv(1024).decode())
	s.send(str(g**y%p).encode())
	secretkey = keyx**y%p
	if s.recv(1024) == 'encryption established':
		print('~~encryption established~~')
	while 1:
		received = s.recv(1024)
		if received != '':
			print('==> ' + coda(secretkey, 'decode',received.decode()))
