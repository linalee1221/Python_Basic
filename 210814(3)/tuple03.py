# 튜플의 경우 리스트에서 사용할 수 있는 "조회" 연산은 모두 가능하다.
# .count()와 .index()를 사용할 수 있다.
# 그리고 튜플은 타 변수에 대입받을 경우 갯수가 맞다면 내부 요소를
# 나눠서 할당하는 기능도 가지고 있다.
tu = "홍길동", "이순신", "강감찬"

hong, lee, kang = tu
print(hong)
print(kang)
print(lee)

a, b = 10, 20
print(a, b)