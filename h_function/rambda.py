# # 람다(lambda): 이름이 없는 함수, 일회성
# # lambda 매개변수, ...: 리턴값
# def add(number1, number2):
#     return number1 + number2
#
# lambda number1, number2: number1 + number2
# # 각 요소를 2를 더해서 리턴
# # 일반함수
# def change(number): #
#     return number + 2
#
# print(list(map(change,[1, 2, 3, 4])))
# #익명함수
# print(list(map(lambda number: number +2, [1, 2, 3, 4])))

datas = [2, 4, 6, 8]
#아래의 list의 각 요소에 2를 곱하여 변경

print(list)
print(list(map(lambda number: number*2, datas)))

# 각 경로 앞에 '/app'를 붙여준다.
# '/app/game', '/app/news', '/app/fashion', '/app/ranking'
urls = ['/game', '/news', '/fashion', '/ranking']
print(list(map(lambda url: f'/app{url}',urls)))

# filter(function, iterator)
# 1~10까지 중 짝수만 출력
print(list(filter(lambda number: number % 2 ==0, [i + 1 for i in range(10)]))) #comprehension

#'game'서비스를 제공하는 경로 찾기
urls = ['/app/game', '/app/news', '/app/fashion', '/app/ranking']
print(list(filter(lambda url: url.split("/")[-1] == 'game', urls)))