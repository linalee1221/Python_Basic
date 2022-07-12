# 리스트 검색은 문자와 큰 차이가 없다.
# .index(자료) : 조회자료가 몇번 인덱스인지, 없을시 에러발생
# .count(자료) : 리스트 내에 찾는 자료가 몇개인지 정수로 출력
score = [88,92,100,78,95,66,32,74]
perfect = score.index(100)
print("만점받은 학생의 번호는 %d번 학생입니다." % (perfect+1))

pernum = score.count(100)
print("만점자의 수는 %d명입니다."% pernum)

# 리스트 길이 조회시 len을 사용하며, 최대값은 max()
# 최소값은 min()을 사용해서 구할 수 있다.
print("학생 수는 %d명입니다." % len(score))
print("최고점수는 %d점입니다." % max(score))
print("최저점수는 %d점입니다." % min(score))

