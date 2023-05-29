import tkinter as tk
from tkinter import messagebox
import random


class PartyHireApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Judy's Party Hire Service")

        self.items = ["Tables", "Chairs", "Decorations", "Sound System", "BBQ"]  # List of available items
        self.orders = []  # List to store orders

        self.create_widgets()

    def create_widgets(self):
        # Frame for the input fields
        input_frame = tk.Frame(self.root)
        input_frame.pack(pady=10)

        # Customer Name
        lbl_name = tk.Label(input_frame, text="Customer Name:")
        lbl_name.grid(row=0, column=0, sticky="w")
        self.entry_name = tk.Entry(input_frame)
        self.entry_name.grid(row=0, column=1)

        # Item Hired
        lbl_item = tk.Label(input_frame, text="Item Hired:")
        lbl_item.grid(row=1, column=0, sticky="w")
        self.selected_item = tk.StringVar()
        self.selected_item.set(self.items[0])  # Set default item
        self.dropdown_item = tk.OptionMenu(input_frame, self.selected_item, *self.items)
        self.dropdown_item.grid(row=1, column=1)

        # Quantity
        lbl_quantity = tk.Label(input_frame, text="Quantity:")
        lbl_quantity.grid(row=2, column=0, sticky="w")
        self.entry_quantity = tk.Entry(input_frame)
        self.entry_quantity.grid(row=2, column=1)

        # Order Button
        self.btn_order = tk.Button(
            self.root, text="Place Order", command=self.place_order, width=20
        )
        self.btn_order.pack(pady=10)

        # Orders List
        self.listbox_orders = tk.Listbox(self.root, width=50)
        self.listbox_orders.pack()

        # Delete Button
        self.btn_delete = tk.Button(
            self.root, text="Delete Order", command=self.delete_order, width=20
        )
        self.btn_delete.pack(pady=10)

        # Validate Customer Name Entry
        self.entry_name.config(validate="key", validatecommand=(self.root.register(self.validate_customer_name), "%P"))
        self.entry_quantity.config(validate="key", validatecommand=(self.root.register(self.validate_quantity), "%P"))

    def validate_customer_name(self, input_text):
        # Validate customer name input
        if all(char.isalpha() or char.isspace() for char in input_text):
            return True
        else:
            messagebox.showerror("Error", "Customer name can only contain alphabetic characters and spaces.")
            return False

    def validate_quantity(self, input_text):
        # Validate quantity input
        if input_text.isdigit() and 1 <= int(input_text) <= 500 or input_text == "":
            return True
        else:
            messagebox.showerror("Error", "Quantity must be a number between 1 and 500.")
            return False

    def place_order(self):
        # Get input values
        name = self.entry_name.get()
        item = self.selected_item.get()
        quantity = self.entry_quantity.get()

        # Validate input
        if not name or not item or not quantity:
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        # Generate receipt number
        receipt_number = random.randint(1000, 9999)

        # Add order to the list
        order = f"Receipt No: {receipt_number} - Customer: {name} - Item: {item} - Quantity: {quantity}"
        self.orders.append(order)

        # Update listbox
        self.listbox_orders.insert(tk.END, order)

        # Clear input fields
        self.entry_name.delete(0, tk.END)
        self.entry_quantity.delete(0, tk.END)

    def delete_order(self):
        # Get the selected index
        selected_index = self.listbox_orders.curselection()

        if selected_index:
            # Remove order from the list
            self.orders.pop(selected_index[0])

            # Update the listbox
            self.listbox_orders.delete(selected_index)


# Create the main window
root = tk.Tk()

# Set window title
root.title("Judy's Party Hire Service")

# Create an instance of the PartyHireApp
app = PartyHireApp(root)

# Run the application
root.mainloop()
