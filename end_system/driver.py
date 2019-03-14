#!/usr/bin/env python
import os
from Cryptography.Encryption import Encryption
from Cryptography.Decryption import Decryption
from Steganography.Steganography_driver import *
from FaceAuth.save_data import *
import sys
sys.path.insert(0, '../cloud_uploads')
from gen_data import * 
from authorize import pass_auth
def end_note():
	os.system('clear')
	print('Thank you for using Stegancryption..!')
def main():
	os.system('clear')
	print('Welcome')
	rl = input('1 - Register\n2 - Login\nEnter Here : ')

	if rl == '1':
		os.system('clear')
		uid = input('Enter UID : ')
		passwd = input('Enter Password : ')
		register_user(uid,passwd)
		save_data(uid)
		gen_data(uid)
		inp = input('Press any key to continue ...')
		main()


	elif rl == '2':
		os.system('clear')
		uid = input('Enter UID : ')
		passwd = input('Enter Password : ')
		if pass_auth(uid,passwd):
			os.system('clear')
			os.system('Welcome')
			opt = input('Menu\n1 - Stegancryption Hide\n2 - Stegancryption Reveal\nEnter Here : ')
			if opt == '1':
				os.system('clear')
				file = input('File to be hidden : ')
				enc = Encryption(file)
				enc_key = enc.encrypt_data()
				ruid = input('Receiver\'s uid : ')
				encode_stegano(enc_key,ruid)
				end_note()

			elif opt == '2':
				os.system('clear')
				file = input('File to be decoded : ')
				enc_data = decode_stegano()
				if enc_data is not None:
					dec = Decryption(file)
					dec.decrypt_data(enc_data)
					end_note()
				else:
					print('Fuck Off')
		else:
			print('wrong password')
			inp = input('Enter any key ....')
			main()

main()


