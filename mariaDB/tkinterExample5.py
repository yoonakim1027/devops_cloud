from tkinter import *
from tkinter import messagebox
# 2021.11.23
# 버튼 만들기
window = Tk()

# 버튼을 사용하여 알림 창 띄우기
def clickButton():
    messagebox.showinfo('버튼 클릭', '버튼을 클릭했습니다.')# messagebox 타이틀, messagebox 내용)


window.title("버튼 이벤트 연습 X 3")
window.geometry("200x200")

button1 = Button(window, text='요기 눌러요1', fg='red', bg='yellow', command=clickButton)
button2 = Button(window, text='요기 눌러요2', fg='red', bg='yellow', command=clickButton)
button3 = Button(window, text='요기 눌러요3', fg='red', bg='yellow', command=clickButton)


# 위치조정은 pack에서 가능함 (padx=10, pady=10)
# 여백, 배치에 관련된 것은 pack 에서 가능 !
button1.pack(side=LEFT, padx=10, pady=10) # 왼쪽 정렬 -> 순서대로 실행. 항상 코드는 위에서 아래로.
button2.pack(side=TOP, padx=10, pady=10) # TOP / BOTTOM
button3.pack(side=RIGHT, padx=10, pady=10) # 오른쪽 정렬


# button1.pack(expand=1)  -> 버튼을 우리가 올릴건데, 버튼을 1개만 올릴 거다 !


window.mainloop()