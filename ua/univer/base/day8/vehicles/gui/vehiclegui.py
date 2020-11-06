import tkinter


class VehicleGui:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.geometry("500x300")

        # Frame1 input vehicle name----------------------------------------------------
        self.input_vehicle_name_fr = tkinter.Frame(self.main_window)
        self.input_vehicle_name_lab = tkinter.Label(self.input_vehicle_name_fr,
                                                    text='Input name of vehicle: ')
        self.vehicle_name_insert_var = tkinter.StringVar()
        self.vehicle_name_insert_var.set(None)
        self.vehicle_name_update_var = tkinter.StringVar()
        self.vehicle_name_update_var.set(None)
        self.vehicle_name_delete_var = tkinter.StringVar()
        self.vehicle_name_delete_var.set(None)
        self.input_vehicle_name_ent = tkinter.Entry(self.input_vehicle_name_fr, width='10')

        self.input_vehicle_name_fr.pack()
        self.input_vehicle_name_lab.pack(side='left')
        self.input_vehicle_name_ent.pack(side='left')

        # Frame2 input vehicle year----------------------------------------------------
        self.input_vehicle_year_fr = tkinter.Frame(self.main_window)
        self.input_vehicle_year_lab = tkinter.Label(self.input_vehicle_year_fr,
                                                    text='Input year of vehicle: ')
        self.vehicle_year_insert_var = tkinter.StringVar()
        self.vehicle_year_insert_var.set(0)
        self.vehicle_year_update_var = tkinter.StringVar()
        self.vehicle_year_update_var.set(0)
        self.input_vehicle_year_ent = tkinter.Entry(self.input_vehicle_year_fr, width='10')

        self.input_vehicle_year_fr.pack()
        self.input_vehicle_year_lab.pack(side='left')
        self.input_vehicle_year_ent.pack(side='left')

        # Frame3 input vehicle price----------------------------------------------------
        self.input_vehicle_price_fr = tkinter.Frame(self.main_window)
        self.input_vehicle_price_lab = tkinter.Label(self.input_vehicle_price_fr,
                                                     text='Input price of vehicle: ')
        self.vehicle_price_insert_var = tkinter.StringVar()
        self.vehicle_price_insert_var.set(0)
        self.vehicle_price_update_var = tkinter.StringVar()
        self.vehicle_price_update_var.set(0)
        self.input_vehicle_price_ent = tkinter.Entry(self.input_vehicle_price_fr, width='10')

        self.input_vehicle_price_fr.pack()
        self.input_vehicle_price_lab.pack(side='left')
        self.input_vehicle_price_ent.pack(side='left')

        # Frame4 button to insert data----------------------------------------------------
        self.vehicle_insert_fr = tkinter.Frame(self.main_window)
        self.insert_vehicle_lab = tkinter.Label(self.vehicle_insert_fr,
                                                     text='Insert data to database: ')
        self.insert_vehicle_but = tkinter.Button(self.vehicle_insert_fr,
                                                 text='Insert', command=self.get_input_data_for_insert)
        self.vehicle_insert_fr.pack()
        self.insert_vehicle_lab.pack(side='left')
        self.insert_vehicle_but.pack(side='left')
        # Frame5 button to update------------------------------------------------------------
        self.vehicle_update_fr = tkinter.Frame(self.main_window)
        self.update_vehicle_lab = tkinter.Label(self.vehicle_update_fr,
                                                text='Update data in database: ')
        self.update_vehicle_but = tkinter.Button(self.vehicle_update_fr,
                                                 text='Update', command=self.get_input_data_for_update)
        self.vehicle_update_fr.pack()
        self.update_vehicle_lab.pack(side='left')
        self.update_vehicle_but.pack(side='left')

        # Frame6 button to delete------------------------------------------------------------
        self.vehicle_delete_fr = tkinter.Frame(self.main_window)
        self.delete_vehicle_lab = tkinter.Label(self.vehicle_update_fr,
                                                text='Delete data from database: ')
        self.delete_vehicle_but = tkinter.Button(self.vehicle_update_fr,
                                                 text='Delete', command=self.get_name_to_delete)
        self.vehicle_delete_fr.pack()
        self.delete_vehicle_lab.pack(side='left')
        self.delete_vehicle_but.pack(side='left')

        # Frame7 radiobuttons to choose appropriate vehicle-----------------------------
        self.vehicle_radiobutton_fr = tkinter.Frame(self.main_window)

        self.radio_var = tkinter.IntVar()
        self.radio_var.set(1)

        self.rb1 = tkinter.Radiobutton(self.vehicle_radiobutton_fr, text='Amfibia',
                                       variable=self.radio_var, value=1)
        self.rb2 = tkinter.Radiobutton(self.vehicle_radiobutton_fr, text='Batmobile',
                                       variable=self.radio_var, value=2)
        self.rb3 = tkinter.Radiobutton(self.vehicle_radiobutton_fr, text='Plane',
                                       variable=self.radio_var, value=3)
        self.rb4 = tkinter.Radiobutton(self.vehicle_radiobutton_fr, text='Car',
                                       variable=self.radio_var, value=4)
        self.rb5 = tkinter.Radiobutton(self.vehicle_radiobutton_fr, text='Ship',
                                       variable=self.radio_var, value=5)

        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()
        self.rb4.pack()
        self.rb5.pack()
        self.vehicle_radiobutton_fr.pack()

        tkinter.mainloop()

    def get_input_data_for_insert(self):
        self.vehicle_name_insert_var.set(self.input_vehicle_name_ent.get())
        self.vehicle_year_insert_var.set(self.input_vehicle_year_ent.get())
        self.vehicle_price_insert_var.set(self.input_vehicle_price_ent.get())

    def get_input_data_for_update(self):
        self.vehicle_name_update_var.set(self.input_vehicle_name_ent.get())
        self.vehicle_year_update_var.set(self.input_vehicle_year_ent.get())
        self.vehicle_price_update_var.set(self.input_vehicle_price_ent.get())

    def get_name_to_delete(self):
        self.vehicle_name_delete_var.set(self.input_vehicle_name_ent.get())