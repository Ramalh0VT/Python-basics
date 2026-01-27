# Made this so i can remember some stuff about OOP in python (and to practice)

class Engine:
    def start(self):
        return "Engine is roaring!"

class Car:
    def ignition(self, engine_object):
        status = engine_object.start()
        print(f"Car status: {status}")

my_engine = Engine()
my_car = Car()
my_car.ignition(my_engine)