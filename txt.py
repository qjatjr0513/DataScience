f = open("dream.txt","r")
contents = f.read()
print(contents)
f.close()


with open("dream.txt","r") as my_file:
    contents = my_file.read()
    print(type(contents), contents)