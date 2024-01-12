#check함수는 주어진 key와 value를 사용하여 사용자를 찾는다. 즉, 중복검사
#핸드폰 번호와 계좌번호를 검사할 수 있다.
def check(*, key: str, value: str) -> dict: #key값 문자열, value값 문자열 리턴 타입은 dict 순서 바뀌지 않게 하기 위해 *붙임
    for bank in Bank.banks: #Bank클래스의 banks리스트(DB)에서 각 은행 정보를 가져온 뒤
        for user in bank: #사용자 검색하기 각 은행에서 회원의 정보를 가져온다.
            if user[key] == value: #입력받은 key와 value가 일치하는지 중복검사
                return user #찾을경우 사용자 정보를 리턴

    return None #일치하는 사용자를 찾지 못했을 경우 'None'을 반환

#은행에 공통적으로 들어가는 부분을 Bank클래스로 한번에 정의
class Bank:
    #정적변수 - 은행의 개수
    total_count = 3

    #은행의 개수만큼 저장공간을 확보해준다.
    banks = [[] for i in range(total_count)]

    #Bank클래스의 인스턴스변수를 초기화하기 위한 '__init__' 메소드이다.
    #클래스가 생성될 때 자동으로 호출, 필요한 정보를 받아 해당 인스턴스의 속성을 초기화
    def __init__(self, owner: str, account_number: str, phone: str, password: str, money: int):
        self.object = self #각 회원의 object 필드에는 필드의 주소값이 담긴다.
        self.owner = owner #예금주
        self.account_number = account_number #계좌번호 (중복 없음)
        self.phone = phone #핸드폰 번호 (중복 없음)
        self.password = password #비밀번호
        self.money = money #통장잔고

    @classmethod #wrappint, 기존 생성자에 추가할 기능을 작성한다.
    #클래스 메소드인 "open_account"를 정의
    #cls: 클래스메소드 자체를 가리키는 매개변수
    #bank_choice: 사용자가 선택한 은행을 나타내는 매개변수
    #**kwargs: 개설에 필요한 모든 회원정보를 받는다
    def open_account(cls, bank_choice, **kwargs):

        #사용자가 선택한 은행에 해당하는 클래스 객체(instance)를 생성
        #은행은 신한, 국민, 카카오중 사용자가 선택한 은행에 해당하는 클래스 객체를 생성
        #생성자는 소괄호()에 담고 객채화
        #bank_choice - 1:
        #예를 들어 새로운 계좌를 신한은행에서 열 때
        #new_account = Bank.open_account(bank_choice=1, .......)
        #bank list의 index값은 0부터 시작이므로 -1을 해서 0부터 선택 할 수 있게 한다.
        bank = [ShinHan, KookMin, KaKao][bank_choice - 1](**kwargs)

        #선택한 은행에 새로운 계좌 정보를 추가하고 "__dict__"는 'bank'객체의 속성을 딕셔너리로 반환
        #즉, 은행 셋 중 하나에 고객의 정보를 dict로 바꿔서 전달
        #상속을 받기 때문에 cls로 받아도 된다.
        cls.banks[bank_choice - 1].append(bank.__dict__)
        return bank #열린 계좌에 대한 정보를 리턴한다.

    @staticmethod #self를 쓰지 않을 때, 한 번에 모든 객체에 적용할 기능
    #정적 메소드인 "chech_account_number"를 정의한다.
    #account_number는 검색하는 계좌번호를 나타내는 문자열 매개변수
    #계좌번호의 정보를 dict로 바꿔서 전달
    def check_account_number(account_number: str) -> dict:

        #check 함수에서 검사할 key와 value를 전달한다.
        #리턴 값은 입력한 계좌번호를 사용하여 'check'함수를 호출하고 해당 계좌번호와 일치하는지 확인
        return check(key='account_number', value=account_number)

    @staticmethod
    #정적 메소드인 "check_phone"을 정의한다.
    #phone은 검색하는 핸드폰 번호를 나타내는 문자열 매개변수
    #핸드폰 번호의 정보를 dic로 바꿔서 전달
    def check_phone(phone: str) -> dict:

        #리턴 값은 입력한 핸드폰 번호를 사용하여 'check'함수를 호출하고 해당 핸드폰번호와 일치하는지 확인
        return check(key='phone', value=phone)

    #입금 - deposit 메소드를 정의
    #money: 예금할 금액을 나타내는 정수 매개변수
    #재정의 하지 않으면 ***레퍼런스 실행
    def deposit(self, money: int):

        #현재 계좌의 잔고인 'self.money'에 예금할 금액인 'money'를 더해주어 해당 계좌의 잔고가 증가하도록 한다.
        self.money += money

    #출금 - withdraw 메소드를 정의
    def withdraw(self, money: int):

        #현재 계좌의 잔고인 'self.money'에 출금할 금액인 'money'를 빼서 해당 계좌의 잔고가 줄어들도록 한다.
        self.money -= money

    #잔고 - balance 메소드를 정의

    def balance(self):

        #현재 계좌의 진고인 'self.money'를 리턴한다.
        return self.money

    #매직 메소드 'def __init__' 재정의
    #문자열을 출력하여 계좌 정보를 문자열로 반환
    def __str__(self):
        return f'{self.owner}, {self.account_number}, {self.phone}, {self.password}, {self.money}'

#신한은행 class를 정의하고 "Bank" class를 상속 받는다.
class ShinHan(Bank):

    #자식 class에서 부모 class와 동일한 메소드명으로 선언 즉, 오버라이딩
    #money: 입금할 금액을 나타내는 정수 매개변수
    def deposit(self, money: int):

        #신한은행에서 입금시 수수료가 50%이므로
        #//=: 입력된 금액을 2로 나눈 후에 해당 값을 다시 money에 할당한다.
        money //= 2

        #부모 class인 'Bank' class의 'deposit'메소드를 호출하여 입금을 처리한다.
        #위의 나눈 값을 전달하여 입금된다.
        super().deposit(money)

#국민은행 class를 정의하고 "Bank" class를 상속 받는다.
class KookMin(Bank):

    #withdraw메소드를 오버라이딩
    def withdraw(self, money: int):

        #국민은행에서 출금시 수수료가 50%이므로
        #출금할 금액과 출금 금액의 50%가 잔고에서 빠져나온다.
        #*=: 입력된 금액에서 1.5를 곱해 해당값을 다시 money에 할당한다.
        money *= 1.5

        #부모 class인 'Bank' class의 'withdraw'메소드를 호출하여 출금을 처리한다.
        #위의 값을 전달하여 출금된다.
        super().withdraw(int(money))

#카카오 class를 정의하고 "Bank" class를 상속 받는다.
class KaKao(Bank):

    #balance메소드를 오버라이딩
    def balance(self):

        #카카오에서 잔액조회시 재산의 반이 빠져나감
        #//=: 조회한 금액의 반으로 나눠 해당값을 다시 self.money에 할당한다.
        self.money //= 2

        #부모 class인 'Bank' class의 'balance'메소드를 호출하여 잔액조회를 처리한다.
        #위의 값을 전달하여 리턴
        return super().balance()

#이 파일이 실행하는 파일이다.
#프로그램의 시작점일 때 아래 코드 실행, 실행되길 원하는 코드를 아래에 넣어주는 것
if __name__ == '__main__':

    bank_menu = "1. 신한 은행\n" \
                "2. 국민 은행\n" \
                "3. 카카오 뱅크\n" \
                "4. 나가기\n"

    menu = "1. 개설\n" \
           "2. 입금\n" \
           "3. 출금\n" \
           "4. 잔액\n" \
           "5. 은행 선택 메뉴로 돌아가기\n"

    owner_message = "예금주: "
    account_number_message = "계좌번호: "
    phone_message = "핸드폰 번호: "
    password_message = "비밀번호(4자리): "
    money_message = "예치금: "
    deposit_message = "입금액: "
    withdraw_message = "출금액: "
    error_message = "다시 시도해주세요"

    while True:
        # 은행 선택 메뉴
        bank_choice = int(input(bank_menu))

        #4번을 선택했을 경우 나가기이므로 break로 빠져 나온다
        if bank_choice == 4:
            break
        #메뉴 번호 이외의 번호를 입력시 밑으로 내려가지 못하게 막아준다.
        #len(Bank.banks)은행의 개수가 늘어 날 수 있으므로 매번 바꿔줄 수 없으니 은행 전체 개수를 적어준다
        if bank_choice < 1 or bank_choice > len(Bank.banks):
            continue

        #은행 선택 후
        while True:
            #동일하게 나오는 공통 메뉴
            menu_choice = int(input(menu))

            #5번을 선택했을 경우 은행 선택 메뉴로 돌아가므로 break로 빠져 나온다
            if menu_choice == 5:
                break

            # 개설
            #1번(개설)을 선택했을 경우
            if menu_choice == 1:
                #예금주명 입력
                owner = input(owner_message)


                while True: #조건이 충족될 때 까지 입력을 계속한다.
                    #계좌번호를 입력받는다.
                    account_number = input(account_number_message)
                    #중복된 계좌번호인지 확인하고 중복이 아닐경우에 종료
                    #None은 False값이지만, 가독성과 직관성을 높이기 위해 is 연산자로 검사한다.

                    if Bank.check_account_number(account_number) is None:
                        break

                while True:
                    #전화번호 입력
                    phone = input(phone_message)
                    #중복된 전화번호인지 확인하고 중복이 아닐경우에 종료
                    if Bank.check_phone(phone) is None:
                        break

                while True:
                    #비밀번호 입력
                    password = input(password_message)
                    #비밀번호의 길이가 4자리인지 확인, 4자리일 경우 종료
                    if len(password) == 4:
                        break

                #계좌 개설시 초기 입금액을 입력받는다.
                money = int(input(money_message))

                #선택한 은행의 계좌를 개설하고 개설된 계좌의 정보를 출력한다.
                #어떤 은행에서 개설했는 지를 baank_choice에 담아서 전달한다.
                #open_account()는 회원의 정보를 **kwargs로 받기 때문에 모두 풀어서 전달해준다.
                user = Bank.open_account(bank_choice, owner=owner, account_number=account_number, phone=phone, password=password, money=money)

                #재정의한 __str__()이 사용되고, 회원의 전체 정보를 확인한다.
                print(user)


            # 입금
            # 실습: 개설한 은행에서만 입금 가능(신한은행)
            #2번(입금)을 선택한 경우
            elif menu_choice == 2:
                #계좌번호를 입력받는다.
                account_number = input(account_number_message)
                #중복된 계좌번호인지 확인
                user = Bank.check_account_number(account_number)
                if isinstance(user.get('object'), ShinHan):
                    if bank_choice != 1:
                        print('개설한 은행에서만 입금 서비스를 사용하실 수 있습니다.')
                        continue
                if user is not None:#중복된 계좌번호일 경우
                    #패스워드 입력받기
                    if user['password'] == input(password_message):
                        deposit_money = int(input(deposit_message))
                        user['object'].deposit(deposit_money)
                        continue


                else:
                    print(error_message)

            # 출금
            elif menu_choice == 3:
                account_number = input(account_number_message)
                user = Bank.check_account_number(account_number)
                if user is not None:
                    if user['password'] == input(password_message):
                        #출금액을 입력받는다.
                        withdraw_money = int(input(withdraw_message))
                        #로그인한 회원의 은행이 국민은행이라면,
                        #출금 수수료가 50%이기 때문에, 잔액 검사시 1.5를 곱해준다.
                        if withdraw_money * (1.5 if isinstance(user['object'], KookMin) else 1) <= user['money']:
                            user['object'].withdraw(withdraw_money)

                        else:
                            print(error_message)

                else:
                    print(error_message)

            # 잔액 조회
            elif menu_choice == 4:
                account_number = input(account_number_message)
                user = Bank.check_account_number(account_number)
                if user is not None:
                    if user['password'] == input(password_message):
                        print(f'현재 잔액: {user["object"].balance()}')
                        continue

                else:
                    print(error_message)

            # 계좌 번호 재설정
            # 핸드폰 번호, 비밀번호 입력 후
            # 정확하면, 해당 회원의 계좌번호 재설정(다시 입력받기)
            elif menu_choice == 5:
                phone = input(phone_message)
                user = Bank.check_phone(phone)
                if user is not None:
                    if user['password'] == input(password_message):
                        while True:
                            account_number = input(account_number_message)
                            if Bank.check_account_number(account_number) is None:
                                break

                        #
                        user.get('object').account_number = account_number
                        continue

                print('핸드폰 번호 혹은 비밀번호를 다시 확인해주세요.')


            else:
                print(error_message)