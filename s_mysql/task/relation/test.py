# 회원가입
    ## save_query = "insert into tbl_user(user_id, password, name, address) \
    ##               values(%s, hex(aes_encrypt(%s, 'hello mysql')), %s, %s)"
    # save_query = "insert into tbl_user(user_id, password, name, address) \
    #               values(%s, %s, %s, %s)"
    # password = hashlib.sha256()
    # password.update('5555'.encode('utf-8'))
    # password = password.hexdigest()
    #
    # save_params = 'hgd9999', password, '홍길동', '서울시 강남구'
    # save(save_query, save_params)

from crud_module import *
import hashlib
from random import randint
from sms.send_sms import send_message

if __name__ == '__main__':
    # 회원가입(SMS API) - 랜덤한 인증번호 6자리 발송 후 검사
    # message = "이메일: "
    # member_email = input(message)
    # # 아이디(이메일) 중복검사
    # find_by_id_query = "select email from tbl_member where email = %s"
    # find_by_id_params = member_email,
    # result = find_by_id(find_by_id_query, find_by_id_params)
    #
    # if not result:
    #     message = "비밀번호: "
    #     member_password = input(message)
    #     encryption = hashlib.sha256()
    #     encryption.update(member_password.encode('utf-8'))
    #     member_password = encryption.hexdigest()
    #
    #     message = "이름: "
    #     member_name = input(message)
    #
    #     message = "핸드폰 번호: "
    #     member_phone = input(message)
    #
    #     # DEBUG FALSE
    #     # certification_number = "".join([str(randint(0, 9))for i in range(6)])
    #     # send_message(member_phone, certification_number)
    #     # message = "인증번호: "
    #     # certification_number_input = input(message)
    #
    #     # DEBUG TRUE
    #     certification_number = "123456"
    #     message = "인증번호: "
    #     certification_number_input = input(message)
    #
    #     if certification_number_input == certification_number:
    #         save_query = "insert into tbl_member(email, password, name) values(%s, %s, %s)"
    #         save_params = (member_email, member_password, member_name)
    #         save(save_query, save_params)
    #         print(f"{member_name}님 환영합니다~!")
    # else:
    #     print("이미 사용중인 이메일입니다.")

    # 로그인 후 마이페이지로 이동
    # 회원 비밀번호 변경(EMAIL API) - 랜덤한 코드 10자리 발송 후 검사

    message = "이메일: "
    member_email = input(message)
    find_by_id_query = "select email, password, name from tbl_member where email = %s"
    find_by_id_params = member_email,
    member = find_by_id(find_by_id_query, find_by_id_params)

    if member:
        message = "비밀번호: "
        member_password = input(message)
        encryption = hashlib.sha256()
        encryption.update(member_password.encode('utf-8'))
        member_password = encryption.hexdigest()

        if member.get("password") == member_password:
            print(f"{member.get('name')}님 환영합니다~!")
            for key in member:
                if key == 'password':
                    continue
                print(member.get(key))

            message = "비밀번호 변경 [Y/n]: "
            check = input(message)

            if check == 'Y':
                code = "".join([chr(i + 65) for i in range(0, 26)] + [i for i in range(0, 10)])
                certification_number = ""
                for i in range(10):
                    certification_number += code[randint(0, len(code))]
                send_email(member.get("email"), certification_number)
                message = f"{member.get('email')}로 인증코드를 전송했습니다.\n10자리 인증번호: "
                certification_number_input = input(message)
                if certification_number_input == certification_number:
                    pass

    # 사용자가 입력한 한국어를 영어로 번역
    # 한국어와 번역된 문장을 DBMS에 저장
    # 번역 내역 전체 조회

    # 업로드한 이미지 파일의 이름과 이미지의 내용을 DBMS에 저장(OCR API)
    # 이미지 경로: https://thumb.mt.co.kr/06/2012/02/2012021613230156226_1.jpg/dims/optimize/
    # 경로와 추출한 텍스트 전체 조회

# 반려동물 추가
    # find_by_id_query = "select id from tbl_owner where id = %s"
    # find_by_id_params = 3,
    # owner = find_by_id(find_by_id_query, find_by_id_params)
    # owner_id = owner.get("id")
    #
    # save_many_query = "insert into tbl_pet(name, ill_name, age, weight, owner_id) \
    #                    values (%s, %s, %s, %s, %s)"
    # save_many_params = (
        # ('둘리', '감기', '10', 4.5, owner_id),
        # ('초코', '독감', '11', 3.20, owner_id),
        # ('또치', '골절', '12', 9, '2'),
        # ('도우너', '기생충 감염', '8', '8.23', None),
        # ('뭉치', '감기', '14', '9.86', '3'),
        # ('설이', '감기', '15', '7.44', None),
    # )

    # save_many(save_many_query, save_many_params)

    # 전체 목록
    # find_all_query = "select id, name, age, phone, address from tbl_owner"
    # owners = find_all(find_all_query)
    # owners_with_pets = []
    # for owner in owners:
    #     find_all_by_query = "select id, name, ill_name, age, weight, owner_id from tbl_pet where owner_id = %s"
    #     find_all_by_params = owner.get("id"),
    #     pets = find_all_by(find_all_by_query, find_all_by_params)
    #     owners_with_pets.append(Owner(owner.get("id"), owner.get("name"), owner.get("age"), owner.get("phone"), owner.get("address"), pets))
    #
    # for owner in owners_with_pets:
    #     print(owner.__dict__)

# 1. datetime.datetime.isoformat()
# 2. datetime.date.isoformat()