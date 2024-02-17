#i will create a list of numbers and operate some simple stats on it.
numbers= list(range(1,11))
print(numbers)
max(numbers)
min(numbers)
sum(numbers)

#list comprehension, this allows me to simplify lines of codes in a single line of code.

squares=[]
for value in range(1,11):
    square= value**2
    squares.append(square)
print(squares) 

#now i will try the list comphrensions
squares= [value**2 for value in range(1,11)]
print(squares)