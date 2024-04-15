from tkinter import *
import base64


root = Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title("Message encyrpter")


Text = StringVar()
private_key = StringVar()
mode = StringVar()

result = StringVar()

Label(root, text = 'Encode Decode',font = "arial 20 bold").pack(side = TOP)

Label(root, text = 'Secure your data',font = "arial 20 bold").pack(side = BOTTOM)


def Encode(key, message):
    enc = []
    for i in range(len(message)):
        key_c =key[i%len(key)]
        enc.append((chr(ord(message[i]) + ord(key_c)) %256))
root.mainloop()