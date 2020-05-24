import socket
import sys
import threading
import tkinter as tk
from tkinter import messagebox
import base64
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad,unpad
host='10.1.1.145'
port=12345

list_changed=False
new_msg=False
send_msg=False

gmsg=''
nmsg=''
RCV='ALL'

theEnd=False

nick=sys.argv[1]
users=[]
useKey = ""
class listen(threading.Thread):
	def __init__(self,soc):
		super(listen, self).__init__()
		self.soc=soc

	def run(self):
		global users
		global list_changed,nmsg,new_msg
		again=True
		while again:
			if theEnd:
				self.soc.close()
				break
			try:
				msg=self.soc.recv(2048)
			except:
				self.soc.close()
				break

			if msg:
				msg2=msg.decode('UTF-8')
				name=''
				if msg2[0]=='2':
					users[:]=[]
					for i in range (2,len(msg2)):
						if msg2[i]==' ':
							users.append(name)
							name=''
						else:
							name+=msg2[i]
					users.append(name)
					list_changed=True
				else:
					if msg2[3]!=nick[2]:
						nmsg=msg2[1:]
						new_msg=True
						print(msg2[1:])


class rd(threading.Thread):
	def __init__(self,soc):
		super(rd, self).__init__()
		self.soc=soc

	def run(self):
		global users,send_msg,gmsg
		msg=bytes('2'+nick,'UTF-8')
		self.soc.send(msg)
		again=True
		while again:
			if theEnd:
				msg2='3'+nick
				msg=bytes(msg2,'UTF-8')
				self.soc.send(msg)
				self.soc.close()
				break
			if send_msg:
				msg=gmsg
				send_msg=False

				if RCV != 'ALL': #msg for 1 person
					msg2='1'+RCV+' '+nick+': '+msg
					msg=bytes(msg2,'UTF-8')
				else:
					msg2='0'+nick+': '+msg
					msg=bytes(msg2,'UTF-8')
				self.soc.send(msg)

class MyApp:
	def __init__(self, root):

		self.root = root
		self.root.title("Chat: "+nick)
		self.root.minsize(600,400)
		self.mainFrame = tk.Frame(self.root,bg="#C0C0C0")
		self.mainFrame.grid(row=0, column=0, sticky=tk.N + tk.S + tk.W + tk.E)
		self.root.rowconfigure(0, weight=1)
		self.root.columnconfigure(0, weight=1)

		self.frame00 = tk.Frame(self.mainFrame, bg="white")
		self.frame00.grid(column=0, row=0, sticky=tk.N + tk.S + tk.W + tk.E,pady=7,padx=7)

		self.frame01 = tk.Frame(self.mainFrame, bg="white")
		self.frame01.grid(column=1, row=0, rowspan=2, sticky=tk.N + tk.S + tk.W + tk.E,pady=7)

		self.frame10 = tk.Frame(self.mainFrame, bg="white")
		self.frame10.grid(column=0, row=1, sticky=tk.N + tk.S + tk.W + tk.E,pady=7,padx=7)

		self.frame20 = tk.Frame(self.mainFrame, bg="#C0C0C0")
		self.frame20.grid(column=0, row=2, columnspan=2, sticky=tk.N + tk.S + tk.W + tk.E,pady=0,padx=0)

		self.mainFrame.rowconfigure(0,weight=4)
		self.mainFrame.rowconfigure(1,weight=2)
		self.mainFrame.rowconfigure(2,weight=1)

		self.mainFrame.columnconfigure(0,weight=3)
		self.mainFrame.columnconfigure(1,weight=1)

		self.button1 = tk.Button(self.frame20)
		self.button1.myName = "Send Button"
		self.button1.config(text="Send Message", background= "#C0C0C0",width=68,height=4)
		self.button1.pack(side=tk.LEFT)
		self.button1.focus_force()
		self.button1.bind("<Button-1>", self.button1Click)
		self.button1.bind("<Return>", self.button1Click)

		self.button2 = tk.Button(self.frame20)
		self.button2.myName = "Exit Button"
		self.button2.config(text="Exit", background= "#C0C0C0",width=22,height=4)
		self.button2.pack(side=tk.RIGHT)
		self.button2.focus_force()
		self.button2.bind("<Button-1>", self.button2Click)
		self.button2.bind("<Return>", self.button2Click)

		self.listbox = tk.Listbox(self.frame01,height=20,width=15)
		self.listbox.pack()
		self.listbox.bind('<<ListboxSelect>>',self.onselect)

		self.text1=tk.Text(self.frame10,height=8)
		self.text1.pack()
		self.text1.bind("<Return>", self.button1Click)

		self.text2=tk.Text(self.frame00)
		self.text2.pack()


	def button1Click(self, event):
		global send_msg,gmsg,useKey
		msg=self.text1.get("1.0",tk.END)
		self.text1.delete("1.0",tk.END)
		if msg!='\n':
			if useKey != "":
				cipher = AES.new(useKey,AES.MODE_CBC)
				ciphertext= cipher.encrypt(pad(msg.encode('utf-8'), AES.block_size))
				msg = base64.b64encode(cipher.iv+ciphertext).decode()

				data = base64.b64decode(msg)
				iv = data[:16]
				cipher = AES.new(useKey,AES.MODE_CBC,iv=iv)
				original_data = unpad(cipher.decrypt(data[16:]), AES.block_size)
				self.text2.insert(tk.INSERT,'me(D): '+original_data.decode()+'\n')
			elif msg.find("useKey") == 0:
				tmp = msg + "                                    "
				useKey = tmp[7:23].encode()
			self.text2.insert(tk.INSERT,'me: '+msg+'\n')
			gmsg=msg
			send_msg=True
		else:
			messagebox.showinfo("Error", "Write something!")

	def button2Click(self, event):
		global theEnd
		theEnd=True
		self.root.destroy()

	def onselect(self,event):
		global RCV
		w = event.widget
		index = int(w.curselection()[0])
		value = w.get(index)
		print(value)
		RCV=value

	def changeList(self):
		global list_changed
		self.listbox.delete(0, tk.END)
		self.listbox.insert(tk.END,'ALL')
		for item in users:
			if item != nick:
				self.listbox.insert(tk.END, item)
		list_changed=False

	def addmsg(self, msg):
		global new_msg
		self.text2.insert(tk.INSERT,msg)
		new_msg=False



def update():
	global list_changed,new_msg,useKey
	if list_changed:
		myapp.changeList()
	root.after(1000,update)
	if new_msg:
		msgE = nmsg[nmsg.find(":")+2:]
		if useKey != "":
			print("Decrypting")
			print("+"+ msgE+"+")
			data = base64.b64decode(msgE)
			data = base64.b64decode(msgE)
			iv = data[:16]
			cipher = AES.new(useKey,AES.MODE_CBC,iv=iv)
			original_data = unpad(cipher.decrypt(data[16:]), AES.block_size)
			myapp.addmsg(original_data.decode())
		else:
			myapp.addmsg(nmsg)
		if nmsg.find("useKey") != -1:
			tmp = nmsg + "                                    "
			useKey = tmp[nmsg.find("useKey")+7:nmsg.find("useKey")+23].encode()
			print("Key set")
			print(useKey)
		
		
soc=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
	soc.connect((host, port))
except:
	sys.exit()

newListen=listen(soc)
newListen.start()

newRd=rd(soc)
newRd.start()

root = tk.Tk()
myapp = MyApp(root)
myapp.changeList()

root.after(1000, update)
root.mainloop()
