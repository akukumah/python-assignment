places=['italy','ghana','india','america','chad']
print(places)
#now i will use the sorted() to temporaly re-arrange the items in the list 
print(sorted(places))
print(places)

#now i wiil use the sorted() to print the items in reverse alphabetical order'
print(sorted(places,reverse=True))

#now i will print the original list just to be sure it the original isn't affected 
print(places)

#now i will use the reverse() method  to permanently change the order of the list.
places.reverse()
print(places)

#now i want the list back to it's original state, i wii run the reverse() once again on the list.
places.reverse()
print(places)

#i will now use the sort() method to re-arrange my list in alphabetical order.
places.sort()
print(places)

#i will now re-arrange in reverse alphabetical order.
places.sort(reverse=True)
print(places)