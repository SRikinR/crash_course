players = ["dhoni","yuvi","kholi","chahal","sachin"]            #exercise 4-3 included
for player in players[0:3]:
    print(player.title())
    print(player.title() + ", is a v.good players! \n")
print( "these are the first three players of our team \nand the current team is: ")

my_players = players[:]
print(my_players)

players.append("sawag")

my_players.append("gambhir")

print("                  ")
print(" one players is added: ")
print(players)

print(" \n one my_players is added: ")
print(my_players)

players.insert(3,"rohit")
players.insert(4,"ishan")
players.insert(5,"bhuvi")

my_players.append("dravid")
my_players.append("azhar")
my_players.append("dada")

print("                                 ")          # exercise 
print(" final Members form players are: ")
print(players)
print("\n first 3 members form players are: ")
print(players[:3])
print(" middle 3 members form players are: ")
print(players[3:-3])
print(" last 3 members form players are: ")
print(players[-3:])

print("                              \nfinal Members form my_players are: ")
print(my_players)
print("\n first 3 members form my_players are: ")
print(my_players[:3])
print(" middle 3 members form my_players are: ")
print(my_players[3:-3])
print(" last 3 members form my_players are: ")
print(my_players[-3:])

print("\n\nso,This is our Team and our team formate.")