class Patient(object):
    status = 'patient'

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.conditions = []

    def get_details(self):
        return f"""{self.name} is a {self.status} at the Chicago General. They're {self.age} years old.
        Current information: {self.conditions}"""


    def add_info(self, information):
        self.conditions.append(information)

patient0 = Patient("Steve", 50)
patient0.add_info("patient treated for ear infection.")

patient1 = Patient("Mary", 45)

print(patient0.get_details())
print(patient1.get_details())

















class Infant(Patient):

    def __init__(self, name, age):
        self.vaccinations = []
        super().__init__(name, age)


    def add_vaccine(self, vaccine):
        self.vaccinations.append(vaccine)

    def get_details(self):
        print(f'''Patient record: {self.name}, {self.age} years old. 
        Patient has had {self.vaccinations} vaccines. 
        Current information: {self.conditions}.
        {self.name} is an infant. has he had all his checks?''')


child = Infant("Harry Potter", 1)
child.add_vaccine('MMR')
print(child.get_details())