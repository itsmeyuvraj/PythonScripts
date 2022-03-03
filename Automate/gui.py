import random
from tkinter import *
from  screenshot import capture
from tkinter import messagebox

def start():
    na = random.choice(name_list)
    fa = random.choice(ifsc_list)
    pa = random.choice(acc_list)
    da = random.choice(bank_list)
    greet = " " + "\n" + na + "\n"  + fa + "\n" + pa + "\n"  +  da

    L1.configure(text=greet)
    capture()
    L1.after(100, start)


window = Tk()
window.geometry("1350x650+0+0")
window.resizable(0,0)

try:
    bank_name= open("C:\\Users\\Yuvraj Sharma\\Desktop\\Python scripts\\Automate\\data\\bank_name.txt",mode="r")
    name= open("C:\\Users\\Yuvraj Sharma\\Desktop\\Python scripts\\Automate\\data\\name.txt",mode="r")
    ifsc= open("C:\\Users\\Yuvraj Sharma\\Desktop\\Python scripts\\Automate\\data\\ifsc.txt",mode="r")
    acc_no= open("C:\\Users\\Yuvraj Sharma\\Desktop\\Python scripts\\Automate\\data\\accno.txt",mode="r")
except:
    messagebox.showerror("Error","File not found")


name_list = name.read().split(',')
ifsc_list = ifsc.read().split()
acc_list = acc_no.read().split()
bank_list = bank_name.read().split(',')


L1 = Label(window, font=('Times New Roman', 28, 'bold'))
L1.pack(expand=YES, fill=BOTH)

start()
window.mainloop()