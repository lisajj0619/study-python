#mutable: 변할 수 있는
data_list1 = [1, 2, 3, 4]
data_list2 = data_list1
data_list2[0] = 10
print(data_list2)
print(data_list1)

#immutable: 변할 수 없는
data_tuple1 = (1, 2, 3, 4) #소괄호 안에 값을 여러개 쓸 경우 튜플
data_tuple2 = data_tuple1

#data_tuple2[0] = 10 #오류 튜플은 값을 넣으면 수정 할 수 없음
data_tuple2 = data_tuple1 + (5, 6) #새로운 튜플 기존과 관계없음
print(data_tuple2)
print(data_tuple1)

#소괄호가 없어도 튜플이 됨
datas = 1, 2
print(type(datas))
print(datas[0])

#값이 하나만 있어도 튜플
ERROR_CODE = 1, #대문자는 값을 변경 할 수 없다 약속함
print(type(ERROR_CODE))

