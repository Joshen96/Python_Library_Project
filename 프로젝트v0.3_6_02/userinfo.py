from tkinter import *
from tkinter import ttk
def userInfo(name, birth, phonnumber, gender, email, 대여권수, createdate, deletecount, photo):  # 나중에 이미지 이름도 인자로 받아와야함!
    win1=Toplevel()
    win1.title('회원 정보')    
    win1.geometry("+680+280")  #
    frame1=Frame(win1, relief='flat', padx=10, pady=10) # relief='flat' : 테두리 없음, padx,y : 외부 패딩값 지정함
    win1.resizable(False, False)
    frame1.grid(row=0, column=0) # 

    # 이름 적는 곳
    labelname=Label(frame1, text='이름 : ')
    labelname.grid(row=0, column=0, columnspan=1, rowspan=1, sticky=W) # sticky : 위치 조정(n, e, s, w, nw, ne, sw, se)

    # 이름 적는 곳
    labelnameText=Label(frame1, text=name)
    labelnameText.grid(row=0, column=1, columnspan=1, rowspan=1, sticky=W)

    # 이미지 넣는 곳
    img=PhotoImage(file='GIF/' + photo, master=win1) # 나중에 이미지이름 인자로 받아와야함!
    labelImg=Label(frame1, text='이미지 넣는 곳', image=img)
    labelImg.grid(row=0, column=3, columnspan=1, rowspan=6, sticky=E, padx=5)

    # 생년월일 적는 곳
    labelbirth=Label(frame1, text='생년월일 : ')
    labelbirth.grid(row=1, column=0, columnspan=1, rowspan=1, sticky=W)

    # 생년월일 적는 곳
    labelbirthText=Label(frame1, text= birth)
    labelbirthText.grid(row=1, column=1, columnspan=1, rowspan=1, sticky=W)

    # 휴대전화 적는 곳
    labelphonnumber=Label(frame1, text='휴대전화 : ')
    labelphonnumber.grid(row=2, column=0, columnspan=1, rowspan=1, sticky=W)

    # 휴대전화 적는 곳
    labelphonnumberText=Label(frame1, text= phonnumber)
    labelphonnumberText.grid(row=2, column=1, columnspan=1, rowspan=1, sticky=W)

    # 성별 적는 곳
    labelgender=Label(frame1, text='성별 : ')
    labelgender.grid(row=3, column=0, columnspan=1, rowspan=1, sticky=W)

    # 성별 적는 곳
    labelgenderText=Label(frame1, text= gender)
    labelgenderText.grid(row=3, column=1, columnspan=1, rowspan=1, sticky=W)

    # 이메일 주소 적는 곳
    labelemail=Label(frame1, text='이메일 주소 : ')
    labelemail.grid(row=4, column=0, columnspan=1, rowspan=1, sticky=W)

    # 이메일 주소 적는 곳
    labelemailText=Label(frame1, text= email, wraplength= 250 ) # wraplength : 자동 줄내림 설정
    labelemailText.grid(row=4, column=1, columnspan=1, rowspan=1, sticky=W)

    # 대여권수 적는 곳
    labelrentcount=Label(frame1, text='대여권수 : ')
    labelrentcount.grid(row=5, column=0, columnspan=1, rowspan=1, sticky=W)

    # 대여권수 적는 곳
    labelrentcountText=Label(frame1, text= 대여권수)
    labelrentcountText.grid(row=5, column=1, columnspan=1, rowspan=1, sticky=W)

    # 가입일 적는 곳
    labelcreatedate=Label(frame1, text='가입일 : ')
    labelcreatedate.grid(row=6, column=0, columnspan=1, rowspan=1, sticky=W)

    # 가입일 적는 곳
    labelcreatedateText=Label(frame1, text= createdate)
    labelcreatedateText.grid(row=6, column=1, columnspan=1, rowspan=1, sticky=W)

    # 탈퇴여부 적는 곳
    labeldeletecount=Label(frame1, text='회원 현황 : ')
    labeldeletecount.grid(row=7, column=0, columnspan=1, rowspan=1, sticky=W)

    # 탈퇴여부 적는 곳
    labeldeletecountText=Label(frame1, text= deletecount, wraplength= 250 ) # wraplength : 자동 줄내림 설정
    labeldeletecountText.grid(row=7, column=1, columnspan=1, rowspan=1, sticky=W)

    win1.mainloop()
