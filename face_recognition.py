from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import numpy as np
import mysql.connector
import cv2
import os
from time import strftime
from datetime import datetime


class Face_Recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_label = Label(self.root,
                            text="FACE RECOGNITION",
                            font=("Helvetica", 38, "bold"), bg="light blue", fg="#da16c6",bd=4, relief=RIDGE)
        title_label.place(x=0, y=0, width=1530, height=45)
        img_top=Image.open(r"college_images/face_detector1.jpg")
        img_top=img_top.resize((650,700))
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=650,height=700)

        img_bottom=Image.open(r"college_images/facial_recognition_system_identification_digital_id_security_scanning_thinkstock_858236252_3x3-100740902-large.jpg")
        img_bottom=img_bottom.resize((950,700))
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f_lbl=Label(self.root,image=self.photoimg_bottom) 
        f_lbl.place(x=650,y=55,width=950,height=700)

        #button
        b2_1=Button(f_lbl,text="Face Recognition",cursor="hand2",command=self.face_recog,font=("Helvetica", 18, "bold"), bg="light blue", fg="#da16c6",bd=4, relief=RIDGE)
        b2_1.place(x=365,y=620,width=210,height=40)

    # function
    #ateendace
    def mark_attendance(self,i,r,n,d):
        with open("priya.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.write(f"\n{i},{r},{n},{d},{dtString},{d1},Present")


    def face_recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighnors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighnors)

            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="face_recognisation")
                my_cursor=conn.cursor()

                my_cursor.execute("SELECT Name FROM students WHERE Student_id=" + str(id))
                result = my_cursor.fetchone()
                n = "+".join(result) if result else "Unknown"

                # Get Roll
                my_cursor.execute("SELECT Roll FROM students WHERE Student_id=" + str(id))
                result = my_cursor.fetchone()
                r = "+".join(result) if result else "Unknown"

                    # Get Department
                my_cursor.execute("SELECT Dep FROM students WHERE Student_id=" + str(id))
                result = my_cursor.fetchone()
                d = "+".join(result) if result else "Unknown"

                my_cursor.execute("SELECT Student_id FROM students WHERE Student_id=" + str(id))
                result = my_cursor.fetchone()
                i = "+".join(result) if result else "Unknown"
                conn.close()



                if confidence>77: #percentage of recognition
                    cv2.putText(img,f"ID:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,25,255),3)
                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,25,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,25,255),3)
                    cv2.putText(img,f"Deparment:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,25,255),3)
                    self.mark_attendance(i,r,n,d)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,2555,255),3)

                coord=[x,y,w,h]
            return coord
        
        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)


        while True:
            ret,img=video_cap.read()
            if not ret or img is None:
                print("Failed to grab frame.")
                continue
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome to face reconisation",img)

            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()









if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()