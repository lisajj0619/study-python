# 만약 값을 매개변수로 전달하지 않았을 경우
# 기본 값을 설정할 수 있고, arg=value로 작성한다.

def sub(num1, num2, num3, num4=0): #안들어 올 수 있는 값을 초기값 설정
    return num1 - num2 - num3 - num4

result = sub(1, 2, 3, 4)
print(result)

#실습
#이름을 전달받지 못하면 '익명'으로 대체하고,
#나이를 전달받지 못하면 0으로 대체한다.

def get_info(name='익명', age=0):
    return {'name': name, 'age': age}

print(get_info(name='박유진'))
print(get_info(age=10))