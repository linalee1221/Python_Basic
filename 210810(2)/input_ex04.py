# 입력될 값이 정수로 사용할 것이 확정적이라면
# 굳이 입력 후에 변환해주는 것이 아니라
# 입력단계에서 아예 정수로 입력을 받는 것도 가능하다.
classroom = int(input("교실 갯수를 입력해주세요."))
desk = int(input("책상 갯수를 입력해주세요."))
sum = classroom * desk
print("수용인원은", sum, "명입니다.")
