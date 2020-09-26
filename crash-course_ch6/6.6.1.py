alien_0 = {"color":"green","position":5}
print(alien_0["color"])
print(alien_0["position"])
new_enemy = {}
new_enemy["color"] = "red"
new_enemy["x-position"]=5
new_enemy["y-position"]=25
print(new_enemy["color"])
new_enemy["speed"]="fast"
print(new_enemy)
alien_0["points"]=10
print("your points are +" + str(alien_0["points"]) )
print("original position was " + str(new_enemy["x-position"]))
if new_enemy["speed"]=="slow":
    print("alien is too lazy,you can get an easy kill. ")
    x_increament = 1
elif new_enemy["speed"]=="medium":
    print("quite a tought one!!, thought many had kill this alien")
    x_increament = 2
elif new_enemy["speed"]=="fast":
    print("alien is too fast, FOCUS!")
    x_increament = 3
else:
    print("we can't predict the speed of the alien.")
new_position = new_enemy["x-position"] + (x_increament)
#print("new position i
print("the current position of the alien is: " + str(new_position))

army_color = {"indian":"army marun","american":"light marun","africa":"army red","russia":"army blue"}
print("uniform color of Indian army is: " + army_color["indian"])