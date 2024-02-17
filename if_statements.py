cars= ['audi','suzuki','bmw','toyota']
print(cars)
#now i will write an if statement 
for car in cars:
    if car=='bmw':
        print(car.upper())
    else:
        print(car.title())    

#checking if an item is not in thhe list with an if statement 
banned_users= ['seth','prince','sherriff'] 
user= 'emma'
if user not in banned_users:
    print(f"Dear {user.title()}, you may feel free to post on facebook") 
else:
    print(f"Dear {user.title()}, you have been banned from posting on facebook")        

#5.1 conditional test.
car ='Audi'
print('is car== audi?, i predict True')
print(car== 'audi')          

#now i will use a loop in an if statement to print the same argument
#test 1 
if car== 'audi':
    print("my prediction was right")
else:
    print("False")    

#test 2
if car== 'toyota':
    print("my prediction was right")
else:
    print("False")        

#5.2 tests
# i will test for equality and inequality with strings

user_1="emma"
user_2= "prince"
user_1==user_2 
user_1!= user_2    

#using the lower() method to ignore a case
if car.lower()== 'audi':
    print("my prediction was right")
else:
    print("False")   

#numerical test 
age_0= 18
age_1 =20 

#equality and inequality test 
age_0 == age_1
age_0 != age_1   

#greater than and less than 
age_0 >= age_1
age_0 <= age_1

#elif_else statments 
#prices_amusement_Park 

age=10
if age < 4:
    print("Your admission fee is $0")
elif age < 18:
    print("Your admission fee is $25")
else:
    print("Your admission fee is $40")    

