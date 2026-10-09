#append item in list
colors= ['red','blue']
colors.append('yellow')
print(colors)
#extend adds multiple eelements

#insert at specific position
colors.insert(1,'pink')
print(colors)

#remove an element from specific position
print('Before removal')
colors.pop(0)
print("AFter removal",colors)