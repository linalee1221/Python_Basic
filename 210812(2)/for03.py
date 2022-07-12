# in 왼쪽에 변수를 사용하면 그 변수는 in 오른쪽 요소를 순서대로
# 받아서 저장할 수 있다.
# 그러나 그것이 반드시 실행문에서 in 왼쪽의 변수를 사용해야 한다는 의미는 아니다.
for a in range(5):
    print("Hello Python!")

for X in range(1, 51):
    if X % 10 == 0:
        print("+", end="")
    else:
        print("-", end="")
print()


for x in range(1, 51):
    if x % 10:
        print("-", end="")
    else:
        print("+", end="")
print()

for x in range(5) :
    print("-" * 9, end="")
    print("+", end="")
print()
x=1