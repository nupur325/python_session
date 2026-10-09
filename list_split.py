a=[12,13,'Nupur',22,'Shah']
m=max(i for i in a
      if type(i)==int)
b=a[:a.index(m)]
c=a[a.index(m):]
print(b)
print(c)


