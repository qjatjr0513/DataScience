import cm_inch
str1="""
Enter 1 to convert inch to cm
Enter 2 to convert cm to inch
Enter 0 to exit"""
while True:
        print(str1)
        number = int(input("Select your choice: "))
        if number == 1:
                num = int(input('인치를 입력하세요 : '))
                result = cm_inch.inch_to_cm(num)
                print('%d inch = %.2f cm'%(num,result))
        elif number == 2:
                num = float(input('센티미터를 입력하세요 : '))
                result = cm_inch.cm_to_inch(num)
                print('%.2f cm => %d inch'%(num,result))
        elif number == 0:
                print("종료")
                break
        else:
                print("잘못 입력하셨습니다.")




