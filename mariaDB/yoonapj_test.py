from tkinter import *
from tkinter import ttk





win1 = Tk()

win1.title("Don't buy a Family, Become the Family")
win1.geometry("400x400")

def click():
	cl = strs.get()
	cl2 = strs2.get()
	lbl4.configure(text="마당유무: "+cl+"\n"+"선호하는 견종 크기: "+cl2)

strs = StringVar() #변수선언
strs2 = StringVar()
strs3 = StringVar()

# 1번 문항
lbl_title1 = Label(win1,text="\n선호하는 견종 크기를 선택해 주세요. ", fg= "blue")
lbl_title1.grid(row=0,column=1)

lbl1 = Label(win1, text="	size", font="NanumGothic 10")
lbl1.grid(row=1, column=0)

Combx1 = ttk.Combobox(textvariable=strs, width=20) #콤보박스 선언
Combx1['value'] = ('-- 선택해주세요-- ','소형견','중형견','대형견') #콤보박스 요소 삽입
Combx1.current(0) #0번째로 콤보박스 초기화
Combx1.grid(row=1,column=1) #콤보박스 배치

lbl_01 = Label(win1,text="\n")
lbl_01.grid(row=2,column=1)

# 2번 문항

lbl_title2 = Label(win1, text="선호하는 성별을 선택해주세요. ", fg= "blue")
lbl_title2.grid(row=3, column=1)

lbl2 = Label(win1, text="	sex", font="NanumGothic 10")
lbl2.grid(row=4, column=0)

Combx2 = ttk.Combobox(textvariable=strs2, width=20)
Combx2['value'] = ('-- 선택해주세요-- ','암컷','수컷')
Combx2.current(0)
Combx2.grid(row=4, column=1)

lbl_02 = Label(win1,text="\n")
lbl_02.grid(row=5,column=1)


# 3번 문항

lbl_title3 = Label(win1, text="선호하는 견종을 선택해주세요. ", fg= "blue")
lbl_title3.grid(row=6, column=1)

lbl3 = Label(win1, text="	breed", font="NanumGothic 10")
lbl3.grid(row=7, column=0)

Combx3 = ttk.Combobox(textvariable=strs3, width=20)
Combx3['value'] = ('-- 선택해주세요-- ','스피츠','비숑','치와와','골든 리트리버','말티즈','믹스','상관없음')
Combx3.current(0)
Combx3.grid(row=7,column=1)

lbl02 = Label(win1, text="\n", font="NanumGothic 10")
lbl02.grid(row=8, column=0)

btn = Button(win1, text="선택 완료",command=click,width=7,height=1, font= 'NanumGothic 15', fg='blue', bg='light pink', relief='groove' )
btn.grid(row=9,column=1)

lbl4 = Label(win1, text="\n#사지마세요 \n\n#입양하세요", font="NanumGothic 11")
lbl4.grid(row=12, column=1)
print(type(strs))
win1.mainloop()