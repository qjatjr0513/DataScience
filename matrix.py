matrix_a=[[1,2,3], [4,5,6]]
result = [[element for element in t]for t in zip(*matrix_a)]
print(result)

result = []
for t in zip(*matrix_a):
    print(t)
    row=[]
    for element in t:
        print(element)
        row.append(element)
        result.append(row)
    print(result)