#!/usr/bin/env python
import os
import cv2
from Steganography.Steganography import *

def encode_stegano(sc_data):
	os.system('clear')
	print('Starting Steganography Encoding Process')
	in_f = input('Source image (should be .png format)\t: ')
	#sc_data = input('Secret data\t: ') 
	key = input('Steganography Encoding key (Caution: sensitive information)\t: ')
	in_im = cv2.imread(in_f)
	stegano = Steganography(in_im,key)
	#sc_data = str.encode(sc_data)
	res_img = stegano.encode_data(sc_data)
	print('AES Encryption key successfully embedded into the image.')
	out_f = input('Encoded image (should be .png format)\t: ')
	cv2.imwrite(out_f,res_img)
	print('Updated image saved.')
	ip = input('Press any key to continue...')

def decode_stegano():
	os.system('clear')
	print('Starting Steganography Decoding Process') 
	in_f = input('Encoded image (shoule be .png format)\t: ')
	key = input('Steganography Encoding key (Caution: sensitive information)\t: ')
	in_im = cv2.imread(in_f)
	stegano = Steganography(in_im,key)
	byte_lst = stegano.decode_data()
	data = bytes(byte_lst)
	return data

