for num in range(1,6):              #exercise 4.2 included
    print(num)
d = list(range(1,6))
print(d)
square = [ value**2 for value in range(0,11)]
print(square)
squares = []
for a in range(0,11):
    value = a**2
    squares.append(value)
print(squares)
sq = []
for b in range(0,11):
    sq.append(b**2)
print(sq)
for on in range(0,20):
    odd = (on%2!=0)
    print(odd)
print(":")
#for million in range(1,1000000):
 #   print(million)
millions = list(range(1,1000001))
#print(millions)
print(min(millions))
print(max(millions))
print(sum(millions))
multi30 = [ value*3 for value in range(1,11)]
print(multi30)
cube = [value**3 for value in range(1,11)]
print(cube)
for value in range(1,11):
    cubes=value**3
    print(cubes)
for odd in range(1,20,2):
    print(odd)
for even in range(0,20,2):
    print(even)