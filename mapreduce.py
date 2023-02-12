ex=[1,2,3,4,5]

f=lambda x:x**2
print(list(map(f,ex)))

print([x**2 for x in ex])

f=lambda x,y:x+y
print(list(map(f,ex,ex)))

print([x+y for x,y in zip(ex,ex)])
print(list(map(lambda x:x**2 if x%2==0 else x,ex)))
print([x**2 if x%2==0 else x for x in ex])