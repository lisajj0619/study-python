# '택시'에서 승객들에게 공통적으로 적용되는 자료
# - 기본 요금 : 5800원
# - 기본 주행 거리 : 2km
# - 택시 요금(기본 주행 거리 이후 거리 1km 당 요금)  : 1000원

# 택시 객체 생성시 승객별로 돈과, 거리를 받아서 생성

# 거리에 따른 요금 계산 메소드 정의
# 거리에 따른 잔돈 계산 메소드 정의

# class Taxi:
#
#     basic_charge = 5800
#     basic_distance = 2
#     charge_per_km = 1000
#
#     def __init__(self, charge, distance):
#         self.charge = charge
#         self.distance = distance
#
#     def taxi_charge(self):
#         cost = Taxi.basic_charge
#         if self.distance > Taxi.basic_distance:
#             cost += (self.distance - Taxi.basic_distance) * Taxi.charge_per_km
#
#         return cost #잔돈을 계산하기 위해 리턴
#
#     def pay_back(self):
#         return self.charge - self.taxi_charge()
#
# taxi = Taxi(20000,1)
# print(taxi.taxi_charge(), taxi.pay_back())
#
# taxi = Taxi(30000, 10)
# print(taxi.taxi_charge(), taxi.pay_back())

#2.
class Taxi:
    #정적변수이므로 모든 객체가 공유한다.
    default_fare = 5800 #기본요금
    default_distance = 2 #기본 주행 거리
    fare_per_km = 1000 #km당 택시 요금

    #택시는 손님이 내리고 타면서 요금이 초기화 되기 때문에 요금을 초기화 해준다.
    def __init__(self):
        self.income = 0

    #택시 요금을 계산하는 메소드 선언
    def calculate_fare(self, money, distance):
        cost = Taxi.default_fare #택시요금
        if distance > Taxi.default_distance: #주행거리가 기본 주행 거리보다 많을 시
            cost += (distance - Taxi.default_distance) * Taxi.fare_per_km
            #택시 요금 = (주행거리 - 기본 주행 거리) * km당 요금

        #주행거리가 기본 주행 거리보다 적거나 같을 시
        self.income += cost #택시 요금 = 기본 요금

        #잔돈을 계산하는 메소드 선언
        def get_change():
            return money - cost #낸 금액에서 택시요금을 빼면 잔돈

        return cost, get_change() #택시요금과 잔돈을 리턴한다


taxi = Taxi()
print(taxi.calculate_fare(20000, 1))
print(taxi.calculate_fare(30000, 10))
print(taxi.income)
