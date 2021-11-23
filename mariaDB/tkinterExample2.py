from tkinter import *
# 2021.11.23
# 문자를 표현할 수 있는 라벨 사용
window = Tk()

# 이 부분에서 화면을 구성하기
# GUI 화면을 꾸미기
# 우리가 항상 브라우저를 열면? 타이틀이 항상 나옴
# 타이틀 : 어떤 프로그램인지 알려주는 것
# window.geometry("400x100")# 사이즈 (넓이 * 높이)
# window.resizable(width=FALSE) 절대 가로를 넓히지 마라
# 고정하는 것 ~ 가로로 많이 쓰면 가로폭을 많이 ~ 세로면 세로

window.title("라벨 사용 연습")
# 윈도우 사이즈 고정하기
window.geometry("400x100")

# 라벨이 어디 소속되어야 하는지(window)
# 라벨 선언 ( 어떻게 만들겠다는 선언)
label1 = Label(window, text='This is MariaDB를')
label2 = Label(window, text='열심히', font=("궁서체", 30), fg='blue')
label3 = Label(window, text='공부 중입니다', bg="magenta", width=20, height=5, anchor=SE)
# bg -> back ground color
# 부모 윈도우
# 윈도우는 영역을 나눠서 여러개 할 수 있음
# 레이블이 올라갈 윈도우를 먼저 선언 -> window  부분
# text = "실제로 출력될 글"
# font = 폰트
# fg = 글자 색
# bg = 배경 색
# anchor = 글자의 위치 South East  / 기본이 center -> 사방위로 줄 수 있음
# window.geometry("400x100") : 사이즈를 주지 않으면 위젯에 맞춰서 셋팅이 됨

# 아예 레트로 감성으로 해도 귀여울듯 ^__^

# 위젯 적용
label1.pack()
label2.pack()
label3.pack()


window.mainloop()