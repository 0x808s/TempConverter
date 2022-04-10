from tkinter import *


class Converter:
    def __init__(self):
        background_color = "light blue"
        self.all_calculations = []
        self.converter_frame = Frame(bg=background_color, pady=10)
        self.converter_frame.grid()

        self.temp_heading_label = Label(self.converter_frame,
                                        text="TEMPERATURE CONVERTER",
                                        font="Arial 19 bold",
                                        bg=background_color,
                                        padx=10, pady=10)
        self.temp_heading_label.grid(row=0)
        self.temp_heading_label = Label(self.converter_frame,
                                        text="Type in the amount to be "
                                             "Converted and then push "
                                             "one of the buttons "
                                             "below...",
                                        font= "Arial 10 italic", wrap=290,
                                        justify=LEFT, bg=background_color,
                                        padx=10, pady=10)
        self.temp_instruction_label.grid(row=1)
