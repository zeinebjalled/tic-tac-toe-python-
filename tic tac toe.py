from tkinter import *
import tkinter.messagebox
tk = Tk()
tk.title("Tic Tac Toe")

pa = StringVar()
playerb = StringVar()
p1 = StringVar()
p2 = StringVar()
s1= IntVar()
s2= IntVar()

s1.set(0)
s2.set(0)

player1_name = Entry(tk, textvariable=p1, bd=5)
player1_name.grid(row=1, column=1, columnspan=8)
player2_name = Entry(tk, textvariable=p2, bd=5)
player2_name.grid(row=2, column=1, columnspan=8)

player1_score = Entry(tk, textvariable=s1, bd=5)
player1_score.grid(row=6, column=1, columnspan=8)

player2_score = Entry(tk, textvariable=s2, bd=5)
player2_score.grid(row=7, column=1, columnspan=8)

def reset():
        button1['text'] = " "
        button1.configure(background="#fbe0c4")
        button2['text'] = " "
        button2['bg'] = "#fbe0c4" 
        button3['text'] = " "
        button3['bg'] = "#fbe0c4"
        button4['text'] = " "
        button4['bg'] = "#fbe0c4" 
        button5['text'] = " "
        button5['bg'] = "#fbe0c4"
        button6['text'] = " "
        button6['bg'] = "#fbe0c4" 
        button7['text'] = " "
        button7['bg'] = "#fbe0c4"
        button8['text'] = " "
        button8['bg'] = "#fbe0c4"
        button9['text'] = " "
        button9['bg'] = "#fbe0c4" 

def new():
   reset()
   s1.set(0)
   s2.set(0)


bclick = True
s = 0


def btnClick(buttons):
    global bclick, s, player2_name, player1_name, playerb, pa
    if buttons["text"] == " " and bclick == True:
        buttons["text"] = "X"
        bclick = False
        checkForWin()
        playerb = p2.get() + " Wins!"
        pa = p1.get() + " Wins!"
        s += 1


    elif buttons["text"] == " " and bclick == False:
        buttons["text"] = "O"
        bclick = True
        checkForWin()
        s += 1
    

    else:
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "Button already Clicked!")

def checkForWin():
    if (button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X' or
        button4['text'] == 'X' and button5['text'] == 'X' and button6['text'] == 'X' or
        button7['text'] =='X' and button8['text'] == 'X' and button9['text'] == 'X' or
        button1['text'] == 'X' and button5['text'] == 'X' and button9['text'] == 'X' or
        button3['text'] == 'X' and button5['text'] == 'X' and button7['text'] == 'X' or
        button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X' or
        button1['text'] == 'X' and button4['text'] == 'X' and button7['text'] == 'X' or
        button2['text'] == 'X' and button5['text'] == 'X' and button8['text'] == 'X' or
        button7['text'] == 'X' and button6['text'] == 'X' and button9['text'] == 'X'):
        tkinter.messagebox.showinfo("Tic-Tac-Toe", pa)
        n= int(s1.get())
        score = (n+1)
        s1.set(score)
     

    elif (button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O' or
          button4['text'] == 'O' and button5['text'] == 'O' and button6['text'] == 'O' or
          button7['text'] == 'O' and button8['text'] == 'O' and button9['text'] == 'O' or
          button1['text'] == 'O' and button5['text'] == 'O' and button9['text'] == 'O' or
          button3['text'] == 'O' and button5['text'] == 'O' and button7['text'] == 'O' or
          button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O' or
          button1['text'] == 'O' and button4['text'] == 'O' and button7['text'] == 'O' or
          button2['text'] == 'O' and button5['text'] == 'O' and button8['text'] == 'O' or
          button7['text'] == 'O' and button6['text'] == 'O' and button9['text'] == 'O'):
        tkinter.messagebox.showinfo("Tic-Tac-Toe", playerb)
        n= int(s2.get())
        score = (n+1)
        s2.set(score)
        


buttons = StringVar()

label = Label( tk, text="Player 1:", font='Times 18 ', bg='#8ab6d6', fg='black', height=1, width=12)
label.grid(row=1, column=0)


label = Label( tk, text="Player 2:", font='Times 18', bg='#8ab6d6', fg='black', height=1, width=12)
label.grid(row=2, column=0)

button1 = Button(tk, text=" ", font='Times 20 bold', bg='#fbe0c4', fg='white', height=5, width=10, command=lambda: btnClick(button1))
button1.grid(row=3, column=0)

button2 = Button(tk, text=' ', font='Times 20 bold', bg='#fbe0c4', fg='white', height=5, width=10, command=lambda: btnClick(button2))
button2.grid(row=3, column=1)

button3 = Button(tk, text=' ',font='Times 20 bold', bg='#fbe0c4', fg='white', height=5, width=10, command=lambda: btnClick(button3))
button3.grid(row=3, column=2)

button4 = Button(tk, text=' ', font='Times 20 bold', bg='#fbe0c4', fg='white', height=5, width=10, command=lambda: btnClick(button4))
button4.grid(row=4, column=0)

button5 = Button(tk, text=' ', font='Times 20 bold', bg='#fbe0c4', fg='white', height=5, width=10, command=lambda: btnClick(button5))
button5.grid(row=4, column=1)

button6 = Button(tk, text=' ', font='Times 20 bold', bg='#fbe0c4', fg='white', height=5, width=10, command=lambda: btnClick(button6))
button6.grid(row=4, column=2)

button7 = Button(tk, text=' ', font='Times 20 bold', bg='#fbe0c4', fg='white', height=5, width=10, command=lambda: btnClick(button7))
button7.grid(row=5, column=0)

button8 = Button(tk, text=' ', font='Times 20 bold', bg='#fbe0c4', fg='white', height=5, width=10, command=lambda: btnClick(button8))
button8.grid(row=5, column=1)

button9 = Button(tk, text=' ', font='Times 20 bold', bg='#fbe0c4', fg='white', height=5, width=10, command=lambda: btnClick(button9))
button9.grid(row=5, column=2)

button10 = Button(tk, text='RESET GAME', font='times 14' , bg='#2978b5', height=5, width=16, command=reset)
button10.grid(row=3, column=3)

button11 = Button(tk, text='NEW GAME', font='times 14' , bg='#2978b5', height=5, width=16, command=new)
button11.grid(row=4, column=3)

label = Label( tk, text="Player 1:", font='Times 18 ', bg='#8ab6d6', fg='black', height=1, width=12)
label.grid(row=6, column=0)

label = Label( tk, text="Player 1:", font='Times 18 ', bg='#8ab6d6', fg='black', height=1, width=12)
label.grid(row=7, column=0)



tk.mainloop()