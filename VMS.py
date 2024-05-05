                     #Software Requirement Specification#
#Vehicle Management System
class Vehicle:
    # class variable
    total_count = 0
    registration_format = 'XX-1234'

    #here constructor define.
    def __init__(self, make, model, year, mileage):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage
 
    # Instance Methods: 
    def get_make(self):
        print(f"make is :",self.make)

    def get_model(self):
        print(f"model is :" ,self.model)
        

    def get_year(self):
        print(f"year is" ,self.year)

    def update_mileage(self, new_mileage):
        self.mileage = new_mileage

    def calculate_maintenance_cost(self):
        print( 100 + (0.1 * self.mileage))

    def display_info(self):
         print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}, Mileage: {self.mileage}")

    #static method
    @staticmethod
    def validate_registration(registration_number):
        # Validate the registration number format 
        if len(registration_number) == 7 and registration_number[2] == '-':
            print(True)
        else:
             print(False)

    #class method
    @classmethod
    def get_total_count(cls):
        print(cls.total_count)

#child class1
class Car(Vehicle):
    def __init__(self, make, model, year, mileage, fuel_type ,transmission_type):
        super().__init__(make, model, year, mileage)
        self.fuel_type = fuel_type
        self.transmission_type = transmission_type

    def calculate_tax(self):
        if self.fuel_type == "electric":
            print(0)
        elif self.fuel_type == "diesel":
            print(25)
        else:
            print(20)

    def calculate_insurance_premium(self):
        print(1000)

#child class2
class Truck(Vehicle):
    def __init__(self, make, model, year, mileage, load_capacity,fuel_efficiency):
        super().__init__(make, model, year, mileage)
        self.load_capacity = load_capacity
        self.fuel_efficiency = fuel_efficiency


    def calculate_fuel_cost(self):
        if self.fuel_efficiency == "high":
            print(100)
        
    def calculate_depreciation(self):
        if self.year < 1968:
            print(0.15)


#child class3
class Motorcycle(Vehicle):
    def __init__(self, make, model, year, mileage, engine_capacity, fuel_capacity):
        super().__init__(make, model, year, mileage)
        self.engine_capacity = engine_capacity
        self.fuel_capacity = fuel_capacity

    def check_engine_status(self):
        print("Engine is functioning normally")

    def calculate_acceleration(self):
        if self.engine_capacity > 1000:
            print(10)

    


class Bicycle(Vehicle):
    def __init__(self, make, model, year, mileage, frame_material,tire_size):
        super().__init__(make, model, year, mileage)
        self.frame_material = frame_material
        self.tire_size =tire_size


    def check_tire_pressure(self):
        if self.tire_size > 20:
            print("Tire pressure is good")

    def calculate_speed(self):
        if self.tire_size > 20:
            print(10)




#object creating for static class
print("Default registration format:", Vehicle.registration_format)
Vehicle.registration_format = "ABC-123"
print("Total vehicles created so far:", Vehicle.get_total_count())

#objecte creating for base class:
car = Vehicle("Toyota", "Camry", 2020, 20000)
car.display_info()
print("Maintenance cost:", car.calculate_maintenance_cost())




# Creating an object of the Car class
car = Car("Toyota", "Camry", 2020, 20000, "electric", "automatic")

# Access attributes
print("Car Make:", car.get_make())
print("Car Model:", car.get_model())
print("Car Year:", car.get_year())
print("Car Mileage:", car.mileage)
print("Fuel Type:", car.fuel_type)
print("Transmission Type:", car.transmission_type)
print("Tax:", car.calculate_tax())
print("Insurance Premium:", car.calculate_insurance_premium())


# Create an object of the Truck class
truck = Truck("Ford", "F150", 2015, 80000, 2000, "high")

# Access attributes
print("Truck Make:", truck.get_make())
print("Truck Model:", truck.get_model())
print("Truck Year:", truck.get_year())
print("Truck Mileage:", truck.mileage)
print("Truck Load Capacity:", truck.load_capacity)
print("Truck Fuel Efficiency:", truck.fuel_efficiency)

# Calling  methods
truck.calculate_fuel_cost()
truck.calculate_depreciation()


# Creating an object of the Motorcycle class
motorcycle = Motorcycle("Honda", "CBR1000RR", 2021, 5000, 1000, 15)

# Access attributes
print("Motorcycle Make:", motorcycle.get_make())
print("Motorcycle Model:", motorcycle.get_model())
print("Motorcycle Year:", motorcycle.get_year())
print("Motorcycle Mileage:", motorcycle.mileage)
print("Engine Capacity:", motorcycle.engine_capacity)
print("Fuel Capacity:", motorcycle.fuel_capacity)

# Calling  methods
motorcycle.check_engine_status()
motorcycle.calculate_acceleration()


# Creating an object of the Bicycle class
bicycle = Bicycle("Trek", "FX3", 2020, 1000, "Aluminum", 22)

# Access attributes
print("Bicycle Make:", bicycle.get_make())
print("Bicycle Model:", bicycle.get_model())
print("Bicycle Year:", bicycle.get_year())
print("Bicycle Mileage:", bicycle.mileage)
print("Frame Material:", bicycle.frame_material)
print("Tire Size:", bicycle.tire_size)

# Calling  methods
bicycle.check_tire_pressure()
bicycle.calculate_speed()