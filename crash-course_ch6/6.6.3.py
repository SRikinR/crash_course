#very imp....practice once or twice.

alien_0 =[]
alien_1 =[]
alien_2 =[]
alien = [alien_0,alien_1,alien_2]
for new_alien in range(1):
    new_alien={"color":"green","speed":"slow","position":5}
    alien_0.append(new_alien)
    alien_1.append(new_alien)
    alien_2.append(new_alien)
print(alien)
print(" yo buddy \n")
print(alien_0)
#alien_0.append({"babes":"hot"})
#print(alien_0[1])
#alien.append("yoyos")
print(" \n")
print(alien[:2])
#for alienn in alien[:2]:
#    if alienn["color"]=="greeen":
#        alienn["color"]="red"
#        alienn["speed"]="fast"
#        alienn["position"]=8
#print(alien)


print("\n faug begins")
faug = []
for fau in range(30):
    fau = {"color":"greeen","speed":"fast","position":45}   
    faug.append(fau)
print("\n")
print(faug[:3])
print("no. of specification in fau: " + str(len(fau)))
print("total number of faug: " + str(len(faug)))
for fau in faug[:3]:
    fau["color"] = "blue"
    fau["speed"] = "slow"
    fau["position"]="30"
print("\n updates!")
print(faug[:5])
for fau in faug[:5]:
    if fau["color"]=="greeen":
        fau["color"]="red"
print("\n updates!")
print(faug[:5])

print(" $$$$$$_new programe!_$$$$$$")
pizza = {
    "crust":"thick",
    "toppings":["chessy","meaonies","mushroom"]         #what if i need to print only the first two toppings.
}
print("you ordered a "+ pizza["crust"] +"-crust pizza with your demanded topings")
print(pizza["toppings"]) 

print("$$$$$$$____new programming___********")
fav_language = {
    "rikin":["python"],
    "tony":["python","java"],
    "advait":["c++"],
    "ruby":["c+"]
}
for name, languages in fav_language.items():
    print("\n")
    print(name + " fav_language is ")
    for language in languages:
        print("\t " + language + ".")
print("bye!")

print("$$$$$$$____new programming___********")
users = {
    "aeinstein":{
        "last_name":"albert",
        "first_name":"aeinstein",
        "location":"germany"
    },
    "mcurie":{
        "last_name":"marie",
        "first_name":"curie",
        "location":"london"
    }
}
for user_name,info in users.items():
    print(user_name + " your info. stored in our server is: ")
    name = info["first_name"] + " " +  info["last_name"]
    location = info["location"]
    print(name + "  " + location)




