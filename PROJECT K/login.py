'''import tkinter as tk
from tkinter import messagebox

# Function to validate the login
def validate_login():
    userid = username_entry.get()
    password = password_entry.get()

    # You can add your own validation logic here
    if userid == "admin" and password == "password":
        messagebox.showinfo("Login Successful", "Welcome, Admin!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# Create the main window
parent = tk.Tk()
parent.title("Login Form")

# Create and place the username label and entry
username_label = tk.Label(parent, text="Userid:")
username_label.pack()

username_entry = tk.Entry(parent)
username_entry.pack()

# Create and place the password label and entry
password_label = tk.Label(parent, text="Password:")
password_label.pack()

password_entry = tk.Entry(parent, show="*")  # Show asterisks for password
password_entry.pack()

# Create and place the login button
login_button = tk.Button(parent, text="Login", command=validate_login)
login_button.pack()

# Start the Tkinter event loop
parent.mainloop()'''


from tkinter import*  
base = Tk()  
base.geometry('500x500')  
base.title("Registration Form")  
  
labl_0 = Label(base, text="Registration form",width=20,font=("bold", 20))  
labl_0.place(x=90,y=53)  
  
  
labl_1 = Label(base, text="FullName",width=20,font=("bold", 10))  
labl_1.place(x=80,y=130)  
  
entry_1 = Entry(base)  
entry_1.place(x=240,y=130)  
  
labl_2 = Label(base, text="Email",width=20,font=("bold", 10))  
labl_2.place(x=68,y=180)  
  
entry_02 = Entry(base)  
entry_02.place(x=240,y=180)  
  
labl_3 = Label(base, text="Gender",width=20,font=("bold", 10))  
labl_3.place(x=70,y=230)  
varblbl = IntVarblbl()  
Radiobutton(base, text="Male",padx = 5, varblbliable=varblbl, value=1).place(x=235,y=230)  
Radiobutton(base, text="Female",padx = 20, varblbliable=varblbl, value=2).place(x=290,y=230)  
  
labl_4 = Label(base, text="Age:",width=20,font=("bold", 10))  
labl_4.place(x=70,y=280)  
  
  
entry_02 = Entry(base)  
entry_02.place(x=240,y=280)  
  
Button(base, text='Submit',width=20,bg='brown',fg='white').place(x=180,y=380)  
# it will be used for displaying the registration form onto the window  
base.mainloop()  
print("Registration form is created seccussfully...")  
