#추가, 수정, 삭제, 검색, 목록
#수정 시 상품명으로 검색하고 새로운 상품명과 가격으로 수정한다.
#(상품명 가격을 따로 수정하지 않고 한번에!)
#검색 시 상품명, 가격을 따로 검색하도록 구현한다.
#가격 검색 시 오차 범위는 ±50%로 설정한다.

name_list = []
price_list = []

title = "또와 과일"
menu = "1. 추가하기\n2. 수정하기\n3. 삭제하기\n4. 검색하기\n5. 목록으로\n6. 나가기\n"
search_menu = "1. 상품명으로 검색\n2. 가격으로 검색\n"
append_message = '추가하실 상품명과 가격을 입력하세요.\n예) 상품명 가격'
search_name_message_for_update = '수정하실 상품명을 입력하세요.'
update_message = '새로운 상품명과 가격을 입력하세요.\n예) 상품명 가격'
delete_message = '삭제하실 상품명을 입력하세요.'
search_name_message, search_price_message = '상품명: ', '가격: '

result_message = ""
append_error_message = "추가 실패(중복된 상품명)"
update_error_message1 = "수정 실패(존재하지 않는 상품명)"
update_error_message2 = "수정 실패(중복된 상품명)"
delete_error_message = "삭제 실패(존재하지 않는 상품명)"
search_name_error_message = "검색 실패(존재하지 않는 상품명)"
search_error_message = "검색 결과가 없습니다."
error_message = "다시 입력해주세요."
no_item_message = "목록이 없습니다."

while True:
    #사용자에게 메뉴를 보여주고 선택한 번호를 choice에 저장
    choice = int(input(title + '\n' + menu))

    #추가
    if choice == 1:
        #사용자에게 상품명과 가격을 동시에 입력받는다(구분점은 공백문자)
        new_name, new_price = input(append_message).split()
        #입력한 상품명이 기존 상품과 중복되지 않는다면
        if new_name not in name_list:
            #이름 list에 추가
            name_list.append(new_name)
            #가격 list에 추가
            price_list.append(int(new_price))
            #오류 메세지를 출력하지 않기 위해 즉시 다음 반복으로 스킵
            continue #성공했을때 오류문이 출력되지 않으려면 continue
        else:
            #입력한 상품명이 기존 상품과 중복되었다면,
            #알맞은 메세지를 result_message에 담아서 소스코드 하단의 일괄처리로 보내기
            result_message = append_error_message
    #수정
    elif choice == 2:
        #상품명을 입력받는다
        name = input(search_name_message_for_update)

        #입력한 상품명이 기존 상품명과 중복일 경우
        if name in name_list:
            #새로운 상품명과 가격을 입력한다.
            new_name, new_price = input(update_message).split()

            #...
            if new_name not in name_list:

                #...
                index = name_list.index(name)
                name_list[index], price_list[index] = new_name, new_price
                continue
            else: #수정실패 중복된 상품명
                result_message = update_error_message2
        else:#수정실패 존재하지 않는 상품명
            result_message = update_error_message1

    #삭제
    elif choice == 3:
        #삭제할 상품명을 입력
        name = input(delete_message)

        #상품명이 기존의 상품명과 중복일 때
        if name in name_list:
            #입력된 상품명의 인덱스 번호를 찾고
            index = name_list.index(name)
            #그 인덱스 번호에 해당하는 이름과 가격을 삭제한다.
            del name_list[index]
            del price_list[index]
            continue

        else:#삭제 실패 존재하지 않는 상품명
            result_message = delete_error_message
    #검색
    elif choice == 4:
        choice = int(input(search_menu))

        #상품명으로 검색
        if choice == 1:
            name = input(search_name_message)

            #상품이 기존 상품과 중복일 경우
            if name in name_list:
                #상품의 인덱스 번호 찾기
                index = name_list.index(name)
                print(f'{name_list[index]}, {price_list[index]}')
                continue
            else: #검색 실패 존재하지 않는 상품명
                result_message = search_name_error_message
        #가격으로 검색
        elif choice == 2:
            price = int(input(search_price_message))
            min = price * 0.5 #입력한 가격의 최솟값
            max = price * 1.5 #입력한 가격의 최댓값

            #입력한 가격이 오차범위 내에 있는 가격list에서 인덱스 번호 검색
            result_index = [price_list.index(i) for i in [price for price in price_list if min <= price <= max]]

            #입력한 가격의 오차범위가 존재할 경우 출력한다
            if len(result_index) != 0:
                for i in result_index:
                    print(f'{name_list[i]}, {price_list[i]}')
                    continue
            #오차범위가 존재하지 않을경우 에러 메세지 출력
            else:
                result_message = search_error_message
        #목록
        elif choice == 5:
            #상품list가 없을 경우
            if len(name_list) == 0:
                result_message = no_item_message
            #상품list가 존재할 경우
            else:
                for i in range(len(name_list)):
                    print(f'{name_list[i]}, {price_list[i]}')
                    continue
        #나가기
        elif choice == 6:
            break

        #그 외
        else:
            result_message = error_message
        print(result_message)
        result_message = ""