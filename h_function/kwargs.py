#keyword arguments
def introduce(**intro):

    print(type(intro))
    print(f'name: {intro["name"]}')

introduce(name="박유진")
introduce(**{'name': '박유진'})

info_dict = {
    'name': '박유진'
}

introduce(name='박유진')
introduce(**info_dict)

#주문 가격과 주문한 회원의 정보 출력
def order_info(*args, **kwargs): #앞은 가격, 뒤는 회원
    '''

    :param args: 주문 가격들
    :param kwargs: 회원의 정보
    :return:
    '''
    total = 0
    for i in args:
        total += i
#
    print(f'{kwargs["name"]}님의 총 주문 가격: {total}원')
#
order_info(3000, 2000, 1000, name='박유진')

#국어, 영어, 수학 점수의 평균 구하기
#kwargs를 사용

def get_average(**kwargs):
    kor = kwargs['kor']
    eng = kwargs['eng']
    math = kwargs['math']
    return (kor + eng + math) / 3

print(get_average(kor=100, eng=90, math=90))

#사용자가 원하는 자리수(round)에서 반올림해준다.
#자리수를 받지 않았다면, 기본 값을 리턴한다.

def get_average(**kwargs):
    kor = kwargs['kor']
    eng = kwargs['eng']
    math = kwargs['math']
    return (kor + eng + math) / 3

message = int(input("원하는 자리수를 입력하세요: "))
print(message)
print(round(get_average(kor=80, eng=90, math=90), int(message)))

def average(**kwargs):
    kor, eng, math = kwargs.get("kor"), kwargs.get("eng"), kwargs.get("math")
    total = kor + eng + math
    average = total / 3

    if "round" in kwargs:
        return round(average, kwargs['round'])

    return average

print(average(kor=100, eng=30, math=22, round=3))

#unpaking
#반드시 key와 함께 사용하고자 할 때에는 매개변수의 시작을 *로 한다.
def avarage(kor, eng, math):
    return (kor + eng + math) / 3

print(avarage(kor=100, eng=30, math=22))