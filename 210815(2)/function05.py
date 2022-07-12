# 함수의 리턴값은 오로지 하나로 리턴된다.
# 하나의 변수에 담을 수 있게 리턴되며, 단 여러개를 나열한 경우는
# ,로 나열해 리턴구문을 사용하게 되며 이때는 튜플로 묶어서 
# 하나의 변수로 받을 수 있게 처리된다.
def sum_and_mul(n1,n2):
    return n1 + n2, n1 * n2
result = sum_and_mul(3,7)
print(result)

sum, mul = sum_and_mul(3,7)
print(sum)
print(mul)