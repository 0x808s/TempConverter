from tkinter import *
import random

class Convertor:
    def __init__(self):
        print("THISWORKS")

    #formatting var
        background_color = "light blue"

    # Converter Main Screen GUI
        self.converter_frame = Frame(width=600, height=600,
                                     bg=background_color, pady=10)
        self.converter_frame.grid()
        # Heading Title in window
        self.temp_converter_label = Label(text="Temperature Converter",
                                          font=("Arial", "16", "bold"),
                                          bg=background_color,
                                          padx=10, pady=10)
        self.temp_converter_label.grid(row=0)
        # Help Button (row 1)
        self.help_button = Button(self.converter_frame, text="Help",
                                  font=("Arial", "14"),
                                  padx=15, pady=15,
                                  command=self.help)
        self.help_button.grid(row=1)
    def help(self):
        print("you asked for help")
        get_help = Help()
        get_help.help_text.configure(text="HelpText")


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Convertor()
    root.mainloop()