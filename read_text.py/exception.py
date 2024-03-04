
try:
    print(5/0)
except ZeroDivisionError:
    print("you can not divide by zero")

     





##divided calculator
print("Give me two numbers and i will divide them")
print("Enter Q anytime to quite")

while True:

    first_number = input("Enter nomenator here:  ")
    if first_number == "Q":
        break 

    second_number = input("Enter denumerator here:  ")
    if second_number == "Q":
        break


    try:
        answer= int(first_number) / int(second_number)
        print("Result:", answer)
    except ZeroDivisionError:
        print("sorry you can not divide by zero")




##handling file not found errors
from pathlib import Path
path = Path("aliceinwonderland.txt")

## handling the error with the expect FileNotFoundError
try:
    contents= path.read_text(encoding='utf-8')
except FileNotFoundError:
    print(f"Sorry the file {path} does not exist")
