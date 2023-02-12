def enter_tree(x, p):
    if a[p] == 0:
        a[p] = x
    elif (x < a[p]):
        enter_tree(x, p*2+1)
    else:
        enter_tree(x, p*2+2)
        
def print_tree(p):
    if a[p]!=0:
        print_tree(p*2+1)
        print(a[p])
        print_tree(p*2+2)


a = []

for i in range(20):
    a.append(0)
    
x = 1
while (x>0):
    x = int(input("Enter a positive number:"))
    enter_tree(x, 0)
    print(a)

    
print_tree(0)







