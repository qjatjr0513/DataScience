matrix_a=[[1,1,2],[2,1,1]]
matrix_b=[[1,1],[2,1],[1,3]]

result=[[sum(a*b for a,b in zip(row_a, column_b))for column_b in zip(*matrix_b)] for row_a in matrix_a]
print(result)

result=[]
for row_a in matrix_a:
    print(row_a)
    value=[]
    for column_b in zip(*matrix_b):
        print(column_b)
        s=0
        for a,b in zip(row_a,column_b):
            s=s+ a * b
        value.append(s)
    result.append(value)
print(result)