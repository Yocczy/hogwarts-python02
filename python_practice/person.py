'''
class 类名:
    静态属性
    动态方法
'''


class Person:
    name: str = 'aa'
    age: int = 0
    gender: str = "男"
    __money: float = 0

    def __init__(self, name, age, gender, money):
        self.name = name
        self.age = age
        self.gender = gender
        self.__money = money

    def get_money(self):
        return self.__money

    def get_class(self):
        return self.__class__

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print("sleeping")

    def run(self):
        print("running")

    def get_message(self):
        print(f'{self.name}')
        print(f'{self.age}')


class FunnyMan(Person):

    def __init__(self, skill):
        # super().__init__(name, age, gender, money)
        self.skill = skill

    def fun(self):
        print(f'{self.name} is funny')


st = FunnyMan(11)
st.fun()
print(st.name)
st.name = 'ST'
print(st.name)
print(st.skill)
print(st)
st.age = 40
st.get_message()

# p_zs = Person()
# print(p_zs.name)
# p_zs.run()
# print(Person.name)

# p_ls = Person('李四', 20, '男', 5000)
# print(p_ls.name)
# print(p_ls.get_money())
# print(p_ls._Person__money)
# p_ls.eat()
# print(dir(p_ls))
# print(p_ls.get_class())
