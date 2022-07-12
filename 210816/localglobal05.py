# 지역 내부의 변수가 전역변수와 같ㅇ느 변수가 되도록 동기화 해야 한다.
# 이때 사용하는 키워드가 바로 global이다.
# global 키워드를 받은 변수는 전역변수와 동기화된다.
# 따라서 global키워드는 전역변수가 미리 선언되어야만 쓸 수 있다.
price = 1000
def sale():
    global price # 지역변수 price를 새로 만들지말고 동기화
    price = 500 # 전역변수 price의 값이 500으로 변경 
sale()
print(price)

