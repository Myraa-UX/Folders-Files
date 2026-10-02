'''Project: Resturant Management System'''

#TTk module:
'''  Themed Tkinter (TTK), tkinter module, ComboBox(Dropdown)'''
##Enumerate funtion
'''  number of list [index(position) + value ]
    syntax enumaerate(iterable,start=0 [default:0])'''
##isdigit method-- bitwise operator:
''' its a string method, checking all character r in digits   '''
##Ternary operator : every language:
''' conditional short cut, single line code'''
##Canvas Widget , Label,button....:

'''shapes drawing, pplacements, image'''

##Resturant Management System

#Step1:Import modules
import tkinter as tk
from tkinter import ttk,messagebox

#Step2: Class
class Resturant_Order_Management:
    #initializer, initialize our application
    def __init__(self,root): #root will be define at last
            self.root=root
            self.root.title('Ankshi Resturant Welcome"s You')
            #menu: dictionary== dishes+ cost
            self.menu_items={ "FRIES MEAL": 2,
                "LUNCH MEAL": 2,
                "BURGER MEAL": 3,
                "PIZZA MEAL": 4,
                "CHEESE BURGER": 2.5,
                "DRINKS": 1,
                "FRENCH FRIES": 1,           
                }
            self.exchange_rate=87  #currency conversion

##            self.setup_background(root) #image variable saved--------------------------------------------------------------

            # Create a frame to hold the widgets
            frame = ttk.Frame(root) #create a Frame 
            frame.place(relx=0.5, rely=0.5,anchor=tk.CENTER)   #placed at center

            # Heading label
            ttk.Label(frame,text="Restaurant Order Management", font=("Arial", 20, "bold")).grid(row=0,columnspan=3,padx=10,pady=10)

    ##        menu labels, stored
            self.menu_labels = {}      # To store references to menu item labels (eg: Burger Meal ($3):)
            self.menu_quantities = {}  # To store references to quantity entry widgets ()empty boxes


            # Create labels and entry widgets for each menu item
            for i, (item, price) in enumerate(self.menu_items.items(), start=1): #items(): key+values== ("FRIES MEAL", 2)
                #(start=1) adds a counter i starting at 1.
                label = ttk.Label(frame,text=f"{item} (${price}):",font=("Algerian", 12)) #"{item} (${price}): shows both label and price
                label.grid(row=i, column=0, padx=10, pady=5)
                self.menu_labels[item] = label

                quantity_entry = ttk.Entry(frame, width=5)
                quantity_entry.grid(row=i, column=1, padx=10, pady=5)
                self.menu_quantities[item] = quantity_entry
                # Currency selection
            self.currency_var = tk.StringVar() #text Variable: IntVar(),StringVar(),BoolVar()
            ttk.Label(frame, text="Currency:",font=("Arial", 12)).grid(row=len(self.menu_items) + 1,column=0,padx=10,pady=5)
            # Dropdown for currency selection, ComboBoxFrom ttk Module
            currency_dropdown = ttk.Combobox(frame,textvariable=self.currency_var,state="readonly",width=18,values=('USD', 'INR'))
            currency_dropdown.grid(row=len(self.menu_items) + 1,column=1,padx=10,pady=5)
            currency_dropdown.current(0)  # Set default currency

            
            # Update prices when currency changes
            self.currency_var.trace('w',self.update_menu_prices)  #w-- write/update

             #createa button to place order

            order_button = ttk.Button(frame, text="Place Order", command=self.place_order)
            order_button.grid(row=len(self.menu_items) + 2, columnspan=3, padx=10, pady=10)

             #insert image for resraunt background
##    def setup_background(self, root):
##        bg_width, bg_height = 800, 600
##        canvas = tk.Canvas(root, width=bg_width, height=bg_height)
##        canvas.pack()
##        original_image = tk.PhotoImage(file="restro_img.png")
##        self.background_image = original_image.subsample( original_image.width() // bg_width, original_image.height() // bg_height)
##        canvas.create_image(0, 0, anchor=tk.NW, image=self.background_image)
##        canvas.image = self.background_image

    # Method/function to update the menu prices based on the selected currency
    def update_menu_prices(self, *args): #(*args)== multiple arguments(Kwarg)
        currency=self.currency_var.get() #get() to get values
        symbol = "₹" if currency == "INR" else "$"
        rate = self.exchange_rate if currency == "INR" else 1
        for item, label in self.menu_labels.items():
                price = self.menu_items[item] * rate
                label.config(text=f"{item} ({symbol}{price}):")
    # Method to place an order
    def place_order(self):
##            null value store
        total_cost=0
        order_summary = "Order Summary:\n"
        #Check which currency
        currency = self.currency_var.get()
        symbol = "₹" if currency == "INR" else "$"
        rate = self.exchange_rate if currency == "INR" else 1
        #Go through all the menu items
        for item, entry in self.menu_quantities.items():
            quantity = entry.get()
        #Check if the number is valid
            if quantity.isdigit():
                quantity = int(quantity)
                #Calculate the price
                price = self.menu_items[item] * rate
                cost = quantity * price
                total_cost += cost
                #Write it down in the summary
                if quantity > 0:
                    order_summary += f"{item}: {quantity} x {symbol}{price} = {symbol}{cost}\n"
        #Show the final result
        if total_cost > 0:
                order_summary += f"\nTotal Cost: {symbol}{total_cost}"
                messagebox.showinfo("Order Placed", order_summary)
        else:
                messagebox.showerror("Error", "Please order at least one item.")


#Main block to run my App
if __name__ == "__main__":
    #Run the following code only if this file is opened directly, not when it’s imported by another file.”
    root = tk.Tk()
    app = Resturant_Order_Management(root)
    root.geometry("900x900")
    root.mainloop()


    







            







            


            


            
            














