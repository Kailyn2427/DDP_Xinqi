# class definition
class people:
    # Defining Basic Properties
    name = ''
    age = 0
    # Define private properties, which cannot be accessed directly from outside the class.
    __weight = 0

    # Define constructor methods
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print("%s say: i am %d years old." % (self.name, self.age))


# Instantiate the class
p = people('Huawei', 10, 30)
p.speak()