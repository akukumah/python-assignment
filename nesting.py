#i will create dictionaries of aliens and nest them 
alien_0= {'color':'green','points':5}
alien_1= {'color':'green','points':10}
alien_2= {'color':'yellow','points':20}

#now  will nest it and assing it a variable 
aliens= [alien_0,alien_1,alien_2]
for alien in aliens:
    print(alien) 



#auto generating 30 aliens 
#first i will create an empty list 
aliens= []

#now i wll use the loop to auto the generatinng process 
for alien_number in range(30):
    new_alien= {'color':'green','points':5, 'speed':'medium'}
    aliens.append(new_alien)

#now i will print the first 5 aliens
for alien in aliens[:5]:
    print(f"\n{alien}")

#now let me print the total number of aliens i have now , i will use the len() function 
print(f"The total number of alien is {len(aliens)}")    

#now i want  to change the firs 3 aliens properties to yellow color, speed- meduim,and give it 10 points 
#i will do this is the loop and if statement 
for alien in aliens:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10        

#now i will show the first alien to see if the code worked
for alien in aliens[:5]:
    print(alien)
##woow is work'
print('i did it!')     
print("...")


#pizza
#i will store information about an order 
pizza= {'crust':'thick',
        'toppings':['mushroosm','extra cheese']
        }

#now i will summurise the  order
print(f"You ordered a {pizza['crust']} pizza with the folling toppings:")
for topping in pizza:
    print(f"\t{topping}")


##favorite language 
favorite_language= {'jen':['python','rust'],
                    'sarah':['c'],
                    'edward':['rust','html'],
                    'phil':['python','haskell'],
                    }

#now i will print out messages to the individuals with the loop 
for name, languages in favorite_language.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language}")


#now i want to print the same messages to the individuals but this time around i want to condition it on the number of languages they chose
for name , languages in favorite_language.items():
    for language in languages:
        if len(languages) > 1:
            print(f"\n{name.title()}'s favorite languages are:")
            print(f"\t{languages}")
        else:
            print(f"{name.title()}'s favorite language is {language}")   



#dictionary in dictionary 
users= { 'aeinstein':{'first':'albert',
                     'last':'einstein',
                     'location':'princeton',
                    },
         'mcurie': {'first':'marie',
                    'last':'curie',
                    'location':'paris',
                    }                      
        }

#for i will loop through and print the user _info
for username ,user_info in users.items():
    print(f"\n{username}")
    full_name= f"{user_info['first']}{user_info['last']}"
    location= f"{user_info['location']}"
    print(f'{full_name}')
    print(f'{location}')


#data base for some people , i will store the infomation in a dictonary 
persons= { 'user_0':{'first':'rose',
                     'last':'akukumah',
                     'city':'accra',
                     'age': 56,
                    },
            'user_1':{'first':'emma',
                      'last':'cudjeo',
                      'city':'takoradi',
                      'age':23,
                     },
            'user_2':{'first':'richard',
                      'last':'osei',
                      'city':'kumasi',
                      'age':58,
                     },
         }                     

#now i will print their details 

for user,user_info in persons.items():
    print(f"\n{user}")
    full_name= f"{user_info['first']} {user_info['last']}"
    location= f"{user_info['city']}"
    age= f"{user_info['age']}"
    print(f'{full_name}')
    print(f'\t{location}')
    print(f'\t{age}')





    
