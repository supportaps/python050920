import tkinter


class VehicleGui:
    def __init__(self):

        self.main_window = tkinter.Tk()
        self.main_window.geometry("500x300")

        self.input_vehicle_name_fr = tkinter.Frame(self.main_window)
        self.input_vehicle_name_lab = tkinter.Label(self.input_vehicle_name_fr,
                                                    text='Input name of vehicle: ')
        self.vehicle_name_var = tkinter.StringVar()
        self.input_vehicle_name_ent = tkinter.Entry(self.input_vehicle_name_fr, width='10')

        self.input_vehicle_year_fr = tkinter.Frame(self.main_window)
        self.input_vehicle_year_lab = tkinter.Label(self.input_vehicle_year_fr,
                                                    text='Input year of vehicle: ')
        self.vehicle_year_var = tkinter.StringVar()
        self.input_vehicle_year_ent = tkinter.Entry(self.input_vehicle_year_fr, width='10')

        self.input_vehicle_price_fr = tkinter.Frame(self.main_window)
        self.input_vehicle_price_lab = tkinter.Label(self.input_vehicle_price_fr,
                                                     text='Input price of vehicle: ')
        self.vehicle_price_var = tkinter.StringVar()
        self.input_vehicle_price_ent = tkinter.Entry(self.input_vehicle_price_fr, width='10')

        self.vehicle_input_fr = tkinter.Frame = tkinter.Button(self.main_window)
        self.input_vehicle_button = tkinter.Button(self.vehicle_input_fr,
                                                   text='Insert', command=self.get_data_for_query)

        self.input_vehicle_name_fr.pack()
        self.input_vehicle_name_lab.pack(side='left')
        self.input_vehicle_name_ent.pack(side='left')

        self.input_vehicle_year_fr.pack()
        self.input_vehicle_year_lab.pack(side='left')
        self.input_vehicle_year_ent.pack(side='left')

        self.input_vehicle_price_fr.pack()
        self.input_vehicle_price_lab.pack(side='left')
        self.input_vehicle_price_ent.pack(side='left')
        self.input_vehicle_button.pack(side='left')
        self.vehicle_input_fr.pack()

        tkinter.mainloop()


    def get_data_for_query(self):
        self.vehicle_name_var.set(self.input_vehicle_name_ent.get())
        self.vehicle_year_var.set(self.input_vehicle_year_ent.get())
        self.vehicle_price_var.set(self.input_vehicle_price_ent.get())




