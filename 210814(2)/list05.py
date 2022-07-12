# 리스트 내부에는 저장할 수 있는 자료 제한이 없기 때문에
# 리스트 내부에 리스트를 직접 적제하는것도 가능하다.

list1 = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
print(list1[0])
print(list1[2][1])

# 이중 리스트를 반복문 처리하여 모든 요소를 사용하려면
# 루프도 이중으로 돌아야 한다.
print("-"*40)
for sub in list1:
    for item in sub:
        print(item, end=" ")
    print()
    
