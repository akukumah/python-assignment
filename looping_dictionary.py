user_0= {"user_name":"efermi",
         "first_name":"enrico",
         "last_name":"fermi",
        }

#now i wiil loop through the dictionary and print each value-key pair 
for key, value in user_0.items():
    print(f"\nkey: {key}")
    print(f"value:{value}")


#rivers in the world, i will creat a dictionary containing rivers and the countries they run through
rivers= {'niger':'nigerian',
         'nile':'egypt',
         'pra':'ghana',
         'orange':'south africa',
         }    

#now i will loop through the dictionary and print a message. i will use the .items() method 
for key,value in rivers.items():
    print(f"The {key} river runs through {value.title()}")

#now i will loop through the dictionary and print out the rivers in there. i will  use the .keys() method 
for key in rivers.keys():
    print(f"\n{key}")    

#now i will print out the countries in the dictionary, i will the  .values() method
for country in rivers.values():
    print(f"\n{country}")


#fav_language_poll 
fav_language= {'emma':'python',
               'frank':'C++',
               'bright':'C',
               'susan':'java',
               'vic':'html',
               'emma':'python',
               'bright':'C',
               }         

#now i will creat a list of some folks and print messages to them, the message will be condition on whether they have registered for my poll 
people= ['emma','frank','rose','vic','efo','susan','mercy','grace']

#now i wll loop through the fav_language dictionary to see if the people list can be found in there and print messages to the, i will equall print messages to those who's names can not be found in there.
for  name in people:
    if name in sorted(fav_language.keys()):
        print(f"\nDear {name.title()} thank you for participating in the poll")
    else:
        print(f"Dear {name.title()},please register for the poll")    