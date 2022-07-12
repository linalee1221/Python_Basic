# 지역변수가 지역 내부에서만 호출 가능하며 지역이 소멸하면
# 같이 소멸되는 유형의 함수였다면, 전역변수는 프로그램 내부 어디에서도
# 호출이 가능하며 프로그램 종료 전까지 유지되는 변수이다.
sale_rate = 0.9 # 전역변수

def calc_price(price):
    print("오늘의 할인율: ", sale_rate)
    today_price = price * sale_rate # 지역변수
    print("오늘의 가격: ", today_price)

calc_price(10000)
sale_rate=0.7
calc_price(1000)
print(sale_rate)
#print(today_price)#에러발생
# 들여쓰기가 돼있으면 지역변수, 없으면 전역변수

