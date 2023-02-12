case_1=["A","B","C"]
case_2=["D","E","A"]

print(case_1)
print(case_2)

result=[i+j for i in case_1 for j in case_2 ]
print(result)

result=[[i+j for i in case_1] for j in case_2 ]
print(result)

result=[[i+j for j in case_2] for i in case_1 ]
print(result)