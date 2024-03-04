##import the path class from the pathlib mudole 
from pathlib import Path as pt 

#extract the file with the path 
path = pt('C:/Users/emma/Desktop/python_work/read_text.py/what i can do in py.txt')

##extract content from the file
##stripping off the extra while line 
contents = path.read_text().rstrip()
print(contents)

##access and extra the lines 
for line in contents.splitlines():
    print(f"\n{line}")


##i will now replace "python" with "C" using the replace() method
    
contents= contents.replace("python","C")
print(contents)







