from tkinter import *

#create a window
window=Tk()
window.title('Event Handler')
window.geometry("800x800") #('X x Y')
#Function/ 
def handle_keypress(event):
    print(event.char)
##    This makes a function that says:
"If someone presses a key, show which key it was."
#bind()-- Event Handler
window.bind("<Key>", handle_keypress)

def handle_click(event):
    print("\nThe button was clicked!")
#widgets (Components) , Button Widgtes
button = Button(text="Click me!",bg='red',font=('Calibri',23))
#placement methods, pack()
button.pack()
# bind clicking function to button widgets
button.bind("<Button-1>", handle_click)


window.mainloop()
