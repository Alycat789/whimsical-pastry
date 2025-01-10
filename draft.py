from tkinter import *
from tkinter import ttk
# from functools import partial

size = 0
theme = " blurp "
FIVE = 25
SEVEN = 49
res = []
buttons = []

def center(n):
    return int((n / 2))

def resolutions(n, l):
    print(f"Please input {n-1} resolutions")
    for i in range(0, n):
        if i == center(n):
            l[i] = "FREE SPACE"
            print(f"{i+1} is the center. FREE SPACE added.")
        else:
            l[i] = input(f"Resolution #{i+1} : ")

def click(button):
    button.configure(text = ";)")
    button["bg"] = "black"

def event(button):
    button["command"] = lambda button=button: click(button)

for i in range(0, SEVEN + 1):
    res.append(" ")

while True:
    size = int(input("How many squares should be on one side of the card? : (5 or 7) "))
    if size == 5 or size == 7:
        break
while True:
    theme = input("Would you like a blue or green theme? : ")
    if theme == "blue" or theme == "green":
        break
if size == 5:
    resolutions(FIVE, res)
elif size == 7:
    resolutions(SEVEN, res)
    
# create the card in a window

count = 0
card = Tk()
card.title("New Year's Resolutions Bingo!")
for _ in range(0, SEVEN):
    buttons.append(Button(card, text = ""))

def create_button(i):
    for r in range(0, i):
        for c in range(0, i):
            buttons[count] = Button(card, text = res[count], width = 30, height = 12, background = theme, foreground = "white", activebackground = "yellow").grid(row = r, column = c)
            # the below function isn't working
            # tried: partial(click, buttons[count]), command = lambda x=x: click(x) [in the Button creation above where x = button[count]], and separating it into it's own function with the lambda [see above function]
            # theres a stack overflow post that says the lambda should work, but the example has the program manipulating the button grid from within a frame. gotta read up on frames before proceeding.
            # title of article: tkinter creating buttons in for loop passing command arguments (3 posts down)
            event(buttons[count])
            count += 1

if size == 5:
    create_button(5)
            
if size == 7:
    create_button(7)

mainloop()

