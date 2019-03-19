#!/usr/bin/env python3
import os
import sys
import cv2
from Cryptography.Encryption import Encryption
from Cryptography.Decryption import Decryption
from Steganography.Steganography import *
from FaceAuth.save_data import save_data
from FaceAuth.get_auth import * #for auth()
sys.path.insert(0, '../cloud_uploads')
from gen_data import *  #register user and gen_data
from authorize import pass_auth
import tkinter
from tkinter import messagebox
from tkinter import filedialog as fd

def showPrev(rframe , frame):
	rframe.grid_forget()
	frame.grid()

def faceData(but_fdata,but_register,uid):
	save_data(uid)
	gen_data(uid)
	but_fdata.config(text = 'Face Details Captured',state = 'disabled')
	but_register.config(state = 'normal')

def registerUser(uid,passwd,sframe,rframe):
	register_user(uid,passwd)
	tkinter.messagebox.showinfo("Success", "Registered")
	showPrev(rframe,sframe)


def showRegFrame(frame):
	frame.grid_forget()
	frame_reg = tkinter.Frame(root)
	lab_uid = tkinter.Label(frame_reg, text='UID')
	lab_passwd = tkinter.Label(frame_reg, text = 'Password')
	box_uid = tkinter.Entry(frame_reg)

	if(os.stat('../cloud_uploads/users.txt').st_size == 0):
		iuid = '1'
	else:
		iuid = len(open('../cloud_uploads/users.txt','r').read().split('\n'))


	box_uid.insert(0,str(iuid))
	box_uid.config(state = 'disabled')
	box_pass = tkinter.Entry(frame_reg,show = '*')
	but_register = tkinter.Button(frame_reg, text ='Register',state = 'disabled', command = lambda:registerUser(box_uid.get(),box_pass.get(),frame,but_register._nametowidget(but_register.winfo_parent())))
	but_main = tkinter.Button(frame_reg, text='Main Menu',command = lambda : showPrev(but_main._nametowidget(but_main.winfo_parent()), frame))
	but_fdata = tkinter.Button(frame_reg, text='Capture Face Data',command = lambda : faceData(but_fdata,but_register,box_uid.get()))
	lab_uid.grid(row = 0,column = 0)
	lab_passwd.grid(row = 1,column =0 )
	box_uid.grid(row = 0,column = 1)
	box_pass.grid(row = 1, column = 1)
	but_fdata.grid(row = 2,columnspan = 2,sticky='nesw')
	but_main.grid(row = 3,column=0,sticky='nesw')	
	but_register.grid(row =3,column=1,sticky='nesw')
	frame_reg.grid()

def login_user(frame,uidb,passwdb):
	frame.grid_forget()
	frame_steg = tkinter.Frame(root)
	uid = uidb.get()
	passwd = passwdb.get()
	if uid != '' and passwd !='':

		if pass_auth(uid,passwd):
			uidb.delete(0,'end')
			passwdb.delete(0,'end')
			but_enc = tkinter.Button(frame_steg,text = 'Encrypt',width = 20, command = lambda: showEncFrame(but_enc._nametowidget(but_enc.winfo_parent())))
			but_dec = tkinter.Button(frame_steg,text = 'Decrypt',width = 20, command = lambda: showDecFrame(but_dec._nametowidget(but_dec.winfo_parent())))
			but_logout = tkinter.Button(frame_steg,text = 'Logout',width = 20, command = lambda:showPrev(but_logout._nametowidget(but_logout.winfo_parent()),frame))
			but_enc.grid(row = 0 , sticky = 'nesw')
			but_dec.grid(row = 1, sticky = 'nesw')
			but_logout.grid(row = 2, sticky='nesw')
			
		else:
			lab_error = tkinter.Label(frame_steg, text = 'Error', fg = 'red',width = 20)
			but_login_again = tkinter.Button(frame_steg,text = 'Try Again', command = lambda:showPrev(but_login_again._nametowidget(but_login_again.winfo_parent()),frame)) 
			lab_error.grid(row = 0)
			but_login_again.grid(row = 1)
	else:
		lab_error = tkinter.Label(frame_steg, text = 'Error', fg = 'red',width = 20)
		but_login_again = tkinter.Button(frame_steg,text = 'Try Again', command = lambda:showPrev(but_login_again._nametowidget(but_login_again.winfo_parent()),frame)) 
		lab_error.grid(row = 0)
		but_login_again.grid(row = 1)
		
	frame_steg.grid()

def getFile(fbox,but,num):
	if num == 1:
		filename = fd.askopenfilename()
	else:
		filename = fd.askdirectory()
	fbox.delete(0,'end')
	fbox.insert(0,filename)
	filename = filename.split('/')[-1]
	but.config(text = filename)

def showEncFrame(frame):
	frame.grid_forget()
	frame_enc = tkinter.Frame(root)
	lab_ruid = tkinter.Label(frame_enc, text = 'Reciever\'s UID')
	box_ruid = tkinter.Entry(frame_enc)
	lab_encfile = tkinter.Label(frame_enc, text = 'File for Encryption')
	box_encfile = tkinter.Entry(frame_enc)
	but_encfile = tkinter.Button(frame_enc, text = 'Choose File', command = lambda: getFile(box_encfile,but_encfile,1))
	lab_encop = tkinter.Label(frame_enc, text = 'Encrypted File Directory')
	box_encop = tkinter.Entry(frame_enc)
	but_encop = tkinter.Button(frame_enc, text = 'Choose Directory', command = lambda: getFile(box_encop,but_encop,0))
	lab_img = tkinter.Label(frame_enc, text = 'Image')
	box_img = tkinter.Entry(frame_enc)
	but_img = tkinter.Button(frame_enc, text = 'Choose File', command = lambda: getFile(box_img,but_img,1))
	lab_outfile = tkinter.Label(frame_enc, text = 'Stegano Image Directory')
	box_outfile = tkinter.Entry(frame_enc)
	but_outfile = tkinter.Button(frame_enc, text = 'Choose Directory', command = lambda: getFile(box_outfile,but_outfile,0))
	lab_emkey = tkinter.Label(frame_enc, text = 'Embedding Key')
	box_emkey = tkinter.Entry(frame_enc,show = '*')
	but_encrypt = tkinter.Button(frame_enc, text = 'Encrypt', command = lambda: encProcess(box_ruid.get(),box_encfile.get(),box_encop.get()+'/encrypted_'+box_encfile.get().split('/')[-1],box_img.get(),box_emkey.get(),box_outfile.get()+'/stegano_'+box_img.get().split('/')[-1],but_encrypt._nametowidget(but_encrypt.winfo_parent()),frame))
	but_menu = tkinter.Button(frame_enc, text = 'Menu', command = lambda: showPrev(but_menu._nametowidget(but_menu.winfo_parent()),frame))

	lab_ruid.grid(row = 0, column = 0)
	box_ruid.grid(row = 0, column = 1)
	lab_encfile.grid(row = 1, column = 0)
	but_encfile.grid(row = 1, column = 1,sticky='nesw')
	lab_encop.grid(row = 2, column = 0)
	but_encop.grid(row = 2, column = 1,sticky='nesw')
	lab_img.grid(row = 3, column = 0)
	but_img.grid(row = 3, column = 1,sticky='nesw')
	lab_outfile.grid(row = 4, column = 0)
	but_outfile.grid(row = 4, column = 1,sticky='nesw')
	lab_emkey.grid(row = 5, column = 0)
	box_emkey.grid(row = 5, column = 1)
	but_encrypt.grid(row = 6, column = 1,sticky='nesw')
	but_menu.grid(row = 6,column = 0,sticky='nesw')
	frame_enc.grid()
	
def encProcess(ruid,encfile,enc_opf,img,emkey,out_f,cframe,nframe):
	print('[INFO] STARTING ENCRYPTION PROCESS.')
	encrytor = Encryption(encfile)
	enc_key = encrytor.encrypt_data(enc_opf)
	print('[INFO] ENCRYPTION COMPLETED SUCCESSFULLY.')
	print('[INFO] LOADING SOURCE IMAGE')
	in_im = cv2.imread(img)
	print('[INFO] SOURCE IMAGE LOADED SUCCESSFULLY.')
	print('[INFO] STARTING STEGANOGRAPHY PROCESS.')
	stegano = Steganography(in_im,emkey)
	res_img = stegano.encode_data(enc_key,ruid)
	cv2.imwrite(out_f,res_img)
	print('[INFO] STEGANOGRAPHY PROCESS COMPLETED SUCCESSFULLY.')
	tkinter.messagebox.showinfo("Success", "Encrypted File and Steganographied Image Saved.")
	showPrev(cframe,nframe)

def showDecFrame(frame):
	frame.grid_forget()
	frame_dec = tkinter.Frame(root)

	lab_decfile = tkinter.Label(frame_dec, text = 'Encrypted File')
	box_decfile = tkinter.Entry(frame_dec)
	but_decfile = tkinter.Button(frame_dec, text = 'Choose File', command = lambda: getFile(box_decfile,but_decfile,1))
	lab_img = tkinter.Label(frame_dec, text = 'Image')
	box_img = tkinter.Entry(frame_dec)
	but_img = tkinter.Button(frame_dec, text = 'Choose File', command = lambda: getFile(box_img,but_img,1))
	lab_outfile = tkinter.Label(frame_dec, text = 'Decrypted File Directory')
	box_outfile = tkinter.Entry(frame_dec)
	but_outfile = tkinter.Button(frame_dec, text = 'Choose Directory', command = lambda: getFile(box_outfile,but_outfile,0))
	lab_emkey = tkinter.Label(frame_dec, text = 'Embedding Key')
	box_emkey = tkinter.Entry(frame_dec,show = '*')
	but_decrypt = tkinter.Button(frame_dec, text = 'Decrypt', command = lambda: decProcess(box_decfile.get(),box_img.get(),box_emkey.get(),box_outfile.get()+'/decrypted_'+box_decfile.get().split('/')[-1],but_decrypt._nametowidget(but_decrypt.winfo_parent()),frame))
	but_menu = tkinter.Button(frame_dec, text = 'Menu', command = lambda: showPrev(but_menu._nametowidget(but_menu.winfo_parent()),frame))
	
	lab_decfile.grid(row = 0, column = 0)
	but_decfile.grid(row = 0, column = 1,sticky='nesw')
	lab_img.grid(row = 1, column = 0)
	but_img.grid(row = 1, column = 1,sticky='nesw')
	lab_outfile.grid(row = 2, column = 0)
	but_outfile.grid(row = 2, column = 1,sticky='nesw')
	lab_emkey.grid(row = 3, column = 0)
	box_emkey.grid(row = 3, column = 1)
	but_decrypt.grid(row = 4, column = 1,sticky='nesw')
	but_menu.grid(row = 4,column = 0,sticky='nesw')
	frame_dec.grid()
					
					


def decProcess(decfile,img,emkey,out_f,cframe,nframe):
	print('[INFO] LOADING MAGE')
	in_im = cv2.imread(img)
	print('[INFO] IMAGE LOADED SUCCESSFULLY.')
	stegano = Steganography(in_im,emkey)
	print('[INFO] GETTING RECIEVER\'S UID.')
	ruid = stegano.extract_receiver()
	print('[INFO] RECIEVER\'S UID : {}.'.format(ruid))
	print('[INFO] INITIATING FACICAL RECOGNITION PROCESS.')
	if(auth(ruid)):
		print('[INFO] RECIEVER AUTHORIZED.')
		print('[INFO] EXTRACTING KEY FROM IMAGE.')
		byte_lst = stegano.decode_data()
		key = bytes(byte_lst)
		print('[INFO] KEY EXTRACTED SUCCESSFULLY.')
		print('[INFO] INITIATING DECRYPTION PROCESS.')
		dec = Decryption(decfile)
		dec.decrypt_data(key,out_f)
		print('[INFO] DECRYPTION COMPLETED SUCCESSFULLY.')
		tkinter.messagebox.showinfo("Success", "DECRYPTED FILE SAVED.")
		

	else:
		print('[INFO] IDENTITY OF RECIEVER NOT VERIFIED.')
		tkinter.messagebox.showinfo("ERROR", "RECIEVER NOT AUTHORIZED.")
		
	showPrev(cframe,nframe)

		

def showLoginFrame(frame):
	frame.grid_forget()
	frame_login = tkinter.Frame(root)
	lab_uid = tkinter.Label(frame_login, text='UID')
	lab_passwd = tkinter.Label(frame_login, text = 'Password')
	box_uid = tkinter.Entry(frame_login)
	box_pass = tkinter.Entry(frame_login,show = '*')
	but_login = tkinter.Button(frame_login, text ='Login',command=lambda:login_user(but_login._nametowidget(but_login.winfo_parent()),box_uid,box_pass))
	but_main = tkinter.Button(frame_login, text='Main Menu',command = lambda : showPrev(but_main._nametowidget(but_main.winfo_parent()), frame))
	lab_uid.grid(row = 0,column = 0,sticky='nesw')
	lab_passwd.grid(row = 1,column = 0 ,sticky='nesw')
	box_uid.grid(row = 0,column = 1,sticky='nesw')
	box_pass.grid(row = 1, column = 1,sticky='nesw')
	but_main.grid(row = 2 , column = 0,sticky='nesw')
	but_login.grid(row = 2, column = 1,sticky='nesw')
	frame_login.grid()

os.system('clear')
print('[INFO] INITIATING STEGANCRYPTION MODULE.')
root = tkinter.Tk()
windowWidth = root.winfo_reqwidth()
windowHeight = root.winfo_reqheight() 
positionRight = int(root.winfo_screenwidth()/2 - windowWidth/2)
positionDown = int(root.winfo_screenheight()/2 - windowHeight/2)
root.geometry("+{}+{}".format(positionRight, positionDown))
root.title('Stegancryption')
frame_main = tkinter.Frame(root)
lab_welcome = tkinter.Label(frame_main, text='Welcome To Stegancryption Platform', fg = 'blue')
but_regframe = tkinter.Button(frame_main, text='Register',command = lambda: showRegFrame(but_regframe._nametowidget(but_regframe.winfo_parent())))
but_loginframe = tkinter.Button(frame_main, text='Login', command = lambda: showLoginFrame(but_loginframe._nametowidget(but_loginframe.winfo_parent())))
lab_welcome.grid(row = 0,sticky='nesw')
but_regframe.grid(row=1,sticky='nesw')
but_loginframe.grid(row=2,sticky='nesw')
frame_main.grid()
root.mainloop()
