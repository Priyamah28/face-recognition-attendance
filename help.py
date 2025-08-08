from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os 
import csv
from tkinter import filedialog

mydata=[]

class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1505x790+0+0")
        self.root.title("Face Recognition System")
        title_label = Label(self.root,
                            text="Help Desk",
                            font=("Helvetica", 38, "bold"), bg="#f0f8ff", fg="#0f52ba",bd=4, relief=RIDGE)
        title_label.place(x=0, y=0, width=1505, height=60)
        
        img=Image.open(r"college_images/dev.jpg")
        img=img.resize((1530,730))
        self.photoimg=ImageTk.PhotoImage(img)

        label1=Label(self.root,image=self.photoimg)
        label1.place(x=0,y=50,width=1530,height=790)

        department_label=Label(label1,text="Email:maheshwaripriya@gmail.com",font=("Helvetica", 20, "bold"))
        department_label.place(x=550,y=260)

if __name__=="__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()
