# 함수를 호 출할 때는 함수 정의시에 지정한 인수(파라미터, 매개변수,
# 입력값)의 개수만큼 값을 전달해야 한다.
# 인수 개수가 달라지면 에러가 난다.
def add(n1, n2):
    return n1 + n2
def add_three(n1,n2,n3):
    return n1 + n2 + n3
result1 = add(3,6)
print(result1)

result2 = add_three(3,6,9)
print(result2)