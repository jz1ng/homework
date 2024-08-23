#숫자 간 연산자
#-// = 나눗셈을 실시하고 나머지를 버리는것.(소숫점 뒷자리)
#-%  = 나눗셈을 실시하고 몫을 버리는것.(소숫점 뒷자리만 가짐)
#-** =숫자를 제곱하는것.

#자료형의 3가지
#-str 문자열 : 글귀 내용 등
#-int, float : 숫자 (정수, 실수)
#-bool : 부울리언 (참과 거짓으로 나눌수 있음)

#인덱싱 및 슬라이싱
print("Bring the light of a dying star"[8]) #8번째 글자만 가져옴
print("Bring the light of a dying star"[:15]) #15번째 숫자까지 가져옴
print("Bring the light of a dying star"[-12::2]) #
print("012345"[0:5:2]) #0부터 5전까지 2칸씩 건너뛰어 표기

#len()의 역할은?
# 문장의 길이를 알려줌

#변수란 무엇인가?
# a = b
# 변수의 선언이란? = 변수를 사용하려면 변수가 있다는것을 컴퓨터에게 알려주어야 한다. 이를 변수를 선언한다고 한다.
# 변수의 할당이란? =(변수 명 = 변수 할당 값)

num = 21
num += 32
num += 12
num += 4
print(num) #이 때 출력되는 num의 값은? 69이다. (21 + 32 + 12 + 4)

#과제
ticker = "btc_krw"
print(str.upper(ticker))

ticker2 = "BTW_KRW"
print(str.lower(ticker2))

w1 = 'name1 = {}, age1 = {}, name2 = {}, age2 = {}'.format("김민수", 13,"이철희",15)
print(w1)

age1 = 10
age2 = 13
name1 ="김민수"
name2 ="이철희"

w2 = f'{age1},{age2},{name1},{name2}'
print(w2)

#5
print("2020/03(E) (IFRS연결)"[:7])
#슬라이싱을 사용하여 2020/03을 출력

#6
data = " freedom "
print(data.strip())
print(data.lstrip())