from html import unescape
from tkinter import *
from tkinter import ttk, messagebox
import sqlite3
import os
from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

class Report:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1200x480+200+250")
        self.root.config(bg="white")
        self.root.focus_force()

        #------------- title --------------
        title = Label(self.root, text="View Student Results", font=("goudy old style", 20, "bold"), bg="orange", fg="#262626").place(x=10, y=15, width=1180, height=50)

        #---------- search -------------
        self.var_search = StringVar()
        self.var_id = ""

        lbl_search = Label(self.root, text="Search By Roll No.", font=("goudy old style", 20, "bold"), bg="white").place(x=280, y=100)
        txt_search = Entry(self.root, textvariable=self.var_search, font=("goudy old style", 20), bg="lightyellow").place(x=520, y=100, width=150)
        btn_search = Button(self.root, text="Search", command=self.search, font=("goudy old style", 15, "bold"), bg="#03a9f4", fg="white", cursor="hand2").place(x=680, y=100, width=100, height=35)
        btn_clear = Button(self.root, text="Clear", command=self.clear, font=("goudy old style", 15, "bold"), bg="gray", fg="white", cursor="hand2").place(x=800, y=100, width=100, height=35)

        #------------- result labels -----------------
        lbl_roll = Label(self.root, text="Roll No", font=("goudy old style", 15, "bold"), bg="white", bd=2, relief=GROOVE).place(x=150, y=230, width=150, height=50)
        lbl_name = Label(self.root, text="Name", font=("goudy old style", 15, "bold"), bg="white", bd=2, relief=GROOVE).place(x=300, y=230, width=150, height=50)
        lbl_course = Label(self.root, text="Course", font=("goudy old style", 15, "bold"), bg="white", bd=2, relief=GROOVE).place(x=450, y=230, width=150, height=50)
        lbl_marks = Label(self.root, text="Marks Obtained", font=("goudy old style", 15, "bold"), bg="white", bd=2, relief=GROOVE).place(x=600, y=230, width=150, height=50)
        lbl_full = Label(self.root, text="Total Marks", font=("goudy old style", 15, "bold"), bg="white", bd=2, relief=GROOVE).place(x=750, y=230, width=150, height=50)
        lbl_per = Label(self.root, text="Percentage", font=("goudy old style", 15, "bold"), bg="white", bd=2, relief=GROOVE).place(x=900, y=230, width=150, height=50)
        
        self.roll = Label(self.root, font=("goudy old style", 15, "bold"), bg="white", bd=2, relief=GROOVE)
        self.roll.place(x=150, y=280, width=150, height=50)
        self.name = Label(self.root, font=("goudy old style", 15, "bold"), bg="white", bd=2, relief=GROOVE)
        self.name.place(x=300, y=280, width=150, height=50)
        self.course = Label(self.root, font=("goudy old style", 15, "bold"), bg="white", bd=2, relief=GROOVE)
        self.course.place(x=450, y=280, width=150, height=50)
        self.marks = Label(self.root, font=("goudy old style", 15, "bold"), bg="white", bd=2, relief=GROOVE)
        self.marks.place(x=600, y=280, width=150, height=50)
        self.full = Label(self.root, font=("goudy old style", 15, "bold"), bg="white", bd=2, relief=GROOVE)
        self.full.place(x=750, y=280, width=150, height=50)
        self.per = Label(self.root, font=("goudy old style", 15, "bold"), bg="white", bd=2, relief=GROOVE)
        self.per.place(x=900, y=280, width=150, height=50)

        btn_delete = Button(self.root, text="Delete", command=self.delete, font=("goudy old style", 15, "bold"), bg="red", fg="white", cursor="hand2").place(x=500, y=350, width=150, height=35)
        btn_print = Button(self.root, text="Print", command=self.print_result, font=("goudy old style", 15, "bold"), bg="green", fg="white", cursor="hand2").place(x=700, y=350, width=150, height=35)

    def search(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_search.get() == "":
                messagebox.showerror("Error", "Roll No. should be required", parent=self.root)
            else:
                cur.execute("select * from result where roll=?", (self.var_search.get(),))
                row = cur.fetchone()
                if row != None:
                    self.var_id = row[0]
                    self.roll.config(text=row[1])
                    self.name.config(text=row[2])
                    self.course.config(text=row[3])
                    self.marks.config(text=row[4])
                    self.full.config(text=row[5])
                    self.per.config(text=row[6])
                else:
                    messagebox.showerror("Error", "No record found!!!", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}")

    def clear(self):
        self.var_id = ""
        self.roll.config(text="")
        self.name.config(text="")
        self.course.config(text="")
        self.marks.config(text="")
        self.full.config(text="")
        self.per.config(text="")
        self.var_search.set("")

    def delete(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_id == "":
                messagebox.showerror("Error", "Search Student Result First", parent=self.root)
            else:
                cur.execute("select * from result where rid=?", (self.var_id,))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid Student Result", parent=self.root)
                else:
                    op = messagebox.askyesno("Confirm", "Do you really want to delete?", parent=self.root)
                    if op == True:
                        cur.execute("delete from result where rid=?", (self.var_id,))
                        con.commit()
                        messagebox.showinfo("Delete", "Result Deleted Successfully", parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}")

    def print_result(self):
        if self.var_id == "":
            messagebox.showerror("Error", "No data to print", parent=self.root)
            return
        
        # Create a new window for displaying the result
        print_window = Toplevel(self.root)
        print_window.title("Print Result")
        print_window.geometry("400x400+500+200")
        print_window.config(bg="white")
        
        # Display the result data in the new window
        Label(print_window, text="Student Result", font=("goudy old style", 20, "bold"), bg="orange", fg="#262626").pack(side=TOP, fill=X)
        
        result_details = f"""Roll No: {self.roll.cget('text')}
        Name: {self.name.cget('text')}
        Course: {self.course.cget('text')}
        Marks Obtained: {self.marks.cget('text')}
        Total Marks: {self.full.cget('text')}
        Percentage: {self.per.cget('text')}"""

        Label(print_window, text=result_details, font=("goudy old style", 15), bg="white", justify=LEFT).pack(pady=10)
        
        # Add result date
        Label(print_window, text="Result Date:", font=("goudy old style", 15, "bold"), bg="white").pack(pady=5)
        self.result_date = StringVar(value=datetime.now().strftime("%Y-%m-%d"))
        Entry(print_window, textvariable=self.result_date, font=("goudy old style", 15), bg="lightyellow").pack(pady=5)

        # Save result button
        btn_save = Button(print_window, text="Save as PDF", command=lambda: self.save_result_as_pdf(result_details), font=("goudy old style", 15, "bold"), bg="blue", fg="white", cursor="hand2")
        btn_save.pack(pady=20)

    def save_result_as_pdf(self, details):
        result_date = self.result_date.get()
        school_name = "P.P.SAVANI UNIVERSITY"  # You can customize this as needed

        # Define the folder where the results will be saved
        folder = "Student_Results_PDF"
        if not os.path.exists(folder):
            os.makedirs(folder)

        # Create a unique filename based on the roll number
        filename = f"{folder}/{self.roll.cget('text')}_result.pdf"

        c = canvas.Canvas(filename, pagesize=unescape(letter))
        width, height = unescape(letter)

        try:
            c = canvas.Canvas(filename, pagesize=letter)
            width, height = letter

            # Add School Name
            c.drawString(72, height - 100, f"School Name: {school_name}")

            # Add Result Date
            c.drawString(72, height - 120, f"Result Date: {result_date}")

            # Add Result Details
            lines = details.split('\n')
            y = height - 160
            for line in lines:
                c.drawString(72, y, line)
                y -= 20

            # Save the PDF file
            c.save()
            messagebox.showinfo("Saved", f"Result saved successfully as PDF at {filename}", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error saving the file: {str(ex)}", parent=self.root)

if __name__ == "__main__":
    root = Tk()
    obj = Report(root)
    root.mainloop()
