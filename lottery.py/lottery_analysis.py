#Analysis 
          
from random import choice as ch 
my_ticket = (23, 'Y')
lottery_numbers = (1, 23, 45, 19, 'A', 'Y', 'X', 'G')

while True:
    result = ch(lottery_numbers)

    if result in my_ticket:
        print("\nCongratulations, you won!")
        break
    else:
        print("Sorry, try again later.")

   