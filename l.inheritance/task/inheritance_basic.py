#인간 (부모)
#이름, 나이
#걷기(walk)
#'두 발로 걷습니다.' 출력

class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        print(f'두 발로 걷습니다.')

human = Human('qwe', 20)
human.walk()
#원숭이 (자식)
#이름, 나이, 동물원 이름
class Monkey(Human):
    def __init__(self, name, age, zoo):
        super().__init__(name, age)
        self.zoo = zoo
#걷기 (walk)
#'두 발로 걷습니다.', '네 발로 걷습니다' 출력
    def walk(self):
        super().walk()
        print(f'네 발로 걷습니다.')

monkey = Monkey('asd', 10,'에버랜드')
monkey.walk()