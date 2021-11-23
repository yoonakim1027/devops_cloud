from tkinter import *
from tkinter import messagebox
# 2021.11.23
# 버튼 만들기/ 라벨 (내용) / 입력받아야 하기 때문에 입력 필요
# 입력 관련 연습

window = Tk()

# 버튼을 사용하여 알림 창 띄우기
def clickButton():
    messagebox.showinfo('버튼 클릭', '버튼을 클릭했습니다.')# messagebox 타이틀, messagebox 내용)


window.title("입력 관련 연습 ")
window.geometry("200x200")

# 프레임 : 영역을 나누기
# 엔트리 : 입력상자 (사용자에게 입력받는) -> 파이썬의 input type =text같은 느낌
# 리스트박스 : 목록 (결과 화면 -> 여러 개의 row를 표현해야 할 때 사용


# 1. 프레임으로 위아래를 나누기. upFrame, downFrame으로 나눠서 영역을 사용
upFrame = Frame(window) # 띄워줄 프레임
upFrame.pack() # upFrame이 먼저 위치선정을 한 것

midFrame =  Frame(window) # 윈도우가 두개의 프레임으로 나뉜것
midFrame.pack()
# pack 하지 않으면 안올라감



downFrame =  Frame(window) # 윈도우가 두개의 프레임으로 나뉜것
downFrame.pack()

button = Button(midFrame, text ='중간')
button.pack(padx =20, pady = 10)
# 2. 입력상자를 upFrame에 배치
editBox = Entry(upFrame, width=10)
editBox.pack(padx =20, pady = 10)

# 3. 리스트박스는  downFrame에 배치

ListBox = Listbox(downFrame)
ListBox.pack()

# q
# 리스트 박스에 값 입력
ListBox.insert(END, "하나")
ListBox.insert(END, "둘")
ListBox.insert(END, "셋")


window.mainloop()

# 데이터의 흐름을 따라가는 것이 커서

# 진짜 저장시키는 것이 .commit()
# 외부에서 변경시키거나~ 하면 commit 꼭 해줘야 함
# 우리가 몇 건을 등록하냐에 따라서~ 최종으로 다 끝나면 commit
# 그리고 제일 중요한 것은 -> 파일을 열면 꼭 닫아줘야함
# open -> close
