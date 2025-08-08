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

class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1505x790+0+0")
        self.root.title("Face Recognition System")
        title_label = Label(self.root,
                            text="Developer",
                            font=("Helvetica", 38, "bold"), bg="#f0f8ff", fg="#0f52ba",bd=4, relief=RIDGE)
        title_label.place(x=0, y=0, width=1505, height=60)

        img=Image.open(r"college_images/dev.jpg")
        img=img.resize((1530,730))
        self.photoimg=ImageTk.PhotoImage(img)

        label1=Label(self.root,image=self.photoimg)
        label1.place(x=0,y=50,width=1530,height=790)

        main_frame=Frame(label1,bd=2)
        main_frame.place(x=1000,y=0,width=500,height=600)

        img1=Image.open(r"college_images/dev.jpg")
        img1=img1.resize((200,200))
        self.photoimg1=ImageTk.PhotoImage(img1)

        label1=Label(main_frame,image=self.photoimg1)
        label1.place(x=300,y=0,width=200,height=200)

        department_label=Label(main_frame,text="Hello my name is priya",font=("Helvetica", 12, "bold"))
        department_label.place(x=0,y=5)




if __name__=="__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()