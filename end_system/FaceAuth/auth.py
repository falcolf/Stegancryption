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

def draw_rect(img,rect):
	(x,y,w,h) = rect
	cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
	return img

def auth():
	cap = cv2.VideoCapture(0)
	rec = cv2.face.LBPHFaceRecognizer_create()
	rec.read('FaceAuth/recognizer.xml')
	fc = cv2.CascadeClassifier('FaceAuth/lbp_frontalface.xml')
	im = 0
	while True:
		ret,frame = cap.read()
		face,rect = detect_face(frame,fc)
		if face is not None:
			fid,conf = rec.predict(face)
			if conf<30:
				if fid == 0:
					print('ok')
				else:
					print('not ok')
			else:
				print('naaaaaaa')
		print('---')
		im+=1
		if im == 100:
			break
	cap.release()
