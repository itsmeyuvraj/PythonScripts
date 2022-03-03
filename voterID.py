from tkinter import *
import random


window = Tk()
window.geometry("1350x650+0+0")
window.resizable(0,0)



names = "Yuvraj , Shreyas , Amit , Sanket , Rajdeep"
number = "1,2,3,4,5"
fname = "Yuvraj , Shreyas , Amit , Sanket , Rajdeep" 

names_list = names.split(',')
fnames_list = fname.split(',')
number_list = number.split(',')

n = random.choice(number_list) 
fn = random.choice(fnames_list)
na = random.choice(names_list)


def start():
    greet = n + "\n" + fn + "\n" + na
    l1= l1