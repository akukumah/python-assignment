#creating a list of people i would ivite to dinner,
invitee=['emma','stephen','godwin','daniel']
print(invitee)

#now i will print individual messages to invite them for t dnner at 5
guest1= f"Hello {invitee[0].title()},do you mind having dinner with me and my family on sunday at 3:00pm? I will be thrilled to have you join us."
print(guest1)

guest2= f"Hello {invitee[1].title()},do you mind having dinner with  me and my family on sunday at 3:00pm? I will be thrilled to have you join us."
print(guest2)

guest3= f"Hello {invitee[2].title()},do you mind having dinner with  me and my family on sunday at 3:00pm? I will be thrilled to have you join us."
print(guest3)

guest4= f"Hello {invitee[3].title()},do you mind having dinner with me  and my family on sunday at 3:00pm? I will be thrilled to have you join us."
print(guest4)

#just heard that stephen will not make it for the dinner so i will invite erica instead.i will replace erica with stephen 
#replace erica with stephen # chaning the list 
invitee[1]='erica'

#reviewing the invitee list to see if it is updated
print(invitee)

#now i will re send the ivitattion messages to them.
guest1= f"Hello {invitee[0].title()},do you mind having dinner with me and my family on sunday at 3:00pm? I will be thrilled to have you join us."
print(guest1)

guest2= f"Hello {invitee[1].title()},do you mind having dinner with  me and my family on sunday at 3:00pm? I will be thrilled to have you join us."
print(guest2)

guest3= f"Hello {invitee[2].title()},do you mind having dinner with  me and my family on sunday at 3:00pm? I will be thrilled to have you join us."
print(guest3)

guest4= f"Hello {invitee[3].title()},do you mind having dinner with me  and my family on sunday at 3:00pm? I will be thrilled to have you join us."
print(guest4)

#printing a message for everyone.
print("hello everyone, i just found a larger table, that means more room for more dinner")

#more guests.
#i will use the insert function to update my invitee list.
#adding rose to the begining of my list. 
#i will use the .insert() function
invitee.insert(0,'rose')

#inserting michael the new guest in the middle of my list
invitee.insert(2,'michael')

#now i will also add one more guest to the end of the list,\
#i used the .append() function.
invitee.append('prince')
print(invitee)

#mesage
print("I am sorry guys, my table hasn't arrived yet i would only invite two folks for now,please accept my applogies for any incovinience")

#shrinking the list with the pop() function
#now i will use the pop() function to remove the values in the list one by one untill i am left with two values
invitee.pop()
invitee.pop()
invitee.pop()
invitee.pop()
invitee.pop() 

#now i would print my new list to see if it's updated
print(invitee)

#now i  will  print a message to the invitees in the list 
guest1= f"Dear {invitee[0].title()}, you are still invited to the dinner."
guest2= f"Dear {invitee[1].title()}, you are still invited to the dinner."

#now i will print out the messages for both guest 1 and 2 
print(guest1)
print(guest2)

#now i will use the del() function to remove the rest of the values in the list so it become empty
del(invitee[0])
del(invitee[0])

#now i wil print my list to make sure it is empty.
print(invitee)

#now i will print a message determining the length of my invitee list.i wiil use the f string and the len()
message= f"i am inviting {len(invitee)} people to my dinner party."
print(message)