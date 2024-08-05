import os
import sqlite3
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from course import Course
from student import Student
from result import Result
from report import Report

class RMS:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1350x700+110+80")
        self.root.config(bg="white")
        
        # icons
        self.logo_dash = ImageTk.PhotoImage(file="images/logo_p.png")
        # title
        title = Label(self.root, text="Student Result Management System", padx=10, compound=LEFT,image=self.logo_dash, bg="#0b5377", fg="white", font=("goudy old style", 20)).place(x=0, y=0, relwidth=1, height=50)
     
        # menu
        M_Frame = LabelFrame(self.root, text="Menus", font=("times new roman", 15), bg="white")
        M_Frame.place(x=12, y=60, width=1330, height=80)  # Adjusted width and position

       
        btn_course=Button(M_Frame,text="Course",command=self.add_course,font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2").place(x=20,y=5,width=250,height=40)
        btn_student=Button(M_Frame,text="Student",command=self.add_student,font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2").place(x=280,y=5,width=250,height=40)
        btn_result=Button(M_Frame,text="Result",command=self.add_result,font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2").place(x=540,y=5,width=250,height=40)
        btn_view=Button(M_Frame,text="View Result",command=self.add_report,font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2").place(x=800,y=5,width=250,height=40)
        btn_exit=Button(M_Frame,text="Exit",command=self.exit,font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2").place(x=1060,y=5,width=250,height=40)

        # Content Window
        self.bg_img = Image.open("images/bg.png")
        self.bg_img = self.bg_img.resize((920, 350), Image.LANCZOS)
        self.bg_img = ImageTk.PhotoImage(self.bg_img)

        self.lbl_bg = Label(self.root, image=self.bg_img).place(x=400, y=180, width=920, height=350)
        
        # update_details
        self.lbl_course = Label(self.root, text="Total Course\n[ 0 ]", font=("goudy old style", 20), bd=10, relief=RIDGE, bg="#e43b06", fg="white")
        self.lbl_course.place(x=400, y=530, width=300, height=100)

        self.lbl_student = Label(self.root, text="Total Student\n[ 0 ]", font=("goudy old style", 20), bd=10,relief=RIDGE, bg="#0676ad", fg="white")
        self.lbl_student.place(x=710, y=530, width=300, height=100)

        self.lbl_result = Label(self.root, text="Total Result\n[ 0 ]", font=("goudy old style", 20), bd=10,relief=RIDGE, bg="#038074", fg="white")
        self.lbl_result.place(x=1020, y=530, width=300, height=100)

        self.update_details()

        # footer
        footer = Label(self.root, text="SRMS - Student Result Management System", bg="#262626", fg="white",
                       font=("goudy old style", 12)).pack(side="bottom", fill=X)

    def connect_db(self):
        """Connect to the SQLite database."""
        con = sqlite3.connect("rms.db")
        cur = con.cursor()
        return con, cur

    def update_details(self):
        con, cur = self.connect_db()

        try:
            cur.execute("SELECT COUNT(*) FROM course")
            total_courses = cur.fetchone()[0]
            self.lbl_course.config(text=f"Total Course\n[ {total_courses} ]")

            cur.execute("SELECT COUNT(*) FROM student")
            total_students = cur.fetchone()[0]
            self.lbl_student.config(text=f"Total Student\n[ {total_students} ]")

            cur.execute("SELECT COUNT(*) FROM result")
            total_results = cur.fetchone()[0]
            self.lbl_result.config(text=f"Total Result\n[ {total_results} ]")
        except sqlite3.Error as e:
            messagebox.showerror("Database Error", f"Error occurred: {e}")
        finally:
            con.close()

    # Course button working
    def add_course(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = Course(self.new_win)
        self.new_win.protocol("WM_DELETE_WINDOW", self.on_closing)

    # Student button working
    def add_student(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = Student(self.new_win)
        self.new_win.protocol("WM_DELETE_WINDOW", self.on_closing)

    # Result button working
    def add_result(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = Result(self.new_win)
        self.new_win.protocol("WM_DELETE_WINDOW", self.on_closing)
    
    # View result working
    def add_report(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = Report(self.new_win)

    # exit button working
    def exit(self):
        op = messagebox.askyesno("Confirm", "Do you really want to Exit?", parent=self.root)
        if op == True:
            self.root.destroy()

    def on_closing(self):
        self.update_details()
        self.new_win.destroy()

if __name__ == "__main__":
    root = Tk()
    obj = RMS(root)
    root.mainloop()
