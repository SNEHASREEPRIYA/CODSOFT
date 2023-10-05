from tkinter import *

number1 = number2 = operator = None

#TO GET DIGITS
def get_digit(digit):
    current = result['text']
    new = current + str(digit)
    result.config(text=new)

#TO CLEAR THE GIVEN TEXT 
def clear():
    result.config(text='')

#TO GET OPERATOR
def get_operator(op):
    global number1,operator

    number1 = int(result['text'])
    operator = op
    result.config(text='')

#TO DISPLAY RESULT
def get_result():
    global number1,number2,operator

    number2 = int(result['text'])

    if operator == '+':
        result.config(text=str(number1+number2))
    elif operator == '-':
        result.config(text=str(number1 - number2))
    elif operator == '*':
        result.config(text=str(number1 * number2))
    else:
        if number2 == 0:
            result.config(text='Error')
        else:
            result.config(text=str(round(number1 / number2,2)))

root = Tk()
#ADDING A TITLE
root.title("CALCULATOR")

#ADDING A ICON
root.iconbitmap(r'C:\Users\ramsu\OneDrive\Desktop\calc_icon.ico')

#SETTING SIZE AND BACKGROUND COLOUR TO THE POPUP WINDOW
root.minsize(280,335)
root.maxsize(280,335)
root.geometry('280x335')
root.configure(background = "sky blue")

#DISPLAYING POINTER OR RESULT
result = Label(root,text='',bg='black',fg='pink')
result.pack(pady = 5)
result.config(font = ('verdana'))
result.grid(row=0,column=0,columnspan=5,pady=(30,15),sticky='w')
result.config(font=('verdana',20,'bold'))

#ADDING BUTTONS
but7 = Button(root,text='7',bg='black',fg='white',width=5,height=2,command=lambda :get_digit(7))
but7.grid(row=1,column=0)
but7.config(font=('verdana',14))

but8 = Button(root,text='8',bg='black',fg='white',width=5,height=2,command=lambda :get_digit(8))
but8.grid(row=1,column=1)
but8.config(font=('verdana',14))

but9 = Button(root,text='9',bg='black',fg='white',width=5,height=2,command=lambda :get_digit(9))
but9.grid(row=1,column=2)
but9.config(font=('verdana',14))

but4 = Button(root,text='4',bg='black',fg='white',width=5,height=2,command=lambda :get_digit(4))
but4.grid(row=2,column=0)
but4.config(font=('verdana',14))

but5 = Button(root,text='5',bg='black',fg='white',width=5,height=2,command=lambda :get_digit(5))
but5.grid(row=2,column=1)
but5.config(font=('verdana',14))

but6 = Button(root,text='6',bg='black',fg='white',width=5,height=2,command=lambda :get_digit(6))
but6.grid(row=2,column=2)
but6.config(font=('verdana',14))

but3 = Button(root,text='3',bg='black',fg='white',width=5,height=2,command=lambda :get_digit(3))
but3.grid(row=3,column=2)
but3.config(font=('verdana',14))

but2 = Button(root,text='2',bg='black',fg='white',width=5,height=2,command=lambda :get_digit(2))
but2.grid(row=3,column=1)
but2.config(font=('verdana',14))

but1 = Button(root,text='1',bg='black',fg='white',width=5,height=2,command=lambda :get_digit(1))
but1.grid(row=3,column=0)
but1.config(font=('verdana',14))

but0 = Button(root,text='0',bg='black',fg='white',width=5,height=2,command=lambda :get_digit(0))
but0.grid(row=4,column=0)
but0.config(font=('verdana',14))

but_add = Button(root,text='+',bg='grey',fg='black',width=5,height=2,command=lambda :get_operator("+"))
but_add.grid(row=2,column=3)
but_add.config(font=('verdana',14))

but_sub = Button(root,text='-',bg='grey',fg='black',width=5,height=2,command=lambda :get_operator("-"))
but_sub.grid(row=3,column=3)
but_sub.config(font=('verdana',14))

but_mul = Button(root,text='*',bg='grey',fg='black',width=5,height=2,command=lambda :get_operator("*"))
but_mul.grid(row=4,column=1)
but_mul.config(font=('verdana',14))

but_div = Button(root,text='/',bg='grey',fg='black',width=5,height=2,command=lambda :get_operator("/"))
but_div.grid(row=4,column=2)
but_div.config(font=('verdana',14))

but_equals = Button(root,text='=',bg='green',fg='black',width=5,height=2,command=get_result)
but_equals.grid(row=4,column=3)
but_equals.config(font=('verdana',14))

but_clear = Button(root,text='clear',bg='red',fg='black',width=5,height=2,command=lambda :clear())
but_clear.grid(row=1,column=3)
but_clear.config(font=('verdana',14))

root.mainloop()