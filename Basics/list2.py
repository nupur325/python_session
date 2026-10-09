my_ls=[1,2,4,5,6,3,8,9,11,6]
print('Sum of last 4 elements of a list',sum(my_ls[:-4]))

print(my_ls.pop(1))
print(my_ls.pop(4))
print(my_ls)
print('Difference between highest and smallest number',max(my_ls)-min(my_ls))

my_ls.append(my_ls[2]//2)
print(my_ls)