motorcycle = ["honda","pulser","royal e."]
print(motorcycle)
motorcycle[1] = "hero"      #replacing elements in the list.
print(motorcycle[1])
motorcycle[0] ="suzuki"
print(motorcycle[0])
motorcycle.append("honda")      #adding elements in the list.
motorcycle.append("bajaj pulser")
print(motorcycle)
motorcycle.insert(0,"maruti suzuki") #insert element in the list

print("0" + str(motorcycle))
popped_motorcycle = motorcycle.pop() #using pop() command.
print("1" + str(motorcycle))
print("2" + str(popped_motorcycle))
del motorcycle[3]               #deleting element in the list.
del motorcycle[1]
print(motorcycle)
motorcycle.remove("honda")      #remove commmand.
motorcycle[1] = "hero honda"
old = "hero honda"
motorcycle.remove(old)      #remove command using diff. method.
motorcycle.append("hundia")
print("3" + str(motorcycle))
print( old + " is too simple i choose maruti suzuki or hundia")