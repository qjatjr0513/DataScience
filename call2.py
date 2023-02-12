def spam(eggs):
    eggs.append(1)

    eggs = [2,3]
    print(eggs)
    
ham = [0]
spam(ham)
print(ham)
