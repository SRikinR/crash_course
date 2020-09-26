Car = input("which car do you want? ")
print("let me see do we have " + Car)

members = int(input("how many members are there? "))
if members>8:
    print("you have to wait for some time!, table is not avaliable")
else:
    print("welcome!!, table is avaliable. :)")

number = int(input("enter the number "))
if number%10==0:
    print("number is a multiple of  10")
else:
    print("number is not a multiple of  10")

current_num =0
count =5
print(" type 'quit' to stop the response.")
while current_num<count:
    toppings = input("enter the toppings  ")
    #current_num+=1
    if toppings=="quit":
        break
    else:
        print(" we’ll add this topping to their pizza.")
print(" thank you!, you'll soon get your pizza.")

age = int(input("enter your age. "))
while age>3:
    if age<12:
        print("ticket cost is $10")
        break
    else:
        print("ticket cost is $15")
        break
else:
    print("ticket is FREE.")
