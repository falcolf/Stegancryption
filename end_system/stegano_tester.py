#!/usr/bin/env python

from Steganography.Steganography_driver import *
import os
import cv2

os.system('clear')
ip = input("1 for encode and 2 for decode : ")
if ip == '1':
	encode_st()

else :
	decode_st()


