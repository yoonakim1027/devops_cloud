from tkinter import *
# 2021.11.23

window = Tk()

# 이 부분에서 화면을 구성하기
# GUI 화면을 꾸미기
# 우리가 항상 브라우저를 열면? 타이틀이 항상 나옴
# 타이틀 : 어떤 프로그램인지 알려주는 것
# window.geometry("400x100")# 사이즈 (넓이 * 높이)
# window.resizable(width=FALSE) 절대 가로를 넓히지 마라
# 고정하는 것 ~ 가로로 많이 쓰면 가로폭을 많이 ~ 세로면 세로

window.title("윈도창 연습")
# 윈도우 사이즈 고정하기
window.geometry("400x100")
window.resizable(width=FALSE, height=TRUE)


window.mainloop()