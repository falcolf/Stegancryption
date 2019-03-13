import cv2
import numpy as np
import time
import os
import sys
sys.path.insert(0, '../cloud_uploads')
from authorize import do_auth
def auth(uid):
	cap = cv2.VideoCapture(0)
	im=0
	while True:
		ret,frame = cap.read()
		cv2.imwrite('frame.jpg',frame)
		ok = do_auth(frame,uid)
		print(ok)
		im+=1
		time.sleep(3)
		if im == 25:
			break
	cap.release()
	