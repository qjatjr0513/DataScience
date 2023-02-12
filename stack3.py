word=input("Input a word: ")
word_list=list(word)
print(word_list)

result=[]
while(len(word_list)>0):
    result.append(word_list.pop())
    print(len(word_list))

print(result)
print(word[::-1])