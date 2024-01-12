#중복이 없고, 순서가 없다.
world_set = {'korea', 'america', 'japan', 'china'}
print(type(world_set))
print(len(world_set))
# print(world_set[1]) #오류: 순서가 없으므로 가져올 수 없음
world_set.add('korea')
print(world_set)
#값의 중복을 제거하기 위해 자료구조 set을 씀
datas = [1, 1, 3, 2, 3, 4, 1, 4, 4]
print(list(set(datas)))