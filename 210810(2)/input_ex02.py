# input()으로 입력받은 값은 숫자를 넣어도 문자를 넣어도
# 자동으로 문자로 인식된다. 따라서 input()으로 입력받은
# 자료를 이용해서는 -, /연산 등을 할 수 없습니다.
a = input("첫 번째 숫자를 입력하세요: ")
b = input("두 번째 숫자를 입력하세요: ")
print("두 수의 합은:", (a + b))
