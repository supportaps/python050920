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

        rb_del = self.gui.radio_var_del.get()
        rb_csv = self.gui.radio_var_csv.get()

        if name_var_ins != 'None':
            print("No DATA: ", name_var_ins, year_var_ins, price_var_ins, name_var_upd, year_var_upd, price_var_upd)
            self.check_conditions_ins_query(name_var_ins, year_var_ins, price_var_ins)
        elif name_var_upd != 'None':
            self.check_conditions_upd_query(name_var_upd, year_var_upd, price_var_upd)
        elif rb_del != 0:
            self.delete_by_vehicle_type()
        elif rb_csv != 0:
            self.get_data_from_db_by_vehicle_type()

    def get_data_from_db_by_vehicle_type(self):
        rb_var = self.gui.radio_var.get()
        if rb_var == 1:
            self.get_data_from_db_list('Amfibia')
        if rb_var == 2:
            self.get_data_from_db_list('BatMobile')
        if rb_var == 3:
            self.get_data_from_db_list('Plane')
        if rb_var == 4:
            self.get_data_from_db_list('Car')
        if rb_var == 5:
            self.get_data_from_db_list('Ship')

    def delete_by_vehicle_type(self):
        rb_var = self.gui.radio_var.get()
        if rb_var == 1:
            self.delete_from_db('Amfibia')
        if rb_var == 2:
            self.delete_from_db('BatMobile')
        if rb_var == 3:
            self.delete_from_db('Plane')
        if rb_var == 4:
            self.delete_from_db('Car')
        if rb_var == 5:
            self.delete_from_db('Ship')

    def check_conditions_ins_query(self, name_var_ins, price_var_ins, year_var_ins):
        rb_var = self.gui.radio_var.get()
        if rb_var == 1:
            amfibia_vehicle = Amfibia(name_var_ins, 1, year_var_ins, 15000, price_var_ins)
            self.insert_to_db(amfibia_vehicle)
        elif rb_var == 2:
            betmobile_vehicle = BatMobile(name_var_ins, 2, year_var_ins, 320, price_var_ins)
            self.insert_to_db(betmobile_vehicle)
        elif rb_var == 3:
            plane_vehicle = Plane(name_var_ins, 1, year_var_ins, 1000, price_var_ins, 125, 12000)
            self.insert_to_db(plane_vehicle)
        elif rb_var == 4:
            car_vehicle = Car(name_var_ins, 2, year_var_ins, 150, price_var_ins)
            self.insert_to_db(car_vehicle)
        elif rb_var == 5:
            ship_vehicle = Ship(name_var_ins, 1, year_var_ins, 1000, price_var_ins, 40, "Odessa", 2323)
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



    def database_connection(self):
        conn_db = sqlite3.connect("vehicles.db")
        cursor = conn_db.cursor()
        return conn_db, cursor

    def close_database_connection(self, conn_db):
        conn_db.commit()
        conn_db.close()

    def insert_to_db(self, vehicle):
        conn_db, cursor = self.database_connection()
        vehicle_type = vehicle.__class__.__name__
        sql_insert = f"insert into vehicles(name, year, price, vehicleType) values ('{vehicle.name}','{vehicle.year}','{vehicle.price}','{vehicle_type}')"
        cursor.execute(sql_insert)
        self.close_database_connection(conn_db)

    def update_entry_db(self, vehicle):
        conn_db, cursor = self.database_connection()
        sql_update = f"update vehicles set price = '{vehicle.price}', year = '{vehicle.year}' where name = '{vehicle.name}'"
        cursor.execute(sql_update)
        self.close_database_connection(conn_db)

    def delete_from_db(self, vehicle_type):
        conn_db, cursor = self.database_connection()
        sql_delete = f"delete from vehicles where vehicleType = '{vehicle_type}'"
        cursor.execute(sql_delete)
        self.close_database_connection(conn_db)

    def get_data_from_db_list(self, vehicle_type):

        conn_db, cursor = self.database_connection()
        sql_select = f"select * from vehicles where vehicleType = '{vehicle_type}'"
        cursor.execute(sql_select)
        result_set = cursor.fetchall()
        print("result: ",result_set)
        db_data_list = []
        for row in result_set:
            name_db = row[0]
            year_db = row[1]
            price_db = row[2]
            type_v_db = row[3]
            db_data_list.append(name_db)
            db_data_list.append(year_db)
            db_data_list.append(price_db)
            db_data_list.append(type_v_db)

            self.close_database_connection(conn_db)

            return db_data_list
        print("Database list: ", db_data_list)
