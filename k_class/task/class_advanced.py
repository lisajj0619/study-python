# 회원
# 번호, 아이디, 비밀번호, 이름
# 번호는 자동으로 1씩 증가한다.
# 관리자로 회원가입 시, 아이디 앞에 'admin_'을 자동으로 붙여준다(class method).

# class Customer:
#     number1 = 0
#
#     def __init__(self, id, password, name):
#         self.id = id
#         self.password = password
#         self.name = name
#         Customer.number += 1
#
#     @classmethod
#     def admin(cls, id, password, name):
#         cls.id = 'admin_' + id
#         return cls('admin_'+id, password, name)
#
#     def print_info(self):
#         print(self.number, id, self.password, self.name)
# #
# #
# customer = Customer.admin('qwe', '1234', '박유진')
# print(customer.number, customer.id, customer.password, customer.name)
# customer = Customer('abc', '33434','박유진')
# print(customer.number, customer.id, customer.password, customer.name)

# 회원
# 번호, 아이디, 비밀번호, 이름
# 번호는 자동으로 1씩 증가한다.
# # 관리자로 회원가입 시, 아이디 앞에 'admin_'을 자동으로 붙여준다(class method).
# class User:
#     # private: 자신의 클래스에서만 접근 가능
#     # 1. 외부에서 접근하지 말자!
#     # 2. 외부에서 접근할 때 꼭 메소드로 접근하자!
#     __user_number = 0
#
#     def __init__(self, user_id, user_password, user_name):
#         User.__user_number += 1
#         self.user_number = User.__user_number
#         self.user_id = user_id
#         self.user_password = user_password
#         self.user_name = user_name
#
#     @staticmethod
#     def get_number():
#         return User.__user_number
#
#     @classmethod
#     def set_admin(cls, **kwargs):
#         kwargs['user_id'] = 'admin_' + kwargs['user_id']
#         return cls(**kwargs)
#
#
# user = User('hds', '1234', '박유진')
# print(user.user_id)
#
# admin = User.set_admin(user_id='hds', user_password='1234', user_name='박유진')
# print(admin.user_id)
#
#
# print(User.get_number())








