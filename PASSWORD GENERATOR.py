from tkinter import *
import pyperclip 
import random

root = Tk()
root.geometry("700x300")
passwrd = StringVar()
passlen = IntVar()
passlen.set(0)

def generate(): # Function to generate the password
	pass1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
			'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
			'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
			'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
			'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
			'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8',
			'9', '0', ' ', '!', '@', '#', '$', '%', '^', '&',
			'*', '(', ')']
	password = ""
	for x in range(passlen.get()):
		password = password + random.choice(pass1)
	passwrd.set(password)
def copypass():
	random_password = passwrd.get()
	pyperclip.copy(random_password)

root.title("MY PASSWORD GENERATOR")
root.iconbitmap(r'C://Users//ramsu//OneDrive//Desktop//GITHUB//TASK-3(PASSWORD GENERATOR)//password.ico')
#bgimg= PhotoImage(r'C:Users//ramsu//OneDrive//Desktop//GITHUB//TASK-3(PASSWORD GENERATOR)//pwbg.jpg')
#label1 = Label( root, image = bgimg) 
#label1.place(x = 0, y = 0)
root.minsize(500,500)
root.maxsize(750,750)
root.geometry('700x500')
root.configure(background = "sky blue")
Label(root, text="PASSWORD GENERATOR", font="Courier 40 bold",fg = "black" , bg = "green",width=20).pack(pady = 15)
Label(root, text="Enter length of password : ",fg = "black" , bg = "pink",width=25,height=2,font=("verdana",15)).pack(pady=12)
Entry(root, textvariable=passlen,fg = "black",bg = "yellow",width=30,font=("verdana",15)).pack(pady=12)
Button(root, text="Generate", command=generate,fg = "black" , bg = "green",height = 1,width= 10,font="Courier 17 bold").pack(pady=12)
Entry(root, textvariable=passwrd,fg = "black" , bg = "yellow",width = 30,font=("verdana",15)).pack(pady=13)
Button(root, text="Tap to Copy.",fg = "black" , bg = "green", height = 1,width= 14,font="Courier 15 bold",command=copypass).pack(pady = 15)
root.mainloop()
