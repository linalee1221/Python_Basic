# continue 명령은 실행시 돌고 있던 바퀴를 강제로 종료시키고
# 바로 다음바퀴로 넘어가는 탈출구문이다.
# 전체 반복문의 종료 여부에는 영향을 미치지 않으며 오로지
# 돌고 있던 바퀴만 스킵하는 기능을 가지고 있다.

score = [92, 46, 22, -1, 87]

for s in score:
    if(s == -1):
        continue
    print(s)
print("점수처리완료")

# range()를 이용해 1 ~ 10 범위를 가지는 리스트를 생성하고
# for in문을 이용해 리스트 내부 요소를 순차적으로 출력하되
# 홀수값만 콘솔창에 출력되고 짝수는 continue 구문으로 생략하는
# 코드를 작성하기.

for a in range(1, 11):
    if a % 2 == 0:
        continue
    print(a, end=" ")
    
    