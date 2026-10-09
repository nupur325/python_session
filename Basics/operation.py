#string functions
text=' Welcome to IMCC '

print('Remove spaces:',text.strip()) #Remove spaces from start
print("Remove spaces from end:",text.rstrip()) #Remove spaces from last
print("Lower case:",text.lower()) #small letters to string
print("Upper case:",text.upper()) #upper case 

text=text.strip() #first strip then capitalize
print("Capitalize first word:",text.capitalize()) #capitalize the first word
print(text.title()) #capitalize each word