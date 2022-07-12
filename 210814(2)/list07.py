# 리스트 내포(list comprehension)
# 리스트 내부의 자료 하나하나마다 특정 조건을 걸어서 새롭게 저장할 때 사용한다.
# 반복문으로 대체할 수 있지만 리스트 내포가 좀 더 코드가 간결하다.
list1 = [1,2,3,4,5,6,7,8,9,10]
# 위 리스트를 for문으로 내부 요소 하나하나에 2씩 곱해 저장하기
list2 = []
for i in list1:
    list2.append(i * 2)
print(list2)

# 리스트 내포 문법 => [저장규칙 for 변수 in 배열]
# 배열요소를 변수에 하나씩 번갈아가며 담아 저장규칙에 따라 새로 저장
list3 = [i * 2 for i in list1]
print(list3)

# 내부 요소 전체가 아닌 조건에 맞는 자료만 저장할 경우
# [저장규칙 for 변수 in 배열 if 조건식]
# 홀수에만 *2 해서 저장하고 짝수는 버리기
list4 = [i * 2 for i in list1 if i % 2 == 1]
print(list4)

# list1 내부에 있는 요소 중 짝수만 제곱해서 저장하기

print("-"*40)
list5 = [i * i for i in list1 if i % 2 == 0]
print(list5)