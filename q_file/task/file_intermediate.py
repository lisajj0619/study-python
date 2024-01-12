# 파일의 단어의 빈도수 구하기

# alice.txt

# 오로지 알파벳만 검사하기
# 대소문자 구문없이 비교
# 글자수 2개 이상인 단어만 카운트 하기
# 빈도수 100회 이상인 단어만 카운트
# 전체 내용을 문자열로 가져오기: file.read()

# with open('alice.txt', 'r', encoding='utf-8') as file:
#      alice = ("".join(file.read()))
#
# alice_lower = (alice.lower())
# alice1 = (alice_lower.replace("'", " ").replace(".", " ").replace("-", " ").replace(",", " ").replace(":", " ").replace("`", " ").replace(";", " ").replace("!", " ").replace("?", " ").replace("(", " ").replace(")", " ").replace('"', " ").replace("'", " ").replace("_", " "))
# alice_list = (alice1.split())
# print(alice_list)

# for word in alice_list:



"""
[출력예]
the 1642
and 872
to 729
it 595
she 553
of 514
said 462
you 411
alice 398
in 369
...
"""



with open('alice.txt', 'r', encoding='utf-8') as file:
     content = file.read().lower()
temp = []
for character in content:
     if 'a' <= character <= 'z': #소문자 범위내에 있는지 확인
          temp.append(character) #있다면 temp리스트에 추가
     else:
          temp.append(" ") #알파벳 외의 문자가 있으면 공백으로 바꿈

content = "".join(temp)

#.split()으로 단어들의 알파벳을 따로 세어보고 단어 개수가 1보다 큰 단어만 words에 포함
words = [word for word in content.split() if len(word) > 1]

result = {} #dict로 바꿔야 key와 value값이 나옴

#단어들이 words리스트에 존재하는지 반복검사
for word in words:
     if result.get(word) is not None:
          result[word] += 1 #기존에 값이 있으면 1씩 증가

     else:
          result[word] = 1 #기존에 값이 없으면 1로 씌워짐

#카운팅 100개 이상인것만 다시 key와 value로 새로운 dict를 만듬
result = {
     word: result[word]
     for word in result if result[word] >= 100
}

#값을 .get이라는 함수에 넣고 reverse로 정렬을 해준다
#value를 가져오는 함수가 get
sorted_key = sorted(result, key=result.get, reverse=True)
for key in sorted_key:
     print(key, result[key])