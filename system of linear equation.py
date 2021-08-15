
from tkinter import *
from tkinter import ttk
from sympy import symbols, Eq, solve
from tkinter import messagebox

fg="#000000"
bg="#f3ca20"

root=Tk()
root.title("system of linear equation".title())
root.geometry("625x500")
root.config(bg=fg)
#dbb30d

style = ttk.Style()
style.theme_use('alt')
style.configure('TButton', font=('timesnewroman', 20),
                background=bg, foreground=fg,)
style.map('TButton',
          background=[('active', '#dbb30d'), ('disabled', 'white')]
          )

l=Label(root,text="Please select your type of system".title(),font="timesnewroman 20 bold",fg=fg,bg=bg).place(y=5,relwidth=1,height=40)
f=Frame(root,bg=bg)
f.place(x=0,y=100,relwidth=1,height=450)

def v3():
    root.geometry("625x500")
    for widgets in f.winfo_children():
      widgets.destroy()
    v1=StringVar()
    v1.set("0")
    v2=StringVar()
    v2.set("0")
    v3=StringVar()
    v3.set("0")
    v4=StringVar()
    v4.set("0")
    v5=StringVar()
    v5.set("0")
    v6=StringVar()
    v6.set("0")
    v7=StringVar()
    v7.set("0")
    v8=StringVar()
    v8.set("0")
    v9=StringVar()
    v9.set("0")
    v10=StringVar()
    v10.set("0")
    v11=StringVar()
    v11.set("0")
    v12=StringVar()
    v12.set("0")

    Label(f,text="X1",fg=fg,font="timesnewroman 20 bold",bg=bg).place(x=5,y=110-80)
    ttk.Entry(f,textvariable=v1,font="timesnewroman 20 bold").place(x=60,y=110-80,width=60)
    Label(f,text="+",fg=fg,font="timesnewroman 20 bold",bg=bg).place(x=135,y=110-80)

    Label(f,text="Y1",fg=fg,font="timesnewroman 20 bold",bg=bg).place(x=170,y=110-80)
    ttk.Entry(f,textvariable=v2,font="timesnewroman 20 bold").place(x=170+55,y=110-80,width=60)
    Label(f,text="+",fg=fg,font="timesnewroman 20 bold",bg=bg).place(x=170+130,y=110-80)

    Label(f,text="Z1",fg=fg,font="timesnewroman 20 bold",bg=bg).place(x=335,y=110-80)
    ttk.Entry(f,textvariable=v3,font="timesnewroman 20 bold").place(x=335+55,y=110-80,width=60)
    Label(f,text="=",fg=fg,font="timesnewroman 20 bold",bg=bg).place(x=335+130,y=110-80)

    Label(f,text="C1",fg=fg,font="timesnewroman 20 bold",bg=bg).place(x=500,y=110-80)
    ttk.Entry(f,textvariable=v4,font="timesnewroman 20 bold").place(x=500+55,y=110-80,width=60)





    Label(f,text="X2",fg=fg,font="timesnewroman 20 bold",bg=bg).place(x=5,y=190-80)
    ttk.Entry(f,textvariable=v5,font="timesnewroman 20 bold").place(x=60,y=190-80,width=60)
    Label(f,text="+",fg=fg,font="timesnewroman 20 bold",bg=bg).place(x=135,y=190-80)

    Label(f,text="Y2",fg=fg,font="timesnewroman 20 bold",bg=bg).place(x=170,y=190-80)
    ttk.Entry(f,textvariable=v6,font="timesnewroman 20 bold").place(x=170+55,y=190-80,width=60)
    Label(f,text="+",fg=fg,font="timesnewroman 20 bold",bg=bg).place(x=170+130,y=190-80)

    Label(f,text="Z2",fg=fg,font="timesnewroman 20 bold",bg=bg).place(x=335,y=190-80)
    ttk.Entry(f,textvariable=v7,font="timesnewroman 20 bold").place(x=335+55,y=190-80,width=60)
    Label(f,text="=",fg=fg,font="timesnewroman 20 bold",bg=bg).place(x=335+130,y=190-80)

    Label(f,text="C2",fg=fg,font="timesnewroman 20 bold",bg=bg).place(x=500,y=190-80)
    ttk.Entry(f,textvariable=v8,font="timesnewroman 20 bold").place(x=500+55,y=190-80,width=60)





    Label(f,text="X3",fg=fg,font="timesnewroman 20 bold",bg=bg).place(x=5,y=270-80)
    ttk.Entry(f,textvariable=v9,font="timesnewroman 20 bold").place(x=60,y=270-80,width=60)
    Label(f,text="+",fg=fg,font="timesnewroman 20 bold",bg=bg).place(x=135,y=270-80)

    Label(f,text="Y3",fg=fg,font="timesnewroman 20 bold",bg=bg).place(x=170,y=270-80)
    ttk.Entry(f,textvariable=v10,font="timesnewroman 20 bold").place(x=170+55,y=270-80,width=60)
    Label(f,text="+",fg=fg,font="timesnewroman 20 bold",bg=bg).place(x=170+130,y=270-80)

    Label(f,text="Z3",fg=fg,font="timesnewroman 20 bold",bg=bg).place(x=335,y=270-80)
    ttk.Entry(f,textvariable=v11,font="timesnewroman 20 bold").place(x=335+55,y=270-80,width=60)
    Label(f,text="=",fg=fg,font="timesnewroman 20 bold",bg=bg).place(x=335+130,y=270-80)

    Label(f,text="C3",fg=fg,font="timesnewroman 20 bold",bg=bg).place(x=500,y=270-80)
    ttk.Entry(f,textvariable=v12,font="timesnewroman 20 bold").place(x=500+55,y=270-80,width=60)



    def compute():
        x, y, z = symbols('X,Y,Z')
        try:
            eq1 = Eq(eval(str(int(v1.get())))*x+eval(str(int(v2.get())))*y+eval(str(int(v3.get())))*z,eval(str(int(v4.get()))))
            eq2 = Eq(eval(str(int(v5.get())))*x+eval(str(int(v6.get())))*y+eval(str(int(v7.get())))*z,eval(str(int(v8.get()))))
            eq3 = Eq(eval(str(int(v9.get())))*x+eval(str(int(v10.get())))*y+eval(str(int(v11.get())))*z,eval(str(int(v12.get()))))
            a=solve((eq1, eq2, eq3), (x, y, z))
            if a==[]:
                messagebox.showinfo("NO SOLUTION","!!!This system does not have any solution!!!")
            else:
                try:
                    l1['text']=str(a[x])  
                except:
                    pass 
                try:
                    l2['text']=str(a[y])  
                except:
                    pass             
                try:         
                    l3['text']=str(a[z])
                except:
                    pass
        except:
            messagebox.showwarning("!!!WARN!!!","Please Enter Valid Values")
        
                



    def enter(e):
        b1["foreground"]=bg
        b1["background"]=fg
    def leave(e):
        b1["foreground"]=fg
        b1["background"]=bg

    b1=Button(f,text="Compute",font="timesnewroman 15 bold",bd=4,command=compute,bg=bg,fg=fg)
    b1.place(y=340-80,relwidth=1)
    b1.bind("<Enter>", enter)
    b1.bind("<Leave>", leave)


    Label(f,text="X",fg=fg,font="timesnewroman 20 bold",bg=bg).place(x=50,y=400-80)
    Label(f,text="=",fg=fg,font="timesnewroman 20 bold",bg=bg).place(x=70,y=400-80)
    l1=Label(f,text="",fg=fg,font="timesnewroman 20 bold",bg=bg)
    l1.place(x=100,y=400-80)
    Label(f,text="Y",fg=fg,font="timesnewroman 20 bold",bg=bg).place(x=250,y=400-80)
    Label(f,text="=",fg=fg,font="timesnewroman 20 bold",bg=bg).place(x=270,y=400-80)
    l2=Label(f,text="",fg=fg,font="timesnewroman 20 bold",bg=bg)
    l2.place(x=300,y=400-80)
    Label(f,text="Z",fg=fg,font="timesnewroman 20 bold",bg=bg).place(x=450,y=400-80)
    Label(f,text="=",fg=fg,font="timesnewroman 20 bold",bg=bg).place(x=470,y=400-80)
    l3=Label(f,text="",fg=fg,font="timesnewroman 20 bold",bg=bg)
    l3.place(x=500,y=400-80)


def v2():
    root.geometry("625x400")



    for widgets in f.winfo_children():
      widgets.destroy()
    
    v1=StringVar()
    v1.set("0")
    v2=StringVar()
    v2.set("0")
    v3=StringVar()
    v3.set("0")
    v4=StringVar()
    v4.set("0")
    v5=StringVar()
    v5.set("0")
    v6=StringVar()
    v6.set("0")


    Label(f,text="X1",fg=fg,font="timesnewroman 20 bold",bg=bg).place(x=5+75,y=110-80)
    ttk.Entry(f,textvariable=v1,font="timesnewroman 20 bold").place(x=60+75,y=110-80,width=60)
    Label(f,text="+",fg=fg,font="timesnewroman 20 bold",bg=bg).place(x=135+75,y=110-80)

    Label(f,text="Y1",fg=fg,font="timesnewroman 20 bold",bg=bg).place(x=170+75,y=110-80)
    ttk.Entry(f,textvariable=v2,font="timesnewroman 20 bold").place(x=170+55+75,y=110-80,width=60)
    Label(f,text="=",fg=fg,font="timesnewroman 20 bold",bg=bg).place(x=170+130+75,y=110-80)

    Label(f,text="C1",fg=fg,font="timesnewroman 20 bold",bg=bg).place(x=335+75,y=110-80)
    ttk.Entry(f,textvariable=v3,font="timesnewroman 20 bold").place(x=335+55+75,y=110-80,width=60)



    Label(f,text="X2",fg=fg,font="timesnewroman 20 bold",bg=bg).place(x=5+75,y=190-80)
    ttk.Entry(f,textvariable=v4,font="timesnewroman 20 bold").place(x=60+75,y=190-80,width=60)
    Label(f,text="+",fg=fg,font="timesnewroman 20 bold",bg=bg).place(x=135+75,y=190-80)

    Label(f,text="Y2",fg=fg,font="timesnewroman 20 bold",bg=bg).place(x=170+75,y=190-80)
    ttk.Entry(f,textvariable=v5,font="timesnewroman 20 bold").place(x=170+55+75,y=190-80,width=60)
    Label(f,text="=",fg=fg,font="timesnewroman 20 bold",bg=bg).place(x=170+130+75,y=190-80)

    Label(f,text="C2",fg=fg,font="timesnewroman 20 bold",bg=bg).place(x=335+75,y=190-80)
    ttk.Entry(f,textvariable=v6,font="timesnewroman 20 bold").place(x=335+55+75,y=190-80,width=60)




    def enter(e):
        b1["foreground"]=bg
        b1["background"]=fg
    def leave(e):
        b1["foreground"]=fg
        b1["background"]=bg


    def compute():
        X,Y= symbols('X,Y')
        try:
            eq1 = Eq(eval(str(int(v1.get())))*X+eval(str(int(v2.get())))*Y,eval(str(int(v3.get()))))
            eq2 = Eq(eval(str(int(v4.get())))*X+eval(str(int(v5.get())))*Y,eval(str(int(v6.get()))))
            a=solve((eq1, eq2), (X, Y))
            if a==[]:
                messagebox.showinfo("NO SOLUTION","!!!This system does not have any solution!!!")
            else:
                try:
                    l1['text']=str(a[X])  
                except:
                    pass 
                try:
                    l2['text']=str(a[Y])  
                except:
                    pass  
                
        except:
            messagebox.showwarning("!!!WARN!!!","Please Enter Valid Values")
        



    b1=Button(f,text="Compute",font="timesnewroman 15 bold",bd=4,command=compute,bg=bg,fg=fg)
    b1.place(y=340-150,relwidth=1)
    b1.bind("<Enter>", enter)
    b1.bind("<Leave>", leave)


    Label(f,text="X",fg=fg,font="timesnewroman 20 bold",bg=bg).place(x=50+130,y=400-150)
    Label(f,text="=",fg=fg,font="timesnewroman 20 bold",bg=bg).place(x=70+130,y=400-150)
    l1=Label(f,text="",fg=fg,font="timesnewroman 20 bold",bg=bg)
    l1.place(x=100+130,y=400-150)

    Label(f,text="Y",fg=fg,font="timesnewroman 20 bold",bg=bg).place(x=250+130,y=400-150)
    Label(f,text="=",fg=fg,font="timesnewroman 20 bold",bg=bg).place(x=270+130,y=400-150)
    l2=Label(f,text="",fg=fg,font="timesnewroman 20 bold",bg=bg)
    l2.place(x=300+130,y=400-150)





v3()

B1=ttk.Button(root,text="System of 2 variables",command=v2).place(x=15,y=50,width=280)
B2=ttk.Button(root,text="System of 3 variables",command=v3).place(x=310,y=50,width=280)



























root.mainloop()





