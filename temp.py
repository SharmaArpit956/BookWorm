import tkinter as tk
from tkinter import scrolledtext


class ScrollableButtonList(tk.Frame):
    def __init__(self, master, buttons, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)

        # create a scrolled frame
        self.scrolled_frame = scrolledtext.ScrolledText(master=self)
        self.scrolled_frame.pack(expand=True, fill="both")

        # create buttons inside the scrolled frame
        for button in buttons:
            btn = tk.Button(self.scrolled_frame, text=button)
            btn.pack()
