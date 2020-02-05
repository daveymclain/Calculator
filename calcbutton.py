from tkinter import Button

button_width = 5
button_height = int(button_width / 2)
app_font = "Calibri {size}".format(size=str(int(button_width * 3)))


class CustomButton(Button):


    def __init__(self, master=None, name_button=None):
        Button.__init__(self, master, width=button_width, height=button_height, text=str(name_button),
                        command=lambda: master.add_to_list(name_button), font=app_font)