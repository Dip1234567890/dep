from tkinter import *
import math

def click(event):

    global scvalue


    text = event.widget.cget("text")
    print(text)

    ex=scvalue.get()

    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            value = eval(screen.get())
        scvalue.set(value)
        screen.update()
    elif text == "C":
        scvalue.set("")
        screen.update()
    elif text =="BS":
        c=scvalue.get()
        scvalue.set(c[:-1])
        screen.update()
    elif text=="√":
        sr=math.sqrt(eval(ex))
        scvalue.set(sr)
        screen.update()
    elif text=="π":
        pie=math.pi
        scvalue.set(pie)
        screen.update()
    elif text=="cos":
        sr=math.cos(math.radians(eval(ex)))
        scvalue.set(sr)
        screen.update()
    elif text=="tan":
        sr=math.tan(math.radians(eval(ex)))
        scvalue.set(sr)
        screen.update()
    elif text=="sin":
        sr=math.sin(math.radians(eval(ex)))
        scvalue.set(sr)
        screen.update()
    elif text=="2π":
        pie=2*math.pi
        scvalue.set(pie)
        screen.update()
    elif text=="cosh":
        sr=math.cosh(eval(ex))
        scvalue.set(sr)
        screen.update()
    elif text=="tanh":
        sr=math.tanh(eval(ex))
        scvalue.set(sr)
        screen.update()
    elif text=="sinh":
        sr=math.sinh(eval(ex))
        scvalue.set(sr)
        screen.update()
    
    elif text=="ln":
        sr=math.log2(eval(ex))
        scvalue.set(sr)
        screen.update()
    elif text=="x\u00B2":
        sr=eval(ex) ** 2
        scvalue.set(sr)
        screen.update()
    elif text=="∛":
        sr=eval(ex) ** (1/3)
        scvalue.set(sr)
        screen.update()
    elif text=="e":
        sr=math.e
        scvalue.set(sr)
        screen.update()
    
    
    






    
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()

root = Tk()
root.geometry("520x685")  
root.minsize(520, 685)
root.maxsize(520, 685)
root.title("Project Calculator")

scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue, font="lucida 40 bold")
screen.pack(fill=X, ipady=20, ipadx=5, pady=5, padx=5)

buttons = [
    "C", "=", "%", "7", "8", "9",
    "-", "+", "*", "4", "5","6",
    "." , "/", "0", "1", "2", "3","BS",
    "√","(",")","[","]","π","cos","tan","sin","2π","cosh",
    "tanh","sinh","x\u00B2","ln","∛","e"
    
     
]


def pack_buttons(buttons, frame):
    for symbol in buttons:
        b = Button(frame, text=symbol, padx=0, pady=0, font="lucida 20 bold", width=4, height=2, fg="black", bg="yellow")
        b.pack(side=LEFT, padx=5, pady=5)
        b.bind("<Button-1>", click)
    frame.pack()


rows = [buttons[i:i+6] for i in range(0, len(buttons), 6)]

for row in rows:
    f = Frame(root,bg ="orange")
    pack_buttons(row, f)

root.mainloop()