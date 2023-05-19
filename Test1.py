import tkinter as tk

class MyApplication:
    def __init__(self, root):
        self.root = root
        self.root.title("Judy's Party Hire Store")

        self.create_widgets()

    def create_widgets(self):
        # TODO: Add widgets here
        pass

# Create the main window
root = tk.Tk()

# Set window title
root.title("Judy's Party Hire Store")

# Create an instance of the MyApplication class
app = MyApplication(root)

# Run the application
root.mainloop() 