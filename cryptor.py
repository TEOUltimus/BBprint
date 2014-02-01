from Crypto.Cipher import AES
import binascii
import string
import random

alphabet = string.ascii_uppercase + string.ascii_lowercase + string.digits
key = 'nvW3BgJDseA1x3Rn'
key2 = 'u0pt2CGQVJlPZjku'
encoder = AES.new(key, AES.MODE_ECB)

def rand15():
	return ''.join(random.choice(alphabet) for c in range(15))

def encode(plaintext):
	plainlist = list(plaintext)
	for i in range(len(plainlist)):
		plainlist[i] = plainlist[i] + rand15()
	return binascii.hexlify(encoder.encrypt(''.join(plainlist)))

def decode(ciphertext):
	szero = hex(ciphertext)
	sone = binascii.unhexlify(szero[2:len(szero) - 1]) 
	#print sone
	#print str(len(sone))
	stwo = encoder.decrypt(sone)
	sthree = str(stwo)
	plainlist = list(sthree)
	plaintext = ''
	j = 0
	while j < len(plainlist):
		plaintext = plaintext + plainlist[j]
		j = j + 16
	#print plaintext
	return plaintext

#secret = encode('Hello, World!')
#print secret
#print decode(secret)
