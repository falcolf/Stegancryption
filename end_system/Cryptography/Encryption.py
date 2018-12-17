#!/usr/bin/env python
import os
from Crypto.Cipher import AES
from Crypto import Random
import base64
import hashlib

class Encryption():

	def __init__(self,sfile):
		
		file = open(sfile,'r')
		self.data = file.read()
		file.close()
		self.block_size = 16

	def gen_key(self):
		self.key = os.urandom(32)
		f = open('key.txt','wb')
		f.write(self.key)
		f.close()

	def pad(self):
		s = self.data
		self.data = s+(self.block_size-len(s)%self.block_size) * chr(self.block_size-len(s)%self.block_size)

	def encrypt_data(self):
		self.gen_key()
		self.pad()
		cip = AES.new(self.key, AES.MODE_CBC, '0'*16)
		self.data = cip.encrypt(self.data)
		enc = base64.b64encode(self.data)
		f = open('encdata.txt','wb')
		f.write(enc)
		f.close()


