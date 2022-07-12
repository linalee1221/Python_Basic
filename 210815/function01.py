# 함수는 반복적으로 사용되는 코드 다발을 함수 이름에 저장한 것이다.
# 변수에는 자료를 저장할 수 있다면 함수에는 실행문을 저장한다.
# 이 실행문은 불완전한 실행문일 수 있으며, 불완전한 실행문인경우
# 실행 가능한 상태로 만들기 위해 자료를 요청할 수 있다.
# 함수문법은 def함수이름(입력값):
# 아래에 실행문을 들여쓰기로 작성한다.

def add(a,b):
    print(a + b)
add(4, 5)

def calcsum(x):
    y = 0
    for num in range(x+1):
        y += num
    return y
result1 = calcsum(4)
result2 = calcsum(10)
print(result2)