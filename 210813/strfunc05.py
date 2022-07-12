# 파이썬에서는 문자열의 왼쪽과 오른쪽의 공백을 제거할 수 있는 명령어로
# .strip(), .lstrip(), .rstrip()을 제공한다.
# .strip()은 양쪽 공백 제거, .lstrip()은 왼쪽 공백 제거,
# .rstrip()은 오른쪽 공백을 제거한다.
s = "   abc1234   "
print(s + "님")
print(s.lstrip() + "님")
print(s.rstrip() + "님")
print(s.strip() + "님")