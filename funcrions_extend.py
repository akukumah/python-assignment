#now let's create a function for this 
##this function simulates the unprinted_models until none is left  and assigns it to the completed_modeld list.
def print_models(unprinted_designs,completed_models):
    """Simulates printing each design, until none is left
    move each to completed_models after printing"""

    while unprinted_designs:
        current_designs= unprinted_designs
        completed_models.append(current_designs)
        




def show_completed_model(completed_models):
    """Displays the completed model"""
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs= ['phone','cap','piece','rag']
completed_models= []

#let's try it out 
print_models(unprinted_designs,completed_models)
show_completed_model(completed_models)


##Exercsie 8.9


##excerise 8.10
#now i  will create a function that prints a text message and assigns it to a new list called sent_messages 

##let's try it 


text_messages= ['hello wossop','please have fun','why so serious','you are hot']
sent_messages=[]
def send_messages(text_messages):
    """Displasy sent_messages"""
    while text_messages:
        current_message= text_messages.pop(0) ## Takesthe first message in the list                                                                                                                                                                                                                                                                              
        sent_messages.append(current_message) 
    print(sent_messages)


##let's try it here 
send_messages(text_messages)

##now i will print the sent sent_messages to verify if it's valid 
print(sent_messages) #it worked

#i wil make a copy of functions ouput and call it Achiev
Achiev= sent_messages[:]
print(Achiev)##it worked 

#now i will print the original to see if it retained it's content 
print(f"\n{sent_messages}") ##it worked 

##passing an arbitrary number of argument 
def make_pizza(*toppings):
    """Displays the list of topping that have been requested"""
    print(toppings)

make_pizza('pepperonni')
make_pizza('mushrooms','green pepper','extra cheese')    


##now i wiil create a  function with one parameter but could accept multiple arguments 
#This will describe the pizza order we are making. 
def make_pizza(*toppings): #*topping will help me add up multiple arguments.
    """prints the pizza order we are making"""
    print(f"\nMaking pizza with the following toppings:")
    #now i will loop through a list of toppings and print them out,
    
    for topping in toppings:
        print(f"-{topping}")


#now i will try out the function 
make_pizza('pepperoni')
make_pizza('extra cheese','greens','mushrooms')  

#now i want my function to print the pizza size and the pizza toppings 
def make_pizza(size,*toppings):
    """Prints the summary of the pizza we are making"""
    print(f"\nMaking -{size} inchs pizza with the following toppings")
    for topping in toppings:
        print(f"-{topping}")

#Now let's try the  function 
make_pizza(16,'pepperoni')
make_pizza(25,'extra cheese','green pepper','mushrooms')  

      
##8-12
#i will creat a function that prints sandwitch and it's toppings ordered.

def build_sandwitch(sandwitch,*toppings):
    """Prints the sandwitch and adds requested toppings"""
    print(f"\nPlease here is your {sandwitch} sandwitch with the requested toppings,enjoy!")

    #now will loop through the tupel of toppings which will be provided and print each one,
    for topping in toppings:
        print(f"-{topping}")

#nowi will try the function
build_sandwitch("Bread","extra cheese","extra pepper","salade")     


#8-13
#building a user profile
def user_profile (first_name,last_name,**user_info):
    """Displays user profile """
    user_info['firstname']= first_name
    user_info['lastname']= last_name
    return user_info

##i will try it now
user_profile("emmanuel","akukumah",occupation="artist",sex="male")


##i will create a function that take two parameters and an arbitary argument and returns a dictionary.

def build_car(manufactorture,model,**car_info):
    car_info['manu_f']= manufactorture
    car_info['model_name']= model
    return car_info

build_car('range','pickup',color= 'blue',size= 50,tow_package=True)


#importing functions
import funcrions_extend
funcrions_extend.make_pizza(16,'pepperoni')


from funcrions_extend import make_pizza as mp
mp(14,'extra cheese')

