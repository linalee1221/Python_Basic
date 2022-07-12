# 파라미터(인수, 입력값, 매개변수)의 이름을 지어줄 때는
# 실제 용도에 맞게 지어주는 것이 좋습니다.
# 그렇게 되면 사용자가 전달하는 자료가 무슨 의미인지 인지하면서
# 전달할 수 있기 때문에 좀 더 사용자의 의도대로 사용하게 된다.
def get_items(weapon, armor):
    w = "'%s' 무기를 획득했습니다." % weapon
    a = "'%s' 방어구를 획득했습니다." % armor
    detail = w + "\n" + a
    return detail

print(get_items("대검","철갑옷"))
print(get_items("지팡이","누더기갑옷"))
print(get_items("청동갑옷","단검"))