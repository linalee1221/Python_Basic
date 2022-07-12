# 문자열은 인덱싱을 이용해 일부 요소만 변경할 수 없다.
# 그러나 리스트는 일부 요소만 변경하는 것이 가능하다.
score = [88, 95, 70, 100, 99]
print(score[2])
score[2] = 77
print(score[2], score)
'''
s1 = "python"
s1[2] = "x"
'''
# 개별 요소 뿐만 아니라 범위를 지정하여 여러 요소를 일괄적으로 바꿀 수도 있다.
nums = [0,1,2,3,4,5,6,7,8,9]
print(nums)
nums[2:5] = [20, 30, 40]
print(nums)
nums[6:8] = [90, 91, 92, 93, 94]
print(nums)