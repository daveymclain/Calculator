from tkinter import Tk
from calcframe import CalculatorFrame
from outputframe import OutputFrame

if __name__ == "__main__":
    window = Tk()
    window.title("Dave's Calc")
    window.iconbitmap(r"calculator.ico")
    output_frame = OutputFrame(window)
    calculator_frame = CalculatorFrame(window, output_frame=output_frame)
    calculator_frame.bind_all("<Key>", calculator_frame.keyboard_press)
    calculator_frame.bind_all("<KeyRelease>", calculator_frame.button_release)
    calculator_frame.mainloop()
