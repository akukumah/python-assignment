#4.3 counting to twenty 
number= []
for value in range(1,21):
    print(value)


#making that same list with the  for loop.
for value in range(1,100):
    print(value)
# this outout prints the numbers in its raw stat.

#4.4 now lets try the looping this exact code.
sets=[]  
for value in range(1,1000001):
    sets.append(value)
    print(sets)

#statistics
min(sets)
max(sets)
sum(sets)

##i will use the range() function to generat odd numbers 
odd_numbers= list(range(1,21,1))
print(odd_numbers)                  

#now let put this in a forloop 
odd_numbers= []
for value in range(0,11):
    value= 2*value+1 
    odd_numbers.append(value)
print(odd_numbers)

#multiple of three 
threes= []
for value in range (1,11):
    value= 3*value
    threes.append(value)
print(threes)

##list of ten cubes 
cubes= []
for value in range(1,11):
    value= value**3
    cubes.append(value)
print(cubes)    

#i will now create a list comprehension for the ten cubes 
cubes= [value**3 for value in range(1,11)]
print(cubes)