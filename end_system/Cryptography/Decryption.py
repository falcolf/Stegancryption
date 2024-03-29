#!/usr/bin/env python
import os
import base64
from Crypto.Cipher import AES

class Decryption():

	def __init__(self,sfile):
		
		file = open(sfile,'rb')
		self.data = file.read()
		file.close()
		self.block_size = 16

	def get_key(self):
		f = open('key.txt','rb')
		self.key = f.read()
		f.close()

	def unpad(self):
		s = self.data
		self.data =  s[:-ord(s[len(s)-1:])]

	def decrypt_data(self,skey,op_f):
		self.key = skey
		self.data = base64.b64decode(self.data)
		cip = AES.new(self.key, AES.MODE_CBC, '0'*16)
		self.data = cip.decrypt(self.data)
		self.unpad()
		f = open(op_f,'w')
		data = []
		for b in self.data:
			data.append(chr(b))
		f.write(''.join(data))
		f.close()