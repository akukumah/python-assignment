##returning a dictionary 
def build_person(first_name,last_name):
    """Returns a dictionary of a person"""
    person= {'first':first_name,'last':last_name}
    return person

##now let's try it.
artist= build_person('emnanuel','akukumah')
print(artist)


##now i will add optional values 
def build_person(first_name,last_name,age= None):
    person= {'first':first_name,'last':last_name}
    if age:
        person['age'] = age
    return person
    
artist= build_person('emmanuel','akukumah',age=57)
print(artist)    


##the album
#i will create a function that a returns a dictionary  of an album 
def build_album(artist_name, album_title):
    """Returns a dictionary of an album"""
    album= {'name':artist_name,'title':album_title}
    return album

##let's try it 
artist_info= build_album('emma','cudjeo')
print(artist_info)


##now i will loop through the function i created, i will ask the user to type in some info
 
def build_album(artist_name,album_title):
    album= {'artist_name':artist_name,'album_title':album_title}

    while True:
        print("\Please enter the album info below")
        print("\Feel free to enter 'q' anytime to quite")

        artist_name= input('artist_name: ')
        if artist_name== 'q':
            break
        album_title= input('ablum_title: ')
        if album_title == 'q':
            break

        artist= build_album('artist_name','album_title')
        print(artist)



##passing a list to a function 
##this function will greet individuals in a list 
def greet_users(names):
    for name in names:
        msg= f"Hello {name.title()}"
        print(msg)

user_name= ['emma','frank','love','kofi']
greet_users(user_name)


##modifying a list 
##now i will start with some designs that needs to be printed; they will be stored in a list 
unprinted_models= ['phone case','robot pendent','dodechedron']


## i will create an empty list, this is where i will keep the printed models
completed_models= []
#Now i will simulate each printing design untill none is left.. let's give it a try, i will use the pop() method
#it would remove the items in the list one after the order.
while unprinted_models:
    current_design = unprinted_models.pop()

##now i have to print it now 
    print(f"\nPrinting:{current_design}")
    completed_models.append(current_design)

##Now let's display the printed models now by appending it to the completed models
print(f"\nThe following are completed models")
for completed_model in completed_models:
    print(completed_model)


##let's make the codes simples but will get the job done.




unprinted_designs= ['cars breaks','wire fun','sweet','candy']
completed_designs= []

while unprinted_designs:
    current_model= unprinted_designs.pop()
    completed_designs.append(current_model)

#this is supposed to the display each completed design in the completed_model list
for completed_design  in completed_designs:
    print(completed_design)

##display 2... This is intended to display the completed_model list it's self. 
print(completed_designs)


#now let's create a function for this 
##this function simulates the unprinted_models until none is left  and assigns it to the completed_modeld list.
def print_models(unprinted_designs,completed_models):
    """Simulates printing each design, until none is left
    move each to completed_models after printing"""

    while unprinted_models:
        current_design= unprinted_designs.pop()
        completed_models.append(current_design)

##this part of the function will display the completed_model, one after the order 
def show_completed_model(completed_models):
    """Displays the completed model"""
    for completed_model in completed_models:
        return completed_model

unprinted_designs= ['phone','cap','piece','rag']
completed_design= []

#let's try it out 
print_models(unprinted_designs,completed_design)
show_completed_model(completed_models)