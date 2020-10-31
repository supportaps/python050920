import tkinter


class CalcMilesPerGalFuel:

    def __init__(self):
        self.main_window = tkinter.Tk()

        self.galon_frame = tkinter.Frame(self.main_window)
        self.miles_frame = tkinter.Frame(self.main_window)
        self.represent_calculation_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)

        self.galons_label = tkinter.Label(self.galon_frame,
                                          text='Input amount of gallons: ')
        self.galons_entry = tkinter.Entry(self.galon_frame,
                                          width=10)
        self.miles_label = tkinter.Label(self.miles_frame,
                                         text='Input amount of miles: ')
        self.miles_entry = tkinter.Entry(self.miles_frame,
                                         width=10)

        self.represent_calculation_label = tkinter.Label(self.represent_calculation_frame,
                                                         text='Miles per galon(MPG): ')
        self.value = tkinter.StringVar()
        self.miles_label_result = tkinter.Label(self.represent_calculation_frame,
                                                textvariable=self.value)

        self.galons_label.pack(side='left')
        self.galons_entry.pack(side='left')
        self.miles_label.pack(side='left')
        self.miles_entry.pack(side='left')
        self.represent_calculation_label.pack(side='left')
        self.miles_label_result.pack(side='left')

        self.calculate_button = tkinter.Button(self.button_frame,
                                               text='Calculate MPG', command=self.calculate_mpg)
        self.exit_button = tkinter.Button(self.button_frame,
                                          text="Exit", command=self.main_window.destroy)

        self.calculate_button.pack(side='left')
        self.exit_button.pack(side='left')

        self.galon_frame.pack()
        self.miles_frame.pack()
        self.represent_calculation_frame.pack()
        self.button_frame.pack(side='top')

        self.main_window.mainloop()

    def calculate_mpg(self):
        galons = float(self.galons_entry.get())
        miles = float(self.miles_entry.get())

        value = miles / galons
        self.value.set(value)