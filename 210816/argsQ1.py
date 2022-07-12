# 연습 - n개의 정수를 전달받아 가장 큰 숫자를 찾아 리턴하는
# 함수를 작성하세요. (get_max)

def get_max(*nums):
    max = nums[0]
    for num in nums:
        if(num>max):
            max = num
    return max

print(get_max(-14,95,-78,33,92,262,87,55))

# 더 간단한 방법

def get_max(*nums):
    maxnum = max(nums)
    return maxnum
print(get_max(-14,95,-78,33,92,262,87,55))



# 연습2
# n개의 정수를 입력받아 그 정수들의 평균을 리턴하는 코드를
# 작성해보세요. 단, 0개를 입력받는 경우는
# "입력받은 요소가 없습니다."라고 출력하세요.

def get_avg(*nums):
    numslen = len(nums)
    sum = 0
    if(numslen == 0):
        print("입력받은 요소가 없습니다.")
    else:
        for num in nums:
            sum+=num
        avg = sum / len(nums)
        return avg
print(get_avg())
