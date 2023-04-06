from tkinter import *
from tkinter import ttk #theme of tk
from tkinter import messagebox

GUI = Tk() #หน้าจอหลักโปรแกรม
GUI.title('โปรแกรมบันทึกข้อมูล') #ชื่อโปรแกรม
GUI.geometry('500x400')  # ขนาดโปรแกรม

L1 = Label(GUI,text='โปรแกรมตารางชีวิต',font=('Angsana New',30),fg='pink')
L1.place(x=30,y=20)

#####################
def Button2():
    text = 'อยากนอนแน้วก้าบบบบ'
    messagebox.showerror('ตาจะปิดมั้ย',text)
    
FB1 = Frame(GUI) #คล้ายกระดาน
FB1.place(x=200,y=100)
B2 = ttk.Button(FB1,text='ง่วงยัง',command=Button2)
B2.pack(ipadx=20,ipady=20)
#####################
def Button3():
    text = 'วันนี้มีละหมาดตารอเวี้ยะห์'
    messagebox.showerror('9pm',text)
    
FB2 = Frame(GUI) #คล้ายกระดาน
FB2.place(x=200,y=200)
B3 = ttk.Button(FB1,text='today',command=Button3)
B3.pack(ipadx=20,ipady=20)
GUI.mainloop()

import tkinter as tk
from PIL import ImageTk, Image

root = tk.Tk()
root.title("Image in Tkinter")

# Load the image
img = Image.open("example.png")
img = img.resize((300, 300), Image.ANTIALIAS)  # Resize the image
photo = ImageTk.PhotoImage(img)

# Create a label to display the image
label = tk.Label(root, image=photo)
label.pack()

root.mainloop()
