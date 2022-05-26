from tkinter import *
from tkinter import ttk

win_rent_name=Tk()
win_rent_name.title('도서관리프로그램')        
win_rent_name.geometry("820x350")
win_rent_name.resizable(False, False)

win_rent_name_frame=Frame(win_rent_name, relief='flat', borderwidth=1,padx=5,pady=10)
win_rent_name_frame.grid(row=0, column=0)

menubar1= Menu(win_rent_name_frame)
submenu1=Menu(menubar1, tearoff=0)
menubar1.add_cascade(label='회원', menu=submenu1)
submenu1.add_command(label='전체 회원', command=() )
submenu2=Menu(menubar1, tearoff=0)
menubar1.add_cascade(label='도서', menu=submenu2)
submenu2.add_command(label='전체 도서', command=() )
submenu3=Menu(menubar1, tearoff=0)
menubar1.add_cascade(label='대여', menu=submenu3)
submenu3.add_command(label='대여하기', command=() )
submenu3.add_command(label='대여정보,반납', command=() )
win_rent_name.config(menu=menubar1)

rent_name_frame=Frame(win_rent_name, relief='flat', borderwidth=1,padx=5,pady=10)
rent_name_frame.grid(row=1,column=1)

#이름레이블
name_Label=Label(rent_name_frame, text='이름') 
name_Label.grid(row=1, column=0, columnspan=1, rowspan=1, sticky=N)

# 이름 검색 엔트리창
name_Entry=ttk.Entry(rent_name_frame ,width='17') # 이름검색 Entry
name_Entry.grid(row=1, column=1, columnspan=1, rowspan=1, sticky=W,pady =1)


#이름 검색 버튼 
search_btn=ttk.Button(rent_name_frame,text='검색',command=' ') # 함수 커맨트 빈칸
search_btn.grid(row=1, column=2, columnspan=1, rowspan=1, sticky=W,pady =1)




#트리뷰 생성
treeview_frame=Frame(rent_name_frame, relief='flat', borderwidth=1,padx=20,pady=10)
treeview_frame.grid(row=2, column=0, columnspan=8, rowspan=1, sticky=N)

name_treeview=ttk.Treeview(treeview_frame, height=10, columns=('#1', '#2', '#3', '#4', '#5', '#6'))

name_treeview.column('#0', width=100, minwidth=100, stretch=NO)
name_treeview.heading('#0',text='이름',anchor=N)
name_treeview.column('#1', width=120, minwidth=120, stretch=NO)
name_treeview.heading('#1',text='생년월일',anchor=N)
name_treeview.column('#2', width=100, minwidth=100, stretch=NO)
name_treeview.heading('#2',text='성별',anchor=N)
name_treeview.column('#3', width=120, minwidth=120, stretch=NO)
name_treeview.heading('#3',text='휴대전화번호',anchor=N)
name_treeview.column('#4', width=100, minwidth=100, stretch=NO)
name_treeview.heading('#4',text='회원현황',anchor=N)
name_treeview.column('#5', width=100, minwidth=100, stretch=NO)
name_treeview.heading('#5',text='대여',anchor=N)
name_treeview.column('#6', width=120, minwidth=120, stretch=NO)
name_treeview.heading('#6',text='이메일주소',anchor=N)
m20aa1=name_treeview.insert("", END, text='', values=('', '', '', '', '', ''))
name_treeview.grid(row=2, column=0, columnspan=1, rowspan=1, sticky=N)


#-m----Button: c0, r3------

select_name_btn=ttk.Button(rent_name_frame,text='회원 선택',command= ' ')
select_name_btn.grid(row=3, column=0, columnspan=1, rowspan=1, sticky=N)
win_rent_name.mainloop()
