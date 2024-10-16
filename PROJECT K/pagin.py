from tkinter import *
from tkinter import ttk
import os
import tempfile

def book():
    titlefont=("time new roman",28,"bold")
    labelfonts=("Garamond",20,"bold")
    labelfont=("Garamond",15,"bold")
    root=Tk()
    root.geometry("1500x700")
    mainframe=Frame(root,width=1500,height=700,bg="gold")
    mainframe.place(relx=0.01,rely=0.001)
    miniframe=Frame(mainframe,width=1500,height=400,bg="gray")
    miniframe.place(relx=0.001,rely=0.2)
    titlelabel=Label(mainframe,text="sports ticket.com",bg="gold",font=titlefont)
    titlelabel.place(relx=0.35,rely=0.01)


    combo = ttk.Combobox(miniframe, values=["CHINNASAMY"],font=labelfont)
    combo.place(relx=0.40,rely=0.34)
    combo1 = ttk.Combobox(miniframe)
    combo1.place(relx=0.40,rely=0.47)
    combo2 = ttk.Combobox(miniframe,values=["1A","2A","3B","4D","5E"],font=labelfont)
    #combo2=ttk.Combobox(miniframe)
    #combo2 = ttk.Combobox(miniframe,values=["6A","7d","8S","6W"],font=labelfont)
    #combo2 = ttk.Combobox(miniframe,values=["22A","71d","82S","61W"],font=labelfont)
    combo2.place(relx=0.40,rely=0.59)
    def movies(event):
         movies=combo.get()
         if(movies=="CHINNASAMY"):
          combo1.config(values=["VIRAT BOC","ABD BOC","GYLE BOC"],font=labelfont)
        
    #elif(movies=="DC"):
        #combo1.config(values=["Bat man","super man","flash","wonder woman","justice league"],font=labelfont)

    def boc(event):
        boc=combo1.get()
        if(boc=="VIRAT BOC"):
            combo2.config(values=["1A","2A","3B","4D","5E"])
        elif(boc=="ABD BOC"):
            combo2.config(values=["6A","7d","8S","6W"])
        elif(boc=="GYLE BOC"):
            combo2.config(values=["22A","71d","82S","61W"])
        
    combo.bind("<<ComboboxSelected>>",movies)  
    combo1.bind("<<ComboboxSelected>>",boc)  

#combo = ttk.Combobox(miniframe, values=["VIRAT BOC","ABD BOC","GYLE BOC"],font=labelfont)
    alabel=Label(miniframe,text="MATCH INDIA VS AUSTRALIA",bg="gray",font=labelfonts).place(relx=0.3,rely=0.01)
    alabel=Label(miniframe,text="MATCH :  IND VS AUS",font=labelfonts,bg="gray").place(relx=0.2,rely=0.22)
    alabel=Label(miniframe,text="STADIUM :",font=labelfonts,bg="gray").place(relx=0.2,rely=0.35)
    alabel=Label(miniframe,text="BLOCK NAME :",font=labelfonts,bg="gray").place(relx=0.2,rely=0.47)
    alabel=Label(miniframe,text="SEAT NUMBER :",font=labelfonts,bg="gray").place(relx=0.2,rely=0.59)
    b=Button(root,text="BOOK",font=labelfont,bg="sky blue")
    b.place(relx=0.45,rely=0.8)
 
    b=Button(root,text="BOOK",font=labelfont,bg="sky blue")
    b.place(relx=0.45,rely=0.8)

#bentry=Entry(miniframe,font=labelfonts)
#bentry.place(relx=0.40,rely=0.34)
#bentry=Entry(miniframe,font=labelfonts)
#bentry.place(relx=0.40,rely=0.47)
#bentry=Entry(miniframe,font=labelfonts)
#bentry.place(relx=0.40,rely=0.59)

    labelfont=("Garamond",15,"bold")

    root.mainloop()
