# while문은 while조건식 : 을 이용해서
# 조건식이 True로 판단되는 동안 반복실행 하다가
# False로 판단되면 종료한다.
# 여태까지 작성한 while문은 전부 처음엔 True였는데
# 코드의 진행에 따라 조건식이 False로 변하며 실행이 종료되었다.
# while문의 조건식에 무조건 True로 판단되는 자료를 넣으면
# 무한루프라고 부르며 이 경우 구문은 종료되지 않는다.
num = 1
while True:
    # break 구문은 조건 여부와 상관없이 바로 반복문 종료
    if num >= 1:
        break
    print(str(num) + "번째 실행중입니다.")
    num += 1
