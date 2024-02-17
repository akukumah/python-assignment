#working with some certain items in a list  known as slicing
players= ['messi','ronaldo','pique','daniel']

#now i will slice the firs two items
print(players[0:2]) 
print(players[:2])

#now i will slice the last three items 
print(players[-3:])
print(players[1:4])

#now i will loop through the slice 
print("Here are the best players i know:")
for player in players[1:4]:
    print(player.title())

#copying a list 
my_foods= ['fufu','banku','cermovita','eba']
my_friend_food= my_foods[1:2]

print("My favourate foods are;")
print(my_foods)

print("\nMy friends favourate foods are;")
print(my_friend_food)


#4.11 i wiil make a make a list(my_foods) a slice it up

#printing the first three items in the list 
print("The first three foods are;")
print(my_foods[:3])

#printing the first three items in the middle
print("The first two foods in the middle are;")
print(my_foods[1:3])

#4.11making a copy of the  list of pizzas and call it friend_pizzas
my_pizzas= ['margherita','pepperoni','hawaiian','supreme']
friend_pizzas= my_pizzas[:]
print(friend_pizzas)
#i will all a new pizza to the the original list 
my_pizzas.append('chicken')

#a prove that the two list are seoarate 
print(my_pizzas)
print(friend_pizzas)

#print a message using loop 
print("\nMy favourate pizzas are;")
for pizza in my_pizzas:
    print(pizza.title())

print("\nMy friend's favourate pizzas are;")
for pizza in friend_pizzas:
    print(pizza.title())