import yaml

class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

with open("car.yaml", "r") as f:
    data = yaml.safe_load(f)
    car = Car(**data)
    print(car.__dict__)