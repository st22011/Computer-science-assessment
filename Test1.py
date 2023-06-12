import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import random
import json


class PartyHireApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Julie's Party Hire Service")

        self.items = ["Tables", "Chairs", "Decorations", "Sound System", "BBQ", "Tents", "Balloons", "TVS",
                      "Arcade Games", "Lounge Furniture"]  # List of available items
        self.orders = []  # List to store orders

        self.create_widgets()

        # Load saved orders
        self.load_orders()

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

        # Tree View
        self.treeview_orders = ttk.Treeview(
            self.root, columns=("Receipt No", "Customer", "Item", "Quantity"), show="headings"
        )
        self.treeview_orders.heading("Receipt No", text="Receipt No")
        self.treeview_orders.heading("Customer", text="Customer")
        self.treeview_orders.heading("Item", text="Item")
        self.treeview_orders.heading("Quantity", text="Quantity")
        self.treeview_orders.pack()

        # Delete Button
        self.btn_delete = tk.Button(
            self.root, text="Delete Order", command=self.delete_order, width=20
        )
        self.btn_delete.pack(pady=10)

        # Save Button
        self.btn_save = tk.Button(
            self.root, text="Save Orders", command=self.save_orders, width=20
        )
        self.btn_save.pack(pady=10)

        # Exit Button
        self.btn_exit = tk.Button(
            self.root, text="Exit", command=self.root.quit, width=20
        )
        self.btn_exit.pack(pady=10)

        # Validate Customer Name Entry
        self.entry_name.config(
            validate="key", validatecommand=(self.root.register(self.validate_customer_name), "%P")
        )
        self.entry_quantity.config(
            validate="key", validatecommand=(self.root.register(self.validate_quantity), "%P")
        )

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
        order = (receipt_number, name, item, quantity)
        self.orders.append(order)

        # Update tree view
        self.treeview_orders.insert("", tk.END, values=order)

        # Clear input fields
        self.entry_name.delete(0, tk.END)
        self.entry_quantity.delete(0, tk.END)

    def save_orders(self):
        # Check if there are orders to save
        if not self.orders:
            messagebox.showwarning("No Orders", "There are no orders to save.")
            return

        # Get the displayed orders from the tree view
        displayed_orders = [self.treeview_orders.item(item)["values"] for item in self.treeview_orders.get_children()]

        # Save the displayed orders to a file
        filename = "orders.json"
        with open(filename, "w") as file:
            json.dump(displayed_orders, file)

        messagebox.showinfo("Orders Saved", f"The displayed orders have been saved to {filename}.")

    def load_orders(self):
        # Load the orders from the file
        filename = "orders.json"
        try:
            with open(filename, "r") as file:
                self.orders = json.load(file)
        except FileNotFoundError:
            self.orders = []  # Set empty list if the file is not found

        # Clear the tree view
        self.treeview_orders.delete(*self.treeview_orders.get_children())

        # Populate the tree view with loaded orders
        for order in self.orders:
            self.treeview_orders.insert("", tk.END, values=order)

    def delete_order(self):
        # Get the selected item
        selected_item = self.treeview_orders.selection()

        if selected_item:
            # Remove order from the list
            index = self.treeview_orders.index(selected_item)
            self.orders.pop(index)

            # Update the tree view
            self.treeview_orders.delete(selected_item)

            # Update the saved orders file
            displayed_orders = [self.treeview_orders.item(item)["values"] for item in
                                self.treeview_orders.get_children()]
            filename = "orders.json"
            with open(filename, "w") as file:
                json.dump(displayed_orders, file)


# Create the main window
root = tk.Tk()

# Set window title
root.title("Julie's Party Hire Service")

# Create an instance of the PartyHireApp
app = PartyHireApp(root)

# Run the application
root.mainloop()
