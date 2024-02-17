requested_toppings= ['mushrooms','green peppers','extra cheese']
for requested_topping in requested_toppings:
    print(f"Adding {requested_topping}.")
print("\nFinish making your pizza!")    

#if we run out of green peppers, i will use an if statement to handle this
requested_toppings= ['mushrooms','green peppers','extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == "green peppers":
        print(f"sorry we are out of {requested_toppings[1]} rigth now")
    else:       
        print(f"Adding {requested_topping}.")

print("\nFinish making your pizza!")  

#checking if the request list topping is empty
requested_toppings= []
if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}")
else:
    print("Please are you sure you want a plain pizza")  

##multiple list 
#in this one i will test a rquested_toppings againts an available toppings
available_toppings= ['mushrooms','olives','green peppers',
                     'pepperoni','pineapple','extra cheese']
requested_toppings= ['mushrooms','french fries','extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}")
    else:
        print(f"sorry we don't have {requested_topping}")
print("\nFinish making your pizza, bon appetti!")            


##exercises 
#5.8 
names = ['emmanuel','jaden','levi','admin','seth']

#now i wll loop through the list and print messages to each name but a special message for the admin  
for name in names:
    if name == "admin":
        print("Hello Admin, would you like to see a status report?")
    else:
        print(f"Hello {name.title()},thank you for logging in again!")     

##checking if my list is empty, if it is true i will ask admin to get us some users.
users= []
if users:
    for user in users:
        print(f"Hello {user.title()}, thank you for logging in again.")
else:
    print("\nAdmin, we need some users")          

#5.10  checking usernames in they already exits in the current_names 
current_names= ['ray','emma','prince','seth','stephen']
new_users= ['ray','rose','prince','frank']
for user in new_users:
    if user in current_names:
        print("\nYou need to enter a new username")
    else:
        print("username is available,thank you")     




 #ordinal_numbers 

#ordinal_umbers
ordinal_numbers= [1,2,3,4,5,6,7,8,9]
for number in ordinal_numbers:
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd") 
    elif number == 3:
        print(f"{number}rd")
    else:
        print(f"{number}th")           
      
         