# animals = ["dog", "cat", "bird", "fish"]
# print(animals)
# print(type(animals))
#
# # #인덱스로 접근
# print(animals[1])
# print(animals[2])
# #
# # #음수 인덱스 가능 (가장 마지막부터 순서대로 앞으로 이동한다)
# print(animals[-1])
# print(animals[-2])
# #
# #len()
# print(len(animals))
#
# # #append() 리스트 추가
# animals.append("hamster")
# print(len(animals))
# print(animals)
#
# animals.append("cat")
# print(animals)
#
# # #insert() 리스트 삽입
# animals.insert(1,"dog")
# print(animals)
#
# # #remove() 리스트 삭제 값을 입력
# animals.remove("fish")
# print(animals)
#
# # #del()리스트 삭제 인덱스 입력
# #del(animals[1])
# del animals[1]
# print(animals)
#
# # #clear()
# animals.clear()
# print(animals)
#
# #index() 값의 인덱스를 출력
# print(animals.index("bird"))
# print(animals.index("tiger")) #없으면 오류
#
# # #수정
# index = animals.index("bird")
# animals[index] = ("lion")
# print(animals)
#
# #그 외
# animals = ["dog", "cat", "bird", "fish"]
# # print(animals * 2)
# print("dog" in animals)
# print("tiger" in animals)
#
# for animal in animals:
#     print(animal)
#
# #실습
# #1~90까지 list에 담고 출력
# number_list = [0] * 90
# for i in range(len(number_list)):
#     number_list[i] = i + 1
#     print(number_list[i])
#
# # ver.2
# number_list = []
# for i in range(90):
#     number_list.append(i+1)
# print(number_list)
#
# #1~100까지 중 짝수만 list에 담고 출력
# number_list = [0] * 50
#
# for i in range(len(number_list)):
#     number_list[i] = (i+1) * 2
#     print(number_list[i])
#
# # #1~10까지 list에 담은 후 짝수만 출력
# number_list = []
#
# for i in range(10):
#     number_list.append(i+1)
# print(number_list)
#
# #even_list = [0] * (len(number_list) / 2)
# even_list = []
#
# for i in range(len(number_list)):
#     if number_list[i] % 2 == 0:
#         even_list.append(number_list[i])
# print(even_list)
#
# #4명의 회원 정보를 list에 담은 뒤 두 번째 회원의 이름을 변경하고 마지막 회원은 삭제
# #1. 두 번째 회원의 이름 수정
# #2. 마지막 회원 삭제
# names = ['박유진', '홍길동', '이순신', '장보고']
#
# names[1] = '서경덕'
# print(names)
#
# names.remove(names[-1])
# print(names)

#list안에 list
number_list = [[1,3,5], [2,4,6]]
# print(number_list[0][0]) 출력시 1이 나온다 like행렬

for i in range(len(number_list)):
    for j in range(len(number_list[i])):
        print(number_list[i][j])