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
    userID, name, birthYear, addr = "", "", "", ""

    # GUI에서 입력한 데이터 담기
    userID = edit1.get()
    name = edit2.get()
    birthYear = edit3.get()
    addr = edit4.get()
# SELECT userID, name, birthYear, mdate
    # 기본적으로 sql초기화
    sql = ""
    # sql 쿼리 만들기
    sql = "INSERT INTO userTBL (userID, name, birthYear, addr, mdate) VALUES " \
          "('" + userID + "' ,'" + name + "', " + birthYear + ", '" + addr + "', CURDATE())"

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
        messagebox.showinfo("성공","회원 정보가 등록 되었습니다.")
        # 2) 데이터 커밋 (진짜 저장)
        conn.commit()
        # 3) 테이블 조회 (새로고침) -> 내가 입력한 데이터가 가장 상위에 나오도록
        selectData()

    # GUI에 입력한 데이터 삭제 (그냥 입력한 데로 남아있음 -> 이렇게 하면 입력하고 나면 지워짐)
    edit1.delete(0, "end")
    edit2.delete(0, "end")
    edit3.delete(0, "end")
    edit4.delete(0, "end")

    conn.close()  # 엔터치면 종료됨 !
# 오류는 나더라도 시스템은 계속 진행되어야 하기때문에 예외/오류를 정해줘야함!


def selectData():
    conn = None  # 접속할 때 쓸 애
    cur = None  # 내가 조정할 수 있게 execute

    # 실제 데이터
    lUserID, lName, lbirthYear, lAddr = [],[],[],[]
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
    lUserID.append("회원 ID")
    lUserID.append("---------------")
    lName.append("회원명")
    lName.append("---------------")

    lbirthYear.append("출생년도")
    lbirthYear.append("---------------")

    lAddr.append("회원 주소")
    lAddr.append("---------------")


    #SELECT 기능 구현
    sql = "SELECT userID, name, birthYear, addr FROM userTBL"
    cur.execute(sql) # 패치를 받아서 우리가 리스트를 넣을 수 있게 되는 것

    while(True):
        row = cur.fetchone() # 커서
        if row == None:
            break # while을 멈출 것
        lUserID.append(row[0])
        lName.append(row[1])
        lbirthYear.append(row[2])
        lAddr.append(row[3])
        # 우리는 출력이 목적이 아님!

    # GUI ListBox에 insert
    # ListUserID, ListName, ListBirthYear, ListAddr
    # 1) 리스트 박스 초기화(초기화 안하면 계속 뒤에 붙음)
    # 화면을 안지워주면 화면 뒤에 붙게 되어있음
    # 초기화가 항상 기본임
    listUserID.delete(0,listUserID.size()-1) #처음 갖고있던 사이즈 -1
    listName.delete(0, listName.size() - 1)
    listBirthYear.delete(0, listBirthYear.size() - 1)
    listAddr.delete(0, listAddr.size() - 1)

    # 2) select 해온 데이터 insert. 여기가 insert
    # 화면
    for item1, item2, item3, item4 in zip(lUserID, lName, lbirthYear, lAddr) :
        listUserID.insert(END, item1) #END - > 끝부터 담음
        listName.insert(END, item2)
        listBirthYear.insert(END, item3)
        listAddr.insert(END, item4)

    conn.close()  # 엔터치면 종료됨 !


# gui 화면구성
window = Tk()
window.geometry("800x300")

# 타이틀
window.title("MariaDB 연동 GUI")

# 입력받는 것  : editFrame
# 조회 : listframe

editFrame = Frame(window)
editFrame.pack()

# list는 무조건 edit 밑에 있어야 함.
listFrame = Frame(window)
listFrame.pack(side=BOTTOM, fill=BOTH, expand=1)


# 라벨 만들기 라텔 - 텍스트박스
label1 = Label(editFrame, text="회원 ID")
label1.pack(side=LEFT, padx=10, pady=10)

edit1 = Entry(editFrame, width=10)
edit1.pack(side=LEFT, padx=10, pady=10)

label2 = Label(editFrame, text="회원명")
label2.pack(side=LEFT, padx=10, pady=10)

edit2 = Entry(editFrame, width=10)
edit2.pack(side=LEFT, padx=10, pady=10)

label3 = Label(editFrame, text="출생년도")
label3.pack(side=LEFT, padx=10, pady=10)

edit3 = Entry(editFrame, width=10)
edit3.pack(side=LEFT, padx=10, pady=10)

label4 = Label(editFrame, text="회원 주소")
label4.pack(side=LEFT, padx=10, pady=10)

edit4 = Entry(editFrame, width=10)
edit4.pack(side=LEFT, padx=10, pady=10)

# 버튼영역
# 입력
btnInsert = Button(editFrame, text="입력", command=insertData)
btnInsert.pack(side=LEFT, padx=10, pady=10)

# 조회
btnSelect = Button(editFrame, text="조회", command=selectData)
btnSelect.pack(side=LEFT, padx=10, pady=10)


listUserID = Listbox(listFrame)
listUserID.pack(side=LEFT, fill=BOTH, expand=1)

listName = Listbox(listFrame)
listName.pack(side=LEFT, fill=BOTH, expand=1)

listBirthYear = Listbox(listFrame)
listBirthYear.pack(side=LEFT, fill=BOTH, expand=1)

listAddr = Listbox(listFrame)
listAddr.pack(side=LEFT, fill=BOTH, expand=1)


window.mainloop()