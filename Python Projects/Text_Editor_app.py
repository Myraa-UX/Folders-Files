from tkinter import *
from tkinter.filedialog import askopenfilename,asksaveasfilename

window=Tk()
window.title("My Text Editor")
window.geometry("600x500")
##rows and columns
window.rowconfigure(0, minsize=800, weight=1) #row=0
window.columnconfigure(1, minsize=800, weight=1) #column=1

#define function to open a file
def open_file():
    """Open a file for editing."""
    filepath = askopenfilename(
		filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
	)
    if not filepath:
        return
    txt_edit.delete(1.0, END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(END, text)
        input_file.close()
    window.title(f"My Text Editor - {filepath}")



#define a function to save a file
def save_file():
    # Save the current file as a new file
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = txt_edit.get(1.0, END)
        output_file.write(text)
    window.title(f"My Text Editor - {filepath}")

txt_edit = Text(window)
txt_edit.grid(row=0, column=1, sticky="nsew")
#grid: placement methods: rows , columns
fr_buttons = Frame(window, relief=RAISED, bd=2)
fr_buttons.grid(row=0, column=0, sticky="ns")

btn_open = Button(fr_buttons, text="Open", command=open_file)
btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)

btn_save = Button(fr_buttons, text="Save As...", command=save_file)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)


window.mainloop()
