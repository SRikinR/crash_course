def greet_users(names):
    for name in names:
        print("Hello, " + name + "!")
usernames= ["hanna","alex","clay"]
greet_users(usernames)


def printed_models(unprinted_design,completed_designs):
    while unprinted_design:
        current_design = unprinted_design.pop()
        print("Currently " + current_design + " is under processes!")
        completed_designs.append(current_design)
def completed_models(completed_designs):
    print("The number of completed designs are: ")
    for designs in completed_designs:
        print(designs)
unprinted_design = ["iphone","samsung","mi","oneplus","google"]
completed_designs = []
print("\ncurrently printing models are follows:")
print(printed_models(unprinted_design,completed_designs))
print("\nhere are the completed designs!")
print(completed_models(completed_designs))


def make_great(magicians,great):
    while magicians:
        current_magician = magicians.pop()
        print("great "+ current_magician)
        great.append(current_magician)
def show_magicians(great):
    for maginian in great:
        print(maginian)
magicians = ["dynamo","karan singh boomer","vijay maliya","harshad metha"]
great=[]
print("\n")
print(show_magicians(magicians))
print("\npresenting! ")
print(make_great(magicians,great))
print("\nfollowing are the magicians! ")
print(show_magicians(great))


def make_pizza(*toppings):
    print(toppings)
print("\ntoppings you requested for your pizza:")
print(make_pizza("a","b","c"))

#def build_profile(first,last, **user_info):
#    profile={}
#    profile["first_name"]=first
#    profile["last_name"]=last
#    for key,value in user_info.items():
#        profile[key]=value
#    return profile
import module
user_profile = module.build_profile("rikin","shah",location = "ahmedabad",passion ="coding",age = '19  ')
print("\nUser Information:")
print(user_profile)

from module import build_profile 
user_profile = module.build_profile("rikin","shah",location = "ahmedabad",passion ="coding",age = '19  ')
print("\n 2) User Information:")
print(user_profile)

import module as rikin
user_profile = rikin.build_profile("rikin","shah",location = "ahmedabad",passion ="coding",age = '19  ')
print("\n 3) User Information:")
print(user_profile)

def make_car(manufacturer,model_name,**car_info):
    car={}
    car["manufacturer"]=manufacturer
    car["model_name"]=model_name
    for info,data in car_info.items():
        car[info]=data
    return car
#import module
cars= make_car("audi","A3",color="black",HSD ="right HSD",country = "India")
print("\ncar information")
print(cars)

