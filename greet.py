def greet_user():
    """"Disaplay a simple greeting"""
    print('hello')

greet_user()    

#passing info in the function 
def greet_user(user_name):
    """"Display a simple message and address the user by name """
    print(f"Hello {user_name.title()}.")

#now let us try it 
greet_user("emma")



#execise 8.1 
#i will write a program that tells what i am learning in this chapter in a  function

def display_message():
    """ Displays what i am learning in this chpater"""
    print('i am learning alot about fumctions')

#let's try it 
display_message()        

#8.2 i will creat a functiom that tells my favourite book
def favourite_book (title):
    """"Displays my favourite book"""
    print(f"\n my favourite book is {title.title()}.")

#let's try my new function
favourite_book("The 5am club")

##postional Arguments
def describe_pet (animal_type,pet_name):
    """ Displasy information about a pet"""
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name}")

##let's try this
describe_pet("hamster","harry")
describe_pet("Dog","suzzy")

#using the keyword argument 
describe_pet(animal_type= 'dog',pet_name='suzzy')


#8.4 shirts 
def shirt_info (size,statement):
    """Displays  the shirt size and the statement"""
    print(f"\n{size}\t{statement.upper()}")

##let's try this shit out with the positional arguement 
shirt_info(10,"Messi")    

##i will make the defult large shirt and print a message 
def shirt_info (statement, size):
    print(f"{size} {statement.upper()}")
    print(f"{statement} {size} shirts")

#let's try it 
shirt_info("i love python","large")    

#medium shirts 
shirt_info("i love python","medium")

##cities in countries 
def describe_city( city_name, country='Ghana'):
    """Displays the city and the country it's found"""
    print(f"{city_name} is found in {country}")

#let's try it 
describe_city("\n\tAccra")    
describe_city("\tkumasi")
describe_city("\ttakoradi")

describe_city("\nNashville","US")

#returning values 
##this function should return a neatly formated full name
def full_name( first_name,Last_name):
    """Displays a neatly formatted name"""
    full_name= f"{first_name} {Last_name}"
    return full_name.title()

statistician = full_name("emmanuel","akukumah")
print(statistician)


#using a function in a while loop
def get_formatted_name( first_name,Last_name):
    full_name= f"{first_name} {Last_name}"
    return full_name.title()

#let's try it 
get_formatted_name('emmanuel','akukumah')

#now let's put it in a while loop 

while True:
    print("\nPlease tell me your name")
    print("\n type'q' to quit ")

    f_name= input("first_name: ")
    if f_name == 'q':
        break
    l_name= input("last_name: ")
    if l_name == 'q':
        break
    
    formatted_name= get_formatted_name(f_name,l_name)
    print(f"\nHello {formatted_name.title()}")


##8.6 city in country 
def city_contry(city,country):
    """Displays the city and the country """
    print(f"{city} {country}")


city_contry("accra","ghana")




##returning a dictionary 
def build_person(first_name,last_name):
    """Returns a dictionary of a person"""
    person= {'first':first_name,'last':last_name}
    return person

##now let's try it.
artist= build_person('emnanuel','akukumah')
print(artist)



##the album
#i will create a function that a returns a dictionary  of an album 
def build_album(artist_name, album_title):
    """Returns a dictionary of an album"""
    album= {'artist_name':artist_name,'album_title':album_title}
    return album

##let's try it 
artist_info= build_album('emma','cudjeo')
print(artist_info)

print(build_album('stephen','hungry'))
print(build_album('godwin','wow'))

###adding optional values 
def build_album (artist_name,album_title,number_of_songs=None):
    album={'artist_name':artist_name,'album_title':album_title}
    if number_of_songs:
        album['number_of_songs']= number_of_songs
    return album    


##let's try it 
album_info= build_album('emma','love',5)
print(album_info)

##let's try to access some items in the dictionary
print(album_info['artist_name']) ## it worked 


##now i will loop through the function i created, i will ask the user to type in some info
 
def build_album(artist_name,album_title):
    return {'artist_name':artist_name,'album_title':album_title}

while True:
    print("\nPlease enter the album info below")
    print("Feel free to enter 'q' anytime to quite")

    artist_name= input('artist name: ')
    if artist_name== 'q':
        break

    album_title= input('ablum title: ')
    if album_title == 'q':
        break

    artist= build_album(artist_name,album_title)
    print(artist)


