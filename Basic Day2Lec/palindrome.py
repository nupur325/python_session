name = input("Enter a name:")
rev=''
n=name
while len(n)>0:
    rev=rev+n[-1]
    n=n[:-1]
print("Reversed string",rev)
if name.lower()==rev.lower():
    print('Palindrome')
else:
    print('Not palindrome')
