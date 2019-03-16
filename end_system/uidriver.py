#!/usr/bin/env python3
import os
from Cryptography.Encryption import Encryption
from Cryptography.Decryption import Decryption
from Steganography.Steganography_driver import *
from FaceAuth.save_data import save_data
import sys
sys.path.insert(0, '../cloud_uploads')
from gen_data import *  #register user and gen_data
from authorize import pass_auth
import tkinter
from tkinter import messagebox

def emptyFrame():
	print('empty')
	pass

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
			but_enc = tkinter.Button(frame_steg,text = 'Encrypt',width = 20, command = emptyFrame)
			but_dec = tkinter.Button(frame_steg,text = 'Decrypt',width = 20, command = emptyFrame)
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
