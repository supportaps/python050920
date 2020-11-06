import sqlite3

from ua.univer.base.day8.vehicles.amfibia import Amfibia
from ua.univer.base.day8.vehicles.batmobile import BatMobile
from ua.univer.base.day8.vehicles.car import Car
from ua.univer.base.day8.vehicles.cargo import Cargo
from ua.univer.base.day8.vehicles.gui.vehiclegui import VehicleGui
from ua.univer.base.day8.vehicles.passenger import Passenger
from ua.univer.base.day8.vehicles.plane import Plane
from ua.univer.base.day8.vehicles.ship import Ship
from ua.univer.base.day8.vehicles.vehicle import Vehicle

# в масиве механизмов получить количество Car и Plane
from ua.univer.base.day8.vehicles.vehicle_able_interface import SwimAble, FlyAble


def count_plane_and_ship(vehicles):
    pass


# получить из масива механизмов Car с наименьшей ценой
def get_car_with_max_price(vehicles):
    pass


# получить из масива механизмов масив пассажирских
def get_passenger_vehicles(vehicles):
    return []


def insert_to_db(vehicle):
    conn_db = sqlite3.connect("vehicles.db")
    cursor = conn_db.cursor()
    sql_insert = f"insert into vehicles(name, year, price) values ('{vehicle.name}','{vehicle.year}','{vehicle.price}')"
    cursor.execute(sql_insert)
    conn_db.commit()
    conn_db.close()

def update_entry_db(vehicle):
    conn_db = sqlite3.connect("vehicles.db")
    cursor = conn_db.cursor()
    sql_update = f"update vehicles set price = '{vehicle.price}', year = '{vehicle.year}' where name = '{vehicle.name}'"
    cursor.execute(sql_update)
    conn_db.commit()
    conn_db.close()

if __name__ == '__main__':
    gui = VehicleGui()

    name_var_ins = gui.vehicle_name_insert_var.get()
    year_var_ins = int(gui.vehicle_year_insert_var.get())
    price_var_ins = float(gui.vehicle_price_insert_var.get())
    name_var_upd = gui.vehicle_name_update_var.get()
    year_var_upd = int(gui.vehicle_year_update_var.get())
    price_var_upd = float(gui.vehicle_price_update_var.get())
    print("No DATA: ",name_var_ins, year_var_ins, price_var_ins, name_var_upd, year_var_upd, price_var_upd)
    rb_var = gui.radio_var.get()
    if rb_var == 1 and name_var_ins != 'None':
        amfibia_vehicle = Amfibia(name_var_ins, 1, price_var_ins, 15000, year_var_ins)
        insert_to_db(amfibia_vehicle)
    elif rb_var == 1 and name_var_upd != 'None':
        amfibia_vehicle = Amfibia(name_var_upd, 1, price_var_upd, 15000, year_var_upd)
        update_entry_db(amfibia_vehicle)
    elif rb_var == 2  and name_var_ins != 'None':
        betmobile_vehicle = BatMobile(name_var_ins, 2, price_var_ins, 320, year_var_ins)
        insert_to_db(betmobile_vehicle)
    elif rb_var == 2 and name_var_upd != 'None':
        betmobile_vehicle = BatMobile(name_var_upd, 2, price_var_upd, 320, year_var_upd)
        update_entry_db(betmobile_vehicle)
    elif rb_var == 3 and name_var_ins != 'None':
        plane_vehicle = Plane(name_var_ins, 1, price_var_ins, 1000, year_var_ins, 125, 12000)
        insert_to_db(plane_vehicle)
    elif rb_var == 3 and name_var_upd != 'None':
        plane_vehicle = Plane(name_var_upd, 1, price_var_upd, 1000, year_var_upd, 125, 12000)
        update_entry_db(plane_vehicle)
    elif rb_var == 4 and name_var_ins != 'None':
        car_vehicle = Car(name_var_ins, 2, price_var_ins, 150, year_var_ins)
        insert_to_db(car_vehicle)
    elif rb_var == 4 and name_var_upd != 'None':
        car_vehicle = Car(name_var_upd, 2, price_var_upd, 150, year_var_upd)
        update_entry_db(car_vehicle)
    elif rb_var == 5 and name_var_ins != 'None':
        ship_vehicle = Ship(name_var_ins, 1, price_var_ins, 1000, year_var_ins, 40, "Odessa", 2323)
        insert_to_db(ship_vehicle)
    elif rb_var == 5 and name_var_upd != 'None':
        ship_vehicle = Ship(name_var_upd, 1, price_var_upd, 1000, year_var_upd, 40, "Odessa", 2323)
        update_entry_db(ship_vehicle)




    # vehicle = Vehicle("An224",1,10000,1000,2000)
    plane1 = Plane("An24", 1, 10000, 1000, 2000, 40, 9000)
    plane2 = Plane("An148", 1, 20000, 1200, 2010, 90, 12000)
    plane3 = Plane("An2", 1, 2000, 900, 1990, 20, 1000)
    planes = [plane1, plane2, plane3]

    max_pass_plane = plane1
    for plane in planes:
        if max_pass_plane.passenger < plane.passenger:
            max_pass_plane = plane
    print("Max Plane: ", max_pass_plane)

    ship1 = Ship("Assedo", 1, 10000, 1000, 2000, 40, "Odessa", 2323)
    ship2 = Ship("IllI", 1, 20000, 2000, 2020, 140, "Illichevsk", 2340)
    ship1.passenger = -10
    print("Ship: ", ship1)
    for plane in planes:
        print("Plane: ", plane)
    car1 = Car("Lanos", 2, 4000, 150, 2005)
    car2 = Car("Tavria", 3, 3000, 120, 1995)
    batmobile = BatMobile("BatMobile", 2, 4000000, 1500, 2005)
    vehicles = [plane1, ship1, car1, plane2, plane3, car2, ship2, batmobile]
    print("*********************** SwimAble")

    average_price = []
    max_speed = []

    for vehicle in vehicles:
        if isinstance(vehicle, SwimAble):
            insert_to_db(vehicle)
            print("Vehicles: ", vehicle)
    print("*********************** SwimAble")
    # print(count_plane_and_ship(vehicles))
    # print(get_car_with_max_price(vehicles))
    passenger_list = get_passenger_vehicles(vehicles)
    for pass_vehicle in passenger_list:
        print(pass_vehicle)
