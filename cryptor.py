from Crypto.Cipher import AES
import binascii
key = 'nvW3BgJDseA1x3Rn'
key2 = 'u0pt2CGQVJlPZjku'
encoder = AES.new(key, AES.MODE_ECB)
from simplecrypt import encrypt, decrypt

def encode(plaintext):
	return encoder.encrypt(plaintext)

def decode(ciphertext):
	return encoder.decrypt(ciphertext)

secret = encode('Hello, World!')
print secret
print decode(secret)
