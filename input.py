#working with the input function.
message = input("Tell me something, and i will repeat it to you: ")
print(message)     

age = input('How old are you?' )
age 


#i will write a program that will tell if a person is tall enough to ride on a roller coster

height= input('Kindly enter your height here:')
height= int(height)
if height >= 48:
    print('You are tall enough to ride!')
else:
    print('Sorry  you will be able to ride when you are a little older.')    


#i will create a program that will reques a user to type in a nummber, it would tell if the number provided is even or odd
#let's try it 
number= input("Please enter a number and i wll tell you if it's even or odd: ")
number= int(number)

#now my bolean stateemt will be right here 
if number % 2 == 0:
    print(f"The number {number} is even.")
else:
    print(f"\nThe number {number} is odd.")    


#lets write a program that predicts if a number input is a mlutiple of 10 or not 
number = input('Please enter a number here: ')
number = int(number)
if number == number ** 10:
    print(f"The number {number} is a multiple of 10") 
else:
    print(f"The number {number} is not a multiple of 10")

##let's try this in the temple, the input function seems not to work in the editor 
