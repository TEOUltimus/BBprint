from Crypto.Cipher import AES
import binascii, random, string

alphabet = string.ascii_uppercase + string.ascii_lowercase + string.digits
key = 'nvW3BgJDseA1x3Rn'
key2 = 'u0pt2CGQVJlPZjku'
encoder = AES.new(key, AES.MODE_ECB)

# return 15 random ascii characters
def rand15():
	return ''.join(random.choice(alphabet) for c in range(15))

# encode a block of plaintext using key
def encode(plaintext):
	plainlist = list(plaintext)
	for i in range(len(plainlist)):
		plainlist[i] = plainlist[i] + rand15()
	return binascii.hexlify(encoder.encrypt(''.join(plainlist)))

#decode encrypted text using key
def decode(ciphertext):
	hextext = hex(ciphertext)
	code = binascii.unhexlify(hextext[2:len(hextext) - 1]) 
	uncode = str(encoder.decrypt(code))
	plainlist = list(uncode)
	plaintext = ''
	j = 0
	while j < len(plainlist):
		plaintext = plaintext + plainlist[j]
		j = j + 16
	return plaintext

'''secret = encode('Hello, World!')
print secret
print decode(int(secret, 16))'''
