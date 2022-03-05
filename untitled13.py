from tkinter import *
from tkinter import ttk
#Loading Assets
root=Tk()
root.geometry("600x600")
root.title("sussy")
#setting up root
op1=["among","sussy","chopped","diced","simple"]
cb1=ttk.Combobox(root,state="readonly",values=op1)
cb1.place(relx=0.25,rely=0.2,anchor=CENTER)

op2=["vented","smoked","grinded","braized","candied"]
cb2=ttk.Combobox(root,state="readonly",values=op2)
cb2.place(relx=0.25,rely=0.3,anchor=CENTER)

op3=["bread","soup","cake","smoothie","blend"]
cb3=ttk.Combobox(root,state="readonly",values=op3)
cb3.place(relx=0.25,rely=0.4,anchor=CENTER)
#setting up comboboxes
lab1=Label(root,text="+")
lab1.place(relx=0.25,rely=0.25,anchor=CENTER)

lab2=Label(root,text="+")
lab2.place(relx=0.25,rely=0.35,anchor=CENTER)

answer=(root)
answer.pack()
#setting up labels
root.mainloop()
#ends code