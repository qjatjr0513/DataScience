def vector_addition(*args):
    return [sum(t) for t in zip(*args)]

u =[2,2]
v=[2,3]
w=[3,5]

print(vector_addition(u,v,w))

row_vectors=[[2,2], [2,3], [3,5]]
print(vector_addition(*row_vectors))