# 연습 - 정수를 입력받아 num이라는 변수에 저장 후
# 아래에 정의해 둔 calcsum()함수를 사용하여
# 1~xxx까지의 누적합:xxx 형식으로 출력하세요.
def calcsum(x):
    y = 0
    for num in range(x+1):
        y += num
    return y
num = int(input("정수를 입력하세요: "))
result = calcsum(num)
print("1~%d까지의 누적합: %d" % (num, result))