from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk

class Course:
    def __init__(self,root):
        
        self.root=root
        self.root.title("Student Result Management Syatem") #add title on top of the screen
        self.root.geometry("1200x480+80+170") #size of the window 1350=width,700=height,0=x axis and 0=y axis
        self.root.config(bg="white") #background color of the window
        self.root.focus()

        #title
        title = Label(self.root, text="Manage Cource Details",bg="#0b5377", fg="white", font=("goudy old style", 20)).place(x=10,y=15,width=1180,height=35) #add title in header  

        #variable
        self.var_course=StringVar()
        self.var_duraction=StringVar()
        self.var_charges=StringVar()
        
        #widgets
        lbl_courseName=Label(self.root,text="Course Name",font=("goudy old style",15,'bold'),bg='white').place(x=10,y=60)
        lbl_duraction=Label(self.root,text="Duraction",font=("goudy old style",15,'bold'),bg='white').place(x=10,y=100)
        lbl_charges=Label(self.root,text="Charges",font=("goudy old style",15,'bold'),bg='white').place(x=10,y=140)
        lbl_descrption=Label(self.root,text="Description",font=("goudy old style",15,'bold'),bg='white').place(x=10,y=180)

        #Entry Fields
        self.txt_courseName=Entry(self.root,textvariable=self.var_course,font=("goudy old style",15,'bold'),bg='light yellow')
        self.txt_courseName.place(x=150,y=60,width=200)
        txt_duraction=Entry(self.root,textvariable=self.var_duraction,font=("goudy old style",15,'bold'),bg='light yellow').place(x=150,y=100,width=200)
        txt_charges=Entry(self.root,textvariable=self.var_charges,font=("goudy old style",15,'bold'),bg='light yellow').place(x=150,y=140,width=200)
        self.txt_description=Text(self.root,font=("goudy old style",15,'bold'),bg='light yellow')
        self.txt_description.place(x=150,y=180,width=500,height=130)

        # Buttons
        self.btn_add=Button(self.root,text="Save",font=("goudy old style",15,"bold"),bg="#2196f3",fg="white",cursor="hand2")
        self.btn_add.place(x=150,y=400,width=110,height=40)
        self.btn_update=Button(self.root,text="Update",font=("goudy old style",15,"bold"),bg="#4caf50",fg="white",cursor="hand2")
        self.btn_update.place(x=270,y=400,width=110,height=40)
        self.btn_delete=Button(self.root,text="Delete",font=("goudy old style",15,"bold"),bg="#f44336",fg="white",cursor="hand2")
        self.btn_delete.place(x=390,y=400,width=110,height=40)
        self.btn_clear=Button(self.root,text="Clear",font=("goudy old style",15,"bold"),bg="#607d8b",fg="white",cursor="hand2")
        self.btn_clear.place(x=510,y=400,width=110,height=40)

        # Search Panel
        self.var_search=StringVar()
        lbl_search_courseName=Label(self.root,text="Course Name",font=("goudy old style",15,'bold'),bg='white').place(x=720,y=60)
        txt_search_courseName=Entry(self.root,textvariable=self.var_search,font=("goudy old style",15,'bold'),bg='light yellow').place(x=870,y=60,width=180)

        btn_seaarch=Button(self.root,text="Search",font=("goudy old style",15,"bold"),bg="#03a9fd",fg="white",cursor="hand2").place(x=1070,y=60,width=120,height=28)

        # Content
        self.C_Frame=Frame(self.root,bd=2,relief=RIDGE)
        self.C_Frame.place(x=720,y=100,width=470,height=340)

        # scroll bar
        scrolly=Scrollbar(self.C_Frame,orient=VERTICAL)
        scrollx=Scrollbar(self.C_Frame,orient=HORIZONTAL)

        # course detail table
        self.CourseTable=ttk.Treeview(self.C_Frame,columns=("cid","name","duraction","charges","description"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.CourseTable.xview) #wo working scroll
        scrolly.config(command=self.CourseTable.yview)

        self.CourseTable.heading("cid",text="Course Id")
        self.CourseTable.heading("name",text="Name")
        self.CourseTable.heading("duraction",text="Duraction")
        self.CourseTable.heading("charges",text="Charges")
        self.CourseTable.heading("description",text="Description")
        self.CourseTable["show"]='headings'

        self.CourseTable.column("cid",width=100)
        self.CourseTable.column("name",width=100)
        self.CourseTable.column("duraction",width=100)
        self.CourseTable.column("charges",width=100)
        self.CourseTable.column("description",width=150)

        self.CourseTable.pack(fill=BOTH,expand=1)


if __name__=="__main__":
    root = Tk()  #tkinter object
    obj=Course(root)
    root.mainloop()