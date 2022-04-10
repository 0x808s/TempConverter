""" Converter trial 1 v1
Based on the 02_Converter_GUI
Added commands to buttons - at line 51 and 58
Then added functions for each conversion - lines 84-96
"""

from tkinter import *
from functools import partial # To prevent unwanted additional windows
import random


class Converter:
    def __init__(self):
        # Formatting variables
        background_color = "light blue"

        # Converter frame
        self.converter_frame = Frame(width=300, bg=background_color, pady=10)
        self.converter_frame.grid()

        # Temperature converter Heading (row 0)
        self.temp_heading_label = Label(self.converter_frame,
                                        text="Temperature Converter",
                                        font="Arial 16 bold",
                                        bg=background_color,
                                        pady=10, padx=10)
        self.temp_heading_label.grid(row=0)

        # User instructions (row 1)
        self.temp_instructions_label = Label(self.converter_frame,
                                             text="Type in the amount to be "
                                                  "converted and then push "
                                                  "one of the buttons "
                                                  "below...",
                                             font="Arial 10 italic", wrap=250,
                                             justify=LEFT, bg=background_color,
                                             padx=10, pady=10)
        self.temp_instructions_label.grid(row=1)

        # Temperature entry box (row 2)
        self.to_convert_entry = Entry(self.converter_frame, width=20,
                                      font="Arial 14 bold")
        self.to_convert_entry.grid(row=2)

        # Conversion buttons frame (row 3), orchid3 | khaki1
        self.conversion_buttons_frame = Frame(self.converter_frame)
        self.conversion_buttons_frame.grid(row=3, pady=10)

        # Celsius temperature conversion
        self.to_c_button = Button(self.conversion_buttons_frame,
                                  text="To Centigrade", font="Arial 10 bold",
                                  command=self.to_cen,
                                  bg="Khaki1", padx=10, pady=10)
        self.to_c_button.grid(row=0, column=0)

        # Fahrenheit temperature conversion
        self.to_f_button = Button(self.conversion_buttons_frame,
                                  text="To Fahrenheit", font="Arial 10 bold",
                                  command=self.to_far,
                                  bg="Orchid1", padx=10, pady=10)
        self.to_f_button.grid(row=0, column=1)

        # Answer label (row 4)
        self.converted_label = Label(self.converter_frame,
                                     font="Arial 14 bold",
                                     fg="purple", bg=background_color,
                                     pady=10, text="Conversion goes here")
        self.converted_label.grid(row=4)

        # History / Help button frame (row 5)
        self.hist_help_frame = Frame(self.converter_frame)
        self.hist_help_frame.grid(row=5, pady=10)

        self.calc_hist_button = Button(self.hist_help_frame,
                                       font="Arial 12 bold",
                                       text="Calculation history",
                                       width=15)
        self.calc_hist_button.grid(row=0, column=0)

        self.help_button = Button(self.hist_help_frame, font="Arial 12 bold",
                                  text="Help", width=5)
        self.help_button.grid(row=0, column=1)

    def to_cen(self):
        which = 1
        self.change(which)

    def to_far(self):
        which = 2
        self.change(which)

    def change(self, which):
        if which == 1:
            print("Centigrade result")
        else:
            print("Fahrenheit result")


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Title goes here")
    something = Converter()
    root.mainloop()
