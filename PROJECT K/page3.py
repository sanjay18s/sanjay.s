from tkinter import *
import pagin

def page():
    titlefont=("time new roman",28,"bold")
    labelfonts=("Garamond",10,"bold")
    labelfont=("Garamond",15,"bold")
    root=Tk()
    root.geometry("1500x700")
    mainframe=Frame(root,width=1500,height=700,bg="sky blue")
    mainframe.place(relx=0.0001,rely=0.001)

    


    leftframe=Frame(mainframe,width=100,height=700,bg="orange")
    leftframe.place(relx=0.0001,rely=0.001)
    rightframe=Frame(mainframe,width=100,height=700,bg="orange")
    rightframe.place(relx=0.85,rely=0.001)
    upframe=Frame(mainframe,width=1300,height=20,bg="orange")
    upframe.place(relx=0.0001,rely=0.0001)
    downframe=Frame(mainframe,width=1300,height=20,bg="orange")
    downframe.place(relx=0.0001,rely=0.98)
    b=Button(root,text="INDIA VS AUSTRALIA",font=labelfont,bg="sky blue",command=lambda:pagin.book())
    b.place(relx=0.3,rely=0.2)

    root.mainloop()