def greet_users(username):
    print("hello " + username.title() + "!")
#greet_users("shah")

def display_message():
    print("I'm learning about functions.")
#display_message()
#greet_users("shah")

def favourite_book(book):
    print("one of my favourite book is: "+ book.title())
greet_users("shah")
display_message()   
favourite_book("lucy")

def describe_pet(animal_type,pet_name):
    print("I have a " + animal_type.title())
    print("My " + animal_type.title() +" name is " + pet_name.title())
print("\n")
describe_pet("dog","muku")
describe_pet("cat","schinzo")

#def make_tshirt(size,print_message):
def make_tshirt(print_message,size="large"):
    print("Size of your T-shirt is: " + size)
    print("Message to be printed on your T-Shirt will be: " + print_message.title())
print("\n")
make_tshirt("small","i'm the best")
make_tshirt(size="medium",print_message="yo bidu")
make_tshirt("i love python language")

def describe_city(city,country="India"):
    print(city.title() + " is in " + country)
print("\n")
describe_city("ahmedabad")
describe_city("mumbai")
describe_city("delhi")
describe_city("london","uk")


def get_formatedname(first_name,last_name=" ",middle_name=" "):
    if middle_name:
        full_name = first_name + " " +middle_name+ " " + last_name
        return full_name.title()
    else:
        full_name = first_name+" "+ last_name
        return full_name.title()
print("\n" + get_formatedname("rikin","shah"))


def get_name(first,last,age=" "):
    name = {"first":first,"last":last}
    if age:
        name["age"]=age
    return name
print("\n")
print(get_name("rikin","shah","19"))


while False:
    print("\nenter 'q' to quit")
    print("\t\tplease enter your name ")
    f_name = input("enter your first name ")
    if f_name=="q":
        break
    l_name = input("enter your last name ")
    if l_name=="q":
        print("Hello!," + get_formatedname(f_name))
        break
    full_naam = get_formatedname(f_name,l_name)
    print("Hello!, " + full_naam)



def city_country(city,country):
    full_info = '"' + city + "," + country + '"'
    return full_info.title()
current_count = 0
count = 3
while current_count<count:
    current_count+=1
    #print("\nEnter 'q' to quit at any point of time")
    print("\n\t\tEnter the city & it's respective country name")
    ci=input("city name? ")
    co=input("city's country name? ")
    print(city_country(ci,co))



def make_album(artist,album_title):
    album = {
        "artist":artist.title(),
        "album_title":album_title.title()
    }
    return album
print(make_album("arijit","channa mereya"))
print(make_album("sonu nigam","kal hoo na hoo!"))
print(make_album("shreya","sun raha hai"))

current_attempt = 0
total_attempt=3
while current_attempt<total_attempt:
    current_attempt+=1
    artist_song = input("artist? ")
    title = input("album title? ")
    if artist_song == "q":
        break
    if title=="q":
        print(artist_song + ",user dosen't know the name of the song!")
        break
    print(make_album(artist_song,title))
