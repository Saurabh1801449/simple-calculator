import tkinter as tk
root=tk.Tk()
root.title("Simple Calculator")
root.geometry("290x320")
root.configure(bg="white")
lbl=tk.Label(root,width=100,height=5,text="")
lbl.pack()
equation=""
def show(value):
    global equation
    equation= equation+value
    lbl.config(text=equation,font=("arial",14))

def clear():
    global equation
    equation= ""
    lbl.config(text=equation,font=("arial",14))
    
def calculate():
    global equation
    result=""
    if equation !="" :
        try:
            result=eval(equation) 
        except:
            result="error"
            
    lbl.config(text=result,font=("arial",15),anchor="centre")       \
              
           

    
    

btn=tk.Button(root,text="C",width=5,height=1,bg='blue',fg='white',font=30,bd=2,command=clear())
btn.place(x=10,y=90)

btn=tk.Button(root,text="/",width=5,height=1,bg='black',fg='white',font=30,bd=2,command=lambda:show("/"))
btn.place(x=80,y=90)

btn=tk.Button(root,text="%",width=5,height=1,bg='black',fg='white',font=30,bd=2,command=lambda:show("%"))
btn.place(x=150,y=90)

btn=tk.Button(root,text="*",width=5,height=1,bg='black',fg='white',font="bold",bd=2,command=lambda:show("*"))
btn.place(x=220,y=90)

btn=tk.Button(root,text="7",width=5,height=1,bg='black',fg='white',font=30,bd=2,command=lambda:show("7"))
btn.place(x=10,y=135)

btn=tk.Button(root,text="8",width=5,height=1,bg='black',fg='white',font=30,bd=2,command=lambda:show("8"))
btn.place(x=80,y=135)

btn=tk.Button(root,text="9",width=5,height=1,bg='black',fg='white',font=30,bd=2,command=lambda:show("9"))
btn.place(x=150,y=135)

btn=tk.Button(root,text="-",width=5,height=1,bg='black',fg='white',font=30,bd=2,command=lambda:show("-"))
btn.place(x=220,y=135)

btn=tk.Button(root,text="4",width=5,height=1,bg='black',fg='white',font=30,bd=2,command=lambda:show("4"))
btn.place(x=10,y=180)

btn=tk.Button(root,text="5",width=5,height=1,bg='black',fg='white',font=30,bd=2,command=lambda:show("5"))
btn.place(x=80,y=180)

btn=tk.Button(root,text="6",width=5,height=1,bg='black',fg='white',font=30,bd=2,command=lambda:show("6"))
btn.place(x=150,y=180)

btn=tk.Button(root,text="+",width=5,height=1,bg='black',fg='white',font=30,bd=2,command=lambda:show("+"))
btn.place(x=220,y=180)

btn=tk.Button(root,text="1",width=5,height=1,bg='black',fg='white',font=30,bd=2,command=lambda:show("1"))
btn.place(x=10,y=225)

btn=tk.Button(root,text="2",width=5,height=1,bg='black',fg='white',font=30,bd=2,command=lambda:show("2"))
btn.place(x=80,y=225)

btn=tk.Button(root,text="3",width=5,height=1,bg='black',fg='white',font=30,bd=2,command=lambda:show("3"))
btn.place(x=150,y=225)

btn=tk.Button(root,text="0",width=11,height=1,bg='black',fg='white',font=30,bd=2,command=lambda:show("0"))
btn.place(x=10,y=270)

btn=tk.Button(root,text=".",width=5,height=1,bg='black',fg='white',font=30,bd=2,command=lambda:show("."))
btn.place(x=150,y=270)

btn=tk.Button(root,text="=",width=5,height=3,bg='orange',fg='white',font=30,bd=2,command=lambda:calculate())
btn.place(x=220,y=225)






root.mainloop()