# 50개의 "-"를 출력하되 매 5번째에는 "+"가 출력되도록
# for in문을 작성하세요.

for a in range(1, 51):
    if a % 5 == 0:
        print("+", end="")
    else:
        print("-", end="")

# 50개의 "-"를 출력하되, 5, 15, 25, 35, 45번째마다 "+"가
# 출력되도록 for in 문을 작성하세요.
print()

for a in range(1, 51):
    if a % 10 == 5 :
        print("+", end="")
    else:
        print("-", end="")
