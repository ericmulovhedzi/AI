# File: csv_db_import.py
# Author: Eric Mulovhedzi
# Created on March 15, 2017, 12:36 PM
# A script of a Graphic User Interface (GUI) for an OVH NN model trained to follow an instruction 
# in a prompt and provide a detailed response. This version only utilizes two fundamental neural network models:
# (a) Convolution Neural Network (CNN) for computer vision processing and Recurrent Neural Network (RNN) for 
# Natural Language Processing (NLP).
	
# importing packadges 

import socket, os
import threading, sys
from tkinter import *
import pprint
import time
from time import sleep
from threading import Timer

CMD_JOINED,CMD_LEFT,CMD_MSG,CMD_LINE,CMD_JOINRESP=range(5)
CurrentLine = CurrentLineJ = 1;
FileNames = {}
readDir = '/Users/ericmulovhedzi/python/FILES/'

socket_ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#socket_.connect(("196.xx.xx.xx", 2626)) # Remote public IP Address

root = Tk() # Define a root Window TK
root.resizable(width=TRUE, height=TRUE)

menubar = Menu(root) # Add menu to the root Wndow TK Oject

# --- Main Paned Window

m1 = PanedWindow(root,bg="#fefefe")
m1.pack(side=TOP,fill=BOTH, expand=1)

# --- Main Frame Labels

lFarem1 = LabelFrame(m1, text="OVH Chat Bot",bg="#fafafa")
lFarem1.pack(side=LEFT,fill="both", expand="yes")

lFarem2 = LabelFrame(m1, text="//",bg="#fefefe")
lFarem2.pack(side=LEFT,fill="both", expand="yes", pady=0)

# ---

lbB = Listbox(lFarem1,width=30,relief='groove',bg="#fafafa",fg="#39892f",border=0,font="Helvetica 11 bold") # Add listbox to the root Wndow TK Oject
#Lb1.insert(CurrentLine, "Welcome to CHAT")
lbB.pack(side=LEFT,fill="both", expand="yes", padx=3, pady=12)

lableTo = Label(lFarem2,text="To: ", anchor=W, justify=LEFT,font="Helvetica 11 bold",fg="#999")
lableTo.pack(side=TOP, fill=X, padx=2, pady=2)

# --- Separator 1
separator = Frame(lFarem2,height=2, bd=1, relief='groove')
separator.pack(fill=X, padx=5, pady=1)

bottomFrame = Frame(lFarem2,bg="#fefefe")
bottomFrame.pack(side=BOTTOM,fill="both", padx=1, pady=5)

Lb1 = Listbox(lFarem2,width=80,height=28,relief='groove',bg="#fefefe",border=0,font="Helvetica 12") # Add listbox to the root Wndow TK Oject
Lb1.pack(side=LEFT,fill="both", expand="yes",padx=3,pady=0)
# lbB.insert(CurrentLineJ," Buddies ")
scrollbar = Scrollbar(lFarem2)
scrollbar.pack(side=RIGHT,fill=Y)

# attach listbox to scrollbar
Lb1.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=Lb1.yview)

E1 = Entry(bottomFrame, bd =0,relief='ridge',border=1,bg="#fefefe",font="Helvetica 12")
E1.pack(side=TOP,fill=X)

#separator1 = Frame(bottomFrame,height=5, bd=0, relief='groove',bg="#fefefe")
#separator1.pack(side=BOTTOM,fill=X, padx=5, pady=5)

var_LableStatus = StringVar()
var_LableStatus.set("Status: ")
lableStatus = Label(bottomFrame,textvariable=var_LableStatus, anchor=W, justify=LEFT,font="Helvetica 12",fg="#bbb")
lableStatus.pack(side=BOTTOM, fill=X, padx=0, pady=5)

# --- --- --- --- Bottom Files PanedWindow

#m2 = PanedWindow(root,bg="#fefefe")
#m2.pack(side=BOTTOM,fill=BOTH, expand=1)

#lFarem3 = LabelFrame(m2, text="//",bg="#fefefe")
#lFarem3.pack(side=LEFT,fill="both", expand="yes", pady=0)

#m2FrameBottom = Frame(lFarem3,bg="#fefefe")
#m2FrameBottom.pack(side=BOTTOM,fill="both", padx=1, pady=5)

#var_m2LableStatus = StringVar()
#var_m2LableStatus.set("File Transfers: (Current Path): "+os.getcwd())
#m2LableStatus = Label(m2FrameBottom,textvariable=var_m2LableStatus, anchor=W, justify=LEFT,font="Helvetica 12",fg="#bbb")
#m2LableStatus.pack(side=BOTTOM, fill=X, padx=0, pady=5)

def resetFileStatus():
	var_LableStatus.set("Status: ")
	#sleep(2)
	
def sendMsg(msg):
	global socket_
	socket_.send(msg)

def donothing():
   filewin = Toplevel(root)
   button = Button(filewin, text="Do nothing button")
   button.pack()

def ListInsertBuddies(text):
	global CurrentLineJ
	CurrentLineJ +=1
	lbB.insert(CurrentLineJ," :- "+text)

def ListInsert(text):
	global CurrentLine
	CurrentLine +=1
	Lb1.insert(CurrentLine," "+text)
	scrollbar.config( command = Lb1.yview )
	
def onReturnKey(event):
	sendMsg(chr(CMD_MSG)+socket.gethostname()+" ("+time.strftime('%X')+") : "+E1.get())
	E1.delete(0, END)

def sendFiles():
	sendMsg("FILES__NOW")
	
def onQuit():
	'user clicked on quit button'
	sendMsg(chr(CMD_LEFT))
	#print(CMD_LEFT+":"+chr(CMD_LEFT))
	root.quit()

def keys(event):
	sendMsg("USER_STATUS__("+socket.gethostname()+") is typing..."+repr(event.char))
	#t_.cancel()
	t_ = Timer(5.0, resetFileStatus)
	t_.start()
	
# ----------------------- File Menu

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New Window", command=donothing)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=onQuit)
menubar.add_cascade(label="File", menu=filemenu)

editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", command=donothing)

editmenu.add_separator()

toolsmenu = Menu(menubar, tearoff=0)
toolsmenu.add_command(label="Computer Vision (CNN)", command=donothing)
toolsmenu.add_command(label="Natural Language Processing (NLP)", command=donothing)

menubar.add_cascade(label="Tools", menu=toolsmenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About...", command=donothing)

menubar.add_cascade(label="Help", menu=helpmenu)
root.config(menu=menubar)

# ----------------------- List Box
Lb1.insert(CurrentLine, "")
CurrentLine=CurrentLine+1
Lb1.insert(CurrentLine, " Welcome to OVH Chat Bot")
CurrentLine=CurrentLine+1
Lb1.insert(CurrentLine, " --")
CurrentLine=CurrentLine+1
Lb1.insert(CurrentLine, " Please, type in your question on the prompt below and press <Enter>.")
CurrentLine=CurrentLine+1

E1.bind('<Return>',onReturnKey)
E1.bind("<Key>", keys)

#m2btn1 = Button(m2FrameBottom, text="Recieve Files", width=10, command=sendFiles)
#m2btn1.pack(side=TOP, fill=X, padx=0, pady=0)

#sendMsg(chr(CMD_JOINED)+socket.gethostname()+" : just logged in")

def msgThread():
	
	while True:
		data = socket_.recv(1024)
		pprint.pprint(data)
		if not data: sys.exit(0)
		
		cmd = data[:data.find('\n')]
		
		if str(data)[:5] == "SYS__":
			listSys = str(data).split("___")
			if listSys[0] == "SYS__JOINED":
				listSys1 = listSys[1].split(":")
				ListInsertBuddies(" "+listSys1[0]+" ("+listSys1[1][:-1]+")")
			elif listSys[0] == "SYS__CONNECTED":
				listSys1 = listSys[1].split(":")
				ListInsertBuddies(" "+listSys1[0]+" ("+listSys1[1][:-1]+")")
		elif str(data)[:13] == "USER_STATUS__":
			var_LableStatus.set(str(data)[13:])
			#t_ = Timer(5.0, resetFileStatus)
			#t_.start()var_m2LableStatus.set("File Transfer COMPLETE: ")
		elif cmd == 'get':
			x, file_name, x = data.split('\n', 2)
			var_m2LableStatus.set("Transfering file: "+file_name)
			if file_name == 'FILELOG.log':
				fl=open(readDir+'/'+file_name, 'w')
				for subdir, dirs, files in os.walk(readDir):
					i=1
					for file in files:
						fl.write(file+'\n') # Write a line into a file
						i+=1
				fl.close()
			socket_.sendall('ok')
			with open(readDir+'/'+file_name, 'rb') as f:
			    data = f.read()
			socket_.sendall('%16d' % len(data))
			socket_.sendall(data)
			socket_.recv(2)
		elif cmd == 'end':
			var_m2LableStatus.set("File Transfer COMPLETE, Thank you.")
			#socket_.close()
			#break
		else:
			dispStr = str(data)
			ListInsert(" "+dispStr[1:])
	

threading.Thread(target= msgThread).start()

root.mainloop()
