# .split("쪼갤지점")을 이용하면 쪼갤 지점을 지정해서
# 하나의 문자열을 여러개로 쪼갤 수 있다.
# 만약 .split()과 같이 쪼갤 지점을 입력하지 않는다면
# 그때는 그냥 띄어쓰기, 탭, 엔터키 등을 기준으로 쪼개준다.
s1 = "떡볶이 김말이 닭강정"
print(s1.split())
s2 = "서울->대전->대구->부산"
city = s2.split("->")
print(city)

for c in city:
    print(c, "찍고", end=" ")
print()