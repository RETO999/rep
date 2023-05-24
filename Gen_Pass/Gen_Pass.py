from tkinter import *
from tkinter import messagebox
import random


spc = ['@','#','$','%','&']
not_spc1 = [0,1,2,3,4,5,6,7,8,9]
not_spc2 = ['@','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
not_spc3 = ['_','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


def password_generator():
	pg = Tk()
	pg.geometry("325x175")
	pg.configure(bg='blue')
	pg.title("Gen_Pass")
	def pass_gen():
		pass_entry_text = ""
		generated = ""
		choice_lst = []
		length = random.randint(8,15)
		for i in range(length):
			choice_lst.append(random.choice(spc))
			choice_lst.append(random.choice(not_spc1))
			choice_lst.append(random.choice(not_spc2))
			choice_lst.append(random.choice(not_spc3))
			choice = random.choice(choice_lst)
			generated += str(choice)
		pass_entry.delete(0, END)
		pass_entry_text = generated
		pass_entry.insert(END, pass_entry_text)
		# print(generated)
	empty = Label(pg, text="", bg="blue")
	empty.pack()
	pass_label = Label(pg, text="GenPass", font=('system', 20), fg="#00FFFF", bg="#1F75FE")
	pass_label.pack()
	empty = Label(pg, text="", bg="blue")
	empty.pack()
	global pass_entry_text
	pass_entry_text = StringVar()
	global pass_entry
	pass_entry = Entry(pg, textvariable=StringVar)
	pass_entry.pack()
	empty = Label(pg, text="", bg="blue")
	empty.pack()
	pass_btn = Button(pg, text="GENERATE", font=('system', 16), fg="#FF4D00", bg="#990066", command=pass_gen)
	pass_btn.pack()
	pg.mainloop()

if __name__ == '__main__':
	password_generator()