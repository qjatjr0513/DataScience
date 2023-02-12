kor = [70,40,70]
eng = [90,50,60]
mth = [80,60,50]

for data in zip(*(kor,eng,mth)):
    print(data)