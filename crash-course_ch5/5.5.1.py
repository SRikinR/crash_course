cars = ["audi","bmw","honda","mercedies","farari"]
for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())
print("above are the list of cars!")

car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

alein_color = input("color?")
if alein_color=="green":
    print("you earned 5 coins.")
elif alein_color=="red":
    print("you earned 10 points.")
else:
    print("you earned 15 points")

age = int(input("age? "))
if age<2:
    print("person is a baby!")
elif age<4 or age==2:
    print("person is a toddler!")
elif age==4 or age<13:
    print("person is a kid!")
elif age==13 or age<20:
    print("person is a teenager!")
elif age==20 or age<65:
    print("person is a adult!")
else:
    print("person ia an elder!")