import csv
import json


def show_info(user):
    print("name =", user[0])
    print("age =", user[1])
    print("weight =", user[2])
    print("height =", user[3])


def is_adult(user):
    if user[1]>18:
        return True
    else:
        return False


def is_baby(user):
    if user[1] < 18 and user[1]>0:
        return True
    else:
        return False


def is_fat(user):
    if user[2] > (user[3]-100):
        return True
    else:
        return False


def set_user(user, name, age, weight, height):
    user[0]=name
    if age>0:
        user[1]=age
    else:
        print("Error age")
        user[1] = 0
    user[2]=weight
    user[3]=height


def method_user():
    user = ["Tom", 20, 75, 175]
    print("Adult : ", is_adult(user))
    print("Baby : ", is_baby(user))
    print("Fat : ", is_fat(user))
    set_user(user, name="Bob", age=-1, weight=80, height=180)
    user[1] = -1
    show_info(user)
    print("Adult : ", is_adult(user))
    print("Baby : ", is_baby(user))


def method_write_read_csv_dict():
    FILENAME = "users.csv"
    users = [
        {"name": "Tom", "age": 28},
        {"name": "Alice", "age": 23},
        {"name": "Bob", "age": 34}
    ]
    with open(FILENAME, "w", newline="") as file:
        columns = ["name", "age"]
        writer = csv.DictWriter(file, fieldnames=columns)
        writer.writeheader()

        # запись нескольких строк
        writer.writerows(users)

        user = {"name": "Sam", "age": 41}
        # запись одной строки
        writer.writerow(user)
    with open(FILENAME, "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(row["name"], "-", row["age"])


def method_str_to_dict():
    jsonData = """ {
        "ID"       : 210450,
        "login"    : "admin",
        "name"     : "John Smith",
        "password" : "root",
        "phone"    : 5550505,
        "email"    : "smith@mail.com",
        "online"   : true
    } """
    mydict = json.loads(jsonData)
    print(mydict)

def method_dict_to_str_to_file():
    dictData = {"ID": 210450,
                "login": "admin",
                "name": "John Smith",
                "password": "root",
                "phone": 5550505,
                "email": "smith@mail.com",
                "online": True}
    jsonData = json.dumps(dictData)
    print(jsonData)
    with open("data.json", "w") as file:
        file.write(jsonData)


if __name__ == '__main__':
    with open("user.json", "r") as file:
        str_json=file.read()
    print(str_json)
    mydict = json.loads(str_json)

    for key in mydict:
        print(key, " - ",mydict[key])
    for child in mydict["children"]:
        print(child["firstName"])