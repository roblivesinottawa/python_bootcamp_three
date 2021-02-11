class Patient(object):
    status = 'patient'

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.conditions = []

    def __repr__(self):
        return f"""{self.name} is a {self.status} at the Chicago General. They're {self.age} years old.
        Current information: {self.conditions}"""


    def add_info(self, information):
        self.conditions.append(information)
    
    __str__ = __repr__


patient0 = Patient("Steve", 50)
patient0.add_info("patient treated for ear infection.")

patient1 = Patient("Mary", 45)

print(patient0)
print(patient1)