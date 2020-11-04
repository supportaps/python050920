import tkinter


class VehicleGui:
    def __init__(self):

        self.main_window = tkinter.Tk()
        self.main_window.geometry("500x300")

        # Frame1 input vehicle name----------------------------------------------------
        self.input_vehicle_name_fr = tkinter.Frame(self.main_window)
        self.input_vehicle_name_lab = tkinter.Label(self.input_vehicle_name_fr,
                                                    text='Input name of vehicle: ')
        self.vehicle_name_var = tkinter.StringVar()
        self.input_vehicle_name_ent = tkinter.Entry(self.input_vehicle_name_fr, width='10')

        self.input_vehicle_name_fr.pack()
        self.input_vehicle_name_lab.pack(side='left')
        self.input_vehicle_name_ent.pack(side='left')

        # Frame2 input vehicle year----------------------------------------------------
        self.input_vehicle_year_fr = tkinter.Frame(self.main_window)
        self.input_vehicle_year_lab = tkinter.Label(self.input_vehicle_year_fr,
                                                    text='Input year of vehicle: ')
        self.vehicle_year_var = tkinter.StringVar()
        self.input_vehicle_year_ent = tkinter.Entry(self.input_vehicle_year_fr, width='10')

        self.input_vehicle_year_fr.pack()
        self.input_vehicle_year_lab.pack(side='left')
        self.input_vehicle_year_ent.pack(side='left')

        # Frame3 input vehicle price----------------------------------------------------
        self.input_vehicle_price_fr = tkinter.Frame(self.main_window)
        self.input_vehicle_price_lab = tkinter.Label(self.input_vehicle_price_fr,
                                                     text='Input price of vehicle: ')
        self.vehicle_price_var = tkinter.StringVar()
        self.input_vehicle_price_ent = tkinter.Entry(self.input_vehicle_price_fr, width='10')

        self.input_vehicle_price_fr.pack()
        self.input_vehicle_price_lab.pack(side='left')
        self.input_vehicle_price_ent.pack(side='left')

        # Frame4 button to send data----------------------------------------------------
        self.vehicle_input_fr = tkinter.Frame(self.main_window)
        self.input_vehicle_button = tkinter.Button(self.vehicle_input_fr,
                                                   text='Insert', command=self.get_input_data_and_choise)
        self.input_vehicle_button.pack(side='left')
        self.vehicle_input_fr.pack()

        # Frame5 radiobuttons to choose appropriate vehicle-----------------------------
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


    def get_input_data_and_choise(self):
        self.vehicle_name_var.set(self.input_vehicle_name_ent.get())
        self.vehicle_year_var.set(self.input_vehicle_year_ent.get())
        self.vehicle_price_var.set(self.input_vehicle_price_ent.get())





