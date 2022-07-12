# 다른 지역간에는 같은 이름의 변수를 서로 보유할 수 있다.
# 이 경우 각각의 변수는 서로 다른 변수로 간주된다.
def kim():
    temp = "김철수"
    print(temp)
def lee():
    temp = 2 ** 10
    return temp
def park(a):
    temp = a * 2
    print(temp)
kim()
print(lee())
park(6)