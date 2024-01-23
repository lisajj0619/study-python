for i in range(1, 11, 1):
    print(f'{i + 1}. 박유진')

for i in range(1, 11):
    print(f'{i}. 박유진')

for i in range(10, 0, -1):
    print(f'{i}. 박유진')

for i in range(10):
    print(f'{i + 1}. 박유진')

for i in range(10):
    print(f'{10 - i}. 박유진')

# 1~10까지 중 3까지만 출력
for i in range(10):
    print(i + 1)
    if i == 2:
        break

# 1~10까지 중 4를 제외하고 출력
for i in range(10):
    if i == 3:
        continue
    print(i + 1)