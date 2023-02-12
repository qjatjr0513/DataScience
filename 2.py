def enter_tree(x,p):
    if a[p]==0:
        a[p]=x
    elif (x<a[p]):
        enter_tree(x, p*2+1)
    else:
        enter_tree(x,p*2+2)



a = [i for i in range(10)]

x=1
while(x>0):
    x=int(input("Enter a positive number: "))
    enter_tree(x,0)
    print(a)
    
a = [i for i in range(10)]    
a.sort()
while 0 in a:
    a.remove(0)

for i in a:
    print(i)
