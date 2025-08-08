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

class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1505x790+0+0")
        self.root.title("Face Recognition System")

        self.var_attn_id=StringVar()
        self.var_attn_name=StringVar()
        self.var_roll=StringVar()
        self.var_dept=StringVar()
        self.var_date=StringVar()
        self.var_time=StringVar()
        self.var_attendance=StringVar()
        
        img=Image.open(r"college_images/iStock-182059956_18390_t12.jpg")
        img=img.resize((800,200))
        self.photoimg=ImageTk.PhotoImage(img)

        label1=Label(self.root,image=self.photoimg)
        label1.place(x=0,y=0,width=800,height=200)

        #2nd image
        img1=Image.open(r"college_images/smart-attendance.jpg")
        img1=img1.resize((800,200))
        self.photoimg1=ImageTk.PhotoImage(img1)
        label1=Label(self.root,image=self.photoimg1)
        label1.place(x=800,y=0,width=800,height=200)

        title_label = Label(self.root,
                            text="Attendance Management System",
                            font=("Helvetica", 38, "bold"), bg="#f0f8ff", fg="#0f52ba",bd=4, relief=RIDGE)
        title_label.place(x=0, y=200, width=1505, height=45)

        main_frame=Frame(self.root,bd=2,bg="#0f52ba")
        main_frame.place(x=20,y=245,width=1480,height=530)

        left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Attendance Details",bg="light blue",font=("Helvetica", 15, "bold"))
        left_frame.place(x=10,y=10,width=730,height=515)

        img_left=Image.open(r"college_images/smart-attendance.jpg")
        img_left=img_left.resize((720,130))
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        label_left=Label(left_frame,image=self.photoimg_left)
        label_left.place(x=5,y=0,width=720,height=130)

        left_inside_frame=Frame(left_frame,relief=RIDGE,bd=2)
        left_inside_frame.place(x=0,y=135,width=715,height=300)

        attendance_id=Label(left_inside_frame,text="Attendance ID:",font=("Helvetica", 12, "bold"))
        attendance_id.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        attendanceID_entry=ttk.Entry(left_inside_frame,textvariable=self.var_attn_id,width=20,font=("Helvetica", 12, "bold"))
        attendanceID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        name_label=Label(left_inside_frame,text="Name:",font=("Helvetica", 12, "bold"))
        name_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        name_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_attn_name,font=("Helvetica", 12, "bold"))
        name_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        roll_label=Label(left_inside_frame,text="Roll:",font=("Helvetica", 12, "bold"))
        roll_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        roll_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_roll,font=("Helvetica", 12, "bold"))
        roll_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        dept_label=Label(left_inside_frame,text="Deparment:",font=("Helvetica", 12, "bold"))
        dept_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        dept_entry=ttk.Entry(left_inside_frame,textvariable=self.var_dept,width=20,font=("Helvetica", 12, "bold"))
        dept_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        time_label=Label(left_inside_frame,text="Time:",font=("Helvetica", 12, "bold"))
        time_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        time_entry=ttk.Entry(left_inside_frame,textvariable=self.var_time,width=20,font=("Helvetica", 12, "bold"))
        time_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        date_label=Label(left_inside_frame,text="Date:",font=("Helvetica", 12, "bold"))
        date_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        date_entry=ttk.Entry(left_inside_frame,textvariable=self.var_date,width=20,font=("Helvetica", 12, "bold"))
        date_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        status_label=Label(left_inside_frame,text="Attendance status:",font=("Helvetica", 12, "bold"))
        status_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        status_combo=ttk.Combobox(left_inside_frame,textvariable=self.var_attendance,font=("Helvetica", 12, "bold"),state="readonly",width=18)
        status_combo["values"]=("Status","Present","Absent")
        status_combo.current(0)
        status_combo.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        button_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        button_frame.place(x=0,y=200,width=715,height=80)

        save_btn=Button(button_frame,text="Import csv ",command=self.import_csv,width=17,font=("Helvetica", 12, "bold"),bg="Light blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(button_frame,text="Export csv",command=self.export_csv,width=17,font=("Helvetica", 12, "bold"),bg="Light blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(button_frame,text="update",width=17,font=("Helvetica", 12, "bold"),bg="Light blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(button_frame,text="Reset",command=self.reset_data,width=16,font=("Helvetica", 12, "bold"),bg="Light blue",fg="white")
        reset_btn.grid(row=0,column=3)




        right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Attendance Details",bg="light blue",font=("Helvetica", 15, "bold"))
        right_frame.place(x=750,y=10,width=720,height=515)

        table_frame=Frame(right_frame,bd=2,relief=RIDGE)
        table_frame.place(x=5,y=5,width=720,height=450)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.attendance_table=ttk.Treeview(table_frame,columns=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.attendance_table.xview)
        scroll_y.config(command=self.attendance_table.yview)

        self.attendance_table.heading("id",text="Attendance Id")
        self.attendance_table.heading("roll",text="Roll")
        self.attendance_table.heading("name",text="Name")
        self.attendance_table.heading("department",text="Deparment")
        self.attendance_table.heading("time",text="Time")
        self.attendance_table.heading("date",text="Date")
        self.attendance_table.heading("attendance",text="Attendance")
        self.attendance_table["show"]="headings"

        self.attendance_table.column("id",width=100)
        self.attendance_table.column("roll",width=100)
        self.attendance_table.column("name",width=100)
        self.attendance_table.column("department",width=100)
        self.attendance_table.column("time",width=100)
        self.attendance_table.column("date",width=100)
        self.attendance_table.column("attendance",width=100)

        self.attendance_table.pack(fill=BOTH,expand=1)
        self.attendance_table.bind("<ButtonRelease>",self.get_cursor)
    
    def fetch_data(self,rows):
        self.attendance_table.delete(*self.attendance_table.get_children())
        for i in rows:
            self.attendance_table.insert("",END,values=i)

    def import_csv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open csv",filetypes=[("CSV File","*.csv"),("All File","*.*")],parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetch_data(mydata)

    def export_csv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("Error","No data found",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open csv",filetypes=[("CSV File","*.csv"),("All File","*.*")],parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("data export","data exprted to"+os.path.basename(fln)+" successfully",parent=self.root)
        except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)

    def get_cursor(self,event=""):
        cursor_focus=self.attendance_table.focus()
        content=self.attendance_table.item(cursor_focus)
        data=content["values"]

        self.var_attn_id.set(data[0])
        self.var_roll.set(data[1])
        self.var_attn_name.set(data[2])
        self.var_dept.set(data[3])
        self.var_time.set(data[4])
        self.var_date.set(data[5])
        self.var_attendance.set(data[6])

    def reset_data(self):
        self.var_attn_id.set("")
        self.var_roll.set("")
        self.var_attn_name.set("")
        self.var_dept.set("")
        self.var_time.set("")
        self.var_date.set("")
        self.var_attendance.set("") 
    










if __name__=="__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()