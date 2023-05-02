import tkinter as tk


item_selected ="hello"
root =0
def button_click(label):
    global item_selected
    global root
    print( label, "is selected")
    item_selected = label
    #TODO button selection closes the current window. right now it has to be manually closed
    
    root.destroy()

def display(button_labels):
    global root
    root = tk.Tk()
    # root.attributes('-fullscreen', True)
    # Create a frame to hold the buttons
    button_frame = tk.Frame(root)
    button_frame.pack()

    # Create a button for each label in the list
    for i, label in enumerate(button_labels):
        #TODO Change the looks of the button here
        button = tk.Button(button_frame, text=label,  bg="white", anchor="w",
                        command=lambda index=i: button_click(button_labels[index]))
        button.pack(fill=tk.BOTH, expand=tk.YES)

    root.mainloop()
    
if __name__ == "__main__":
    items=["USB Drive","Website's URL aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"]
    display(items)
    print("wait for me ")