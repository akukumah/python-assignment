names=['prince','sherrif','seth','emmanuel']

#now i will call out individual names according to their assinged index 
print(names[0]) 
print(names[1])
print(names[-1])

#now i wil wrtite a message to the individuals, i will use the f-string 
message= f"hello {names[0].title()},would you like to study some python codes with me?"
print(message)

#message for sherrif
message= f"hello {names[1].title()},would you like to study some python codes with me?"
print(message)

#message for seth index[2]
message= f"hello {names[2]} would you like to study some python codes with me ?"
print(message)