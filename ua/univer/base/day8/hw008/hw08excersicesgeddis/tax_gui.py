import tkinter


class Tax:
    def __init__(self):
            self.main_window = tkinter.Tk()

            self.input_price_frame = tkinter.Frame(self.main_window)
            self.input_price_label = tkinter.Label(self.input_price_frame,
                                                   text='Input prise of property: ')
            self.input_price_entry = tkinter.Entry(self.input_price_frame,width='10')

            self.evaluated_price_frame = tkinter.Frame(self.main_window)
            self.evaluated_price_label = tkinter.Label(self.evaluated_price_frame,
                                                   text='Evaluated prise is: ')
            self.evaluated_price_value = tkinter.StringVar()
            self.evaluated_price_result_label = tkinter.Label(self.evaluated_price_frame,
                                                       textvariable=self.evaluated_price_value)

            self.tax_frame = tkinter.Frame(self.main_window)
            self.tax_label = tkinter.Label(self.tax_frame,
                                                       text='Tax for property is: ')
            self.tax_value = tkinter.StringVar()
            self.tax_result_label = tkinter.Label(self.tax_frame,
                                                              textvariable=self.tax_value)

            self.tax_frame.pack()
            self.tax_label.pack(side='left')
            self.tax_result_label(side='left')

            self.input_price_frame.pack()
            self.input_price_label.pack(side='left')
            self.input_price_entry.pack(side='left')

            self.evaluated_price_frame.pack()
            self.evaluated_price_label.pack(side='left')
            self.evaluated_price_result_label.pack(side='left')

            self.main_window.mainloop()


    def calculate_evaluated_price(self):
        price = float(self.input_price_entry.get())
        evaluated_price = (price/100) * 60
        self.evaluated_price_value.set(evaluated_price)

    def calculate_tax(self):
        pass