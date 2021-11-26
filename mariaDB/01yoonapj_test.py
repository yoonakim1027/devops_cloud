
from tkinter import ttk
from tkinter import *
from tkinter import messagebox




win1 = Tk()

win1.title("Don't buy a Family, Become the Family")
win1.geometry("400x400")



class MyFrame1(Frame):  # 클래스 정의
    def __init__1(self, master):
        img = PhotoImage(file='C:/Users/user/Desktop/MariaDB/강쥐.jpg')  # 이미지 읽고
        lbl = Label(image=img)  # 이미지 넣어
        lbl.image = img  # 레퍼런스 추가
        lbl.pack()


def main1():  # 메인함수로 정의
    win1.title('이미지 보기')
    win1.geometry('400x850')
    myframe1 = MyFrame1(win1)  # 클래스 사용


if __name__ == '__main__':  # 메인함수 호출
    main1()





# def click():
# 	cl = strs.get()
# 	cl2 = strs2.get()




def clickButton():
    messagebox.showinfo("매칭 정보 저장", "매칭 정보가 저장되었습니다")
    userName, size, sex, breed = "", "", "", ""
    userName = edit_name.get()
    size = strs.get()
    sex = strs2.get()
    breed = strs3.get()

def matching():
    strs = StringVar() #변수선언
    strs2 = StringVar()
    strs3 = StringVar()

    # #### 신청자 이름 받기 #### 쿼리로 받아오기 newusertbl에서
    ## 입력으로 받기
    # def button_make():

    #이름 입력
    label_name = Label(win1, text="\n이름을 입력해 주세요.\n")
    label_name.grid(row=0, column=1)

    edit_name = Entry(win1, width=10)
    edit_name.grid(row=1, column=1)

    # 1번 문항
    lbl_title1 = Label(win1, text="\n선호하는 견종 크기를 선택해 주세요. ", fg="blue")
    lbl_title1.grid(row=2, column=1)

    lbl1 = Label(win1, text="	size", font="NanumGothic 10")
    lbl1.grid(row=3, column=0)


    Combx1 = ttk.Combobox(textvariable=strs,width=20) #콤보박스 선언
    Combx1['value'] = ('--- 선택해주세요 ---','소형견','중형견','대형견') #콤보박스 요소 삽입
    Combx1.current(0) #0번째로 콤보박스 초기화
    Combx1.grid(row=3,column=1) #콤보박스 배치


    lbl_01 = Label(win1,text="\n")
    lbl_01.grid(row=5,column=1)

    # 2번 문항

    lbl_title2 = Label(win1, text="선호하는 성별을 선택해주세요. ", fg= "blue")
    lbl_title2.grid(row=6, column=1)

    lbl2 = Label(win1, text="	sex", font="NanumGothic 10")
    lbl2.grid(row=7, column=0)


    Combx2 = ttk.Combobox(textvariable=strs2, width=20)
    Combx2['value'] = ('--- 선택해주세요 ---','암컷','수컷')
    Combx2.current(0)
    Combx2.grid(row=7, column=1)


    lbl_02 = Label(win1,text="\n")
    lbl_02.grid(row=8,column=1)


    # 3번 문항

    lbl_title3 = Label(win1, text="선호하는 견종을 선택해주세요. ", fg= "blue")
    lbl_title3.grid(row=9, column=1)

    lbl3 = Label(win1, text="	breed", font="NanumGothic 10")
    lbl3.grid(row=10, column=0)

    Combx3 = ttk.Combobox(textvariable=strs3, width=20)
    Combx3['value'] = ('--- 선택해주세요 ---','스피츠','비숑','치와와','골든 리트리버','말티즈','믹스','상관없음')
    Combx3.current(0)
    Combx3.grid(row=10,column=1)


    lbl02 = Label(win1, text="\n", font="NanumGothic 10")
    lbl02.grid(row=11, column=0)

    btn = Button(win1, text="선택 완료",command=clickButton,width=7,height=1, font= 'NanumGothic 15', fg='blue', bg='light pink', relief='groove' )
    btn.grid(row=12,column=1)

    lbl4 = Label(win1, text="\n#사지마세요 \n\n#입양하세요", font="NanumGothic 11")
    lbl4.grid(row=13, column=1)




# class MyFrame1(Frame):  # 클래스 정의
#     def __init__1(self, master):
#         img1 = PhotoImage(file='C:/Users/user/Desktop/MariaDB/chrong.png')  # 이미지 읽고
#         lbl = Label(image=img1)  # 이미지 넣어
#         lbl.image = img1  # 레퍼런스 추가
#         lbl.pack()
#
#
# def main1():  # 메인함수로 정의
#     win1.geometry('400x850')
#     myframe1 = MyFrame1(win1)  # 클래스 사용
#
#
# if __name__ == '__main__':  # 메인함수 호출
#     main1()
#
#
#



win1.mainloop()