#!/usr/bin/env python
import os
import cv2
from Steganography.Steganography import *

def encode_st():
	os.system('clear')
	print('Starting Steganography Encoding Process')
	in_f = input('Source image (should be .png format)\t:')
	out_f = input('Updated image (should be .png format)\t:')
	sc_data = input('Secret data\t: ') 
	key = input('Steganography Encoding key (Caution : Remeber the key as non recoverable for safety reasons)\t: ')
	in_im = cv2.imread(in_f)
	stegano = Steganography(in_im,key)
	sc_data = str.encode(sc_data)
	res_img = stegano.encode_data(sc_data)
	cv2.imwrite(out_f,res_img)
	print('AES Encryption key successfully embedded into the image.\nUpdated image saved.\n')
	ip = input('Press any key to continue...')

def decode_st():
	os.system('clear')
	print('Starting Steganography Decoding Process')
	in_f = input('Image with key(shoule be .png format)\t:')
	key = input('Steganography Encoding key (Caution : Remeber the key as non recoverable for safety reasons)\t: ')
	in_im = cv2.imread(in_f)
	stegano = Steganography(in_im,key)
	byte_lst = stegano.decode_data()
	byte_lst = [chr(b) for b in byte_lst]
	dt = ''.join(byte_lst)
	print(dt)
