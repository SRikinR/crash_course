guests = ["patel","shikhar","shah"]
print("hey u r invited to dinner " + str(guests[0]))        # example 3-4
print("hey u r invited to dinner " + str(guests[1]))
print("hey u r invited to dinner " + str(guests[2]))
print(str(guests[2]) + " would not be able to come! " )     # example 3-5
guests[2]="bonde"
print(guests)
print(" invitation message: ")
print("hey u r invited to dinner " + str(guests[0]))
print("hey u r invited to dinner " + str(guests[1]))
print("hey u r invited to dinner " + str(guests[2]))
guests.insert(0,"advait")                                      #example 3-6
guests.insert(2,"prashant")
guests.append("pavan")
print("                           ")
print("hey u r invited to dinner " + str(guests[0]))
print("hey u r invited to dinner " + str(guests[1]))
print("hey u r invited to dinner " + str(guests[2]))
print("hey u r invited to dinner " + str(guests[-3]))
print("hey u r invited to dinner " + str(guests[-2]))
print("hey u r invited to dinner " + str(guests[-1]))
print("i found a bigger dinner table! so now we all can get dinner together.")
num = (len(guests))
print(f'{num} no. of people are invited')
print("                                            ")
print(" bigger table wont be till the time of dinner.")        #example 3-7
print("                                             ")
popped_guests = guests.pop()
print(popped_guests + " sorry i can't invite you to dinner.")
popped_guests = guests.pop()
print(popped_guests + " sorry i can't invite you to dinner.")
guests.remove("prashant")
print( " prashant sorry i can't invite you to dinner.")
out = "advait"
guests.remove(out)
print( out + " sorry i can't invite you to dinner.")

print("hey u r still invited to dinner " + guests[0])
print("hey u r still invited to dinner " + guests[1])
del guests[0]
del guests[1]
print(guests)
print(len(guests))