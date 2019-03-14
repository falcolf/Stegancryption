import cv2
import numpy as np
import time
import os

def detect_face(img,fc):
	gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	faces = fc.detectMultiScale(gray_img,scaleFactor=1.2,minNeighbors=5)
	if len(faces)==0:
		return None,None
	x,y,w,h = faces[0]
	return gray_img[y:y+h,x:x+w],tuple(faces[0])

def do_auth(img,uid):
	path = os.getcwd()
	os.chdir('../cloud_uploads/')
	rec = cv2.face.LBPHFaceRecognizer_create()
	rec.read(str(uid)+'/recognizer.xml')
	fc = cv2.CascadeClassifier('haarface.xml')
	face,rect = detect_face(img,fc)
	os.chdir(path)
	if face is not None:
		fid,conf = rec.predict(face)
		if conf<25:
			if fid == 0:
				return 1
		else:
			return -1
	else:
		return None

def pass_auth(uid,paswd):
	f = open('../cloud_uploads/users.txt','r')
	lines = f.read().split('\n')
	print(lines)
	users = []
	for line in lines:
		user = line.split(',')
		users.append(user)
	print(users)
	for user in users:
		if str(uid) == user[0]:
			print(user[1])
			if str(paswd) == user[1]:
				return True
	return False

