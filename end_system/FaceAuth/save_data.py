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
	
def draw_rectangle(img, rect):
	(x, y, w, h) = rect
	cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
	return img

def gen_data():
	paths=[]
	cap=cv2.VideoCapture(0)
	labels = []
	faces = []
	faces_data = []
	images = 0
	fc = cv2.CascadeClassifier('FaceAuth/lbp_frontalface.xml')
	while images<20:
		ret,frame = cap.read()
		face,rect = detect_face(frame,fc)
		if face is not None:
			cv2.imshow("face",face)
			frame = draw_rectangle(frame,rect)
			faces.append(face)
			labels.append(0)
			fdata=[face,rect,labels]
			faces_data.append(fdata)
			images += 1
		cv2.imshow("Frame", frame)
		cv2.resizeWindow('image', 600,600)
		key = cv2.waitKey(1) & 0xFF
		if key == ord("q"):
			break
		time.sleep(3)
	cap.release()
	
	face_recognizer = cv2.face.LBPHFaceRecognizer_create()
	face_recognizer.train(faces, np.array(labels))
	face_recognizer.write('FaceAuth/recognizer.xml')


