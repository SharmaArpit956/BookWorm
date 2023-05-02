import tkinter as tk
import web_scraper

url = ""
root = 0
# Create a variable to store the user's input
name_var =0

# Function to handle button click
def submit():
    global url
    global root
    global name_var
    url = name_var.get()
    # print(url)
    name_var.set("")
    root.destroy()

def display():
    global name_var
    global root
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    name_var = tk.StringVar()

    # Create a label widget
    label = tk.Label(root, text="Please enter your website's URL")
    label.pack()

    # Create an Entry widget to get user input
    name_entry = tk.Entry(root, textvariable=name_var)
    name_entry.pack()

    # Create a button to submit the input
    submit_button = tk.Button(root, text="Submit", command=submit)
    submit_button.pack()
    root.mainloop()

if __name__ == "__main__":
    select()


