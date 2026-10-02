from tkinter import *
from tkinter import messagebox  #showinfo,showwarning
#image PIL.. pillow
from PIL import Image, ImageTk

root = Tk()
root.title('Denomination Counter')
root.configure(bg='light blue')
root.geometry('750x900')

# Adding Image and Labels in the Main Window
upload = Image.open("app_img.jpg")
# Resize the image using resize() method
upload = upload.resize((700, 800))
image = ImageTk.PhotoImage(upload)
label = Label(root, image=image, bg='light blue')
label.place(x=180, y=20)

label1 = Label(root,text="Hey User! Welcome to Denomination Counter Application.",
               bg='blue', font=('Sans Serif',25))
label1.place(relx=0.5, y=340, anchor=CENTER)

def msg():
    MsgBox = messagebox.showinfo("Alert", "Do you want to calculate the denomination count?")
    if MsgBox == 'ok':
        topwin()
button1 = Button(root,text="Let's get started!",command=msg,bg='brown',fg='white')
button1.place(x=260, y=360)

def topwin():
    top = Toplevel()
    top.title("Denominations Calculator")
    top.configure(bg='light grey')
    top.geometry("600x950+50+50")
    label = Label(top, text="Enter total amount", bg='light grey',font=('Algerian',25))
    entry = Entry(top)
    lbl = Label(top, text="Here are number of notes for each denomination", bg='light grey',font=('Algerian',25))

    l1 = Label(top, text="2000", bg='light grey',font=('Algerian',25))
    l2 = Label(top, text="500", bg='light grey',font=('Algerian',25))
    l3 = Label(top, text="100", bg='light grey',font=('Algerian',25))

    t1 = Entry(top)
    t2 = Entry(top)
    t3 = Entry(top)
    def calculator():
##  try and except blocks:
        try:
            #global ... whole script
            global amount
            amount = int(entry.get())  #amount variable is declared globally
            
            note2000 = amount // 2000
            amount %= 2000
            
            note500 = amount // 500
            amount %= 500
            
            note100 = amount // 100

            # Clear old results
            t1.delete(0, END)  #1-->last character
            t2.delete(0, END)
            t3.delete(0, END)

            # Insert new results
            t1.insert(END, str(note2000))
            t2.insert(END, str(note500))
            t3.insert(END, str(note100))

        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")
            
        
        #place all widgets in New window
        # Centering Widgets in the Top Window
    btn = Button(top, text='Calculate', command=calculator, bg='brown', fg='white',font=('Algerian',25))

    label.place(x=230, y=50   )
    entry.place(x=200, y=80   )
    btn.place(x=240, y=120   )
    lbl.place(x=140, y=170   )

    l1.place(x=180, y=200   )
    l2.place(x=180, y=230   )
    l3.place(x=180, y=260   )

    t1.place(x=270, y=200   )
    t2.place(x=270, y=230   )
    t3.place(x=270, y=260)

    top.mainloop()


root.mainloop()













        

