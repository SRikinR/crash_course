def make_car(manufacturer,model_name,**car_info):
    car={}
    car["manufacturer"]=manufacturer
    car["model_name"]=model_name
    for info,data in car_info.items():
        car[info]=data
    return car

def build_profile(first,last, **user_info):
    profile={}
    profile["first_name"]=first
    profile["last_name"]=last
    for key,value in user_info.items():
        profile[key]=value
    return profile