import tkinter


class KiloConventerGUI2:

    def __init__(self):
        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame(self.main_window)
        self.mid_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.promt_label = tkinter.Label(self.top_frame,
                                         text='Input distance in km: ')
        self.kilo_entry = tkinter.Entry(self.top_frame,
                                        width=10)

        self.promt_label.pack(side='left')
        self.kilo_entry.pack(side='left')

        self.descr_label = tkinter.Label(self.mid_frame,
                                         text='Processed in miles: ')
        self.value = tkinter.StringVar()
        self.miles_label = tkinter.Label(self.mid_frame,
                                         textvariable=self.value)

        self.descr_label.pack(side='left')
        self.miles_label.pack(side='left')

        self.calc_button = tkinter.Button(self.bottom_frame,
                                          text='Calculate', command=self.convert)
        self.quit_button = tkinter.Button(self.bottom_frame,
                                          text="Exit", command=self.main_window.destroy)

        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')

        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    def convert(self):
        kilo = float(self.kilo_entry.get())
        miles = kilo * 0.6214
        self.value.set(miles)
