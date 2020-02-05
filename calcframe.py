from tkinter import *


from calcbutton import CustomButton


class CalculatorFrame(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master=master)
        self.list_numbers = []
        self.grid()
        self.button_list = []

        self.make_buttons_list()
        self.position_buttons()

        self.running_equation = ""

        self.output_variable = StringVar()
        self.output = Entry(self, textvariable=self.output_variable, width=self.button["width"]*5-2, font=self.button["font"],
                            state="disabled", disabledforeground="black", disabledbackground="white", justify="right")
        self.output.grid(row=0, columnspan=5)

        self.showing_result = False

    def clear(self):
        self.output_variable.set("")
        self.list_numbers = []
        self.running_equation = ""

    def calculate(self):
        equation = ""
        for i in self.list_numbers:
            if i == "=":
                break
            equation += str(i)
        try:
            total = eval(equation)
        except SyntaxError:
            self.list_numbers = []
            self.output_variable.set("Error")
            self.showing_result = True
        self.output_variable.set(total)
        self.showing_result = True

    def add_to_list(self, number_to_add):
        if number_to_add == "del":
            self.del_button()
        else:
            if self.showing_result:
                self.clear()
                self.showing_result = False
            """display output string"""
            self.running_equation += str(number_to_add)
            self.output_variable.set(str(self.running_equation))
            """number to list for computation"""
            if number_to_add == "X" or number_to_add == "x":
                number_to_add = "*"
            self.list_numbers.append(number_to_add)
            if number_to_add == "=":
                self.calculate()

    def make_buttons_list(self):
        """Make buttons and adds them to a list. The Numbers are made in the for loop and the custom buttons are
        added at specific points as the position button uses a for loop to place every thing in a grid"""
        for i in range(10):
            self.button = CustomButton(self, name_button=i)
            self.button_list.append(self.button)
            self.button["bg"] = "light steel blue"
        self.button_list.insert(9, self.button_list.pop(0))  # Move 0 button to the last position
        """add custom buttons"""
        self.button = CustomButton(self, name_button="del")
        self.button_list.insert(9, self.button)
        self.button["bg"] = "tomato"

        self.button = CustomButton(self, name_button=".")
        self.button_list.append(self.button)

        self.button = CustomButton(self, name_button="/")
        self.button_list.insert(3, self.button)

        self.button = CustomButton(self, name_button="X")
        self.button_list.insert(7, self.button)

        self.button = CustomButton(self, name_button="-")
        self.button_list.insert(11, self.button)

        self.button = CustomButton(self, name_button="+")
        self.button_list.insert(15, self.button)

        self.button = CustomButton(self, name_button="=")
        self.button["height"] = (int(self.button["height"])*5)
        self.button["bg"] = "light blue"

    def del_button(self):
        """Delete the last thing pressed"""
        self.list_numbers.pop()
        self.running_equation = self.running_equation[:-1]
        self.output_variable.set(str(self.running_equation))

    def keyboard_press(self, event):
        """When a key is pressed run it through the key check to see if it is used. If it is, press press the button"""
        print("Button pressed", event.keysym)
        if self.button["text"] == self.key_check(event.char):
            self.button.invoke()
            self.button["relief"] = "sunken"
        for i in self.button_list:  # check all the buttons in the list
            if i["text"] == self.key_check(event.char):
                i["relief"] = "sunken"
                i.invoke()

    def button_release(self, event):
        """When the key is released, raise the button back up. event.keysym has to be checked as the Return and
        BackSpace key don't return anything in event.char for some reason"""
        for i in self.button_list:
            if i["text"] == self.key_check(event.keysym) or i["text"] == self.key_check(event.char):
                i["relief"] = "raised"
            if "=" == self.key_check(event.keysym):
                self.button["relief"] = "raised"

    def position_buttons(self):
        """Setup: position buttons from list"""
        total_columns = 4
        row = 2
        column = 1
        for i in range(len(self.button_list)):
            if column > total_columns:
                column = 1
                row += 1
            self.button_list[i].grid(row=row, column=column)
            column += 1
        self.button.grid(column=5, row=2, rowspan=4)

    def key_check(self, test):
        """Return a string if it is a used key and convert it to what it needs to be
        """
        switcher = {
            "1": "1",
            "2": "2",
            "3": "3",
            "4": "4",
            "5": "5",
            "6": "6",
            "7": "7",
            "8": "8",
            "9": "9",
            "0": "0",
            "*": "X",
            "x": "X",
            "X": "X",
            "\x08": "del",
            "/": "/",
            "-": "-",
            "+": "+",
            ".": ".",
            "\r": "=",
            # the last two entries are for the event.keysym check
            "Return": "=",
            "BackSpace": "del"

        }
        return switcher.get(test)