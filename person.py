class Person(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def about_me(self):
        print("이름:", self.name,"나이:", str(self.age))

class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def do_work(self):
        print("열심히 일을 한다.")

    def about_me(self):
        super().about_me()
        print("급여:", self.salary)

michael = Employee("michael",25,1000000)
print(michael.age)
print(michael.salary)
michael.about_me()