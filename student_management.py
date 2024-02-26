from tkinter import *
from tkinter import ttk
import mysql.connector as connecter

con = connecter.connect(
    host="localhost", database="studmanage", username="root")

cursor = con.cursor()


def submit():
    cursor.execute(f'''insert into  stud_details(Name,Father_name,Mother_name,address,email,dob,mobile_no,gender,stream,course,hobby)
                VALUES ("{e1.get()}","{e2.get()}","{e3.get()}","{e4.get()}","{e5.get()}","{e6.get()}","{e7.get()}",
                "{gender.get()}","{stream.get()}","{cor.get()}","{e11.get()}")''')
    clear()
    con.commit()


def clear():
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)
    e6.delete(0, END)
    e7.delete(0, END)
    cor.delete(0, END)
    e11.delete(0, END)


def show_det():
    cursor.execute('Select * from stud_details')
    data = cursor.fetchall()

    f5 = Toplevel(win)

    t1 = ttk.Treeview(
        f5, columns=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], show="headings")
    t1.heading(column=0, text="Student_Name")
    t1.heading(column=1, text="Father_Name")

    t1.heading(column=2, text="Mother_Name")
    t1.heading(column=3, text="Address")
    t1.heading(column=4, text="E-mail")
    t1.heading(column=5, text="DOB")
    t1.heading(column=6, text="Mobile no")
    t1.heading(column=7, text="Gender")
    t1.heading(column=8, text="Stream")
    t1.heading(column=9, text="Course")
    t1.heading(column=10, text="Hobby")

    for i in range(len(data)):
        t1.insert(parent='', index=END, values=data[i])

    t1.pack()
    f5.mainloop()


def update_det():

    def subm():
  
        cursor.execute(f'''update stud_details set Name="{t2.get()}",Father_name="{e2.get()}",Mother_name="{e3.get()}",address="{e4.get()}",email="{e5.get()}",dob="{e6.get()}", mobile_no="{e7.get()}",
                gender="{gender.get()}",stream="{stream.get()}",course="{cor.get()}",hobby="{e11.get()}" where mobile_no = "{t1.get()}"''')
        con.commit()

    f8 = Toplevel(win)
    f8.geometry('500x500')

    a1 = Label(f8, text='Please enter your Mobile Number :')
    a1.grid(row=0, column=1)

    t1 = Entry(f8)
    t1.grid(row=0, column=2)

    a2 = Label(f8, text='Update')
    a2.grid(row=1, column=2)

    a3 = Label(f8, text="Student Name :", font=("Arial", 0, "bold"))
    a3.grid(row=2, column=1)

    
    t2 = Entry(f8, width=30, justify="center", font=("Arial", 0, ""))
    t2.grid(row=2, column=2)

    l2 = Label(f8, text="Father Name :", font=("Arial", 0, "bold"))
    l2.grid(row=3, column=1)

    e2 = Entry(f8, width=30, justify="center", font=("Arial", 0, ""))
    e2.grid(row=3, column=2, pady=10)

    l3 = Label(f8, text="Mother Name :", font=("Arial", 0, "bold"))
    l3.grid(row=4, column=1)

    e3 = Entry(f8, width=30, justify="center", font=("Arial", 0, ""))
    e3.grid(row=4, column=2)

    l4 = Label(f8, text="Address :", font=("Arial", 0, "bold"))
    l4.grid(row=5, column=1)

    e4 = Entry(f8, width=30, justify="center", font=("Arial", 0, ""))
    e4.grid(row=5, column=2, pady=10)

    l5 = Label(f8, text="E-mail :", font=("Arial", 0, "bold"))
    l5.grid(row=6, column=1)

    e5 = Entry(f8, width=30, justify="center", font=("Arial", 0, ""))
    e5.grid(row=6, column=2)

    l6 = Label(f8, text="Date of birth :", font=("Arial", 0, "bold"))
    l6.grid(row=7, column=1)

    e6 = Entry(f8, width=30, justify="center", font=("Arial", 0, ""))
    e6.grid(row=7, column=2, pady=10)

    l7 = Label(f8, text="Mobile No :", font=("Arial", 0, "bold"))
    l7.grid(row=8, column=1)

    e7 = Entry(f8, width=30, justify="center", font=("Arial", 0, ""))
    e7.grid(row=8, column=2)

    f1 = Frame(f8)

    gender = StringVar()

    l8 = Label(f8, text="Gender :", font=("Arial", 0, "bold"))
    l8.grid(row=9, column=1)

    g1 = Radiobutton(f1, text="Male", value="Male", variable=gender)
    g2 = Radiobutton(f1, text="Female", value="Female", variable=gender)
    g1.grid(row=9, column=2)
    g2.grid(row=9, column=3)

    f1.grid(row=9, columnspan=3, pady=10)

    f2 = Frame(f8)

    stream = StringVar()

    l9 = Label(f8, text="Stream :", font=("Arial", 0, "bold"))
    l9.grid(row=10, column=1)

    s1 = Radiobutton(f2, text="Science", value="Science", variable=stream)
    s2 = Radiobutton(f2, text="Commerce", value="Commerce", variable=stream)
    s3 = Radiobutton(f2, text="Arts", value="Arts", variable=stream)
    s1.grid(row=10, column=2)
    s2.grid(row=10, column=4)
    s3.grid(row=10, column=6)
    f2.grid(row=10, columnspan=3)

    l10 = Label(f8, text="Course :", font=("Arial", 0, "bold"))
    l10.grid(row=11, column=1, pady=10)

    cor = ttk.Combobox(f8)
    cor['values'] = ['BSCIT', 'BSCCS', 'BCOM', 'BMS', 'BAF', 'BMM']
    cor.grid(row=11, columnspan=3)

    l11 = Label(f8, text="Hobby :", font=("Arial", 0, "bold"))
    l11.grid(row=12, column=1)

    e11 = Entry(f8, width=30, font=("Arial", 0, ""))
    e11.grid(row=12, column=2, pady=10)

    b1 = Button(f8, text="Submit", command=subm)
    b1.grid(row=13, column=2, pady=10)

    f8.mainloop()


def delete_det():

    def sub():
        cursor.execute(f'delete from stud_details where "{en1.get()}"')
        con.commit()

    f7 = Toplevel(win)
    la = Label(f7, text="Enter your Name:")
    la.grid(row=0, column=1)
    en = Entry(f7)
    en.grid(row=0, column=2)

    lab = Label(f7, text="Enter Mobile No:")
    lab.grid(row=1, column=1)
    en1 = Entry(f7)
    en1.grid(row=1, column=2)

    b8 = Button(f7, text="Submit", command=sub)
    b8.grid(row=2, column=2)
    f7.mainloop()


win = Tk()
win.title("Student Management")
win.geometry('500x500')

f4 = Frame(win)

l1 = Label(f4, text="Student Name :", font=("Arial", 0, "bold"))
l1.grid(row=2, column=1)

e1 = Entry(f4, width=30, justify="center", font=("Arial", 0, ""))
e1.grid(row=2, column=2)


l2 = Label(f4, text="Father Name :", font=("Arial", 0, "bold"))
l2.grid(row=3, column=1)

e2 = Entry(f4, width=30, justify="center", font=("Arial", 0, ""))
e2.grid(row=3, column=2, pady=10)


l3 = Label(f4, text="Mother Name :", font=("Arial", 0, "bold"))
l3.grid(row=4, column=1)

e3 = Entry(f4, width=30, justify="center", font=("Arial", 0, ""))
e3.grid(row=4, column=2)

l4 = Label(f4, text="Address :", font=("Arial", 0, "bold"))
l4.grid(row=5, column=1)

e4 = Entry(f4, width=30, justify="center", font=("Arial", 0, ""))
e4.grid(row=5, column=2, pady=10)

l5 = Label(f4, text="E-mail :", font=("Arial", 0, "bold"))
l5.grid(row=6, column=1)

e5 = Entry(f4, width=30, justify="center", font=("Arial", 0, ""))
e5.grid(row=6, column=2)

l6 = Label(f4, text="Date of birth :", font=("Arial", 0, "bold"))
l6.grid(row=7, column=1)

e6 = Entry(f4, width=30, justify="center", font=("Arial", 0, ""))
e6.grid(row=7, column=2, pady=10)

l7 = Label(f4, text="Mobile No :", font=("Arial", 0, "bold"))
l7.grid(row=8, column=1)

e7 = Entry(f4, width=30, justify="center", font=("Arial", 0, ""))
e7.grid(row=8, column=2)

f1 = Frame(f4)

gender = StringVar()

l8 = Label(f4, text="Gender :", font=("Arial", 0, "bold"))
l8.grid(row=9, column=1)

g1 = Radiobutton(f1, text="Male", value="Male", variable=gender)
g2 = Radiobutton(f1, text="Female", value="Female", variable=gender)
g1.grid(row=9, column=2)
g2.grid(row=9, column=3)

f1.grid(row=9, columnspan=3, pady=10)

f2 = Frame(f4)

stream = StringVar()

l9 = Label(f4, text="Stream :", font=("Arial", 0, "bold"))
l9.grid(row=10, column=1)

s1 = Radiobutton(f2, text="Science", value="Science", variable=stream)
s2 = Radiobutton(f2, text="Commerce", value="Commerce", variable=stream)
s3 = Radiobutton(f2, text="Arts", value="Arts", variable=stream)
s1.grid(row=10, column=2)
s2.grid(row=10, column=4)
s3.grid(row=10, column=6)
f2.grid(row=10, columnspan=3)

l10 = Label(f4, text="Course :", font=("Arial", 0, "bold"))
l10.grid(row=11, column=1, pady=10)

cor = ttk.Combobox(f4)
cor['values'] = ['BSCIT', 'BSCCS', 'BCOM', 'BMS', 'BAF', 'BMM']
cor.grid(row=11, columnspan=3)


l11 = Label(f4, text="Hobby :", font=("Arial", 0, "bold"))
l11.grid(row=12, column=1)

e11 = Entry(f4, width=30, justify="center", font=("Arial", 0, ""))
e11.grid(row=12, column=2, pady=10)

b1 = Button(f4, text="Submit", command=submit)
b1.grid(row=13, column=2, pady=10)

b2 = Button(f4, text="Update", command=update_det)
b2.grid(row=14, column=1)

b3 = Button(f4, text="Delete", command=delete_det)
b3.grid(row=14, column=2)


b4 = Button(f4, text="Show Details", command=show_det)
b4.grid(row=14, column=5)

f4.pack()


win.mainloop()
