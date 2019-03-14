#!/usr/bin/env python
import os
import cv2
from Steganography.Steganography import *
from FaceAuth.get_auth import * #for auth()

def encode_stegano(sc_data,uid):
	os.system('clear')
	print('Starting Steganography Encoding Process')
	in_f = input('Source image (should be .png format)\t: ')
	key = input('Steganography Encoding key (Caution: sensitive information)\t: ')
	in_im = cv2.imread(in_f)
	stegano = Steganography(in_im,key)
	res_img = stegano.encode_data(sc_data,uid)
	print('AES Encryption key successfully embedded into the image.')
	out_f = input('Encoded image (should be .png format)\t: ')
	cv2.imwrite(out_f,res_img)
	print('Updated image saved.')
	ip = input('Press any key to continue...')

def decode_stegano():
	os.system('clear')
	print('Starting Steganography Decoding Process') 
	in_f = input('Encoded image (shoule be .png format)\t: ')
	in_im = cv2.imread(in_f)
	key = input('Steganography Encoding key (Caution: sensitive information)\t: ')
	stegano = Steganography(in_im,key)
	ruid = stegano.extract_receiver()
	print('meant for '+str(ruid))
	if(auth(ruid)):
		
		byte_lst = stegano.decode_data()
		data = bytes(byte_lst)
		return data
	else:
		print('not authorized')
		return None

