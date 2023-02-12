def countdown(n):
    if n>1:
        countdown(n-1)
    if n % 2 ==0:
        print(n, "is even")
    else:
        print(n, "is odd")  
n=int(input("Enter a number: "))
countdown(n)