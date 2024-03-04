#importing the Path class from the pathlib modiule 
from pathlib import Path  as p 
path = p('C:/Users/emma/Desktop/python_work/read_text.py/pi_digits.txt')
contents = path.read_text()

print(contents)

##i need to strip the white space, i need the added empty sapce in the ouput, i will use the .rstrip() method 
##the results came with an extra space at the button i will now strip that off with the rstrip() method 

contents= contents.rstrip()
print(contents)

##sriping the white line immediately when reading the contents 
contents= path.read_text().rstrip()
print(f"\n{contents}")

##now i want to work  with each line in the content of the file, i will use the . splitline() method for this 
#extracting the lines 
lines = contents.splitlines()
for line in lines:
    print(f"\n{line}")

##working with the contents in the file
#the pi_string 

pi_string= " "
for line in lines:
    pi_string += line 

print(pi_string) 

# checking the lenth 
print(len(pi_string))

    




##is your birthday in Pi, lets find out 
#read the files into memory 
#import the Path class from the pathlib module 

from pathlib import Path as pt 

path= pt("D:/py.books/pcc_3e-main/chapter_10/reading_from_a_file/pi_million_digits.txt")

#exracting the contents from the file 
contents = path.read_text().rstrip()

#extract the lines and print each lines 
lines = contents.splitlines()
pi_string=" "
for line in lines:
    pi_string += line 
    

##print first 50 lines 
print(pi_string[:100
                ])


#now lets check if pi contains your birthday 
birthday = input("Enter your bitthday in this format, mmddyy:  ")
if birthday in pi_string:
    print("your bithday appears in the first million digits of pi")
else:
    print("your birthday does not apear in the first million digits of pi")    


