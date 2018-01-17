import hashlib
import os
from Tkinter import Tk
from tkFileDialog import askopenfilename
from threading import Thread
import time

def testPassword(inp,enc):
	if hashlib.sha512(inp).hexdigest() == enc:
		print '\r\n[$] Password Found: ' + inp
try:		
	encryptedPass = raw_input('(-) Input the Encrypted Password:')
	print('\r\n(-) Please select wordlist')
	time.sleep(3)
	Tk().withdraw()
	filename = askopenfilename()

	with open(filename) as myList:
		for line in myList:
			testPassword(line[:-1], encryptedPass)
			

except KeyboardInterrupt:
	pass