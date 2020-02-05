from tkinter import Tk
from calcframe import CalculatorFrame

if __name__ == "__main__":
    window = Tk()
    window.title("Dave's Calc")
    window.iconbitmap(r"calculator.ico")
    calculator_frame = CalculatorFrame(window)
    calculator_frame.bind_all("<Key>", calculator_frame.keyboard_press)
    calculator_frame.bind_all("<KeyRelease>", calculator_frame.button_release)
    calculator_frame.mainloop()
