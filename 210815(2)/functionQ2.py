# 문제
# get_weapon() 함수를 만들어주세요.
# 이 함수는 파라미터(매개변수, 입력값, 인자)로 입력받은 자료를
# 이용해서 "xx을(를) 획득했습니다."라고 출력해주는 함수입니다.
def get_weapon(w_name):
    w = "%s을(를) 획득했습니다." % w_name
    return w

print(get_weapon("도끼"))
print(get_weapon("지팡이"))
print(get_weapon("단검"))