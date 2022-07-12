# 인수의 기본값
# 아래의 코드는 간격이 1인 경우도 간격을 입력해야 해서 불편하다.
def calc_stepsum(start, end, step):
    sum = 0
    for num in range(start, end + 1, step):
        sum += num
    return sum
print(calc_stepsum(1,10,2))

# 만약 일반적인 상황에 넣어주는 인수값이 정해져 있다면
# 디폴트값 선언을 통해 특수한 경우에만 인수를 입력하게 만들어줄 수도 있다.
def calc_stepsum2(start, end, step=1):
    sum = 0
    for num in range(start, end + 1, step):
        sum += num
    return sum
print(calc_stepsum(1,10,2))
print(calc_stepsum2(1,10))

# 인수의 기본값을 지정할 때는 항상 마지막에 지정해야 한다.
# def calc_sum(start, step = 1, end) <- X 에러발생

#키워드 인수 입력하기
# 함수를 호출할 때는 왼쪽부터 값을 하나씩 전달한다.
# 단, 예외적으로 원하는 순서대로 입력하고 싶을 경우는
# 인수 전달을 인수이름=값, 인수이름2=값2와 같이
# 이름을 지정해 전달할 수 있다.
# 일부 요소만 이름 지정시 지정 안한 요소의 위치를 주의해야 한다.
print(calc_stepsum(3,7,1))
print(calc_stepsum(step=1, end=7, start=3))
print(calc_stepsum(3, step=1, end=7))