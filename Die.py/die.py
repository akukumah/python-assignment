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

#rolling the die 10 times 
for value in range(21):
    print(die.roll_die())




