# 딕셔너리 자료형도 2개 이상을 합쳐줄 수 있다.
# 이 경우 기존 딕셔너리.update(병합딕셔너리)를 사용하며
# 만약 key값이 겹치는 경우는 병합딕셔너리의 key값이 최종반영된다.
dic1 = {"boy":"소년","school":"학교","book":"서적"}
dic2 = {"student":"학생","teacher":"선생님","book":"책"}
dic1.update(dic2)
print(dic1)

# dict()를 이용해 비어있는 딕셔너리를 만들 수도 있고,
# 다른 자료형을 딕셔너리 자료형으로 변경할 수도 있다.
# 2차원 리스트를 딕셔너리로 변경 가능하다.
li = [
        ["이순신",95],
        ["김유신",84],
        ["강감찬",35]
     ]
print(li)

dic = dict(li)
print(dic)


#딕셔너리를 비우고 싶다면 빈 딕셔너리를 대입
#혹은 .clear()를 이용해 비울 수도 있다.
# dic = {}
# print(dic)
dic.clear()
print(dic)

