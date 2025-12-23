from tkinter import *
import random

def nextPlayer(row,column):
    global player
    
    if checkWinner() is False and buttons[row][column]["text"] == "":
        if player == players[0]:

            buttons[row][column]["text"] = player

            if checkWinner() is False:
                player = players[1]
                label.config(text=player+" 's turn")
            elif checkWinner() is True:
                label.config(text=player+" won !!")
            elif checkWinner() == "Tie":
                label.config(text="Tie!")

        else:
            buttons[row][column]["text"] = player

            if checkWinner() is False:
                player = players[0]
                label.config(text=player+" 's turn")
            elif checkWinner() is True:
                label.config(text=player+" won !!")
            elif checkWinner() == "Tie":
                label.config(text="Tie!")

def checkWinner():
    for i in range(3):
        if buttons[i][0]["text"] == buttons[i][1]["text"] ==buttons[i][2]["text"] != "":
            return True
        elif buttons[0][i]["text"] == buttons[1][i]["text"] == buttons[2][i]["text"] != "":
            return True

    if buttons[0][0]["text"] == buttons[1][1]["text"] ==buttons[2][2]["text"] != "":
        return True
    elif buttons[0][2]["text"] == buttons[1][1]["text"] ==buttons[2][0]["text"] != "":
        return True
    elif emptySpaces() is False:
        return "Tie"
    return False

def emptySpaces():
    space : int = 9
    for i in range(3):
        for j in range(3):
            if buttons[i][j]["text"] != "":
                space-=1
    if space==0:
        return False
    else:
        return True   

def newGame():
    for i in range(3):
        for j in range(3):
            buttons[i][j]["text"]=""
    label.config(text=player+" 's turn")

window = Tk()
window.title("TIC TAC TOE")

buttons = [['O','O','O'],
           ['O','O','O'],
           ['O','O','O']]

players = ['X','O']
player = random.choice(players)

label = Label(window,text=player+"'s turn",bg="black",fg="#00FF00")
label.config(font=("Inkfree",20,"bold"))
label.pack()

resetButton = Button(window,text="reset",font=("Inkfree",20,"bold"),bg="black",fg="#00FF00",padx=5,
                     command=newGame)
resetButton.pack()

frame = Frame(window)
frame.pack()

for i in range(3):
    for j in range(3):
        buttons[i][j] = Button(frame,text="",font=("",25,"bold"),width=4,height=2,
                               activebackground="black",activeforeground="#00FF00",
                               command= lambda row=i,column=j : nextPlayer(row,column))
        buttons[i][j].grid(row=i,column=j)

window.mainloop()   