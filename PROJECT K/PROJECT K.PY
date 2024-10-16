from tkinter import*
from tkinter import ttk
from tkinter import*
from PIL import Image
from PIL.ImageTk import PhotoImage 
import login1
#global
labelfont=("Garamond",20,"bold")
titlefont=("time new roman",28,"bold")
labelfont=("Garamond",20,"bold")
root=Tk()
root.geometry("1500x700")
titleframe=Frame(root,width=1600,height=70,bg="sky blue")
titlelabel=Label(titleframe,text="sports ticket.com",bg="sky blue",fg="red",font=titlefont)
titlelabel.place(relx=0.40,rely=0.3)
titleframe.pack()


mainframe=Frame(root,width=1500,height=600,bg="yellow")
mainframe.place(relx=0.001,rely=0.1)
img1=PhotoImage(Image.open("sas.jpg"))
label=Label(root,image=img1)
label.place(relx=0.00000001,rely=0.1)

b=Button(root,text="GO TO BOOK",font=labelfont,bg="sky blue",command=lambda:login1.login())
b.place(relx=0.44,rely=0.28)

bottomframe=Frame(root,width=1600,height=60,bg="sky blue")
bottomlabel=Label(bottomframe,text="sports ticket.com",bg="sky blue",fg="red",font=titlefont)
bottomlabel.place(relx=0.34,rely=0.001)
bottomframe.place(relx=0.001,rely=0.93)
root.mainloop()