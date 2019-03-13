from FaceAuth.save_data import *
from FaceAuth.get_auth import *
import sys
sys.path.insert(0, '../cloud_uploads')
from gen_data import *

ip = input('1 to gen data 2 for predict : ')
uid = input('Enter uid : ')
if ip == '1':
	save_data(uid)
	gen_data(uid)
else:
	auth(uid)


