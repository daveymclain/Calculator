from tkinter import *
import config


class OutputFrame(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)

        self.output_variable = StringVar()
        self.output = Entry(self, textvariable=self.output_variable, width=config.button_width*5-2,
                            font=config.app_font, state="disabled", disabledforeground="black",
                            disabledbackground="white", justify="right")
        self.output.grid(row=0, columnspan=5)
        self.grid(row=0)
