import cv2
import os
import time
import numpy as np

def save_data(uid):
	cap=cv2.VideoCapture(0)
	images = 0
	os.system('mkdir uploads')
	while images<100:
		ret,frame = cap.read()
		cv2.imwrite('uploads/'+str(images)+'.jpg',frame)
		images+=1
	cap.release()
	print('[INFO] IMAGES CAPTURED AND TRANFERRED SUCCESSFULLY. ')

	#temporary cloud transfer
	os.system('mkdir ../cloud_uploads/'+str(uid))
	os.system('mv uploads/* ../cloud_uploads/'+str(uid)+'/')

	os.system('rm -rf uploads')


