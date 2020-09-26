unverified = ["rikin","al","brata"]
verified = []
while unverified:
    current_user = unverified.pop()
    print("verifing_user: " + current_user) 
    verified.append(current_user)
print("verified users:\t" + str(verified))

pets = ["dog","cat","monkey","cat","tortoies","cat"]
while "cat" in pets:
    pets.remove("cat")
print(pets)


responses = {}
polling_test = False
while polling_test:
    name = input("enter your name! ")
    response = input("which mountain would you like to climb? ")
    responses[name] = response
    repeat_response = input("would you like others to enter the response?(yes/no) ")
    if repeat_response == "no":
        polling_test =False
    for name,response in responses.items():
        print(name + " would you like to climb " + response)
else:
    print(" response stoped! ")
#for name,response in responses.items():
#    print(name + " would you like to climb " + response)

                    #exercise begins.

sandwich_orders = ["cheese sandwich","vegetable sandwich","america sandwich","crust sandwich","Pastrami sandwich"]
finished_sandwich = []
while sandwich_orders:
    if "Pastrami sandwich" in sandwich_orders:
        print(" we have run out of pastrami ")
        sandwich_orders.remove("Pastrami sandwich")
    current_order = sandwich_orders.pop()
    print("I made your " + current_order)
    finished_sandwich.append(current_order)
print("Total sandwich made are ")
print(finished_sandwich)


inlet = {}
poll = True
while poll:
    name = input("enter your name ")
    place = input("enter the place you'ld like to visit in this world ")
    inlet[name]=place
    allow = input("yes/no ")
    if allow=="no":
        poll=False
for name,places in inlet.items():
    print(name + " would like to go " + places)