# 문자열 슬라이싱이란 범위를 지정해 여러 문자열을 묶어서
# 잘라오는 것을 의미한다.
# []를 이용해 잘라오게 되며 범위지정이기 때문에 : 을 이용해
# 문자열[시작값:끝값+1(:구간)]을 나타낸다.
# 끝값은 range()처럼 -1을 해줘야 정상적으로 작동한다.
s = "Python"

print(s[2:5]) # 2번~5-1번(4번) 인덱스까지 가져오기
print(s[3:])  # 맨 뒤 칸을 비우면 마지막 글자까지 자동 지정
print(s[:4])  # 앞 칸을 비우면 0번째로 자동 지정
print(s[2:-2])# 끝값은 물리적으로 -1 해줘야 함. 