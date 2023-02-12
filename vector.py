u=[2,2]
v=[2,3]
w=[3,5]
result=[]

for i in range(len(u)):
    result.append(u[i]+v[i]+w[i])

print(result)

result = [sum(t) for t in zip(u,v,w)]

print(result)