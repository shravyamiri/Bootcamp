class Demo:
    def instance_method(self):
        print("Called instance_method")
        print("self:", self)

    @classmethod
    def class_method(cls):
        print("Called class_method")
        print("cls:", cls)

    @staticmethod
    def static_method():
        print("Called static_method")
        # self or cls would raise an error if used here

# Create an instance
d = Demo()

# Call all methods
d.instance_method()
d.class_method()
d.static_method()
