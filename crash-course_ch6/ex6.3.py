person_info1 = {"first_name":"rikin","last_name":"shah","age":19,"city":"ahmedabad"}
person_info2 = {"first_name":"zakir","last_name":"khan","age":35,"city":"indore"}
person_info3 = {"first_name":"shahrukh","last_name":"khan","age":54,"city":"delhi"}
people = [person_info1,person_info2,person_info3]
print(people)

dog = {
    "kind":"loyal pet",
    "owner":"turyam"
}
monkey = {
    "kind":"naughty",
    "owner":"tony"
}
pets = [dog,monkey]
for animals in pets:
    for char,about in animals.items():
        print("it's " + char + " - " + about )

print("\n$$$$$$$********^^^$$$$")
favourite_places = {
    "rikin":["himachal","sweden"],
    "patel":["greece"],
    "tony":["canada","shimla"]
}
for names, place in favourite_places.items():
    print(names + "'s favourite place is ")
    for destination in place:
        print("\t" + destination)

print("\n$$$$$$$********^^^$$$$")
fav_number = {"rikin":[23,5],"advait":[0,5],"brata":[1,5],"tony":[22],"shah":[11]}
for names, num in fav_number.items():
    print(names + "'s favourite numbers is/are:")
    for fn in num:
        print("\t \t " + str(fn)) 

print("\n$$$$$$$********^^^$$$$")
cities ={
    "ahmedabad":{
        "country":"india",
        "population":"seventy lacs",
        "fact":"histrorical city"},
    "surat":{
        "country":"india",
        "population":"60 lacks",
        "fact":"city of bridges"},
    "anand":{
        "country":"india",
        "population":"25 lacs",
        "fact":"milk hub"}
        }
for city,data in cities.items():
    location = data["country"] + " with a the population of " + data["population"]
    fact = " & the fact about this city is that it's a " + data["fact"]
    print(city + " is located in " + location + fact)