# 중첩 반복문은 바깥쪽 반복문이 세로를, 안쪽 반복문이 가로를 담당한다.
# 아래와 같은 형태의 별을 중첩 반복문을 이용해 찍어보자.
# *
# **
# ***
# ****

for j in range(1,5):
    for i in range(j):
        print("*", end="")
    print()