# 문자열은 숫자 자료에 비해 복잡하므로 보다 다양한 함수, 매서드를
# 사용해 편집하거나 조작할 수 있도록 지원한다.
# 함수 : 공용적으로 내장된 기능(. 없이 실행)
# 매서드 : 클래스에 속한 함수(.가 왼쪽에 붙음)
s = "python programming class"

print(len(s))

print(s.find("o"), s.rfind("o"))

s1 = "C programming"
if s1.find("java") == -1:
    print("C와 관련없는 단어입니다.")
else:
    print("C와 관련된 단어입니다.")
    
    
# print(s1.index("x")) # 에러발생

print(s.count("n"))
print(s.count("python"))


s2 = """생각이란 생각할수록 생각나므로 생각하지 말아야 할 생각은 
생각하지 않으려고 하는 생각이 좋은 생각이라고 생각합니다."""
print("'생각'의 등장 횟수: ", s2.count("생각"))