# 사용자에게 아래의 메뉴를 출력하고 번호를 입력받는다.

# 1. 빨간색
# 2. 검은색
# 3. 노란색
# 4. 흰색

# menu = '메뉴의 번호를 입력하세요. \n1.빨간색 \n2. 검은색\n3. 노란색\n4. 흰색\n' #입력 받을 메뉴
# choice = int(input(menu)) #메뉴에서 번호 입력
#
# if choice == 1: #1번을 골랐을 경우
#     print("red")
# elif choice == 2: #2번을 골랐을 경우
#     print("black")
# elif choice == 3: #3번을 골랐을 경우
#     print("yellow")
# else: #4번을 골랐을 경우, 위의 경우가 모두 아니기 때문에 따로 조건식을 쓸 필요가 없다.
#     print("white")
#
# 사용자가 입력한 번호의 색상을 영어로 출력한다. - 강사님.ver
title = "색상은 골라주세요!\n"
menu = "1. 빨간색\n" \
       "2. 검은색\n" \
       "3. 노란색\n" \
       "4. 흰색\n"

choice = int(input(title + menu)) #문자열끼리 '+'를 사용하여 같이 출력할 수 있음
choice1, choice2, choice3, choice4 = choice == 1, choice == 2, choice == 3, choice == 4 #선택 항목을 한번에 정리
color1, color2, color3, color4 = "red", "black", "yellow", "white" #변수를 한번에 설정할 수 있다.
result = None #어떤 종류의 값이 들어갈지 모를 때 None으로 초기화를 한다. 불린 타입으로 변환하면 False값

if choice1:
    result = color1
elif choice2:
    result = color2
elif choice3:
    result = color3
elif choice4:
    result = color4

print(result)
