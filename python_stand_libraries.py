#now i will try some python standard libraries 

#i will import the Random module and use some functions in it 
from random import randint
#randomly select a number from the tuple
print(randint(1,6))

from random import choice 
#randomly select a name from the list 
players = ['emma','frank','grace','peter','love']
up_first= choice(players)
print(up_first)


#9.13 Die 
class Die:
    """a attempt to model a die"""
    def __init__(self,sides= 6) :
        """initializing the parameter with a default value 6"""
        self.sides= sides

    def roll_die(self):
        """rolls die and return a random number from 1 to 6 inclusively and prints number"""
        from random import randint
        print(randint(1,self.sides))    

#instance 
die = Die()
die.roll_die()

##now i will roll the die 10 times 
      