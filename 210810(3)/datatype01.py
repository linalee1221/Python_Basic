# 파이썬의 변수는 선언시 별도의 데이터타입을 지정하지 않는다.
# 데이터타입은 변수에 저장되는 자료의 속성을 의미하는데
# 정수, 실수, 문자, 논리 등이 있다.
# 파이썬에서는 데이터타입 구분을 하지만 다른 언어처럼 변수에
# 저장할 때 변수 자체에서 받아들일 데이터타입을 결정하는게 아니라
# 최초로 대입되는 값을 데이터타입으로 결정한다.
# 변수에 대입된 값은 언제든 다른 값으로 교체할 수 있다.
# 변수의 타입을 알고 싶을 때는 type()으로 감싸서 확인한다.
value = 1234
print(type(value))
value = "가나다라"
print(type(value))
value = 1.2345
print(type(value)) 