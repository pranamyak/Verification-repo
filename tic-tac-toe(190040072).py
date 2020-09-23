from tkinter import *
import tkinter.messagebox

tic = Tk()
tic.title("Tic Tac Toe")
tic.geometry("300x300")

label = Label( tic, text="Player 1 Name :", font='Times 12 bold', bg = "black" , fg ="yellow", width=10)
label.grid(row=1, column=0)

label = Label( tic, text="Player 2 Name :", font='Times 12 bold', bg = "black" , fg ="yellow", width=10)
label.grid(row=2, column=0)

player1_name = Entry(tic,width =8)
player1_name.grid(row =1 , column =1)

player2_name = Entry(tic,width =8)
player2_name.grid(row =2 , column =1)

bclick = True
flag=0

def disableButton():
    b1.configure(state=DISABLED)
    b2.configure(state=DISABLED)
    b3.configure(state=DISABLED)
    b4.configure(state=DISABLED)
    b5.configure(state=DISABLED)
    b6.configure(state=DISABLED)
    b7.configure(state=DISABLED)
    b8.configure(state=DISABLED)
    b9.configure(state=DISABLED)

def btnClick(a):
    global bclick,flag

    if a["text"] == " " and bclick == True:
        a["text"] = "X"
        bclick = False
        checkForWin()
        flag += 1


    elif a["text"] == " " and bclick == False:
        a["text"] = "O"
        bclick = True
        checkForWin()
        flag += 1

    else:
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "Button already Clicked!")

def checkForWin():
    p1 = player1_name.get() + "  wins"
    p2 = player2_name.get() + "  wins"
    if (b1['text'] == 'X' and b2['text'] == 'X' and b3['text'] == 'X' or
        b4['text'] == 'X' and b5['text'] == 'X' and b6['text'] == 'X' or
        b7['text'] =='X'  and b8['text'] == 'X' and b9['text'] == 'X' or
        b1['text'] == 'X' and b5['text'] == 'X' and b9['text'] == 'X' or
        b3['text'] == 'X' and b5['text'] == 'X' and b7['text'] == 'X' or
        b1['text'] == 'X' and b2['text'] == 'X' and b3['text'] == 'X' or
        b1['text'] == 'X' and b4['text'] == 'X' and b7['text'] == 'X' or
        b2['text'] == 'X' and b5['text'] == 'X' and b8['text'] == 'X' or
        b7['text'] == 'X' and b6['text'] == 'X' and b9['text'] == 'X'):
        disableButton()
        tkinter.messagebox.showinfo("Tic-Tac-Toe", p1)

    elif(flag == 8):
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "It is a Tie")

    elif (b1['text'] == 'O' and b2['text'] == 'O' and b3['text'] == 'O' or
          b4['text'] == 'O' and b5['text'] == 'O' and b6['text'] == 'O' or
          b7['text'] == 'O' and b8['text'] == 'O' and b9['text'] == 'O' or
          b1['text'] == 'O' and b5['text'] == 'O' and b9['text'] == 'O' or
          b3['text'] == 'O' and b5['text'] == 'O' and b7['text'] == 'O' or
          b1['text'] == 'O' and b2['text'] == 'O' and b3['text'] == 'O' or
          b1['text'] == 'O' and b4['text'] == 'O' and b7['text'] == 'O' or
          b2['text'] == 'O' and b5['text'] == 'O' and b8['text'] == 'O' or
          b7['text'] == 'O' and b6['text'] == 'O' and b9['text'] == 'O'):
        disableButton()
        tkinter.messagebox.showinfo("Tic-Tac-Toe", p2)

b1 = Button(tic , text=" ", height = 3 ,  width=8, bg ="light sky blue", command=lambda: btnClick(b1))
b1.grid(row=5, column=1)

b2 = Button(tic, text=' ', height = 3 ,  width=8, bg ="light goldenrod" , command=lambda: btnClick(b2))
b2.grid(row=5, column=3)

b3 = Button(tic, text=' ', height = 3 ,  width=8, bg ="light sky blue", command=lambda: btnClick(b3))
b3.grid(row=5, column=5)

b4 = Button(tic, text=' ', height = 3 , width=8, bg ="light goldenrod", command=lambda: btnClick(b4))
b4.grid(row=7, column=1)

b5 = Button(tic, text=' ', height = 3 ,width=8, bg ="light sky blue", command=lambda: btnClick(b5))
b5.grid(row=7, column=3)

b6 = Button(tic, text=' ', height = 3 , width=8, bg ="light goldenrod", command=lambda: btnClick(b6))
b6.grid(row=7, column=5)

b7 = Button(tic, text=' ', height = 3 ,  width=8, bg ="light sky blue", command=lambda: btnClick(b7))
b7.grid(row=9, column=1)

b8 = Button(tic, text=' ', height = 3 ,  width=8, bg ="light goldenrod", command=lambda: btnClick(b8))
b8.grid(row=9, column=3)

b9 = Button(tic, text=' ', height = 3 , width=8, bg ="light sky blue", command=lambda: btnClick(b9))
b9.grid(row=9, column=5)

tic.mainloop()
