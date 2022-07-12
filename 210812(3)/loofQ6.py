# 중첩 반복문은 바깥쪽 반복문이 세로를, 안쪽 반복문이 가로를 담당한다.
# 아래와 같은 형태의 별을 중첩 반복문을 이용해 찍어보자.
 #    *
 #   ***
 #  *****
 # *******
 
for i in range(1, 6):
    for j in range(5 - i):
        print(" ", end="")
    for i in range(2 * i - 1):
        print("*", end="")
    print()