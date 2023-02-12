def enter_tree(x,p):
    if a[p]==0:
        a[p]=x
    elif (x<a[p]):
        enter_tree(x, p*2+1)
    else:
        enter_tree(x,p*2+2)

a=[]

for i in range(10):
    a.append(0)

x=1
while(x>0):
    x=int(input("Enter a positive number: "))
    enter_tree(x,0)
    print(a)
    
for i in range(1, len(a)): 
    for j in range(i, 0, -1): 
        if a[j] < a[j-1]: 
            a[j], a[j-1] = a[j-1], a[j] 
        else : 
            break

while 0 in a:
    a.remove(0)

for i in a:
    print(i)

