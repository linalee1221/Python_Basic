# 파이썬은 전역 영역도 하나의 지역으로 간주하며 따라서 다른 지역간에는
# 같은 이름의 변수를 여럿 만들 수 있다는 규칙에 따라 전역변수와
# 지역변수를 동시에 같은 이름으로 생성할 수 있다.
# 이 경우 호출하는 위치에서 가장 가까운 변수가 우선적으로 호출된다.
price = 1000

def sale():
    price = 500
    print("local:", id(price))
    
sale()
print("global:", id(price))
print(price)

