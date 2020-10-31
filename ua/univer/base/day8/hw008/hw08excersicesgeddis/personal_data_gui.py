import tkinter
from tkinter import *

class PersonalDataGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
        
        self.value = tkinter.StringVar()
        self.personal_data_label = tkinter.Label(self.top_frame,
                                                 textvariable=self.value)
        self.personal_data_label.pack(side='left')
        
        self.show_info_button = tkinter.Button(self.bottom_frame,
                                               text='Show info', command = self.show_info)
        self.exit_button = tkinter.Button(self.bottom_frame,
                                               text='Exit', command = self.main_window.destroy)

        

        self.show_info_button.pack(side='left')
        self.exit_button.pack(side='left')

        self.top_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    def show_info(self):
        personal_data = '08114, USA Alaska state,\n, Vancuver, \nSanta Claus postal'
        self.value.set(personal_data)
        


