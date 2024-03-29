# 원래 숫자와 문자간에는 기본적으로 +연산을 할 수 없다.
# 따라서 숫자를 문자로 바꿔주거나 문자를 솟자로 바꿔줘야 한다.
# 문자를 숫자로 바꾸는 방법은 int()를 이용하고,
# 숫자를 문자로 바꾸는 방법은 str()로 바꿀 숫자를 감싸준다.
s = "홍길동의 점수 : "
n = 96
print(s + str(n))

# int()를 이용해서 문자를 숫자로 바꿀 때는 문자열 안에 반드시
# 숫자가 들어가 있어야 한다.
print(10 + int("34"))

# 기본적으로는 int()는 괄호 사이의 문자를 10진수 숫자로 바꾼다.
# 그러나 ,를 이용해 뒤쪽에 숫자를 하나 더 기입하면 그 진법으로
# 바꿔서 출력해준다.
num1 = int('1a', 16)
num2 = int('110', 2)
print(num1, num2, int('77', 8))
