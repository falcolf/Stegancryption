import cv2
import os
import time
import numpy as np


def detect_face(img,fc):
	grayimg = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
	faces = fc.detectMultiScale(grayimg,scaleFactor=1.2,minNeighbors=5)
	if len(faces) == 0:
		return None,None
	x,y,w,h = faces[0]
	return grayimg[y:y+h, x:x+w], tuple(faces[0])

def gen_data(uid):
	labels = []
	faces = []
	images = 0
	path = os.getcwd()
	os.chdir('../cloud_uploads/')
	fc = cv2.CascadeClassifier('haarface.xml')
	for file in os.listdir(str(uid)):
		face,rect = detect_face(cv2.imread(str(uid)+'/'+file),fc)
		if face is not None:
			faces.append(face)
			labels.append(0)
			images += 1	
	face_recognizer = cv2.face.LBPHFaceRecognizer_create()
	face_recognizer.train(faces, np.array(labels))
	face_recognizer.write(str(uid)+'/recognizer.xml')
	print('file generated')
	os.chdir(path)

def register_user(uid,passwd):
	f = open('../cloud_uploads/users.txt','a')
	line = str(uid)+','+str(passwd)+'\n'
	f.write(line)
	f.close()

