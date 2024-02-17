#this code will keep counting as long as some conditions are true 
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1


prompt= "\nTell me something and i will repeat it to you."
prompt += "\nEnter 'quite' to end the program, "
message= " "
while message != 'quite':
    message= input(prompt)
    print(message)   


#let's try somenew 
current_number = 0 
while current_number > 10:
    current_number += 1
    print(current_number)