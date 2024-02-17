#chaning a list containing cars 
motor_cycles=['honda','suzuki','toyota','benz']

# i will change replace the value of index 1 now 
motor_cycles[1]='civic'
print(motor_cycles[1])

print(motor_cycles)

#adding_item_to_a_list Using the append fumction.
#i will  add high lander to the motor_cycles list i made using the .append fuction, lets try it 
motor_cycles.append('high lander')

#now lets print the list motor_cycles lets see if the high_lander is included
print(motor_cycles)

#the .append function makes it possiblet to add items or values to an empty list,lets try it.
#creat an empty list.
foods=[]

#now i will add items to the empty list.
foods.append('banga')
foods.append('fufu')
foods.append('rice')
foods.append('salad')
foods.append('soup')
print(foods)

#using the del statement to remove items in a list 
print(foods)                                   
del(foods[0])
print(foods)
print(foods)


#the pop allows me to remove the last item on a list, but allows me to still use it.
motor_cycles= ['honda','toyota','suzuki','audi']

#running the pop() on the motor_cycle
pop_motorcycles= motor_cycles.pop()
print(pop_motorcycles)

#i can see that Audi which is the last item on the item is gone but i can still get access to it when i run the pop_motorcycle.
print(motor_cycles)

#i will create a message with the pop()
message= f"The last motor i owned was {pop_motorcycles.title()}, i reall enjoyed it"
print(message)