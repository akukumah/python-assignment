#this block passes the  test 
alien_color= 'green'
if alien_color == "green":
    print("You just earned 5 points")

#this block fails the test 
if alien_color == "red":
    print("You just earned 5 points")
else:
    print("sorry you lose")   


color_alien= "red"
if color_alien == "green":
    print("You just earned 5 points")
elif color_alien == " yellow":
    print("You just earned 10 points")    
else:
    print("You just earned 20 points ")         


#5.6 stages in life 
age = 16
if age < 2:
    print("You are a baby")
elif age < 4:
    print("You are a toddler")
elif age < 13:
    print("You are a kid") 
elif age < 20:
    print("You are a teenager") 
elif age < 65:
    print("You are an adult")
else:
    print("You are an elder")                  


#fruits.py 
# i will search the list is there are certaim fruits 
fruits= ['banana','pear','apple','pineapple'] 
if 'banana' in fruits:
    print("yes")  
if 'apple' in fruits:
    print("yes")     


#i will search the fruit list for certain fruits using if statements 
favorite_fruits= ['apple','banana','pear']
if 'apple' in favorite_fruits:
    print(f"You really like {favorite_fruits[0].title()}")
if 'banana' in favorite_fruits:
    print("You really like apples")
if  'pear' in favorite_fruits:
    print("You really like pears") 
if  'apple' in favorite_fruits:
    print("You really like apples")
if  ' Guava' in favorite_fruits:
    print("You really love Guavas")         