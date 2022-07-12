# 리턴값
# 리턴값은 함수를 호출한 위치에 가져다 줄 자료를 지정한다.
# return 전달값 형태로 지정한다.
# 함수 호출 구문은 return 자료가 있다면 return된 자료로 대체되므로
# 함수의 호출구문을 다른 함수의 인수로, 혹은 다른 변수에 결과값을
# 저장하는 용도로도 사용할 수 있다.
def add(num1, num2):
    return num1+num2
result = add(10,7)
print(result)
print(add(14,19))

# 모든 함수에 리턴값을 다 작성할 필요는 없다.
# 함수 실행 후 내부 로직만 실행하고 끝낼 의도라면 굳이
# 리턴을 적지 않고 실행할 실행문만 작성한다.
def multi(n1, n2):
    result = n1 * n2
    print("%d x %d = %d" % (n1,n2,result))
multi(4,7)
multi(11,9)

a = multi(3,6)
print(a)

#print(multi(7,2)*3) 에러발생

print(add(6,3)*3)