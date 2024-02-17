#i will write a code that  will tell if an idividual is eligible to vote or not.
#let's begin
users = {'Abish': {'age':16,
                   'electorial_area':'bomso',
                   'sex':'female'},
         'cudjeo': {'age':23,
                    'electorial_area':'bomso',
                    'sex':'male',},          
        }
 
for user,user_info in users.items():
    if user_info['age'] >= 18:
        print(f'Dear {user} are qualify to vote')
    else:
        print(f'Dear {user},kindly register when you are 18')    


#working with the input function.
message = input("Tell me something, and i will repeat it to you: ")
print(message)                

##greetings
name = input("please enter your name: ")
print(f"Hello {name.title()}!") 