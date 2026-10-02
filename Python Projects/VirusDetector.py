# Import necessary libraries
from tkinter import *
from tkinter import messagebox

# Setup Tkinter Window
root = Tk()
root.geometry("200x200")

# Function for Displaying Warning Message
# This will be called once the button is clicked
#messagebox.showsuccessful('MessageTitle','convey Message')
# messagebox.showwarning("Window Name", "Text to be displayed")
def msg():
	messagebox.showwarning("Alert", "Stop! Virus Found.")
	messagebox.showerror('Oops! ','Virus got Stuck')
	messagebox.showinfo('Ready to Go','Virus got Eliminated')
	

# Adding Button Widget to Window
button = Button(root, text="Scan for Virus", command=msg) #command-- to call function
button.place(x=40, y=80)

# Entering main event loop
root.mainloop()
