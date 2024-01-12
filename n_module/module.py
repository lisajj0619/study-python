import calc_add #같은 경로에 있는 파일일 경우
# import calc.calc_sub#다른 경로에 있는 파일일 경우 패키지 명부터 적는다.
# import calc.calc_sub as sub
from calc.calc_sub import sub
# from calc.calc import Calculator #Calculator가 클래스
from calc.calc import * # *은 모든 필드를 가져온다

import os
import sys

print(sys.path)
print(os.path.abspath(os.path.dirname(__file__)))

# if __name__ == '__main__': #실행할 파일
#     print(calc_add.add(2,3))
#     # print(calc.calc_sub.sub(10, 5))
#     # print(sub.sub(10, 5))
#     print(sub(10,5))
#     print('=' * 20)
#     c = Calculator(10, 5)
#     print(c.add())
#     print(c.sub())