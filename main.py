from tkinter import*
from tkinter import ttk
import tkinter.messagebox
from PIL import Image,ImageTk
from student import Student
import os
import tkinter
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from help import Help
from developer import Developer


class face_recognition_system:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1505x790+0+0")
        self.root.title("Face Recognition System")

        #ist image
        img=Image.open(r"college_images/Stanford.jpg")
        img=img.resize((620,130))
        self.photoimg=ImageTk.PhotoImage(img)

        label1=Label(self.root,image=self.photoimg)
        label1.place(x=0,y=0,width=500,height=130)

        #2nd image
        img1=Image.open(r"college_images/face-recognition.png")
        img1=img1.resize((620,130))
        self.photoimg1=ImageTk.PhotoImage(img1)

        label2=Label(self.root,image=self.photoimg1)
        label2.place(x=500,y=0,width=500,height=130)

        #3rd image
        img2=Image.open("college_images/u.jpg")
        img2=img2.resize((720,130))
        self.photoimg2=ImageTk.PhotoImage(img2)

        label3=Label(self.root,image=self.photoimg2)
        label3.place(x=1000,y=0,width=500,height=130)

        # background image
        back_img = Image.open("college_images/bg1.jpg")
        back_img = back_img.resize((1505, 790))
        self.photoimg3 = ImageTk.PhotoImage(back_img)

        self.bg_label = Label(self.root, image=self.photoimg3)
        self.bg_label.place(x=0, y=130, width=1505, height=790)

        # Title label placed ON the background label
        title_label = Label(self.bg_label,
                            text="FACE RECOGNIZATION ATTENDANCE SYSTEM",
                            font=("Helvetica", 38, "bold"), bg="#f0f8ff", fg="#0f52ba",bd=4, relief=RIDGE)
        title_label.place(x=0, y=0, width=1505, height=45)

        #student button
        img4 = Image.open("college_images/student-portal_1.jpg")
        img4 = img4.resize((220, 220))
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1=Button(self.bg_label,image=self.photoimg4,command=self.student_detail,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)

        b1_1=Button(self.bg_label,text="Student details",command=self.student_detail,cursor="hand2",font=("Helvetica", 15, "bold"), bg="dark blue", fg="white",bd=4, relief=RIDGE)
        b1_1.place(x=200,y=300,width=220,height=40)

        #detect face button
        img5 = Image.open("college_images/face_detector1.jpg")
        img5 = img5.resize((220, 220))
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b2=Button(self.bg_label,command=self.face_data,image=self.photoimg5,cursor="hand2")
        b2.place(x=500,y=100,width=220,height=220)

        b2_1=Button(self.bg_label,text="Face Detector",command=self.face_data,cursor="hand2",font=("Helvetica", 15, "bold"), bg="dark blue", fg="white",bd=4, relief=RIDGE)
        b2_1.place(x=500,y=300,width=220,height=40)

        #attendance button
        img6 = Image.open("college_images/har.jpg")
        img6 = img6.resize((220, 220))
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b2=Button(self.bg_label,image=self.photoimg6,command=self.attendance_data,cursor="hand2")
        b2.place(x=800,y=100,width=220,height=220)

        b2_1=Button(self.bg_label,text="Attendance",command=self.attendance_data,cursor="hand2",font=("Helvetica", 15, "bold"), bg="dark blue", fg="white",bd=4, relief=RIDGE)
        b2_1.place(x=800,y=300,width=220,height=40)

        #help button
        img7 = Image.open("college_images/help.jpg")
        img7 = img7.resize((220, 220))
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b2=Button(self.bg_label,image=self.photoimg7,command=self.help_data,cursor="hand2")
        b2.place(x=1100,y=100,width=220,height=220)

        b2_1=Button(self.bg_label,text="Help Desk",cursor="hand2",command=self.help_data,font=("Helvetica", 15, "bold"), bg="dark blue", fg="white",bd=4, relief=RIDGE)
        b2_1.place(x=1100,y=300,width=220,height=40)

        #train button
        img8 = Image.open("college_images/train.jpg")
        img8 = img8.resize((220, 220))
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b2=Button(self.bg_label,command=self.train_data,image=self.photoimg8,cursor="hand2")
        b2.place(x=200,y=380,width=220,height=220)

        b2_1=Button(self.bg_label,text="Train Data",cursor="hand2",command=self.train_data,font=("Helvetica", 15, "bold"), bg="dark blue", fg="white",bd=4, relief=RIDGE)
        b2_1.place(x=200,y=580,width=220,height=40)

        #photos button
        img9 = Image.open("college_images/photo.png")
        img9 = img9.resize((220, 220))
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b2=Button(self.bg_label,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b2.place(x=500,y=380,width=220,height=220)

        b2_1=Button(self.bg_label,text="Photos",cursor="hand2",command=self.open_img,font=("Helvetica", 15, "bold"), bg="dark blue", fg="white",bd=4, relief=RIDGE)
        b2_1.place(x=500,y=580,width=220,height=40)

        #developer button
        img10 = Image.open("college_images/developer.jpg")
        img10 = img10.resize((220, 220))
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b2=Button(self.bg_label,image=self.photoimg10,command=self.developer_data,cursor="hand2")
        b2.place(x=800,y=380,width=220,height=220)

        b2_1=Button(self.bg_label,text="Developer",command=self.developer_data,cursor="hand2",font=("Helvetica", 15, "bold"), bg="dark blue", fg="white",bd=4, relief=RIDGE)
        b2_1.place(x=800,y=580,width=220,height=40)

        #exit button
        img11 = Image.open("college_images/exit.jpg")
        img11= img11.resize((220, 220))
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b2=Button(self.bg_label,command=self.exist_data,image=self.photoimg11,cursor="hand2")
        b2.place(x=1100,y=380,width=220,height=220)

        b2_1=Button(self.bg_label,text="Exits",command=self.exist_data,cursor="hand2",font=("Helvetica", 15, "bold"), bg="dark blue", fg="white",bd=4, relief=RIDGE)
        b2_1.place(x=1100,y=580,width=220,height=40)

    #function button
    def student_detail(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

    
    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

    
    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

    def exist_data(self):
        self.iExit=tkinter.messagebox.askyesno("exist","r u sure u want to exit",parent=self.root)
        if self.iExit>0:
            self.root.destroy()
        else:
            return


    
    def open_img(self):
        os.startfile("data")








if __name__=="__main__":
    root=Tk()
    obj=face_recognition_system(root)
    root.mainloop()