#f(x) = 2x+1
# def f(x):
#     return 2 * x + 1
#
# result = f(2)
# print(result)

# 두 정수의 곱셈 함수
# def get_multiplication(x, y):
#     return x * y
#
# result = get_multiplication(2, 3)
# print(result)

# def multiple(number1, number2):
#     return number1 * number2

# 두 정수의 나눗셈 후 몫과 나머지 구하는 함수
# def get_modulos(x, y):
#     return x // y, x % y
#
# result = get_modulos(10, 2)
# print(result)

# def divide(number1, number2):
#     if number2 !=0:
#         return number1 // number2, number1 % number2
#     return None
#
# result = divide(10, 2)
# if result:
#     value, rest = result
#     print(f'몫: {value}, 나머지: {rest}')
# else:
#     print('0으로 나눌 수 없습니다.')

#1~10까지 print()로 출력하는 함수
# def get_number(x):
#     for i in range(1,11):
#         print(i)
#     return
#
# print(get_number(1))

# def print_from1_to10():
#     for i in range(10):
#         print(i+1, end=' ')
#
# print_from1_to10()

# 이름을 n번 print()로 출력하는 함수
# def get_name(x):
#     for i in range(x):
#         print('박유진')
#     return x

# print(get_name(5))

# def print_name(name, count):
#     for i in range(count):
#         print(name)
#     return
#
# print(print_name('박유진',3))

#1~n까지의 합을 구해주는 함수
# def get_sum(x):
#     total = 0
#     for i in range(x):
#         total += i + 1
#         print(total)
#     return total
#
# print(get_sum(5))

# def get_total_from1(end):
#     total = 0
#     for i in range(end):
#         total += i
#
#     return total

#1~100까지 중 n의 배수를 print()로 출력하는 함수
# def get_times(n):
#     for i in range(1, 101):
#         if i % n == 0:
#             print(i)
#     return
#
# print(get_times(5))
# def print_time_from1_to100(time):
#     for i in range(100):
#         if (i + 1) % time == 0:
#             print(i+1)

#세 정수의 뺄셈 함수
# def get_substraction(x, y, z):
#     return x - y - z
#
# print(get_substraction(10,5,3))

#문자열을 입력받고 원하는 문자의 개수를 구해주는 함수
# def get_string():
#     message = (input("문자열을 입력하세요: ").count(input("원하는 문자를 입력하세요: ")))
#     return str(message)
#
# print(get_string())

# def get_count_of_result(target, keyword):
#     # return len([i for i in target if i == keyword])
#     count = 0
#     for i in target:
#         if i == keyword:
#             count += 1
#     return count

'''
문자열과 문자를 입력받은 뒤 해당 문자가 몇 번째 인덱스에 있는지 검사하고,
만약 해당 문자가 없으면 -1을 리턴하는 함수
'''

# def get_message():
#     message1 = input("문자열을 입력하세요: ")
#     message2 = input("문자를 입력하세요: ")
#     if message2 in message1

# def find(target, keyword):
#     for i in range(len(target)): #문자가 있을때
#         if target[i] == keyword:
#             return i
#
#     return -1 #문자가 없을때

# print(find('apple','l'))

# def find(target, keyword):
#     result = -1
#     for i in range(len(keyword)):
#         if target [i] == keyword:
#             result = i
#             break
#
#     return result
#
# print(find('apple', 'l'))