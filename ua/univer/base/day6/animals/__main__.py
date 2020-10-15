from ua.univer.base.day6.animals.cat import Cat
from ua.univer.base.day6.animals.mouse import Mouse

if __name__ == '__main__':
    cat1 = Cat(name ="Tom",year = 2000,weight = 10)
    #value = int(input("Enter weight of food"))
    #cat1.set_weight(value)
    print("get_weight =",cat1.get_weight())
    print("year",cat1.get_age())
    cat1.show()
    cat2 = Cat("TomLee",13, 17)
    cat2.show()
    cat3 = Cat()
    cat3.show()
    mouse1 = Mouse("Jerry",1)
    mouse1.set_weight(0.1)
    mouse1.show()
    cat1.eat_mouse(mouse1)
    cat1.show()
    mouse1.show()
    cat2.eat_mouse(mouse1)