# 파이썬의 표준 출력함수는 print()이며
# 괄호 안에 출력하고 싶은 변수, 상수, 수식 등을 적는다.

value = 1234

# 코드 실행 단축키 = Ctrl + F11
print("value")
print(value * 2)
print("3+4")

4 * 5


# 변수와 문자열을 함께 출력하려면 + 혹은 ,로 나열한다.

a = "10"
print("a에 저장된 값은 " + a + " 입니다.")
print("a에 저장된 값은", a, "입니다.")

# print()구문은 자동으로 마지막에 커서가 다음줄로 넘어가도록
# 설정되어 있다. 다음줄로 커서를 넘기기 싫다면
# end 요소를 이용한다.
print(123, end=",")
print(456)

# 퀴즈
# end를 이용해서 '서울 대전 대구 부산 광주 제주'
# 라는 문자열을 print()구문 6개를 이용해 한줄로 출력해라
print("서울", end=" ")
print("대전", end=" ")
print("대구", end=" ")
print("부산", end=" ")
print("광주", end=" ")
print("제주")