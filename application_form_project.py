from csv import *
from tkinter import *
from tkinter import messagebox
import os

from tkcalendar import DateEntry 

x=1000000

window=Tk()
window.configure(bg = "lightblue")
window.title("Data Entry")
window.geometry("700x600")

with open("data_entry.csv","w") as file:
  Writer=writer(file)
  Writer.writerow(["Name","Date of Birth","Gender","Semester","Contact","Address","Collage Name","Department","Token Number"])


for i in range(50):
    window.columnconfigure(i, weight=1)
    window.rowconfigure(i, weight=1)

def Save():
    if checkbox_var.get()!= 1:
        messagebox.showinfo("Error",f"Please agree to the terms and conditions")
        return 
    global x 
    x = x+ 1
    lst=[name.get(),age.get(),gender.get(),sem.get(),contact.get(),address.get(),collagename.get(),Department.get(),x]
    
    with open("data_entry.csv","a") as file:
        Writer=writer(file)
        Writer.writerow(lst)
    messagebox.showinfo("Information",f"The data has been added successfully\n\nUnique Token No: {x}")
    return x 



def Clear():
   name.delete(0,END)
   age.delete(0,END)
   gender.set("Select Gender")
   sem.set("Select Semester")
   contact.delete(0,END)
   address.delete(0,END)
   collagename.delete(0,END)
   Department.set("Select Your Department")




# Heading 


heading_label = Label(window, text="DATA ENTRY APPLICATION", font=("italicbold", 20),activebackground="blue", bg="blue", fg="white")

# Center the alignment 
heading_label.grid(row=0,column = 25, padx= 20, pady=10)


# labels,  buttons, entry fields
label1=Label(window,text="Name: ",padx=10,pady=10,background="lightblue",foreground="black")
label2=Label(window,text="Date of Birth(DD/MM/YYYY): ",padx=10,pady=10,background="lightblue",foreground="black")
label21=Label(window,text="Gender: ",padx=10,pady=10,background="lightblue",foreground="black")
label22=Label(window,text="Semester: ",padx=10,pady=10,background="lightblue",foreground="black")
label3=Label(window,text="Contact: ",padx=10,pady=10,background="lightblue",foreground="black")
label31=Label(window,text="Address:",padx=10,pady=11,background="lightblue",foreground="black")
label4=Label(window,text="Collage name: ",padx=10,pady=10,background="lightblue",foreground="black")
label5=Label(window,text="Department: ",padx=10,pady=10,background="lightblue",foreground="black")


name=Entry(window,width=30,borderwidth=3)



age = DateEntry(window, selectmode = 'day')

 
def grad_date():
    date.config(text = "Selected Date is: " + age.get_date())
 

date = Label(window, text = "")



gender=StringVar(window)
gender.set("Select Gender")
drop_menu1=OptionMenu(window,gender,"Male","Female","Others")

sem=StringVar(window)
sem.set("Select Semester")
drop_menu2=OptionMenu(window,sem,1,2,3,4,5,6,7,8)

contact=Entry(window,width=30,borderwidth=3)
address = Entry(window,width = 30 , borderwidth = 4)
collagename=Entry(window,width=30,borderwidth=3)




Department = StringVar(window)
Department.set("Select Your Department")
drop_menu = OptionMenu(window, Department,"Computer Science and Engineering(CSE)", "Information Technology(IT)","Electronics and Communication Engineering(ECE)","Electrical Engineering(EE)","Artificial Intelligence and Machine Learning(AI&ML)")

checkbox_var = IntVar()
checkbox = Checkbutton(window, text="I agree to the terms and conditions", variable=checkbox_var)
checkbox.grid(row=26,column=25,columnspan=2)

save=Button(window,text="Save",font="Arial 12",padx=7,pady=5,background="Blue",foreground="White",command=Save)

clear=Button(window,text="Clear",font = "Arial 12",padx=7,pady=5,background="Blue",foreground="White",command=Clear)
Exit=Button(window,text="Exit",font="Arial 12",padx=7,pady=5,background="red",foreground="White",command=window.quit)

label1.grid(row=10,column=24)
label2.grid(row=12,column=24)
label21.grid(row=14,column=24)
label22.grid(row=16,column=24)
label3.grid(row=18,column=24)
label31.grid(row =20, column=24)
label4.grid(row = 22,column=24)
label5.grid(row = 24,column=24)

name.grid(row=10,column=25)

age.grid(row=12,column=25)
drop_menu1.grid(row=14,column=25)
drop_menu2.grid(row=16,column=25)
contact.grid(row=18,column=25)
address.grid(row=20,column=25)
collagename.grid(row=22,column=25)
drop_menu.grid(row=24,column=25)
save.grid(row=28,column=25,columnspan=2)
clear.grid(row=26,column=26,columnspan=2)
Exit.grid(row=28,column=26,columnspan=2)

def DataFile():
    try:
        os.startfile("data_entry.csv")
    except:
        messagebox.showinfo("Error",f"File does not exist")
    
def Delete():
    try:
        os.remove("data_entry.csv")
        messagebox.showinfo("INFO",f"File has been deleted")
    except:
        messagebox.showinfo("Error",f"File does not exist")

menubar = Menu(window)
 
# MenuBar :
filemenu = Menu(menubar, tearoff = 0)

menubar.add_cascade(label = 'Options', menu = filemenu)


filemenu.add_command(label = "Open the data file", command = DataFile)
filemenu.add_command(label = "Delete the data file", command = Delete)

window.config(menu=menubar)

window.mainloop()
