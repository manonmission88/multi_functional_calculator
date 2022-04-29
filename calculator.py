import math 
import tkinter
from tkinter import *
#for calculating factors 
def factor(a):
    output=''
    if a > 0:
        for i in range(1,a+1):
            if a % i==0:
                if a!=i:
                    output += str(i) + ','
                else:
                    output += str(i)
        return output
    else:
        return 'Number Should Be Greater Than Zero'
                
def click(event):
    global value_on
    text = event.widget.cget("text")
    if text == "=":
        if value_on.get().isdigit():
            value = int(value_on.get())
        else:
            try:
                value = eval(value_on.get())

            except Exception as e:
                print(e)
                value = "Error"

        value_on.set(value)
        screen.update()
    elif text=='DEL':
        value= str(value_on.get())
        delete=value[:-1]
        value_on.set(delete)
        screen.update()
    elif text == "AC":
        value_on.set("")
        screen.update()
    elif text=='√x':
        value=float(value_on.get())
        sqrt=math.sqrt(value)
        value_on.set(f'√{value}' + '=' + str(sqrt))
        screen.update()
    elif text=='x²':
        value=float(value_on.get())
        squa=math.pow(value,2)
        value_on.set(round(squa,4))
        screen.update()
    elif text=='factor':
        value=int(value_on.get())
        fact=factor(value)
        value_on.set('factor of ' + str(value) + ' is '+ fact)
        screen.update()
    elif text=='10^':
        value=float(value_on.get())
        power=math.pow(10,value)
        value_on.set('10^'+str(value)+ '=' + str(power))
        screen.update()
        screen.update()
    elif text=='log10':
        value=float(value_on.get())
        logar=math.log10(value)
        value_on.set(logar)
        screen.update()
    elif text=='e':
        value=float(value_on.get())
        expo=math.pow(math.e,value)
        value_on.set('e^'+str(value)+'='+ str(expo))
        screen.update()
    elif text=='!':
        value=int(value_on.get())
        permu=math.perm(value)
        value_on.set(f'{value}! ='+str(permu))
        screen.update()

    else:
        value_on.set(value_on.get() + text)
        screen.update()




win = Tk()
# button = tkinter.Button()
# button.config(height=100, 
# 			  width=100)
win.geometry('650x630')
win.configure(background='light green')
win.title('Multi Functional Calculator')
value_on =StringVar()
value_on.set("")
font_value=("Comic Sans MS", 28, "bold")
screen = Entry(win, textvariable=value_on, font=("times new roman", 40, "bold"),
               justify=RIGHT, bg="gray", fg="white", relief=GROOVE)
screen.pack(side=TOP, fill=X, pady=10, padx=8, ipady=20)

# first frame 
first=Frame(win,padx=8)
# numberes 
list_buttons1=['9','8','7','DEL','AC']
for i in list_buttons1:
    but1=Button(first,text=f'{i}',font=font_value,height=2,width=4,bg='yellow',fg='gray',padx=8)
    but1.pack(side='left')
    but1.bind("<Button-1>",click)
first.pack()
# second frame 
second=Frame(win,padx=8)
list_buttons2=['6','5','4','*','/']
for i in list_buttons2:
    but1=Button(second,text=f'{i}',font=font_value,height=2,width=4,bg='yellow',fg='gray',padx=8)
    but1.pack(side='left')
    but1.bind("<Button-1>",click)
second.pack()
# third frame 
third=Frame(win,padx=8)
list_buttons3=['3','2','1','+','-']
for i in list_buttons3:
    but1=Button(third,text=f'{i}',font=font_value,height=2,width=4,bg='yellow',fg='gray',padx=8)
    but1.pack(side='left')
    but1.bind("<Button-1>",click)
third.pack()
# fourth frame 
fourth=Frame(win,padx=8)
list_buttons4=['0','.','√x','x²','=']
for i in list_buttons4:
    but1=Button(fourth,text=f'{i}',font=font_value,height=2,width=4,bg='yellow',fg='gray',padx=8)
    but1.pack(side='left')
    but1.bind("<Button-1>",click)
fourth.pack()

#fifth frame 
fifth=Frame(win,padx=8)
list_buttons5=['10^','factor','log10','e','!']
for i in list_buttons5:
    but1=Button(fifth,text=f'{i}',font=font_value,height=2,width=4,bg='yellow',fg='gray',padx=8)
    but1.pack(side='left')
    but1.bind("<Button-1>",click)
fifth.pack()
sixth=Label(win,padx=8,text='Everything around you is numbers, everything around you is mathematics',font=("times new roman", 17, "bold"),bg='#ADD8E6',fg='black')
sixth.pack(side=BOTTOM,pady=10, padx=8, ipady=20)
win.mainloop()