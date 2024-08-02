from tkinter import*
from PIL import Image,ImageTk
class RMS:
    def __init__(self,root):
        

        self.root=root
        self.root.title("Student Result Management Syatem")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        
        # icons
        self.logo_dash=ImageTk.PhotoImage(file="images/logo_p.png")
        # title
        title = Label(self.root, text="Student Result Management System",padx=10,compound=LEFT,image=self.logo_dash,bg="#0b5377", fg="white", font=("Arial", 20)).place(x=0,y=0,relwidth=1,height=50)

        # menu
        M_Frame=LabelFrame(self.root,text="Menus",font=("times neew roman",15),bg="white")
        M_Frame.place(x=100,y=70,width=1340,height=80) #height of the menu title

        btn_course=Button(M_Frame,text="Course",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2").place(x=20,y=5,width=200,height=40)
        btn_student=Button(M_Frame,text="Student",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2").place(x=240,y=5,width=200,height=40)
        btn_result=Button(M_Frame,text="Result",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2").place(x=460,y=5,width=200,height=40)
        btn_view=Button(M_Frame,text="View Student Result",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2").place(x=680,y=5,width=200,height=40)
        btn_logout=Button(M_Frame,text="Logout",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2").place(x=900,y=5,width=200,height=40)
        btn_exit=Button(M_Frame,text="Exit",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2").place(x=1120,y=5,width=200,height=40)

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

        self.lbl_result=Label(self.root,text="Total Result\n[ 0 ]",font=("goudy old stye",20),bd=10,relief=RIDGE,bg="#038074", fg="white",)
        self.lbl_result.place(x=1020,y=530,width=300,height=100)

        # footer
        footer = Label(self.root, text="SRMS-Student Result Management System",bg="#262626", fg="white", font=("goudy old style", 12)).pack(side="bottom",fill=X)

      
if __name__=="__main__":
    root = Tk()
    obj=RMS(root)
    root.mainloop()