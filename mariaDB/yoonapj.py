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

win.geometry("600x1000")
win.title("Don't buy a Family, Become the Family")

# Label -> 글 ?써지는거 ?
label1 = Label(win, text="\n유기동물 입양 사이트 입니다",  font="NanumGothic 15")
label1.pack() # .pack() 구동? 실행 ?
label2 = Label(win, text="\n 소형견 : 1 ~ 8 kg \n 중형 : 8 ~ 12 kg \n 대형 : 12 ~ kg \n")
label2.pack()


class MyFrame(Frame):  # 클래스 정의
    def __init__(self, master):
        img = PhotoImage(file='C:/Users/user/Desktop/MariaDB/chrong.png')  # 이미지 읽고
        lbl = Label(image=img)  # 이미지 넣어
        lbl.image = img  # 레퍼런스 추가
        lbl.pack()


def main():  # 메인함수로 정의
    win.title('유기동물 입양 사이트')
    win.geometry('400x850')
    myframe = MyFrame(win)  # 클래스 사용


if __name__ == '__main__':  # 메인함수 호출
    main()






# Button(버튼 만드는거)


# 버튼 클릭하면 나오는 정보
def clickButton():
    messagebox.showinfo("유기동물 정보 저장", "동물 친구 정보가 저장되었습니다")

# 버튼 누르고 나서 이동하는 화면

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
        # breed, color, sex, age, size,  protected_place, groundOX(마당필요 유무),protected_date
        lbreed, lcolor, lsex, lage, lsize, lprotected_place, lgroundOX ,lprotected_date = [], [], [], [], [], [], [], []

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

        lgroundOX.append("보호장소")
        lgroundOX.append("---------------")

        lprotected_date.append("보호날짜")
        lprotected_date.append("---------------")

        # SELECT 기능 구현
        sql = "SELECT breed, color, sex, age, size, protected_place, groundOX,protected_date FROM lostpettbl"
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
            lgroundOX.append(row[6])
            lprotected_date.append(row[7])

            # 우리는 출력이 목적이 아님!

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
        listgroundOX.delete(0, listgroundOX.size() - 1)
        listprotected_date.delete(0, listprotected_date.size() - 1)

        # 2) select 해온 데이터 insert. 여기가 insert
        # 화면
        for item1, item2, item3, item4, item5, item6, item7, item8 \
                in zip(lbreed, lcolor, lsex, lage, lsize, lprotected_place, lgroundOX,lprotected_date):
            listbreed.insert(END, item1)
            listcolor.insert(END, item2)
            listsex.insert(END, item3)
            listage.insert(END, item4)
            listsize.insert(END, item5)
            listprotected_place.insert(END, item6)
            listgroundOX.insert(END, item7)
            listprotected_date.insert(END, item8)

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
        breed, color, sex, age, size, protected_place, groundOX ,protected_date = "", "", "", "", "", "", "",""

        # GUI에서 입력한 데이터 담기
        breed = edit1.get()
        color = edit2.get()
        sex = edit3.get()
        age = edit4.get()
        size = edit5.get()
        protected_place = edit6.get()
        groundOX = edit7.get()

        # 기본적으로 sql초기화
        sql = ""
        # sql 쿼리 만들기
        sql = "INSERT INTO lostpettbl(breed, color, sex, age, size, protected_place, groundOX, protected_date) VALUES " \
              "('" + breed + "' ,'" + color + "', '" + sex + "'," \
                "'" + age + "', '" + size + "','" + protected_place + "','"+ groundOX +"', CURDATE())"
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
        edit7.delete(0, "end")


        # protected_date

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

    label7 = Label(new, text="마당 필요 유무")
    label7.pack(side=TOP, padx=10, pady=10)

    edit7 = Entry(new, width=10)
    edit7.pack(side=TOP, padx=10, pady=10)

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

    listgroundOX = Listbox(new)
    listgroundOX.pack(side=LEFT, fill=BOTH, expand=1)

    listprotected_date = Listbox(new)
    listprotected_date.pack(side=LEFT, fill=BOTH, expand=1)



def new2():
    global newtwo
    newtwo = Toplevel()

    win.geometry("400x600")
    win.title("Don't buy a Family, Become the Family")

    def selectData1():
        conn = None  # 접속할 때 쓸 애
        cur = None  # 내가 조정할 수 있게 execute

        # 실제 데이터
        # userName, region, typeOfResidence
        luserName, lregion, lgroundOX, ltodayDate = [], [], [], []
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
        # luserName, lregion, ltypeOfResidence
        luserName.append("---------------")
        luserName.append("이름")
        luserName.append("---------------")

        lregion.append("---------------")
        lregion.append("거주지역")
        lregion.append("---------------")

        lgroundOX.append("---------------")
        lgroundOX.append("마당유무")
        lgroundOX.append("---------------")

        ltodayDate.append("---------------")
        ltodayDate.append("입양신청 날짜")
        ltodayDate.append("---------------")

        # SELECT 기능 구현
        sql = "SELECT userName, region, groundOX, todayDate FROM newusertbl"
        cur.execute(sql)  # 패치를 받아서 우리가 리스트를 넣을 수 있게 되는 것

        while (True):
            row = cur.fetchone()  # 커서
            if row == None:
                break  # while을 멈출 것
            luserName.append(row[0])
            lregion.append(row[1])
            lgroundOX.append(row[2])
            ltodayDate.append(row[3])

        # GUI ListBox에 insert

        # 1) 리스트 박스 초기화(초기화 안하면 계속 뒤에 붙음)
        # 화면을 안지워주면 화면 뒤에 붙게 되어있음
        # 초기화가 항상 기본임
        listuserName.delete(0, listuserName.size() - 1)  # 처음 갖고있던 사이즈 -1
        listregion.delete(0, listregion.size() - 1)
        listgroundOX.delete(0, listgroundOX.size() - 1)
        listtodayDate.delete(0, listtodayDate.size() - 1)

        # 2) select 해온 데이터 insert. 여기가 insert
        # 화면
        for item1, item2, item3, item4 \
                in zip(luserName, lregion, lgroundOX, ltodayDate):
            listuserName.insert(END, item1)
            listregion.insert(END, item2)
            listgroundOX.insert(END, item3)
            listtodayDate.insert(END, item4)

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
        userName, region, groundOX, todayDate = "", "", "", ""

        # GUI에서 입력한 데이터 담기
        userName = edit1.get()
        region = edit2.get()
        groundOX = edit3.get()


        # 기본적으로 sql초기화
        sql = ""
        # sql 쿼리 만들기
        sql = "INSERT INTO newusertbl(userName, region, groundOX, todayDate) VALUES " \
              "('" + userName + "' ,'" + region + "', '" + groundOX + "', CURDATE())"
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
        edit3.delete(0, "end")



        # protected_date

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

    label3 = Label(newtwo, text="마당유무")
    label3.pack(side=TOP, padx=10, pady=10)

    edit3 = Entry(newtwo, width=10)
    edit3.pack(side=TOP, padx=10, pady=10)







    # 버튼영역
    # 입력
    btnInsert = Button(newtwo, text="입력", command=insertData1)
    btnInsert.pack(side=LEFT, padx=10, pady=10)

    # 조회
    btnSelect = Button(newtwo, text="조회", command=selectData1)
    btnSelect.pack(side=LEFT, padx=10, pady=10)

    # luserName, lregion, ltypeOfResidence, ltoday_date
    # listbreed, listcolor, listsex, listage, listsize, listprotected_place



    listuserName= Listbox(newtwo)
    listuserName.pack(side=LEFT, fill=BOTH, expand=1)

    listregion = Listbox(newtwo)
    listregion.pack(side=LEFT, fill=BOTH, expand=1)

    listgroundOX = Listbox(newtwo)
    listgroundOX.pack(side=LEFT, fill=BOTH, expand=1)

    listtodayDate = Listbox(newtwo)
    listtodayDate.pack(side=LEFT, fill=BOTH, expand=1)

def matching():


    # global newthree
    # newnewthree = Toplevel()

    matching = Tk()

    matching.title("Don't buy a Family, Become the Family")
    matching.geometry("400x400")
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

    def clickButton():
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








    # #### 신청자 이름 받기 #### 쿼리로 받아오기 newusertbl에서
    ## 입력으로 받기
    # def button_make():

    #이름 입력
    label_name = Label(matching, text="\n이름을 입력해 주세요.\n")
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

    btn = Button(matching, text="선택 완료",command=clickButton,width=7,height=1, font= 'NanumGothic 15', fg='blue', bg='light pink', relief='groove' )
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