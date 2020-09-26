dishes = ("roti","sabji","dal","chaval","sweet")
print("\nMenu")
for dish in dishes:
    print(dish)
# dishes(2) = "dal-tadka"           replacing is not allowed in tuple
print("\nNew menu is: ")
dishes = ("butter-roti","sabji","dal-tadka","chaval","sweet")
for dish in dishes:
    print(dish)

