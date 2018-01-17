import crypt
import os
from Tkinter import Tk
from tkFileDialog import askopenfilename
import io
import time

def testPassword(inp,salt,enc):
	if crypt.crypt(inp,salt) == enc:
		print '\r\n[$] Password Found: ' + inp
try:		
	encryptedPass = raw_input('(-) Input the Encrypted Password:')
	salt = encryptedPass[:2]
	print('\r\n(-) Please select wordlist')
	time.sleep(3)
	Tk().withdraw()
	filename = askopenfilename()

	with open(filename) as myList:
		for line in myList:
			testPassword (line[:-1], salt, encryptedPass)

except KeyboardInterrupt:
	print'\r\nInterrupted By User\r\n'
	pass