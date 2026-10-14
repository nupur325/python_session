with open("file.txt","r") as f:
    data = f.read()

count = 0
for i in data:
    if i in "aeiouAEIOU":
        count += 1
print("Total vowels:",count)