#!/usr/bin/python

import Tkinter
import tkMessageBox

top = Tkinter.Tk()
top.minsize(width=400,height=400)

def helloCallBack():
   tkMessageBox.showinfo( "Hello Python", "Hello World")
   
def showBarcode():
    BarcodeSerial.insert(0, "Hello.....")   
    
#Create button object
HelloButton = Tkinter.Button(top, text ="Hello", command = helloCallBack, height=5, width=20 )
QueryDB = Tkinter.Button(top, text ="Retrieve", height=5, width=20, command = showBarcode)
BarcodeSerial = Tkinter.Text(top, height=5, width=20)

HelloButton.pack()
QueryDB.pack()
BarcodeSerial.pack()
top.mainloop()