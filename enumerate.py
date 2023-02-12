for i,v in enumerate(['AAA','BBB','CCC']):
    print(i,v)

x={i:j for i,j in enumerate('AAA BBB CCC'.split())}
print(x)

alist=['a1','a2','a3']
blist=['b1','b2','b3']
for a,b in zip(alist,blist):
    print(a,b)

for i,(a,b) in enumerate(zip(alist, blist)):
    print(i,a,b)

a,b,c=zip((1,2,3), (10,20,30), (100,200,300))
print(a,b,c)
x=[sum(x) for x in zip((1,2,3),(10,20,30),(100,200,300))]
print(x)