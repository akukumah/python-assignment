#let's try somenew 
current_number = 0 
while current_number > 10:
    current_number += 1
    print(current_number)
print("Dude your code is wark ")  
##notes.. the code did excute but the while loop was fasel so it printed the last command 

#now let's make it work 
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2: 
        print(current_number)


#let's see if we can loop forever ..i edited it 
x= 1 
while x < 5:
    x += 1
    print(f"\n{x}")

##while looping a pizza toppinng 
prompt = "\nPlease enter your prefered pizza topping" 
prompt+= "\nEnter 'quite' to ebd the request"

message= " "
while message != 'quite':
    message= input(prompt)
    print(message)
print("Thank you for you request")


##movie ticket
prompt = "\nHello, how old are you?"
prompt += "\nType quite to end the program"

age = " "
while age  != 'quite':
    age = input(prompt )
    age= int(age)
    if age < 3:
        print("Your ticket is free,enjoy the movies")
    elif age <= 12:
        print("Your ticket cost $10")
    elif age > 12:
        print("Your ticket cost $15")
              



