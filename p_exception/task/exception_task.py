# #캐릭터 닉네임을 정할 때, 비속어를 사용하지 못하게 막아주기
# # 바보 멍게 해삼 운영자
# # 직접 Error를 제작하여, 발생 시 안내 매세지까지 출력하기
#
# class NicknameError(Exception):
#     def __str__(self):
#         return "해당 닉네임은 사용할 수 없습니다."

# def check_nickname(message):
#     if '바보' in message:
#         raise NicknameError
#
#     elif '멍게' in message:
#         raise NicknameError
#
#     elif '해삼' in message:
#         raise NicknameError
#
#     elif '운영자' in message:
#         raise NicknameError
#
# nickname = input('닉네임: ')
#
# try:
#     check_nickname(nickname)
#     print('닉네임: ', nickname)
#
# except NicknameError as e:
#     print(e)

#
#
class NickNameError(Exception):
    def __str__(self):
        return "해당 닉네임은 사용하실 수 없습니다."

def check_nickname(message):
    bad_nickname_list = ['바보', '멍게', '해삼', '운영자']
    for name in bad_nickname_list:
      if name in bad_nickname_list:
        raise NickNameError


nickname = input('닉네임: ')

try:
    check_nickname(nickname)
    print('닉네임: ', nickname)

except NickNameError as e:
    print(e)