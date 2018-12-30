from FaceAuth.save_data import *
from FaceAuth.auth import *

ip = input('1 to gen data 2 for predict')

if ip == '1':
	gen_data()

else:
	auth()

	


