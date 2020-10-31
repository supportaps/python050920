import tkinter
import tkinter.messagebox


class KiloConventerGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.promt_label = tkinter.Label(self.top_frame,
                                         text='Input distance in km: ')
        self.kilo_entry = tkinter.Entry(self.top_frame,
                                        width=10)

        self.promt_label.pack(side='left')
        self.kilo_entry.pack(side='left')

        self.calc_button = tkinter.Button(self.bottom_frame,
                                          text='Calculate', command=self.convert)
        self.quit_button = tkinter.Button(self.bottom_frame,
                                          text="Exit", command=self.main_window.destroy)

        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')

        self.top_frame.pack(side='left')
        self.bottom_frame.pack(side='left')

        tkinter.mainloop()

    def convert(self):
        kilo = float(self.kilo_entry.get())
        miles = kilo * 0.6214
        tkinter.messagebox.showinfo('Result ', str(kilo) + 'ecvivalent km ' + str(miles) + ' miles')
