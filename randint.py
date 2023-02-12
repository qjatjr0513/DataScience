import random
for i in range(1000000):
    number = random.randint(0,10)
    if(i==0):
        max = number
        min = number
    else:
        if(number < min):
            min = number
        elif(number > max):
            max = number
print(min,max)