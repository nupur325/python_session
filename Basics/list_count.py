list=[1,3,5,7,9,11,13,15,2,4,6,7]
count=0
sum=0
for i in list:
    if i%2==0:
        sum+=i
        count+=i
    if count==10:
        break
print(sum)
