text=' Welcome to IMCC '

print("Letter C occurs :",text.count("C"),"times in text") #counts occurence
print("Position of IMCC in the text is:",text.find("IMCC"))  #returns position of substring
print(text.replace("IMCC","Python"))  #replace a substring

#check if string starts or ends with certain substring
print(text.startswith(" We"))
print(text.endswith(" "))
print(text.split()) #split the string

word=['Python','is','fun']
print(" ".join(word))  #join the letters to a complete string