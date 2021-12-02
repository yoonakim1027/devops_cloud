import pymysql
from tkinter import *
from tkinter import messagebox



# 커서 받은 다음에 select 기능 구현



# 제일 먼저 해야하는 것
# import tkinter

# 데이터베이스 연동 함수
def insertData():
    conn = None  # 접속할 때 쓸 애
    cur = None  # 내가 조정할 수 있게 execute
# 데이터베이스 접속
    conn = pymysql.connect(host='127.0.0.1',
                           user='root',
                           password='1234',
                           db='sqlDB',
                           charset='utf8')  # 내 로컬 호스트에 접속
    # 커서
    cur = conn.cursor()

    # 회원 정보 insert 기능 구현
    # 사용자에게 데이터를 받아야 함 (단독의 데이터 한 건씩이니까 리스트로 안해도 됨)
    # 사용자에게 입력 받은 회원 정보 초기화
    breed, color, sex, age, size, find_date, protected_place = "", "", "", "", "", "", ""

    # GUI에서 입력한 데이터 담기
    breed = edit1.get()
    color = edit2.get()
    sex = edit3.get()
    age = edit4.get()
    size = edit5.get()
    protected_place = edit6.get()

    # 기본적으로 sql초기화
    sql = ""
    # sql 쿼리 만들기
    sql = "INSERT INTO lostpettbl(breed, color, sex, age, size, protected_place, protected_date) VALUES " \
          "('" + breed + "' ,'" + color + "', '" + sex + "','" + age + "', '" + size + "','" + protected_place + "', CURDATE())"
    print(sql)
    # print(sql) #배포할 땐 지워야함 !!! 그냥 확인용으로만 ~ 공유할 때는 지우고 올려야함
    # 쿼리 실행
    # << 예외처리 >>
    # 쿼리를 실행하면서, exception이 발생할 가능성이 높아짐 -> 사용자가 입력을 안할 경우, null값이 생길 경우
    # 그러면 이제 exception 구문을 정해줘야함!
    # try 구문 -> 오류가 발생할 수 있겠다는 가능성을~ 나면 그냥 진행, 아니면(except)여기에 들어감
    # 로직상으로는 사용자에게 데이터를 받아야 하는데, excetpion이 발생하는 경우 예외처리가 필요함 !
    try:
        cur.execute(sql)
    except:
        messagebox.showerror("입력오류","데이터 입력 오류가 발생 했습니다.") # 오류처리
    else:
        # 오류가 안나면 ? -> 오류가 안나고 잘 됬다고도 말해줘야함
        # 쿼리 실행이 완료(오류 없이)
        # 1) 메시지 박스로 성공알림
        messagebox.showinfo("성공","동물친구 정보가 등록 되었습니다.")
        # 2) 데이터 커밋 (진짜 저장)
        conn.commit()
        # 3) 테이블 조회 (새로고침) -> 내가 입력한 데이터가 가장 상위에 나오도록
        selectData()

    # GUI에 입력한 데이터 삭제 (그냥 입력한 데로 남아있음 -> 이렇게 하면 입력하고 나면 지워짐)
    edit1.delete(0, "end")
    edit2.delete(0, "end")
    edit3.delete(0, "end")
    edit4.delete(0, "end")
    edit5.delete(0, "end")
    edit6.delete(0, "end")
    edit7.delete(0, "end")

    # protected_date



    conn.close()  # 엔터치면 종료됨 !
# 오류는 나더라도 시스템은 계속 진행되어야 하기때문에 예외/오류를 정해줘야함!


def selectData():
    conn = None  # 접속할 때 쓸 애
    cur = None  # 내가 조정할 수 있게 execute

    # 실제 데이터
    # breed, color, sex, age, size, find_date, protected_place
    lbreed, lcolor, lsex, lage, lsize, lprotected_place, lprotected_date  = [],[],[],[],[],[],[]
    # 리스트


    # 데이터베이스 접속
    conn = pymysql.connect(host='127.0.0.1',
                           user='root',
                           password='1234',
                           db='sqlDB',
                           charset='utf8')  # 내 로컬 호스트에 접속
    # 커서
    cur = conn.cursor()

    # 데이터 초기화
    # lbreed, lcolor, lsex, lage, lsize, lfind_date, lprotected_place, lprotected_date
    lbreed.append("품종")
    lbreed.append("---------------")

    lcolor.append("색상")
    lcolor.append("---------------")

    lsex.append("성별")
    lsex.append("---------------")

    lage.append("나이")
    lsize.append("---------------")

    lsize.append("몸집크기")
    lsize.append("---------------")

    lprotected_place.append("보호장소")
    lprotected_place.append("---------------")

    lprotected_date.append("보호날짜")
    lprotected_date.append("---------------")


    #SELECT 기능 구현
    sql = "SELECT breed, color, sex, age, size, protected_place, protected_date FROM lostpettbl"
    cur.execute(sql) # 패치를 받아서 우리가 리스트를 넣을 수 있게 되는 것

    while(True):
        row = cur.fetchone() # 커서
        if row == None:
            break # while을 멈출 것
        lbreed.append(row[0])
        lcolor.append(row[1])
        lsex.append(row[2])
        lage.append(row[3])
        lsize.append(row[4])
        lprotected_place.append(row[5])
        lprotected_date.append(row[6])

        # 우리는 출력이 목적이 아님!

    # GUI ListBox에 insert
    # ListUserID, ListName, ListBirthYear, ListAddr
    # 1) 리스트 박스 초기화(초기화 안하면 계속 뒤에 붙음)
    # 화면을 안지워주면 화면 뒤에 붙게 되어있음
    # 초기화가 항상 기본임
    listbreed.delete(0,listbreed.size()-1) #처음 갖고있던 사이즈 -1
    listcolor.delete(0, listcolor.size() - 1)
    listsex.delete(0, listsex.size() - 1)
    listage.delete(0, listage.size() - 1)
    listsize.delete(0, listsize.size() - 1)
    listprotected_place.delete(0, listprotected_place.size() - 1)
    listprotected_date.delete(0, listprotected_date.size() - 1)

    # 2) select 해온 데이터 insert. 여기가 insert
    # 화면
    for item1, item2, item3, item4, item5, item6, item7\
            in zip(lbreed, lcolor, lsex, lage, lsize,lprotected_place, lprotected_date):
        listbreed.insert(END, item1)
        listcolor.insert(END, item2)
        listsex.insert(END, item3)
        listage.insert(END, item4)
        listsize.insert(END, item5)
        listprotected_place.insert(END, item6)
        listprotected_date.insert(END, item7)

    conn.close()  # 엔터치면 종료됨 !

## 얘 구역 def 1
# gui 화면구성
window = Tk()
window.geometry("1200x300")

# 타이틀
window.title("유기견 매칭 프로그램 ")

# 입력받는 것  : editFrame
# 조회 : listframe

editFrame = Frame(window)
editFrame.pack()

# list는 무조건 edit 밑에 있어야 함.
listFrame = Frame(window)
listFrame.pack(side=BOTTOM, fill=BOTH, expand=1)


# 라벨 만들기 라텔 - 텍스트박스
# 화면에 항목 뜨게 하기

label1 = Label(editFrame, text="품종")
label1.pack(side=LEFT, padx=10, pady=10)

edit1 = Entry(editFrame, width=10)
edit1.pack(side=LEFT, padx=10, pady=10)

label2 = Label(editFrame, text="색상")
label2.pack(side=LEFT, padx=10, pady=10)

edit2 = Entry(editFrame, width=10)
edit2.pack(side=LEFT, padx=10, pady=10)

label3 = Label(editFrame, text="성별")
label3.pack(side=LEFT, padx=10, pady=10)

edit3 = Entry(editFrame, width=10)
edit3.pack(side=LEFT, padx=10, pady=10)

label4 = Label(editFrame, text="나이")
label4.pack(side=LEFT, padx=10, pady=10)

edit4 = Entry(editFrame, width=10)
edit4.pack(side=LEFT, padx=10, pady=10)

label5 = Label(editFrame, text="몸집크기")
label5.pack(side=LEFT, padx=10, pady=10)

edit5 = Entry(editFrame, width=10)
edit5.pack(side=LEFT, padx=10, pady=10)


label6 = Label(editFrame, text="보호장소")
label6.pack(side=LEFT, padx=10, pady=10)

edit6 = Entry(editFrame, width=10)
edit6.pack(side=LEFT, padx=10, pady=10)



# 버튼영역
# 입력
btnInsert = Button(editFrame, text="입력", command=insertData)
btnInsert.pack(side=LEFT, padx=10, pady=10)

# 조회
btnSelect = Button(editFrame, text="조회", command=selectData)
btnSelect.pack(side=LEFT, padx=10, pady=10)




# listbreed, listcolor, listsex, listage, listsize, listprotected_place


listbreed = Listbox(listFrame)
listbreed.pack(side=LEFT, fill=BOTH, expand=1)

listcolor = Listbox(listFrame)
listcolor.pack(side=LEFT, fill=BOTH, expand=1)

listsex = Listbox(listFrame)
listsex.pack(side=LEFT, fill=BOTH, expand=1)

listage = Listbox(listFrame)
listage.pack(side=LEFT, fill=BOTH, expand=1)

listsize = Listbox(listFrame)
listsize.pack(side=LEFT, fill=BOTH, expand=1)


listprotected_place = Listbox(listFrame)
listprotected_place.pack(side=LEFT, fill=BOTH, expand=1)

listprotected_date = Listbox(listFrame)
listprotected_date.pack(side=LEFT, fill=BOTH, expand=1)


window.mainloop()