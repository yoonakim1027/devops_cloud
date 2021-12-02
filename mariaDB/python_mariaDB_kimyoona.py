from tkinter import *
import pymysql
from tkinter import messagebox
from tkinter import ttk

conn = None
cur = None

# 데이터베이스 접속
conn = pymysql.connect(
    host="127.0.0.1", user="root", password="1234", db="sqlDB", charset="utf8"
)


win = Tk()

win.geometry("500x900")
win.title("Don't buy a Family, Become the Family")

# Label -> 글 ?써지는거 ?
label1 = Label(win, text="\n♥ 유기동물 입양 사이트 입니다 ♥",  font="NanumGothic 17")
label1.pack() # .pack() 구동? 실행 ?
label2 = Label(win, text="\n 소형견 : 1 ~ 8 kg \n 중형견 : 8 ~ 12 kg \n대형견 : 12 ~ kg")
label2.pack()


class MyFrame(Frame):  # 클래스 정의
    def __init__(self, master):
        img = PhotoImage(file='C:/Users/user/Desktop/MariaDB/chrong.png')  # 이미지 읽고
        lbl = Label(image=img)  # 이미지 넣어
        lbl.image = img  # 레퍼런스 추가
        lbl.pack()


def main():  # 메인함수로 정의
    win.title('유기동물 입양 사이트')
    win.geometry('500x900')
    myframe = MyFrame(win)  # 클래스 사용


if __name__ == '__main__':  # 메인함수 호출
    main()



# Button(버튼 만드는거)




# 버튼 클릭하면 나오는 정보
def clickButton():
    messagebox.showinfo("유기동물 정보 저장", "동물 친구 정보가 저장되었습니다")

# 버튼 누르고 나서 이동하는 화면

def selectAllData():
    conn = None
    cur = None

    userName = edit1.get()
    region = edit2.get()
    today_date = edit3.get()

    luserName, lregion, ltoday_date = [], [], []

    conn = pymysql.connect(host='127.0.0.1', user='root', password='1234', db='mariaDB', charset='utf8')

    cur = conn.cursor()

    luserName.append("신청자 이름")
    luserName.append("--------")

    lregion.append("거주지역")
    lregion.append("--------")

    ltoday_date.append("신청날짜")
    ltoday_date.append("--------")

    sql = "SELECT userName, region, today_date FROM newusertbl"


def new1():
    global new
    new = Toplevel()
    win.geometry("400x600")
    win.title("Don't buy a Family, Become the Family")


    # 입력받는 것  : editFrame
    # 조회 : listframe

    def selectData():
        conn = None  # 접속할 때 쓸 애
        cur = None  # 내가 조정할 수 있게 execute
# -- <<<<<<<<<<<<<< groundOX 수정해라>>>>>>>>>>>>
        # 실제 데이터
        # breed, color, sex, age, size,  protected_place,,protected_date
        lbreed, lcolor, lsex, lage, lsize, lprotected_place, lprotected_date = [], [], [], [], [], [], []

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

        # SELECT 기능 구현
        sql = "SELECT breed, color, sex, age, size, protected_place, protected_date FROM lostpettbl"
        cur.execute(sql)  # 패치를 받아서 우리가 리스트를 넣을 수 있게 되는 것

        while (True):
            row = cur.fetchone()  # 커서
            if row == None:
                break  # while을 멈출 것
            lbreed.append(row[0])
            lcolor.append(row[1])
            lsex.append(row[2])
            lage.append(row[3])
            lsize.append(row[4])
            lprotected_place.append(row[5])
            lprotected_date.append(row[6])

        # GUI ListBox에 insert
        # ListUserID, ListName, ListBirthYear, ListAddr
        # 1) 리스트 박스 초기화(초기화 안하면 계속 뒤에 붙음)
        # 화면을 안지워주면 화면 뒤에 붙게 되어있음
        # 초기화가 항상 기본임
        listbreed.delete(0, listbreed.size() - 1)  # 처음 갖고있던 사이즈 -1
        listcolor.delete(0, listcolor.size() - 1)
        listsex.delete(0, listsex.size() - 1)
        listage.delete(0, listage.size() - 1)
        listsize.delete(0, listsize.size() - 1)
        listprotected_place.delete(0, listprotected_place.size() - 1)
        listprotected_date.delete(0, listprotected_date.size() - 1)

        # 2) select 해온 데이터 insert. 여기가 insert
        # 화면
        for item1, item2, item3, item4, item5, item6, item7\
                in zip(lbreed, lcolor, lsex, lage, lsize, lprotected_place,lprotected_date):
            listbreed.insert(END, item1)
            listcolor.insert(END, item2)
            listsex.insert(END, item3)
            listage.insert(END, item4)
            listsize.insert(END, item5)
            listprotected_place.insert(END, item6)
            listprotected_date.insert(END, item7)

        conn.close()  # 엔터치면 종료됨 !

        # -----------------------
    def insertData():
        conn = None  # 접속할 때 쓸 애
        cur = None  # 내가 조정할 수 있게 execute
            # 데이터베이스 접속
        conn = pymysql.connect(host='127.0.0.1',# 데이터베이스 연동 함수
                                user='root',
                                password='1234',
                                db='sqlDB',
                                charset='utf8')  # 내 로컬 호스트에 접속

        # 커서
        cur = conn.cursor()

        # 회원 정보 insert 기능 구현
        # 사용자에게 데이터를 받아야 함 (단독의 데이터 한 건씩이니까 리스트로 안해도 됨)
        # 사용자에게 입력 받은 회원 정보 초기화
        breed, color, sex, age, size, protected_place,protected_date = "", "", "", "", "", "",""

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
              "('" + breed + "' ,'" + color + "', '" + sex + "'," \
                "'" + age + "', '" + size + "','" + protected_place + "', CURDATE())"
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
            messagebox.showerror("입력오류", "데이터 입력 오류가 발생 했습니다.")  # 오류처리
        else:
            # 오류가 안나면 ? -> 오류가 안나고 잘 됬다고도 말해줘야함
            # 쿼리 실행이 완료(오류 없이)
            # 1) 메시지 박스로 성공알림
            messagebox.showinfo("성공", "동물친구 정보가 등록 되었습니다.")
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


        conn.close()  # 엔터치면 종료됨 !
    # 오류는 나더라도 시스템은 계속 진행되어야 하기때문에 예외/오류를 정해줘야함!

    # 라벨 만들기 라텔 - 텍스트박스
    # 화면에 항목 뜨게 하기

    label1 = Label(new, text="품종")
    label1.pack(side=TOP, padx=10, pady=10)

    edit1 = Entry(new, width=10)
    edit1.pack(side=TOP, padx=10, pady=10)

    label2 = Label(new, text="색상")
    label2.pack(side=TOP, padx=10, pady=10)

    edit2 = Entry(new, width=10)
    edit2.pack(side=TOP, padx=10, pady=10)

    label3 = Label(new, text="성별")
    label3.pack(side=TOP, padx=10, pady=10)

    edit3 = Entry(new, width=10)
    edit3.pack(side=TOP, padx=10, pady=10)

    label4 = Label(new, text="나이")
    label4.pack(side=TOP, padx=10, pady=10)

    edit4 = Entry(new, width=10)
    edit4.pack(side=TOP, padx=10, pady=10)

    label5 = Label(new, text="몸집크기")
    label5.pack(side=TOP, padx=10, pady=10)

    edit5 = Entry(new, width=10)
    edit5.pack(side=TOP, padx=10, pady=10)

    label6 = Label(new, text="보호장소")
    label6.pack(side=TOP, padx=10, pady=10)

    edit6 = Entry(new, width=10)
    edit6.pack(side=TOP, padx=10, pady=10)


    # 버튼영역
    # 입력
    btnInsert = Button(new, text="입력", command=insertData)
    btnInsert.pack(side=LEFT, padx=10, pady=10)

    # 조회
    btnSelect = Button(new, text="조회", command=selectData)
    btnSelect.pack(side=LEFT, padx=10, pady=10)

    # listbreed, listcolor, listsex, listage, listsize, listprotected_place

    listbreed = Listbox(new)
    listbreed.pack(side=LEFT, fill=BOTH, expand=1)

    listcolor = Listbox(new)
    listcolor.pack(side=LEFT, fill=BOTH, expand=1)

    listsex = Listbox(new)
    listsex.pack(side=LEFT, fill=BOTH, expand=1)

    listage = Listbox(new)
    listage.pack(side=LEFT, fill=BOTH, expand=1)

    listsize = Listbox(new)
    listsize.pack(side=LEFT, fill=BOTH, expand=1)

    listprotected_place = Listbox(new)
    listprotected_place.pack(side=LEFT, fill=BOTH, expand=1)

    listprotected_date = Listbox(new)
    listprotected_date.pack(side=LEFT, fill=BOTH, expand=1)

    # 삭제
    def deleteData():
        conn = None
        cur = None

        conn = pymysql.connect(host='127.0.0.1', user='root', password='1234', db='mariaDB', charset='utf8')

        cur = conn.cursor()

        memberID = listuserName.get(listuserName.curselection())
        print(memberID)

        sql = "DELETE FROM newusertbl WHERE username = '" + username + "'"

        print(sql)

        try:
            cur.execute(sql)
        except:
            messagebox.showerror("삭제오류", "데이터 삭제 오류가 발생 했습니다.")
        else:
            messagebox.showinfo("성공", "회원 정보가 삭제되었습니다.")
            conn.commit()
            selectAllData()

        conn.close()





def new2():
    global newtwo
    newtwo = Toplevel()

    win.geometry("600x1000")
    win.title("Don't buy a Family, Become the Family")

    def selectData1():
        conn = None  # 접속할 때 쓸 애
        cur = None  # 내가 조정할 수 있게 execute

        # 실제 데이터
        # userName, region, typeOfResidence
        luserName, lregion, ltodayDate = [], [], []
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
        luserName.append("---------------")
        luserName.append("이름")
        luserName.append("---------------")

        lregion.append("---------------")
        lregion.append("거주지역")
        lregion.append("---------------")

        ltodayDate.append("---------------")
        ltodayDate.append("입양신청 날짜")
        ltodayDate.append("---------------")

        # SELECT 기능 구현
        sql = "SELECT userName, region, todayDate FROM newusertbl"
        cur.execute(sql)  # 패치를 받아서 우리가 리스트를 넣을 수 있게 되는 것

        while (True):
            row = cur.fetchone()  # 커서
            if row == None:
                break  # while을 멈출 것
            luserName.append(row[0])
            lregion.append(row[1])
            ltodayDate.append(row[2])

        # GUI ListBox에 insert

        # 1) 리스트 박스 초기화(초기화 안하면 계속 뒤에 붙음)
        # 화면을 안지워주면 화면 뒤에 붙게 되어있음
        # 초기화가 항상 기본임
        listuserName.delete(0, listuserName.size() - 1)  # 처음 갖고있던 사이즈 -1
        listregion.delete(0, listregion.size() - 1)
        listtodayDate.delete(0, listtodayDate.size() - 1)

        # 2) select 해온 데이터 insert. 여기가 insert
        # 화면
        for item1, item2, item3\
                in zip(luserName, lregion, ltodayDate):
            listuserName.insert(END, item1)
            listregion.insert(END, item2)
            listtodayDate.insert(END, item3)

        conn.close()  # 엔터치면 종료됨 !

        # -----------------------
    def insertData1():
        conn = None  # 접속할 때 쓸 애
        cur = None  # 내가 조정할 수 있게 execute
            # 데이터베이스 접속
        conn = pymysql.connect(host='127.0.0.1',

                                   # 데이터베이스 연동 함수
                                user='root',
                                password='1234',
                                db='sqlDB',
                                charset='utf8')  # 내 로컬 호스트에 접속

        # 커서
        cur = conn.cursor()

        # 회원 정보 insert 기능 구현
        # 사용자에게 데이터를 받아야 함 (단독의 데이터 한 건씩이니까 리스트로 안해도 됨)
        # 사용자에게 입력 받은 회원 정보 초기화
        userName, region, todayDate = "", "", ""

        # GUI에서 입력한 데이터 담기
        userName = edit1.get()
        region = edit2.get()


        # 기본적으로 sql초기화
        sql = ""
        # sql 쿼리 만들기
        sql = "INSERT INTO newusertbl(userName, region, todayDate) VALUES " \
              "('" + userName + "' ,'" + region + "', CURDATE())"
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
            messagebox.showerror("입력오류", "데이터 입력 오류가 발생 했습니다.")  # 오류처리
        else:
            # 오류가 안나면 ? -> 오류가 안나고 잘 됬다고도 말해줘야함
            # 쿼리 실행이 완료(오류 없이)
            # 1) 메시지 박스로 성공알림
            messagebox.showinfo("성공", "입양인 정보가 등록되었습니다.")
            # 2) 데이터 커밋 (진짜 저장)
            conn.commit()
            # 3) 테이블 조회 (새로고침) -> 내가 입력한 데이터가 가장 상위에 나오도록
            selectData1()

        # GUI에 입력한 데이터 삭제 (그냥 입력한 데로 남아있음 -> 이렇게 하면 입력하고 나면 지워짐)
        edit1.delete(0, "end")
        edit2.delete(0, "end")


        conn.close()  # 엔터치면 종료됨 !
    # 오류는 나더라도 시스템은 계속 진행되어야 하기때문에 예외/오류를 정해줘야함!

    # 라벨 만들기 라텔 - 텍스트박스
    # 화면에 항목 뜨게 하기
    # 이름, 거주지역, 거주형태, 입양신청날짜
    label1 = Label(newtwo, text="이름")
    label1.pack(side=TOP, padx=10, pady=10)

    edit1 = Entry(newtwo, width=10)
    edit1.pack(side=TOP, padx=10, pady=10)

    label2 = Label(newtwo, text="거주지역")
    label2.pack(side=TOP, padx=10, pady=10)

    edit2 = Entry(newtwo, width=10)
    edit2.pack(side=TOP, padx=10, pady=10)



    # 버튼영역
    # 입력
    btnInsert = Button(newtwo, text="입력", command=insertData1)
    btnInsert.pack(side=LEFT, padx=10, pady=10)

    # 조회
    btnSelect = Button(newtwo, text="조회", command=selectData1)
    btnSelect.pack(side=LEFT, padx=10, pady=10)

    btnDelete = Button(newtwo, text="삭제", command=deleteData1)
    btnDelete.pack(side=LEFT, padx=10, pady=10)




    listuserName= Listbox(newtwo)
    listuserName.pack(side=LEFT, fill=BOTH, expand=1)

    listregion = Listbox(newtwo)
    listregion.pack(side=LEFT, fill=BOTH, expand=1)

    listtodayDate = Listbox(newtwo)
    listtodayDate.pack(side=RIGHT, fill=BOTH, expand=1)

def deleteData1():
    conn = None
    cur = None

    conn = pymysql.connect(host='127.0.0.1', user='root', password='1234', db='mariaDB', charset='utf8')

    cur = conn.cursor()

    memberID = listuserName.get(listuserName.curselection())
    print(memberID)

    sql1 = "SELECT userName, region, todayDate DELETE FROM newusertbl WHERE userName = '" + userName + "'"

    print(sql1)

    try:
        cur.execute(sql1)
    except:
        messagebox.showerror("삭제오류", "데이터 삭제 오류가 발생 했습니다.")
    else:
        messagebox.showinfo("성공", "회원 정보가 삭제되었습니다.")
        conn.commit()
        selectData1()

        conn.close()



def matching():


    # global newthree
    # newnewthree = Toplevel()

    matching = Tk()

    matching.title("Don't buy a Family, Become the Family")
    matching.geometry("500x550")
    strs = StringVar()  # 변수선언
    strs2 = StringVar()


    conn = None  # 접속할 때 쓸 애
    cur = None  # 내가 조정할 수 있게 execute
    # 데이터베이스 접속
    conn = pymysql.connect(host='127.0.0.1',

                           # 데이터베이스 연동 함수
                           user='root',
                           password='1234',
                           db='sqlDB',
                           charset='utf8')  # 내 로컬 호스트에 접속

    def selectData2():
        conn = None  # 접속할 때 쓸 애
        cur = None  # 내가 조정할 수 있게 execute

        # 실제 데이터
        # L.size, L.breed, L.color,L.sex
        lsize, lbreed, lsex = [], [], []
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

        lsize.append("   크기")
        lsize.append("---------------")


        lbreed.append("   품종")
        lbreed.append("---------------")

        lsex.append("   성별")
        lsex.append("---------------")

# 중복데이터 - > DISTINCT를 통해서 했으면

# 포트폴리오 작성 시 보완해서 하기.
# 따로 입력하지 않아도 이미 값을 받아서 중복 하지 않도록
# 코드 정리가 필요하다
#  grid() 랑 pack()는 같이 사용 불가능.


        # SELECT 기능 구현
        sql = "SELECT L.size, L.breed, L.sex ,L.protected_place FROM  lostpettbl L , newusertbl U, matchtbl M" \
              " WHERE L.size = M.size AND U.userName = M.userName AND  L.protected_place = U.region AND L.sex = M.sex"

        cur.execute(sql)  # 패치를 받아서 우리가 리스트를 넣을 수 있게 되는 것

        while (True):
            row = cur.fetchone()  # 커서
            if row == None:
                break  # while을 멈출 것
            lsize.append(row[0])
            lbreed.append(row[1])
            lsex.append(row[2])


        # GUI ListBox에 insert

        # 1) 리스트 박스 초기화(초기화 안하면 계속 뒤에 붙음)

        listsize.delete(0, listsize.size() - 1)  # 처음 갖고있던 사이즈 -1
        listbreed.delete(0, listbreed.size() - 1)
        listsex.delete(0, listsex.size() - 1)


        # 2) select 해온 데이터 insert. 여기가 insert
        # 화면
        for item1, item2, item3 in zip(lsize, lbreed, lsex):
            listsize.insert(END, item1)
            listbreed.insert(END, item2)
            listsex.insert(END, item3)

        conn.close()  # 엔터치면 종료됨 !



    def insert_info():
        sql = "SELECT userName, size, sex FROM matchtbl"
        # cur.execute(sql)  # 패치를 받아서 우리가 리스트를 넣을 수 있게 되는 것

        userName, size, sex = "", "", ""

        # GUI에서 입력한 데이터 담기
        userName = edit_name.get()
        size = Combx1.get()
        sex = Combx2.get()

        cur = conn.cursor()
        # 기본적으로 sql초기화
        sql = ""
        # sql 쿼리 만들기
        sql = "INSERT INTO matchtbl(userName, size, sex) VALUES " \
              "('" + userName + "' ,'" + size + "', '" + sex + "')"

        print(sql)


        try:
            cur.execute(sql)
        except:
            messagebox.showerror("입력오류", "데이터 입력 오류가 발생 했습니다.")  # 오류처리
        else:
            # 오류가 안나면 ? -> 오류가 안나고 잘 됬다고도 말해줘야함
            # 쿼리 실행이 완료(오류 없이)
            # 1) 메시지 박스로 성공알림
            messagebox.showinfo("매칭 정보 저장", "매칭 정보가 저장되었습니다")
            # 2) 데이터 커밋 (진짜 저장)
            conn.commit()
            conn.close()
            selectData2()

    listsize = Listbox(matching)
    listsize.grid(row=14, column=0)

    listbreed = Listbox(matching)
    listbreed.grid(row=14, column=1)

    listsex = Listbox(matching)
    listsex.grid(row=14, column = 2)

    # #### 신청자 이름 받기 #### 쿼리로 받아오기 newusertbl에서
    ## 입력으로 받기
    # def button_make():

    #이름 입력
    label_name = Label(matching, text="\n♥ 이름을 입력해 주세요.♥\n")
    label_name.grid(row=0, column=1)

    edit_name = Entry(matching, width=10)
    edit_name.grid(row=1, column=1)

    # 1번 문항
    lbl_title1 = Label(matching, text="\n선호하는 견종 크기를 선택해 주세요. ", fg="blue")
    lbl_title1.grid(row=2, column=1)

    lbl1 = Label(matching, text="	size", font="NanumGothic 10")
    lbl1.grid(row=3, column=0)


    Combx1 = ttk.Combobox(matching, textvariable=strs,width=20) #콤보박스 선언
    Combx1['value'] = ('--- 선택해주세요 ---','소형','중형','대형') #콤보박스 요소 삽입
    Combx1.current(0) #0번째로 콤보박스 초기화
    Combx1.grid(row=3, column=1) #콤보박스 배치


    lbl_01 = Label(matching,text="\n")
    lbl_01.grid(row=5,column=1)

    # 2번 문항

    lbl_title2 = Label(matching, text="선호하는 성별을 선택해주세요. ", fg= "blue")
    lbl_title2.grid(row=6, column=1)

    lbl2 = Label(matching, text="	sex", font="NanumGothic 10")
    lbl2.grid(row=7, column=0)


    Combx2 = ttk.Combobox(matching, textvariable=strs2, width=20)
    Combx2['value'] = ('--- 선택해주세요 ---','암컷','수컷')
    Combx2.current(0)
    Combx2.grid(row=7, column=1)


    lbl_02 = Label(matching,text="\n")
    lbl_02.grid(row=8,column=1)



    lbl02 = Label(matching, text="\n", font="NanumGothic 10")
    lbl02.grid(row=11, column=0)

    btn = Button(matching, text="선택 완료",command=insert_info,width=7,height=1, font= 'NanumGothic 15', fg='blue', bg='light pink', relief='groove' )
    btn.grid(row=12,column=1)

    lbl4 = Label(matching, text="\n#사지마세요 #입양하세요", font="NanumGothic 11")
    lbl4.grid(row=13, column=1)



btn1 = Button(win, text="내 정보 등록")
btn2 = Button(win, text="유기동물 등록")
btn3 = Button(win, text="유기동물 매칭")

btn1.config(command=new2)
btn2.config(command=new1)
btn3.config(command=matching)
# btn3.config(command=new2)

btn1.pack()
btn2.pack()
btn3.pack()

#btn2.pack_forget()
win.mainloop()

# num, userName, region, typeOfResidence, today_date

# 암묵적으로 컬럼만, null 로 명시해서 처리
# if문으로 컬럼안에 null이 아닌 애들만 받아서 처리하던가 ~

# join조건 ~
# 내가 어디까지 할거다~ 정도로만 하고, 나중에 발전된 버전
# 오늘 2021.11.26의 버전! 이렇게 포트폴리오로 저장해두기
# 나중에 발표할 때 비교하기

# 추가할 것  : 브라우저 종료, 뒤로가기
# 화면전환 프로세스 , 자기 창을 자기가 끄고, 검색버튼 누르면 검색 화면으로 이동
# 무슨 화면이 나와야 한다는 화면 설계 -> 자동으로 프로세스가 되도록~
# 코드에 대한 본인의 이해
# 본인이 코드를 작성하고, 코드를 이해하고 작성하고 받아들일 수 있어야 함

