def countdown(n):
    if n % 2 ==0:
        print(n, "is even")
    else:
        print(n, "is odd")
    if n>1:
        countdown(n-1)
n=int(input("Enter a number: "))
countdown(n)