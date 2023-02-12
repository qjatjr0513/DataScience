a=[3,4,5]

for i in range(10):
    try:
        if(i==1):
            print(a[3])
        elif(i==2):
            print(b)
        else:
            print(10/i)
    except ZeroDivisionError as e: #as e는 어떤 메시지 자동으로 나옴옴
        print(e)
    except NameError as e:
        print(e)
    except IndexError as e:
        print(e)       