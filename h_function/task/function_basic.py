# 회원의 주문 금액(pay)과 회원의 쿠폰 할인율과 개수(coupon, count)를 전달받은 뒤
# 회원이 보유한 쿠폰의 할인율을 주문 금액에 순차 적용하는 함수 제작
# 할인율이 적용된 주문 금액이 정수로 리턴된다.
# 쿠폰의 할인율은 백분율로 되어있다.
# 쿠폰의 개수는 주문 개수보다 많을 수 있다.
# comprehension을 사용한다.

# 입력 예시1
# [2000, 4000, 5000]
# coupon=50
# count=2

# 출력 예시1
# [1000, 2000]

# 입력 예시2
# [1000, 4000, 5000]
# coupon=30
# count=100

# 출력 예시2
# [700, 2800, 3500]

# def order_info(*args, **kwargs):
#     '''
#
#     :param args: 주문 금액
#     :param kwargs: 쿠폰 할인율
#     :return:
#     '''
#     pay_list = list(args)
#     count = kwargs.get('count')
#     discount = int(kwargs.get('coupon')) / 100
#     ran = len(pay_list)
#
#     if ran >= count:
#         for i in range(count):
#             print(pay_list[i] - (pay_list[i] * discount))
#
#     elif ran < count:
#         for i in range(ran):
#             print(pay_list[i] - (pay_list[i] * discount)))
#
#     result = [pay - pay * sale for pay in pay_list if len(list(args)) <= count else pay_list = count]
#     print(result)





#
#
# pay = [10000, 4000, 5000]
#
#
# def user_coupon(*args, **kwargs):
#     count = kwargs['count']
#     discount = 1 - kwargs['coupon'] * 0.01
#
#     result = [item if args.index(item)-count >= 0 else round(item * discount) for item in args]
#     return result
#
#
# print(user_coupon(*pay, coupon=10, count=3))
#
# print(user_coupon(*pay, coupon=10, count=1))

pay = [2000, 4000, 6000]
def order_info(*args, **kwargs):
    pay_list = args
    number = len(pay_list) # 주문 금액 개수(길이)
    count = kwargs.get('count') #쿠폰 개수

    #할인율
    discount = float(1 - kwargs.get('coupon')/100)
    # discount = int(kwargs.get('coupon')) / 100

    # 할인된 금액,
    # 주문 개수가 쿠폰의 개수보다 적을때 주문 개수 모두에 적용,
    # 주문 개수가 쿠폰의 개수보다 많을때 쿠폰 개수만큼 적용
    result = [int(round(pay_list[num] * discount)) if num < count else pay_list[num] for num in range(number)]
    # result = [int(pay_list[num] - (pay_list[num] * discount)) if num < count else pay_list[num] for num in range(number)]
    print(result)

order_info(*pay, coupon=50, count=2)

# def coupon_discount (pay_list, coupon, count):
#     '''
#
#     :param pay_list: 회원의 주문 금액 리스트
#     :param coupon: 쿠폰 할인율
#     :param count: 쿠폰 개수
#     :return:
#     '''
#
#     discount = [int(round(pay * (1 - coupon / 100))) if pay_list < count else pay_list for pay in range(pay_list)]
#     count -= 1
#     return discount
#
#
# pay_list = [2000, 4000, 5000]
# coupon = 50
# count = 1
# result = coupon_discount(pay_list, coupon, count)
# print(result)

# def use_coupon(*pay, **kwargs):
#     '''
#
#     :param pay: 주문 금액들
#     :param kwargs: {coupon: 할인율, count: 쿠폰의 개수}
#     :return:
#     '''
#
#     if 'coupon' in kwargs:
#         return [
#             int((1 - kwargs.get('coupon') * 0.01) * pay[i]) #할인된 금액
#             for i in
#             range(kwargs.get('count') if kwargs.get('count') <= len(pay) else len(pay))
#         ]
#
#     return None
#
# result = use_coupon(1000, 2000, 3000, coupon=50, count=2)
#
# if result:
#     print(result)
# else:
#     print('쿠폰이 없습니다.')

# pay = [2000, 4000, 6000]
# def order_info(*arg, **kwargs):
#     pay_list = arg
#     number = len(pay_list) #주문 개수
#     count = kwargs.get('count') #쿠폰 개수
#     discount = int(kwargs.get('coupon'))/100 #할인율
#
#     result = [int(pay_list[num] - (pay_list[num] * discount)) if num < count else pay_list[num] for num in range(number)]
#     # 할인된 금액,
#     # 주문 개수가 쿠폰의 개수보다 적을때 주문 개수 모두에 적용,
#     # 주문 개수가 쿠폰의 개수보다 많을때 쿠폰 개수만큼 적용
#
#     print(result)
#
# order_info(*pay, coupon=50, count=2)