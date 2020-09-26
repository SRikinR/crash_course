words ={"rikin":"legend","list":"bunch of things stored together","turyam":"the 4th one ","if-else":"statement to fulfilll conditions","otherworldly":"diff. universe"}
print("\nMEANINGS:\n")
for name, meaning in words.items():                   #for keys,value in words.items():
    print(name + " means "+ meaning)                  # .keys() & .values()
inlet = input("name??")
if inlet in words.keys():
    print("yo member!")
elif inlet in words.values():
    print("ohhh you entered the meaning ")
else:
    print("loda member baan ne ketli var BC! :)")
for meaning in words.values():
    print(meaning)

rivers ={"delhi":"ganga","egypt":"neil","ahmedabad":"samarbati"}
for river in rivers.values():
    print(river)
for place, river in rivers.items():
    print(river + " runs through " + place)
for place in rivers.keys():
    print(place)
