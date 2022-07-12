# 리스트에서 사용하는 매서드들
# append(자료):배열의 마지막 인덱스+1 위치에 입력된 자료 전부 추가
# insert(위치,자료):지정한 위치 뒤로 기존 자료 밀어내고 새 자료 추가
# extend(리스트):리스트+리스트 처리(단 기존 리스트에 바로 적용)
nums = [1,2,3,4]
nums.append(5)
print(nums)

nums.insert(2, 99)
print(nums)

print("-"*40)
list1 = [1,2,3,4,5]
list2 = [10,11]
list1 + list2
print(list1, list2) # 이렇게 한다고 해서 list1과 list2에 변동이 있진 않는다.

list1.extend(list2)
print(list1) # list1과 list2의 내용이 변경되어 저장된다.