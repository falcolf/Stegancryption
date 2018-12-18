#!/usr/bin/env python
import os
import base64
from Crypto.Cipher import AES

class Encryption():

	def __init__(self,sfile):
		
		file = open(sfile,'r')		#file containing data
		self.data = file.read()
		file.close()
		self.block_size = 16		#defines block size

	def gen_key(self):
		self.key = os.urandom(32)	#32 bytes for AES 256
		#f = open('key.txt','wb')
		#f.write(self.key)
		#f.close()

	def pad(self):
		s = self.data
		self.data = s+(self.block_size-len(s)%self.block_size) * chr(self.block_size-len(s)%self.block_size)

	def encrypt_data(self):
		print('Starting Encryption Process...')
		self.gen_key()				# generate random key
		self.pad()					# padding to fill in data with
		cip = AES.new(self.key, AES.MODE_CBC, '0'*16)
		self.data = cip.encrypt(self.data)
		enc = base64.b64encode(self.data) #base64 encoding
		print('Encryption complete.')
		op_f = input('Encrypted Data File : ')
		f = open(op_f,'wb')	
		f.write(enc)
		f.close()
		print('Encrypted File Writen...')
		ip = input('Press any key to continue...')
		return self.key


