# 일정 범위에 리스트에 빈 리스트를 대입하면 해당 범위의 요소를 모두 삭제한다.
nums = [0,1,2,3,4,5,6,7,8,9]
print(nums)
nums[2:5] = []
print(nums)

# 요소 1개만 삭제할 때는 del이라는 명령을 사용한다.
del nums[4]
print(nums)

# 리스트에 +, * 연산을 적용하면 문자열에서의 연산과 동일하게 작동한다.
list1 = [1,2,3,4,5]
list2 = [10,11]
listadd = list1 + list2
print(listadd)

listmulti = list2 * 4
print(listmulti)