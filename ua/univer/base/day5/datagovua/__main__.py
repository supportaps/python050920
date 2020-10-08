import csv
import json

# def write_to_json_average():

# NAME = "zp-lupen-2019"
# FILENAME = NAME + "csv"
from pip._vendor import chardet


def get_data_from_csv_file(name, encoding_of_file):
    average = 0
    sum = 0

    FILENAME = name + ".csv"
    csvfile = open(FILENAME, "r")
    reader = csv.DictReader(csvfile, delimiter=";")

    with open(name + ".csv", "r", newline="", encoding=encoding_of_file) as file:

        users_from_file = csv.DictReader(file, delimiter=";")
        users_list = list(users_from_file)

        stat_dict = dict()
        for key in users_list[0]:

            if key not in ("Працівник", "Посада", "\ufeffПрацівник"):
                mydict = dict()
                mydict["Average"] = average_by_users(users_list, key)
                mydict["Max"] = min_by_users(users_list, key)
                mydict["Min"] = min_by_users(users_list, key)
                stat_dict[key] = mydict

        print(stat_dict)
        jsonData = json.dumps(stat_dict, ensure_ascii=False)
        print(jsonData)
        with open(name + "stat.json", "w") as file:
            file.write(jsonData)


def print_info(users):
    for user in users:
        for key in user:
            print(key, " - ", user[key])


def average_by_users(users, key_name):
    count = 0
    sum = 0
    for user in users:
        user_string = user[key_name].replace(",", ".").replace("₴", "").replace(" ", "")
        value = float(user_string)
        if value != 0:
            sum += value
            count += 1
    if count != 0:
        return sum / count
    else:
        return 0


def min_by_users(users, key_name):
    # print(key_name)
    is_First = True
    mymin = 0

    for user in users:
        user_string = user[key_name].replace(",", ".").replace("₴", "").replace(" ", "")
        value = float(user_string)
        if is_First == True:
            mymin = value
            is_First = False
        else:
            if value < mymin:
                mymin = value

    return mymin


def max_by_users(users, key_name):
    is_First = True
    mymax = 0
    for user in users:
        user_string = user[key_name].replace(",", ".").replace("₴", "").replace(" ", "")
        value = float(user_string)
        if is_First == True:
            mymax = value
            is_First = False
        else:
            if value > mymax:
                mymax = value

    return mymax


def check_encoding_of_file(name):
    with open(name + ".csv", "rb") as file:
        result = chardet.detect(file.read())
        return result['encoding']


if __name__ == '__main__':

    names = ["zp-kviten-2019", "zp-lupen-2019", "berezen-2019"]
    NAME = "zp-lupen-2019"
    FILENAME = NAME + "csv"
    for name in names:
        encoding_of_file = check_encoding_of_file(name)

        get_data_from_csv_file(name, encoding_of_file)
