class dog():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def sit(self):
        print(self.name.title() + " is now sitting.")
    def roll_over(self):
        print(self.name + " is rolling over.")
my_pet = dog("chat","2 months")
print("\nMy pet's name is " +  my_pet.name + ".")
print("My pet's age is " + my_pet.age + ".")
my_pet.sit()
my_pet.roll_over()

your_pet = dog("steve","3 years")
print("\nYour pet's name is "+ your_pet.name + ".")
print("Your pet's age is "+ your_pet.age + ".")
your_pet.sit()
your_pet.roll_over()


class resturants():
    def __init__(self,resturant_name,cusine_type):
        self.resturant_name = resturant_name
        self.cusine_type=cusine_type
        self.num=0 #relation with line 31
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
#------------------------------------------------
resturant1 = resturants("HAYAT","punjabi")
resturant1.describe_resturant()
resturant1.open_resturant()
#--------------- 9-4, below 3 lines----------------
resturant1.update_number_served(3)
resturant1.increment_served(2)
resturant1.number_served()
#---------------------------------------------------
resturant2 = resturants("SU BOLU","casual")
resturant2.describe_resturant()
resturant2.open_resturant()
#--------------- 9-4, below 3 lines-----------------
resturant2.update_number_served(30)
resturant2.increment_served(2)
resturant2.number_served()
#----------------------------------------------------


class user():
    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name
        self.logins=0
    def describe_user(self,age,location):
        print("\n"+ self.first_name + " " + self.last_name + " is "+ age +" years old and stays in " + location +".")
    def greet_user(self):
        print("Hi "+self.first_name + ", Have a good day Ahead!!")
#--------------- 9-5, below 4 methods-----------------------------------------------------------
    def login_attempt(self):
        print("login attempts = "+ str(self.logins))
    def update_login(self,updated_login_count):
        self.logins = updated_login_count
    def increment_logins(self):
        self.logins+=1
        if self.logins>3:
            print("sorry no more logins...you have reached your logins limit.")   
    def reset_login(self):
        self.logins=0
#--------------------------------------------------------------------------------------------------
user1 = user("Rikin","Shah")
user1.describe_user("19","Ahmedabad,India")
user1.greet_user()
#--------------- 9-5, below lines-----------------------------------------------------------
user1.increment_logins()
user1.login_attempt()
user1.update_login(3)
print("login attempt updates: ")
user1.login_attempt()
user1.increment_logins()
user1.reset_login()
print("reseted login attempt to zero")
user1.login_attempt()
 #--------------------------------------------------------------------------------------------

user2 =user("shahrukh","khan")
user2.describe_user("55","Mumbai,India")
user2.greet_user()
#--------------- 9-5, below lines-----------------------------------------------------------
user2.increment_logins()
user2.login_attempt()
user2.update_login(2)
print("login attempt updates: ")
user2.login_attempt()
user2.increment_logins()
user2.reset_login()
print("reseted login attempt to zero")
user2.login_attempt()
 #--------------------------------------------------------------------------------------------



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
new_car = cars("Audi","A3","2019")
print(new_car.get_descriptive_name())
new_car.odometer=23
new_car.read_odometer()

new_car2=cars("BMW","Q2","2020")
print(new_car2.get_descriptive_name())
new_car2.update_odometer(52)
new_car2.read_odometer()

new_car3=cars("Ford","Peak","2020")
print(new_car3.get_descriptive_name())
new_car3.update_odometer(30)
new_car3.increment_odometer(5)
new_car3.read_odometer()
