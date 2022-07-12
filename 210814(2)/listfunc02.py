# 리스트 삭제
# 리스트 내부 요소를 삭제하는데는 인덱스 번호를 이용하거나 혹은
# 자료 그 자체를 지목해서 삭제할 수 있다.
# .remove(자료) : 삭제할 자료를 직접 지목
# del(리스트[인덱스번호]):해당 리스트의 해당 인덱스 번호 삭제
# 리스트[:]=[]해당 범위 자료 삭제, 슬라이싱 지정 가능
score = [88,95,70,100,99,80,78,50]
score.remove(100)
print(score)
del(score[2])
print(score)
score[1:4] = []
print(score)

# 리스트 내의 요소 전체 삭제하기
list1 = [1,3,5,7,9]
list1.clear()
print(list1)

list2 = [2,4,6,8,10]
list2[:]=[]
print(list2)