class cars():
    def __init__(self,name,model,year):
        self.name=name
        self.model=model
        self.year=year
        self.odometer=0
    def get_descriptive_name(self):
        #print( self.year + " " +self.name +" "+ self.model)
        print(" ")
        long_name = (self.year + " " +self.name +" "+ self.model)
        return long_name
    def read_odometer(self):
        print("Car is "+str(self.odometer) + " miles old.")
    def update_odometer(self,milage):
        self.odometer=milage
    def increment_odometer(self,miles):
        self.odometer+=miles

class battery():
    def __init__(self,battery_size=70):
        self.battery_size=battery_size
    def describe_battery(self):
        print("Car has a battery size of " + str(self.battery_size) + "-kwh.")
    def get_range(self):
        if self.battery_size==70:
            range=240
            message = "Car can run approx. run upto " + str(range) 
            message +=  " miles on full charge battery."
            print(message)
        elif self.battery_size==80:
            range=270
            message = "Car can run approx. run upto " + str(range) 
            message +=  " miles on full charge battery."
            print(message)

class electrical_car(cars,battery):
    def __init__(self,name,model,year):
        super().__init__(name,model,year)
        self.battery=battery()
    #def describe_battery(self):
    #    print("Car has a battery size of " + str(self.battery_size) + "-kwh.")
    def fill_gas_tank(self):
        print("This car dosen't need gas!, It runs on battery. ")

tesla = electrical_car("tesla","model_s","2018")
print(tesla.get_descriptive_name())
tesla.battery.describe_battery()
tesla.fill_gas_tank()
tesla.update_odometer(5)    
tesla.increment_odometer(8)
tesla.read_odometer()
tesla.battery.get_range()



class resturants():
    def __init__(self,resturant_name,cusine_type):
        self.resturant_name = resturant_name
        self.cusine_type=cusine_type
        self.num=0 
    def describe_resturant(self):
        print("\nHyy!, welcome to " + self.resturant_name +"\nIt's pleasure to have you.")
    def open_resturant(self):
        print("Resturant is open now!!, we'll be glad to have you.")
#----relation with ex_9-4, below 3 def (methods)----------
    def number_served(self): 
        print("Number of customer served are "+str(self.num) )
    def update_number_served(self,current_serve):
        self.num=current_serve
    def increment_served(self,inc_num):
        self.num+=inc_num
    
class IceCreamStand(resturants):
    def __init__(self,resturant_name,cusine_type):
        super().__init__(resturant_name,cusine_type)
        #self.falavour=[]
    def flavour(self):
        print("ice cream flavours we have!")
        print(falavour)

desert = IceCreamStand("Havmore","Ice-cream")
falavour = ["vanila","chocolate","pista","strawberry"]
desert.describe_resturant()
desert.flavour()


