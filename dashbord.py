from tkinter import*
from PIL import Image,ImageTk
from course import Course
from student import Student
from result import Result

class RMS:
    def __init__(self,root):
        

        self.root=root
        self.root.title("Student Result Management Syatem") #add title on top of the screen
        self.root.geometry("1350x700+0+0") #size of the window 1350=width,700=height,0=x axis and 0=y axis
        self.root.config(bg="white") #background color of the window
        
        # icons
        self.logo_dash=ImageTk.PhotoImage(file="images/logo_p.png") #add icon in header
        # title
        title = Label(self.root, text="Student Result Management System",padx=10,compound=LEFT,image=self.logo_dash,bg="#0b5377", fg="white", font=("goudy old style", 20)).place(x=0,y=0,relwidth=1,height=50) #add title in header
     
        # menu
        M_Frame=LabelFrame(self.root,text="Menus",font=("times neew roman",15),bg="white")
        M_Frame.place(x=40,y=70,width=1470,height=80) #height of the menu title

        btn_course=Button(M_Frame,text="Course",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_course).place(x=20,y=5,width=220,height=40)
        btn_student=Button(M_Frame,text="Student",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_student).place(x=260,y=5,width=220,height=40)
        btn_result=Button(M_Frame,text="Result",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_result).place(x=500,y=5,width=220,height=40)
        btn_view=Button(M_Frame,text="View Student Result",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2").place(x=740,y=5,width=220,height=40)
        btn_logout=Button(M_Frame,text="Logout",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2").place(x=980,y=5,width=220,height=40)
        btn_exit=Button(M_Frame,text="Exit",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2").place(x=1220,y=5,width=220,height=40)

        # Contant Window
        self.bg_img=Image.open("images/bg.png")
        self.bg_img=self.bg_img.resize((920,350),Image.LANCZOS)
        self.bg_img=ImageTk.PhotoImage(self.bg_img)

        self.lbl_bg=Label(self.root,image=self.bg_img).place(x=400,y=180,width=920,height=350)
        
        # update_details
        self.lbl_course=Label(self.root,text="Total Course\n[ 0 ]",font=("goudy old stye",20),bd=10,relief=RIDGE,bg="#e43b06", fg="white",)
        self.lbl_course.place(x=400,y=530,width=300,height=100)

        self.lbl_student=Label(self.root,text="Total Student\n[ 0 ]",font=("goudy old stye",20),bd=10,relief=RIDGE,bg="#0676ad", fg="white",)
        self.lbl_student.place(x=710,y=530,width=300,height=100)

        self.lbl_result=Label(self.root,text="Total Result\n[ 0 ]",font=("goudy old stye",20),bd=10,relief=RIDGE,bg="#038074", fg="white",)
        self.lbl_result.place(x=1020,y=530,width=300,height=100)

        # footer
        footer = Label(self.root, text="SRMS-Student Result Management System",bg="#262626", fg="white", font=("goudy old style", 12)).pack(side="bottom",fill=X)
    
    # course button working
    def add_course(self): #function for course
        self.new_win=Toplevel(self.root)
        self.new_obj=Course(self.new_win)

    # Student button working
    def add_student(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=Student(self.new_win)

    # result butooon working
    def add_result(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=Result(self.new_win)
      
if __name__=="__main__":
    root = Tk()  #tkinter object
    obj=RMS(root)
    root.mainloop()