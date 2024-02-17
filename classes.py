 
#trying to model a dog 
from typing import Self


class Dog:
    """A simple attempt to model a dog."""

    def __init__(self,name,age):
        """Initialize name and age attribute"""
        self.name = name 
        self.age  = age

    def sit(self):
        """Simulate a dog sitting to respond to a command""" 
        print(f"{self.name} is sitting now")

    def roll_over(self):
        """Simulate a dog rollin_over to respond to a command"""
        print(f"{self.name} is rolling over!")

#trying the dog class ..creating an instance 
my_dog= Dog('frank',6)
print(f"my dog's name is {my_dog.name}.")
print(f"my dog is {my_dog.age} years old")

my_dog.sit()
my_dog.roll_over()



##9.1 restaurant 
#i will create a class for a restaurant 

class Restaurant:
    """A simple model for a restaurant"""
    
    def __init__ (Restaurant,restaurant_name,cuisine_type):
        """initializes the attribte restaurant_name and cuisine_type"""
        Restaurant.name= restaurant_name
        Restaurant.cuisine= cuisine_type

    def descibe_restaurant(Restaurant):
        """Prints the restaurant name and the cuisne"""    
        print(f"\n{Restaurant.name} makes {Restaurant.cuisine}")

    def open_restuarnt(Restaurant):
        """indicates the restaurant is open"""    
        print(f"{Restaurant.name} is open")


#instance 
restaurant=Restaurant("sister Ama'schop bar","fufu") 

restaurant.descibe_restaurant()
restaurant.open_restuarnt()
    


##9.2 I will create three instances for the class  and call the decribe_restaurant method 
pizza= Restaurant("papa's pizza","pizza")
sandwitch = Restaurant("pizza man","sandwitch")
icycup   =  Restaurant("icycupe joint","yougourt")


pizza.descibe_restaurant()
sandwitch.descibe_restaurant()
icycup. descibe_restaurant()




#9.3 
class user:
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name  = last_name
       
        

    def descibe_user(self):
        print(f"\n{self.first_name} {self.last_name}")

    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}")        
        
#insatnce
User= user("emmanuel","akukumah")

user.descibe_user(User)
user.greet_user(User)




##new
class User:
    def __init__(self, first_name, last_name, **user_info):
        self.user_info = {}
        self.user_info['first_name'] = first_name
        self.user_info['last_name'] = last_name
        for key, value in user_info.items():
            self.user_info[key] = value

    def describe_user(self):
        """Prints a summary of the user's information"""
        print(self.user_info)


    def greet_user(self):
        """Greets the user"""
        print(f"\nHello {self.user_info['first_name']} {self.user_info['last_name']}!")


# instance
user_instance = User("emmanuel", "akukumah", age=25, location="Earth")
user_instance.describe_user()
user_instance.greet_user()




##i will create a class that will represents a particular car i'm working with 
class car:
    """A simple attempt to represent the car i am working with"""

    #now i will initialize the parameters i will use,i will first add the self parametre ana the rest will follow
    def __init__(self,name,model,year):
        """Initializing the parameters"""
        self.name = name 
        self.model= model
        self.year = year

        #now i wiil define what should happen when the class is called
    def get_discriptive_name(self):
        """Returns neatly formatted descriptivce  name of the automobile"""
        automobile= f"{self.name} {self.model} {self.year}"
        print(automobile.title())
               
#now i will test the class with an instance 
#instance 
my_car= car('audi','a4',2021)
my_car.get_discriptive_name()





class comupute_discount :
    """An attempt to model a discount calculator"""

    def __init__(self,price,discount):
        """initialize the parameters"""
        self.price    = price
        self.discount = discount

    def get_discount(self):
        """Returns the discounted price of the commodity"""
        discounted_price= self. price * self.discount/100
        print(f"You price will now be {discounted_price}cedis, thank you for shopping with us.")    

        
#instance 
emma_discount= comupute_discount(500,10)
emma_discount.get_discount()


#9.4 Number served 
##9.1 restaurant 
#i will create a class for a restaurant 

class Restaurant:
    """A simple model for a restaurant"""
    
    def __init__ (self,restaurant_name,cuisine_type):
        """initializes the attribte restaurant_name and cuisine_type"""
        self .name= restaurant_name
        self .cuisine= cuisine_type
        #adding a new attributes 
        self.number_served= 0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             

    def descibe_restaurant(self):
        """Prints the restaurant name and the cuisne"""    
        print(f"\n{self.name} makes {self .cuisine}")

    def open_restuarnt(self):
        """indicates the restaurant is open"""    
        print(f"{self.name} is open")

    #now i will add a method in here so i can access the added attribute
    def people_served(self):
        """Prints the number of individuals who have been served"""
        print(f"{self.number_served} individuals have been served")    

    #now i wll add up a method that will allow me to set the number of people served in the instance 
    def set_number_served(self,set_number):
        """allows me to set the number of people who have been served in the instance"""
        self.number_served = set_number
        
    #Now i will add a method that can help increase the number of people served 
    def increment_number_served(self, increase):
        """adds numbers to increase the number of people served""" 
        self.number_served += increase 



#instance 
restaurant=Restaurant("sister Ama'schop bar","fufu") 

restaurant.descibe_restaurant()
restaurant.open_restuarnt()
restaurant.set_number_served(25)
restaurant.people_served()

restaurant.increment_number_served(100)
restaurant.people_served()


#9.5 login attempt 
#9.3 
class user:
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name  = last_name
       #i will add login attempt in here as an attribute 
        self.login_attempt= 0  
        

    def descibe_user(self):
        print(f"\n{self.first_name} {self.last_name}")

    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}")  

    def login(self):
        """Indicates the number of login attemptes"""
        print(f"You have attempted {self.login_attempt} logins")  

    #i will add a method i here 
    def increatment_login(self):
        """Increases the login attempts by one"""
        self.login_attempt += 1 
    
    def reset_logins(self):
        """reset the entire login attempts to 0"""
        self.login_attempt = 0


        
#insatnce
User= user("emmanuel","akukumah")

User.greet_user()
User.increatment_login()
User.login()

#resetting the logins attempts to 0
User.reset_logins()
User.login()


##working on inheritance, the child class
#i will create a class called electric CAr that will inherite the attributes and methods of its parent class. 

class Electric_car(car):
    """Represents a car but with specification to electric ones"""

    def __init__(self, name, model, year):
        """initialising attributes from parent class and attributes speacial for electric car"""
        super().__init__(name, model, year)
        self.battery_size = 40 
        self.battery= Battery()

    #i will add up a method too
    def describe_battery(self):
        """Describes the car's battery"""
        print(f"The car has a {self.battery_size}-KWH battery")    



#i wiil do a composition in here
class Battery:
    """A simple attempt to discribe the car's battery size"""
    def __init__(self,battery=40):
        """initializing the paranmeter"""
        self.battery_size= battery
    def discribe_battery(self):
        """Prints the battery size"""    
        print(f"Your car has a {self.battery_size}-KWH battery.")

    def get_range(self):
        """prints statemet about the range the a battery can over"""
        if self.battery_size == 40:
            range= 150
        elif self.battery_size == 65:
            range= 225
        print(f"Your car can go about {range} miles on full charge") 

    def upgrade_batter(self):
        """ Check the battery size and set the capacitor to 65 if it isn't""" 
        if self.battery_size != 65:
            capacitor = 65   




#now i will test it
#instance 
my_vehicle = Electric_car("nissan","pickup",2025)
my_vehicle.get_discriptive_name()    
my_vehicle.describe_battery()    
my_vehicle.battery.discribe_battery()
my_vehicle.battery.get_range()



#9.6 Icecream stand as a child class and Restaurant the parent class
class Icecream_stand(Restaurant):
    """An attempt to model an ice cream stand"""
    def __init__(self, restaurant_name, cuisine_type):
        """initiliazing attributes from parent class,Restaurant"""
        super().__init__(restaurant_name, cuisine_type) 
        
        

    def get_flavors(self):
        """Print the flavors"""
        print(f'{self.flavors}')



class Flavors:
    """collect a list of icecream flavors"""
    def __init__(self,*flavors):
        """initializing parameter"""
        self.flavors= flavors

    
    def get_flavors(self):
            """retruns a list of flavours"""
            print(list(self.flavors))
    
    

#instance 
ice_cream= Icecream_stand("icycup","Fresh yougourt") 
##accesing the method from  parent class
ice_cream.descibe_restaurant()        
fal= Flavors("vanilla","scrawbery","chocolate")







    
#9.8
#creating a privilege class and then calling it in the Admin class
class Privileges:
    """A simple attempt to model privilages admins are entiled to"""

    def __init__(self,*privileges):
        "Initilize the parameter"
        self.privileges= privileges

    def show_privileges( self):
        """Shows the privileges the admin is enetilted to """
        print(f"{self.privileges}")     



##9.7 Adnim 
#i will create a child class that inherites it's attributes from the parent class 
class Admin(user):
    """An attempt to model a administrator"""
    def __init__(self, first_name, last_name):
        """Initializing attritutes from parent class User"""
        super().__init__(first_name, last_name)
        self.privileges= Privileges()


 #instance 
admin = Admin("John", "Doe")
admin.privileges = Privileges("can add post", "can delete post", "can ban user")
admin.privileges.show_privileges()
    
 

#9.9 battery upgrade 

#i wiil do a composition in here
class Battery:
    """A simple attempt to discribe the car's battery size"""
    def __init__(self,battery=40):
        """initializing the paranmeter"""
        self.battery_size= battery
    def discribe_battery(self):
        """Prints the battery size"""    
        print(f"Your car has a {self.battery_size}-KWH battery.")

    def get_range(self):
        """prints statemet about the range the a battery can over"""
        if self.battery_size == 40:
            range= 150
        elif self.battery_size == 65:
            range= 225
        print(f"Your car can go about {range} miles on full charge") 

    def upgrade_battery(self):
        """ Check the battery size and set the capacitor to 65 if it isn't""" 
        if self.battery_size != 65:
            self.battery_size= 65
            capacitor = 65   


##instance 
myElectric= Electric_car("toyota","pickup",2025)
myElectric.battery.discribe_battery()
myElectric.battery.get_range()
##now i will upgrade the battery and check the range again
myElectric.battery.upgrade_battery()
myElectric.battery.get_range()##after upgrading the battery the range changed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    