import yaml


class Animal():

    def __init__(self, name: str, color: str, age: int, gender='male'):
        self.name = name
        self.color = color
        self.age = age
        self.gender = gender

    def shout(self):
        print('会叫')

    def run(self):
        print('会跑')


class Cat(Animal):

    def __init__(self, name, color, age, gender, hair='short'):
        super().__init__(name, color, age, gender)
        self.hair = hair

    def catch_mouse(self):
        print('会捉老鼠')

    def shout(self):
        print('喵喵叫')

    def get_cat(self):
        print(f'我叫{self.name}, 毛色{self.color}, {self.age}岁, {self.gender}, 毛发{self.hair}')
        self.catch_mouse()


class Dog(Animal):

    def __init__(self, name, color, age, gender, hair='long'):
        super().__init__(name, color, age, gender)
        self.hair = hair

    def housekeeping(self):
        print('会看家')

    def shout(self):
        print('汪汪叫')

    def get_dog(self):
        print(f'我叫{self.name}, 毛色{self.color}, {self.age}岁, {self.gender}, ，毛发{self.hair}')
        self.housekeeping()


if __name__ == '__main__':
    mao = Cat('猫猫', '白色', 3, 'female', 'short')
    mao.get_cat()
    gou = Dog('狗狗', '黑色', 5, 'male', 'long')
    gou.get_dog()


    def get_data():
        with open('animal.yml', encoding='utf-8') as f:
            datas = yaml.safe_load(f)
        return datas


    print(get_data())

    m = yaml.safe_dump({'maomao': {'name': '猫猫', 'color': '白色', 'age': '3', 'gender': 'female', 'hair': 'short'}})
    print(m)
    g = yaml.safe_dump({'gougou': {'name': '狗狗', 'color': '黑色', 'age': '5', 'gender': 'male', 'hair': 'long'}})
    print(g)
