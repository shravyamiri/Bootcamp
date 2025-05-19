import yaml

class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

car = Car("Toyota", "Corolla")
with open("car.yaml", "w") as f:
    yaml.dump(car.__dict__, f)