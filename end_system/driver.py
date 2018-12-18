#!/usr/bin/env python
import os
from Cryptography.Encryption import Encryption
from Cryptography.Decryption import Decryption
from Steganography.Steganography_driver import *

def end_note():
	os.system('clear')
	print('Thank you for using Stegancryption..!')

os.system('clear')
print('Welcome...')
opt = input('Menu\n1 - Stegancryption Hide\n2 - Stegancryption Reveal\nEnter Here : ')

if opt == '1':
	os.system('clear')
	file = input('File to be hidden : ')
	enc = Encryption(file)
	enc_key = enc.encrypt_data()
	encode_stegano(enc_key)
	end_note()

elif opt == '2':
	os.system('clear')
	file = input('File to be decoded : ')
	enc_data = decode_stegano()
	dec = Decryption(file)
	dec.decrypt_data(enc_data)
	end_note()


