import sqlite3

from ua.univer.base.day8.vehicles.amfibia import Amfibia
from ua.univer.base.day8.vehicles.batmobile import BatMobile
from ua.univer.base.day8.vehicles.car import Car
from ua.univer.base.day8.vehicles.cargo import Cargo
from ua.univer.base.day8.vehicles.controller.controller import Controller
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




if __name__ == '__main__':

    controller = Controller()
    controller.get_vars_and_execute()




    # vehicle = Vehicle("An224",1,10000,1000,2000)
    #plane1 = Plane("An24", 1, 10000, 1000, 2000, 40, 9000)
    #plane2 = Plane("An148", 1, 20000, 1200, 2010, 90, 12000)
    #plane3 = Plane("An2", 1, 2000, 900, 1990, 20, 1000)
    #planes = [plane1, plane2, plane3]

    #max_pass_plane = plane1
    #for plane in planes:
        #if max_pass_plane.passenger < plane.passenger:
            #max_pass_plane = plane
    #print("Max Plane: ", max_pass_plane)

    #ship1 = Ship("Assedo", 1, 10000, 1000, 2000, 40, "Odessa", 2323)
    #ship2 = Ship("IllI", 1, 20000, 2000, 2020, 140, "Illichevsk", 2340)
    #ship1.passenger = -10
    #print("Ship: ", ship1)#
    #for plane in planes:
    # print("Plane: ", plane)
    # car1 = Car("Lanos", 2, 4000, 150, 2005)
    #car2 = Car("Tavria", 3, 3000, 120, 1995)
    #batmobile = BatMobile("BatMobile", 2, 4000000, 1500, 2005)
    #vehicles = [plane1, ship1, car1, plane2, plane3, car2, ship2, batmobile]
    #print("*********************** SwimAble")

    #average_price = []
    #max_speed = []

    #for vehicle in vehicles:
        #if isinstance(vehicle, SwimAble):
            #insert_to_db(vehicle)
            #print("Vehicles: ", vehicle)
    #print("*********************** SwimAble")
    # print(count_plane_and_ship(vehicles))
    # print(get_car_with_max_price(vehicles))
    #passenger_list = get_passenger_vehicles(vehicles)
    #for pass_vehicle in passenger_list:
        #print(pass_vehicle)
