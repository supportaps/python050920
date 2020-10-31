import tkinter


class Temperature:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.temperature_celsium_frame = tkinter.Frame(self.main_window)
        self.represent_farengeit_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)


        self.celsium_label = tkinter.Label(self.temperature_celsium_frame,
                                           text='Input temperature in celsium: ')
        self.celsium_entry = tkinter.Entry(self.temperature_celsium_frame,
                                           width=10)


        self.represent_calculation_label = tkinter.Label(self.represent_farengeit_frame,
                                                         text='Temperature in Farengeit scale: ')
        self.value = tkinter.StringVar()
        self.temperature_label_result = tkinter.Label(self.represent_farengeit_frame,
                                                      textvariable=self.value)

        self.celsium_label.pack(side='left')
        self.celsium_entry.pack(side='left')

        self.represent_calculation_label.pack(side='left')
        self.temperature_label_result.pack(side='left')

        self.calculate_button = tkinter.Button(self.button_frame,
                                               text='Transform in Farengeit gradus', command=self.transform_in_farengeit)
        self.exit_button = tkinter.Button(self.button_frame,
                                          text="Exit", command=self.main_window.destroy)

        self.calculate_button.pack(side='left')
        self.exit_button.pack(side='left')

        self.temperature_celsium_frame.pack()
        self.represent_farengeit_frame.pack()
        self.button_frame.pack(side='top')

        self.main_window.mainloop()

    def transform_in_farengeit(self):
        temperature_in_celsium = float(self.celsium_entry.get())
        temperature_in_farengeit = temperature_in_celsium * (9 / 5) + 32
        self.value.set(temperature_in_farengeit)