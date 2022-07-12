# 문제
# 음식점 메뉴판을 만들어보겠습니다.
# 이 메뉴판은 메뉴를 추가할 수도 있고 추가된 메뉴를 확인할 수도 있는 메뉴판입니다.
# 1번 선택시 key(메뉴이름):value(가격,정수로) 를 foods에 입력
# 2번 선택시 "menu : foods[menu]원 입니다"라고 메뉴 이름과
# 가격을 전체메뉴를 이용해 출력하기
# ex) 김치찌개 : 7000원입니다.
# 3번은 종료로직이지만 이미 추가했으므로 생략
foods = {}

while True:
    print("\n======음식점 메뉴 관리 프로그램======")
    print("1. 신규 메뉴 등록")
    print("2. 메뉴판 전체 보기")
    print("3. 프로그램 종료")
    num = int(input("> "))
    
    if num == 1:
        name = input("메뉴명: ")
        
        if name in foods:
            print("이미 등록된 메뉴입니다.")
        else:
            price = input("가격: ")
            foods[name] = price
            print("신규 메뉴 %s(이)가 등록되었습니다." % name)
    elif num == 2:
        print("\n------메뉴판------")
        menulist = foods.keys()
        for menu in menulist:
            print(menu, ":", foods[menu], "원")
        # 메뉴판 전체보기를 한 다음 바로 메뉴판 보여주는게 아니라
        # select 변수에 input을 이용해서 추가로 선택지를 받는다.
        print("-"*40)
        print("1. 기존메뉴 수정 | 2. 메뉴 삭제 | 3. 나가기")
        select = int(input(">"))
        # select가 1일 경우는 가격을 변경할 메뉴 이름을 입력받고
        # 있는 메뉴명을 입력한 경우는 추가로 가격을 입력받아
        # 가격을 수정하게 만들어라.
        # 만약 없는 메뉴 이름을 넣었으면 "등록된 메뉴가 아닙니다."
        # 라고만 출력하면 된다.
        if select == 1:
            name = input("가격을 변경할 메뉴의 이름을 입력하세요: ")
            
            if name in foods:
                newprice = input("변경할 가격 입력: ")
                foods[name] = newprice
                print("%s의 가격이 %s원으로 변경되었습니다." % (name, newprice))
            else:
                print("%s(은)는 등록된 메뉴가 아닙니다." % name)
        # select가 2인 경우도 마찬가지로 삭제할 메뉴 이름을 입력받고
        # 있는 메뉴인 경우는 메뉴를 삭제하고
        # 없는 메뉴 이름을 넣었으면 "등록된 메뉴가 아닙니다."라고 출력해라
        elif select == 2:
            name = input("삭제할 메뉴의 이름을 입력하세요: ")
            
            if name in foods:
                del foods[name]
                print("%s(이)가 삭제되었습니다." % name)
            else:
                print("%s(은)는 등록된 메뉴가 아닙니다." % name)
    if num == 3:
        print("프로그램을 종료합니다. ")
        break