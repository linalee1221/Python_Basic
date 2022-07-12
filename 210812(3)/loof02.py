# 아래 구문은 *을 다섯 번 연달아 찍는 구문이다.
# for i in range(5):
#     print("*", end="")
# 그렇다면 이 구문을 5번 반복시키면 5*5형 별을 찍을 수 있다.

for j in range(5):
    for i in range(5):
        print("*", end="")
    print()