from tkinter import *
import random

class Convertor:
    def __init__(self):
        print("hello wrld")

    #formatting var
        background_color = "light blue"

    # Converter Main Screen GUI
        self.converter_frame = Frame(width=300, height=300, bg=background_color)
        self.converter_frame.grid()
# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Convertor()
    root.mainloop()