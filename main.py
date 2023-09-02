
from tkinter import *
from PIL import ImageTk,Image
import pyodbc
from tkinter import messagebox
from AddBooks import *
from DeleteBook import *
from ViewBooks import *
from SearchBook import *
from IssueBook import *
from ReturnBook import *



# Enter Table Names here
empTable = "Emp" #Employee Table
stuTable = "stud" #Student Table

root = Tk()
root.title("UBIT Library")
root.minsize(width=400,height=400)
root.geometry("600x500")
count = 0
empFrameCount = 0

con = pyodbc.connect('Driver={SQL SERVER};'
                    'Server= your server;'
                    'Database=Library management system;'
                    'Trusted_Connection=yes;')
cur = con.cursor()


'''
This are the menus after logging in
'''
def empMenu():
    
    global headingFrame1,headingFrame2,headingLabel,SubmitBtn,Canvas1,labelFrame,backBtn,btn1,btn2,btn3,btn4,btn5,btn6,btn7
    headingFrame1.destroy()
    headingFrame2.destroy()
    headingLabel.destroy()
    Canvas1.destroy()
    SubmitBtn.destroy()

    Canvas1 = Canvas(root)

    Canvas1.config(bg="#FFEBCD",width = newImageSizeWidth, height = newImageSizeHeight)
    Canvas1.pack(expand=True,fill=BOTH)
    
    headingFrame1 = Frame(root,bg="#333945",bd=5)
    headingFrame1.place(relx=0.25,rely=0.08,relwidth=0.5,relheight=0.13)
        
    headingFrame2 = Frame(headingFrame1,bg="#EAF0F1")
    headingFrame2.place(relx=0.01,rely=0.05,relwidth=0.98,relheight=0.9)
        
    headingLabel = Label(headingFrame2, text="Employee MENU", fg='black')
    headingLabel.place(relx=0.25,rely=0.15, relwidth=0.5, relheight=0.5)
    
    btn1 = Button(root,text="Add Book Details",bg='black', fg='white', command=addBooks)
    btn1.place(relx=0.28,rely=0.275, relwidth=0.45,relheight=0.095)
    
    btn2 = Button(root,text="Delete Book",bg='black', fg='white', command=delete)
    btn2.place(relx=0.28,rely=0.37, relwidth=0.45,relheight=0.095)
    
    btn3 = Button(root,text="View Book List",bg='black', fg='white', command=View)
    btn3.place(relx=0.28,rely=0.46, relwidth=0.45,relheight=0.095)
    
    btn4 = Button(root,text="Search Book",bg='black', fg='white', command=searchBook)
    btn4.place(relx=0.28,rely=0.55, relwidth=0.45,relheight=0.095)
    
    btn5 = Button(root,text="Issue Book to Student",bg='black', fg='white', command = issueBook)
    btn5.place(relx=0.28,rely=0.64, relwidth=0.45,relheight=0.095)

    btn6 = Button(root, text="Return Book", bg='black', fg='white', command=returnBook)
    btn6.place(relx=0.28, rely=0.73, relwidth=0.45, relheight=0.095)

    btn7 = Button(root, text="Register", bg='black', fg='white', command=Student)
    btn7.place(relx=0.28, rely=0.82, relwidth=0.45, relheight=0.095)

    backBtn = Button(root,text="Logout",bg='#455A64', fg='white', command=Employee)
    backBtn.place(relx=0.06,rely=0.9, relwidth=0.18,relheight=0.08)
    



'''
This Section handles the database
'''
def gettingEmpDetails():
    
    EmpId = en1.get()
    name = en2.get()
    password = en3.get()

    
    try:
        if (type(int(EmpId)) == int):
            pass
        else:
            messagebox.showinfo("Invalid Value","Employee ID should be an integer")
            return
    except:
        messagebox.showinfo("Invalid Value","Employee ID should be an integer")
        return
        

    
    sql = "insert into "+empTable+" values ('"+EmpId+"','"+name+"','"+password+"')"
    try:
        cur.execute(sql)
        con.commit()
    except:
        messagebox.showinfo("Error inserting","Cannot add data to Database")
    
    print(EmpId)
    print(name)
    print(password)

    en1.delete(0, END)
    en2.delete(0, END)
    en3.delete(0, END)


def gettingStuDetails():
    
    Rollno = en1.get()
    name = en2.get()
    contact = en3.get()
    gender = en4.get()
    department = en5.get()
    
    try:
        if (type(int(Rollno)) == int):
            pass
        else:
            messagebox.showinfo("Invalid Value","Roll number should be an integer")
            return
    except:
        messagebox.showinfo("Invalid Value","Roll number should be an integer")
        return

    
    sql = "insert into "+stuTable+" values ('"+Rollno+"','"+name+"','"+contact+"','"+gender+"','"+department+"')"
    try:
        cur.execute(sql)
        con.commit()
    except:
        messagebox.showinfo("Error inserting","Cannot add data to Database")
        
    print(Rollno)
    print(name)
    print(contact)
    print(gender)
    print(department)
    en1.delete(0, END)
    en2.delete(0, END)
    en3.delete(0, END)
    en4.delete(0, END)
    en5.delete(0, END)

    
def gettingLoginDetails():
    
    login =en1.get()
    name = en2.get()
    password = en3.get()


    

    sqlLoginID = "select empid from "+empTable+" where password = '"+password+"'"
    sqlName = "select name from "+empTable+" where password = '"+password+"'"
        
    try:
        cur.execute(sqlLoginID)
        for i in cur:
         getLoginID = i[0]
        cur.execute(sqlName)
        for i in cur:
            getName = i[0]

        if(getLoginID == login and getName == name):
            empMenu()
            messagebox.showinfo("SUCCESS","You have successfully logged in")
        else:
            messagebox.showerror("Failure","Can't log in, check your credentials")
    except:
        messagebox.showinfo("FAILED","Please check your credentials")

    
def EmpRegister():
    btn1.destroy()
    btn2.destroy()
    btn4.destroy()
    global labelFrame
    
    global count
    count += 1

    if(count>=2):
        labelFrame.destroy()
    
    global en1,en2,en3,en4,en5,en6

    labelFrame = Frame(root, bg='#8B2323')
    labelFrame.place(relx=0.2, rely=0.44, relwidth=0.6, relheight=0.3)
    
    # Employee ID
    lb1 = Label(labelFrame,text="Emp ID : ", bg='#8B2323', fg='white')
    lb1.place(relx=0.05,rely=0.08)
    
    en1 = Entry(labelFrame)
    en1.place(relx=0.3,rely=0.08, relwidth=0.62)
    
    #Employee Name
    lb2 = Label(labelFrame,text="Name : ", bg='#8B2323', fg='white')
    lb2.place(relx=0.05,rely=0.35)
    
    en2 = Entry(labelFrame)
    en2.place(relx=0.3,rely=0.35, relwidth=0.62)
    
    #Employee Paswword
    lb3 = Label(labelFrame,text="Password : ", bg='#8B2323', fg='white')
    lb3.place(relx=0.05,rely=0.62)
    
    en3 = Entry(labelFrame)
    en3.place(relx=0.3,rely=0.62, relwidth=0.62)
    
    #Submit Button
    SubmitBtn = Button(root,text="SUBMIT",bg='#264348', fg='white',command=gettingEmpDetails)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)

    Backbtn = Button(root, text="<-- Back", bg='black', fg='white', command=Student)
    Backbtn.place(relx=0.02, rely=0.1, relwidth=0.18, relheight=0.08)

# Login both for Employee and Student
def Login():
    
    global labelFrame
    
    global count
    count += 1

    if(count>=2):
        labelFrame.destroy()
    
    global en1,en2,en3,en4,SubmitBtn,btn1,btn2
    
    labelFrame = Frame(root,bg='#242424')
    labelFrame.place(relx=0.2,rely=0.44,relwidth=0.6,relheight=0.3)
    
    # Login ID
    lb1 = Label(labelFrame,text="Login ID : ", bg='#242424', fg='white')
    lb1.place(relx=0.05,rely=0.1)
    
    en1 = Entry(labelFrame)
    en1.place(relx=0.3,rely=0.1, relwidth=0.62)
    
    # Name
    lb2 = Label(labelFrame,text="Name : ", bg='#242424', fg='white')
    lb2.place(relx=0.05,rely=0.3)
    
    en2 = Entry(labelFrame)
    en2.place(relx=0.3,rely=0.3, relwidth=0.62)
    
    # Paswword
    lb3 = Label(labelFrame,text="Password : ", bg='#242424', fg='white')
    lb3.place(relx=0.05,rely=0.5)
    
    en3 = Entry(labelFrame)
    en3.place(relx=0.3,rely=0.5, relwidth=0.62)
    

    
    #Submit Button
    SubmitBtn = Button(root,text="SUBMIT",bg='#264348', fg='white',command=gettingLoginDetails)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)

# Student Registration
def studentRegister():
    btn2.destroy()
    btn4.destroy()
    global labelFrame
    
    global count
    count += 1

    if(count>=2):
        labelFrame.destroy()
    
    global en1,en2,en3,en4,en5
    
    labelFrame = Frame(root,bg='#8B2323')
    labelFrame.place(relx=0.2,rely=0.40,relwidth=0.6,relheight=0.42)
    
    # Student Roll no
    lb1 = Label(labelFrame,text="Roll No : ", bg='#8B2323', fg='white')
    lb1.place(relx=0.05,rely=0.05)
    
    en1 = Entry(labelFrame)
    en1.place(relx=0.3,rely=0.05, relwidth=0.62)
    
    # Sudent Name
    lb2 = Label(labelFrame,text="Name : ", bg='#8B2323', fg='white')
    lb2.place(relx=0.05,rely=0.2)
    
    en2 = Entry(labelFrame)
    en2.place(relx=0.3,rely=0.2, relwidth=0.62)
    
    # Student contact
    lb3 = Label(labelFrame,text="Contact : ", bg='#8B2323', fg='white')
    lb3.place(relx=0.05,rely=0.35)
    
    en3 = Entry(labelFrame)
    en3.place(relx=0.3,rely=0.35, relwidth=0.62)

    # Student Gender
    lb4 = Label(labelFrame, text="Gender : ", bg='#8B2323', fg='white')
    lb4.place(relx=0.05, rely=0.5)

    en4 = Entry(labelFrame)
    en4.place(relx=0.3, rely=0.5, relwidth=0.62)

    # Student Department
    lb5 = Label(labelFrame, text="Department : ", bg='#8B2323', fg='white')
    lb5.place(relx=0.05, rely=0.65)

    en5 = Entry(labelFrame)
    en5.place(relx=0.3, rely=0.65, relwidth=0.62)
    #Submit Button
    SubmitBtn = Button(root,text="SUBMIT",bg='#264348', fg='white',command=gettingStuDetails)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)

    Backbtn = Button(root, text="<-- Back", bg='black', fg='white', command=Student)
    Backbtn.place(relx=0.02, rely=0.1, relwidth=0.18, relheight=0.08)

# Employee Home Page 
def Employee():
    
    global headingFrame1,headingFrame2,headingLabel,btn1,Canvas1
    headingFrame1.destroy()
    headingFrame2.destroy()
    headingLabel.destroy()
    Canvas1.destroy()
    btn1.destroy()
    
    Canvas1 = Canvas(root)

    Canvas1.config(bg="#838B8B",width = newImageSizeWidth, height = newImageSizeHeight)
    Canvas1.pack(expand=True,fill=BOTH)

    
    headingFrame1 = Frame(root,bg="#333945",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
    
    headingFrame2 = Frame(headingFrame1,bg="#EAF0F1")
    headingFrame2.place(relx=0.01,rely=0.05,relwidth=0.98,relheight=0.9)
    
    headingLabel = Label(headingFrame2, text="Hello, Employee", fg='black')
    headingLabel.place(relx=0.25,rely=0.15, relwidth=0.5, relheight=0.5)
    

    
    btn2 = Button(root,text="Login",bg='black', fg='white', command=Login)
    btn2.place(relx=0.3,rely=0.5, relwidth=0.4,relheight=0.1)
    
    btn3 = Button(root,text="Quit",bg='#455A64', fg='white', command=root.quit)
    btn3.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)

# Student Home Page   
def Student():
    
    global headingFrame1,headingFrame2,headingLabel,btn1,btn3,btn2,btn4,Canvas1
    headingFrame1.destroy()
    headingFrame2.destroy()
    headingLabel.destroy()
    labelFrame.destroy()
    Canvas1.destroy()
    btn1.destroy()
    btn2.destroy()
    btn3.destroy()
    btn4.destroy()
    btn5.destroy()
    btn6.destroy()
    btn7.destroy()

    Canvas1 = Canvas(root)

    Canvas1.config(bg="#FDF5E6",width = newImageSizeWidth, height = newImageSizeHeight)
    Canvas1.pack(expand=True,fill=BOTH)

    
    headingFrame1 = Frame(root,bg="#333945",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
    
    headingFrame2 = Frame(headingFrame1,bg="#EAF0F1")
    headingFrame2.place(relx=0.01,rely=0.05,relwidth=0.98,relheight=0.9)
    
    headingLabel = Label(headingFrame2, text="Registration", fg='black')
    headingLabel.place(relx=0.25,rely=0.15, relwidth=0.5, relheight=0.5)
    
    btn1 = Button(root,text="Student",bg='black', fg='white', command=studentRegister)
    btn1.place(relx=0.40,rely=0.5, relwidth=0.2,relheight=0.1)

    btn4 = Button(root, text="Employee", bg='black', fg='white', command=EmpRegister)
    btn4.place(relx=0.40, rely=0.4, relwidth=0.2, relheight=0.1)

    btn2 = Button(root, text="Back", bg='black', fg='white', command=empMenu)
    btn2.place(relx=0.25, rely=0.9, relwidth=0.18, relheight=0.08)
    
    btn3 = Button(root,text="Quit",bg='#455A64', fg='white', command=root.quit)
    btn3.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)

# Take n greater than 0.25 and less than 5
same=True
n=0.3

# Adding a background image
background_image =Image.open("lib1.jpg")
[imageSizeWidth, imageSizeHeight] = background_image.size

newImageSizeWidth = int(imageSizeWidth*n)
if same:
    newImageSizeHeight = int(imageSizeHeight*n) 
else:
    newImageSizeHeight = int(imageSizeHeight/n) 
    
background_image = background_image.resize((newImageSizeWidth,newImageSizeHeight),Image.ANTIALIAS)
img = ImageTk.PhotoImage(background_image)

Canvas1 = Canvas(root)

Canvas1.create_image(110,270,image = img)
Canvas1.config(bg="#CDC0B0",width = newImageSizeWidth, height = newImageSizeHeight)
Canvas1.pack(expand=True,fill=BOTH)

headingFrame1 = Frame(root,bg="#333945",bd=5)
headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)

headingFrame2 = Frame(headingFrame1,bg="#EAF0F1")
headingFrame2.place(relx=0.01,rely=0.05,relwidth=0.98,relheight=0.9)

headingLabel = Label(headingFrame2, text="Welcome to UBIT Library", fg='black')
headingLabel.place(relx=0.25,rely=0.1, relwidth=0.5, relheight=0.5)

btn1 = Button(root,text="START",bg='black', fg='white', command=Employee)
btn1.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)

root.mainloop()
