import sqlite3

from ua.univer.base.day8.vehicles.amfibia import Amfibia
from ua.univer.base.day8.vehicles.batmobile import BatMobile
from ua.univer.base.day8.vehicles.gui.vehiclegui import VehicleGui
from ua.univer.base.day8.vehicles.plane import Plane
from ua.univer.base.day8.vehicles.car import Car
from ua.univer.base.day8.vehicles.ship import Ship


class Controller():
    def __init__(self):
        self.gui = VehicleGui()

    def get_vars_and_execute(self):
        name_var_ins = self.gui.vehicle_name_insert_var.get()
        year_var_ins = int(self.gui.vehicle_year_insert_var.get())
        price_var_ins = float(self.gui.vehicle_price_insert_var.get())
        name_var_upd = self.gui.vehicle_name_update_var.get()
        year_var_upd = int(self.gui.vehicle_year_update_var.get())
        price_var_upd = float(self.gui.vehicle_price_update_var.get())
        if name_var_ins != 'None':
            print("No DATA: ", name_var_ins, year_var_ins, price_var_ins, name_var_upd, year_var_upd, price_var_upd)
            self.check_conditions_ins_query(name_var_ins,year_var_ins, price_var_ins)
        else:
            self.check_conditions_upd_query(name_var_upd, year_var_upd, price_var_upd)


    def check_conditions_ins_query(self, name_var_ins, price_var_ins, year_var_ins):
        rb_var = self.gui.radio_var.get()
        if rb_var == 1:
            amfibia_vehicle = Amfibia(name_var_ins, 1, price_var_ins, 15000, year_var_ins)
            self.insert_to_db(amfibia_vehicle)
        elif rb_var == 2:
            betmobile_vehicle = BatMobile(name_var_ins, 2, price_var_ins, 320, year_var_ins)
            self.insert_to_db(betmobile_vehicle)
        elif rb_var == 3:
            plane_vehicle = Plane(name_var_ins, 1, price_var_ins, 1000, year_var_ins, 125, 12000)
            self.insert_to_db(plane_vehicle)
        elif rb_var == 4:
            car_vehicle = Car(name_var_ins, 2, price_var_ins, 150, year_var_ins)
            self.insert_to_db(car_vehicle)
        elif rb_var == 5:
            ship_vehicle = Ship(name_var_ins, 1, price_var_ins, 1000, year_var_ins, 40, "Odessa", 2323)
            self.insert_to_db(ship_vehicle)


    def check_conditions_upd_query(self, name_var_upd, year_var_upd, price_var_upd):
        rb_var = self.gui.radio_var.get()
        if rb_var == 1:
            amfibia_vehicle = Amfibia(name_var_upd, 1, price_var_upd, 15000, year_var_upd)
            self.update_entry_db(amfibia_vehicle)
        elif rb_var == 2:
            betmobile_vehicle = BatMobile(name_var_upd, 2, price_var_upd, 320, year_var_upd)
            self.update_entry_db(betmobile_vehicle)
        elif rb_var == 3:
            plane_vehicle = Plane(name_var_upd, 1, price_var_upd, 1000, year_var_upd, 125, 12000)
            self.update_entry_db(plane_vehicle)
        elif rb_var == 4:
            car_vehicle = Car(name_var_upd, 2, price_var_upd, 150, year_var_upd)
            self.update_entry_db(car_vehicle)
        elif rb_var == 5 and name_var_upd != 'None':
            ship_vehicle = Ship(name_var_upd, 1, price_var_upd, 1000, year_var_upd, 40, "Odessa", 2323)
            self.update_entry_db(ship_vehicle)

    def insert_to_db(self, vehicle):
        conn_db = sqlite3.connect("vehicles.db")
        cursor = conn_db.cursor()
        sql_insert = f"insert into vehicles(name, year, price) values ('{vehicle.name}','{vehicle.year}','{vehicle.price}')"
        cursor.execute(sql_insert)
        conn_db.commit()
        conn_db.close()

    def update_entry_db(self, vehicle):
        conn_db = sqlite3.connect("vehicles.db")
        cursor = conn_db.cursor()
        sql_update = f"update vehicles set price = '{vehicle.price}', year = '{vehicle.year}' where name = '{vehicle.name}'"
        cursor.execute(sql_update)
        conn_db.commit()
        conn_db.close()
