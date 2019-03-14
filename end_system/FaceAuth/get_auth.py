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
	res = []
	while True:
		ret,frame = cap.read()
		ok = do_auth(frame,uid)
		if ok is not None:
			res.append(ok)
			im+=1
		time.sleep(3)
		if im == 20:
			break
	cap.release()
	ones = res.count(1)
	probab = ones/len(res)
	if probab > 0.8:
		return True
	else:
		return False
	