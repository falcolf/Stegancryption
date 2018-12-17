from Cryptography.Encryption import Encryption
from Cryptography.Decryption import Decryption
import os

os.system('clear')
ip = input("1 for encryption and 2 for decryption : ")
f = input('File : ')
if ip == '1':
	enc = Encryption(f)
	enc.encrypt_data()

else :
	dec = Decryption(f)
	dec.decrypt_data()