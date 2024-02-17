# the dictionary stores information about a particular variable 
alien_0= {'color': 'green', 'points':5}
#now i will access infomation in the dictionaries 
print(alien_0['color'])
print(alien_0['points'])

#manipulations in dictionaries 
#adding new keys pairs to my dictionary 
alien_0['x_position']= 0
alien_0['y_position']= 25 
alien_0['speed']= 'meduim'

#now i will print my dictionary to see if it is updated 
print(alien_0)

#now i will write a program that will move the alien to the rigth depending on its speed 

#i wiil print the current position of the alien on the rigth 
print(f" original position: {alien_0['x_position']}")

#lets get to business
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'meduim':
    x_increment = 2
# else this alien must be really fast 
else:
    x_increment = 3

#now this should tell me the alien's current x_position
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(alien_0['x_position'])    


#person_dictionary 
person= {'first_name':'emma',
         'last_name':'cudjeo',
         'age':23,
         'city':'daboase',
        }

#printimg each key 
print(person['age'])
print(person['city'])
print(person['first_name'])
print(person['last_name'])

fav_numbers= {'rose':4,
              'atta':5,
              'francis':10,
              'paps':20,
              'juliet':56,
              }

#now i will print the values of the keys 
print(fav_numbers['atta'])
print(fav_numbers['francis'])
print(fav_numbers['paps'])

glossary= {'indent': 'skipping some spaces, its normarly 4 spaces',
           '\n':'this allows me to get a new line',
           '\t':'This allows me to get a new tab ',
          }

print('\n')
print(glossary['\n'])



#looping through the dictionary, come on this should be fun, i can't wait.
for name,number in fav_numbers.items():
    print(f"\nname:{name}")
    print(f"number:{number}")

    print(f"{name.title()}'s favourite number is {number}")

#now if i need to loop through only the keys, i will you the .keys() method 
for name in fav_numbers.keys():
    print(f"\n{name.title()}")   

#now what if i want to loop through only the values, lets try. well it worked i used .values()
print('The following numbers has been picked')
for number in fav_numbers.values():
    print(f"\n{number}")      
                  