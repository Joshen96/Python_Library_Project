from asyncio.windows_events import NULL
from doctest import master
from tkinter import N
from tkinter import messagebox
from tkinter.messagebox import NO
from tkinter.ttk import Combobox
from tkinter import *
from tkinter import ttk
import tkinter as tk
import pandas as pd 
import bookinfo # 도서정보 py 불러오기
import userinfo # 회원정보 py 불러오기

## 조창현이 추가한 import
import string
from datetime import date
import datetime
import csv
## 조창현이 추가한 import

Rentdf = pd.DataFrame(index=range(0,0), columns=['SEQ', 'Book_ISBN','Book_title','User_number','User_name','Rent_date','Rent_retun','Rent_YN'])
Rentdf.to_csv('Rent.csv',index=False,encoding='utf-8-sig') #csv파일 생성 최초실행
########################################################################################






df1 = pd.read_csv ('book3.csv')
df1_list = df1.values.tolist()

    #win.update()
def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame


class MainTk(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry("+600+300")
        self.resizable(False, False)


        self._frame = None
        self.switch_frame(Userpage)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame

        # 메뉴바 부분
        menubar1=tk.Menu(self._frame)
        submenu1=tk.Menu(menubar1, tearoff=0)
        menubar1.add_cascade(label='회원', menu=submenu1)
        submenu1.add_command(label='전체 회원', command=lambda: self.switch_frame(Userpage))
        submenu2=tk.Menu(menubar1, tearoff=0)
        menubar1.add_cascade(label='도서', menu=submenu2)
        submenu2.add_command(label='전체 도서', command=lambda: self.switch_frame(BookPage) )
        submenu3=tk.Menu(menubar1, tearoff=0)
        menubar1.add_cascade(label='대여', menu=submenu3)
        submenu3.add_command(label='대여하기', command=lambda: self.switch_frame(RentPage) )
        submenu3.add_command(label='대여정보,반납', command=lambda: self.switch_frame(RentInfo) )
        self.config(menu=menubar1)
        self._frame.grid(row=0, column=0)


class BookPage(tk.Frame):  #### 전체 도서 페이지 
    
    def __init__(self, master):
        df1 = pd.read_csv ('book3.csv')
        df1_list = df1.values.tolist()
        tk.Frame.__init__(self, master)
        self.grid()
        self.entryValue = tk.StringVar()
        self.entry1 = tk.Entry(self, width='35', textvariable=self.entryValue)
        self.entry1.grid(row=1, column=2, columnspan=1, rowspan=1, sticky=N, pady=1) # 위치 N, 외부 패딩 1

        self.master.bind("<Key>", self.keyEvent )
        
        #self.entryValue.set("입력!")
        self.entry1.focus_set()
        self.entry1.select_range(0, tk.END)
        
        # 콤보 박스 부분
        frameCombo=tk.Frame(self, relief='flat')
        frameCombo.grid(row=1, column=1, columnspan=1, rowspan=1, sticky=N)
        self.comboBox1= Combobox(frameCombo, width=5, state='readonly')
        self.comboBox1['values']=('제목', '저자')
        self.comboBox1.current(0)
        self.comboBox1.grid(row=0, column=1,sticky=N)
        labelCombo=tk.Label(frameCombo, text='')
        labelCombo.grid(row=0, column=0,sticky=N)

        cboxText = self.comboBox1.get() # 콤보박스

        # 트리뷰 부분
        frame2=tk.Frame(self, relief='flat', borderwidth=1, padx=20, pady=10)
        frame2.grid(row=2, column=0, columnspan=5, rowspan=1, sticky=N)
        self.Treeview1=ttk.Treeview(frame2, height=10, columns=('#1', '#2', '#3', '#4', '#5', '#6'))
        self.Treeview1.column('#0', width=40, minwidth=40, stretch=NO) # stretch : 열의 너비 조정 설정 여부
        self.Treeview1.heading('#0',text='권수',anchor=N)
        self.Treeview1.column('#1', width=140, minwidth=100, stretch=NO) # stretch : 열의 너비 조정 설정 여부
        self.Treeview1.heading('#1',text='도서명',anchor=N)
        self.Treeview1.column('#2', width=70, minwidth=60, stretch=NO)
        self.Treeview1.heading('#2',text='저자',anchor=N)
        self.Treeview1.column('#3', width=70, minwidth=50, stretch=NO)
        self.Treeview1.heading('#3',text='가격',anchor=N)
        self.Treeview1.column('#4', width=100, minwidth=70, stretch=NO)
        self.Treeview1.heading('#4',text='ISBN',anchor=N)
        self.Treeview1.column('#5', width=70, minwidth=50, stretch=NO)
        self.Treeview1.heading('#5',text='대출여부',anchor=N)
        self.Treeview1.column('#6', width=180, minwidth=150, stretch=NO)
        self.Treeview1.heading('#6',text='URL',anchor=N)

        c = 1
        # 표에 데이터 삽입
        for i in df1_list:
            rent=self.rent1(i[4])
            TreeviewText=self.Treeview1.insert("", END, text=c, values=(i[0], i[1], i[2], i[3], rent, i[5] ), iid= c-1)
            c += 1
        self.Treeview1.grid(row=0, column=0, columnspan=1, rowspan=1, sticky=N)

        #tk.Label(self, text="Start page", font=('Helvetica', 18, "bold")).grid(row=0, column=0)
        # 검색 버튼
        btnSearch=ttk.Button(self, text='검색', command=lambda: self.bookSearch() )
        btnSearch.grid(row=1, column=3, columnspan=1, rowspan=1, sticky=N, padx=5)
        
        # 도서등록 버튼
        btnBookRegist=ttk.Button(self, text='도서등록',command=())
        btnBookRegist.grid(row=3, column=0, columnspan=1, rowspan=1, sticky=N, padx=25, pady=3)

        # 도서정보 버튼
        btnBookInformation=ttk.Button(self, text='도서정보', command=lambda: self.info() )
        btnBookInformation.grid(row=3, column=1, columnspan=1, rowspan=1, sticky=W, padx=5, pady=3)

        # 도서수정 버튼
        btnBookEdit=ttk.Button(self, text='도서수정',command=())
        btnBookEdit.grid(row=3, column=2, columnspan=1, rowspan=1, sticky=W, padx=25, pady=3)

        # 도서 삭제 버튼
        btnBookDelete=ttk.Button(self, text='도서 삭제',command=() )
        btnBookDelete.grid(row=3, column=4, columnspan=1, rowspan=1, sticky=N, padx=25, pady=3)


    def info(self): # 트리뷰 클릭한 값 넘기기
        try: # 도서 클릭안하고 도서정보 버튼 눌렀을 경우 예외처리 
            aaa = self.Treeview1.focus() # 트리뷰 클릭한 줄
            treeviewValues = self.Treeview1.item(aaa).get('values')
            for k in df1_list:
                if treeviewValues[0] == k[0]  :
                    bookinfo.bookInfo(k[0], k[1], k[6], k[2], k[5], k[3], k[7], k[8])
        except IndexError:
            messagebox.showinfo("알림", "도서를 클릭해주세요.")
            print("도서를 클릭해주세요. ")

    def bookSearch(self):  # 도서 검색
        
        searchText = self.entryValue.get() # 검색창 값 가져오기
        print(searchText)
        cboxText = self.comboBox1.get() # 콤보박스 값 가져오기
        print(cboxText)

        for i in self.Treeview1.get_children(): # 트리뷰의 값들을 다 지워주고 창 새로고침
            self.Treeview1.delete(i)

        if self.comboBox1.get() == '제목':
            c = 1
            for e in df1_list:
                if self.entryValue.get() in e[0]: # 제목과 부분일치할 경우 
                    # 표에 데이터 삽입
                    rent=self.rent1(e[4])
                    TreeviewText=self.Treeview1.insert("", END, text=c, values=(e[0], e[1], e[2], e[3], rent, e[5] ), iid= c-1)
                    c += 1
        elif self.comboBox1.get() == '저자':
            c = 1
            for e in df1_list:
                if self.entryValue.get() in e[1]: # 저자와 부분일치할 경우 
                    # 표에 데이터 삽입
                    rent=self.rent1(e[4])
                    TreeviewText=self.Treeview1.insert("", END, text=c, values=(e[0], e[1], e[2], e[3], rent, e[5] ), iid= c-1)
                    c += 1

    def keyEvent(self, event):  # 실시간 검색 기능
        if 8 <= event.keycode <= 105:
            self.bookSearch()
            print(event.keycode)
    def rent1(self, r):
            rent =''
            if r == 0: # 대여가능
                rent = '대여가능'

            elif r == 1: # 대여불가
                rent = '대여불가'
            return rent


class Userpage(tk.Frame):   #### 전체 회원 페이지 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    def __init__(self, master):
        df2 = pd.read_csv ('user.csv')
        df2_list= df2.values.tolist()
        tk.Frame.__init__(self, master)
        self.grid()
        self.entryValue = tk.StringVar()
        self.entry1 = tk.Entry(self, width='35', textvariable=self.entryValue)
        self.entry1.grid(row=1, column=2, columnspan=1, rowspan=1, sticky=N, pady=1) # 위치 N, 외부 패딩 1

        self.master.bind("<Key>", self.keyEvent )
        
        #self.entryValue.set("입력!")
        self.entry1.focus_set()
        self.entry1.select_range(0, tk.END)
        
        # 콤보 박스 부분
        frameCombo=tk.Frame(self, relief='flat')
        frameCombo.grid(row=1, column=1, columnspan=1, rowspan=1, sticky=N)
        self.comboBox1= Combobox(frameCombo, width=5, state='readonly')
        self.comboBox1['values']=('이름', '전화번호')
        self.comboBox1.current(0)
        self.comboBox1.grid(row=0, column=1,sticky=N)
        labelCombo=tk.Label(frameCombo, text='')
        labelCombo.grid(row=0, column=0,sticky=N)

        cboxText = self.comboBox1.get() # 콤보박스

        # 트리뷰 부분
        frame2=tk.Frame(self, relief='flat', borderwidth=1, padx=20, pady=10)
        frame2.grid(row=2, column=0, columnspan=5, rowspan=1, sticky=N)
        self.Treeview1=ttk.Treeview(frame2, height=10, columns=('#1', '#2', '#3', '#4', '#5', '#6', '#7'))
        self.Treeview1.column('#0', width=50, minwidth=40, stretch=NO) # stretch : 열의 너비 조정 설정 여부
        self.Treeview1.heading('#0',text='회원수',anchor=N)
        self.Treeview1.column('#1', width=80, minwidth=70, stretch=NO) # stretch : 열의 너비 조정 설정 여부
        self.Treeview1.heading('#1',text='이름',anchor=N)
        self.Treeview1.column('#2', width=100, minwidth=100, stretch=NO)
        self.Treeview1.heading('#2',text='생년월일',anchor=N)
        self.Treeview1.column('#3', width=50, minwidth=40, stretch=NO)
        self.Treeview1.heading('#3',text='성별',anchor=N)
        self.Treeview1.column('#4', width=130, minwidth=120, stretch=NO)
        self.Treeview1.heading('#4',text='전화번호',anchor=N)
        self.Treeview1.column('#5', width=60, minwidth=50, stretch=NO)
        self.Treeview1.heading('#5',text='회원현황',anchor=N)
        self.Treeview1.column('#6', width=60, minwidth=40, stretch=NO)
        self.Treeview1.heading('#6',text='대여',anchor=N)
        self.Treeview1.column('#7', width=140, minwidth=120, stretch=NO)
        self.Treeview1.heading('#7',text='이메일주소',anchor=N) 

        c = 1
        # 표에 데이터 삽입
        for i in df2_list:
            gen = self.gender1(i[3])
            #rent = self.rent1(i[7])
            cUser = self.currentUser(i[6])
            TreeviewText=self.Treeview1.insert("", END, text=c, values=(i[1], i[2], gen, i[0], cUser, i[7], i[4] ), iid= c-1)
            c += 1
        self.Treeview1.grid(row=0, column=0, columnspan=1, rowspan=1, sticky=N)

        #tk.Label(self, text="Start page", font=('Helvetica', 18, "bold")).grid(row=0, column=0)

        # 회원검색 버튼
        btnSearch=ttk.Button(self, text='검색', command=lambda: self.userSearch() )
        btnSearch.grid(row=1, column=3, columnspan=1, rowspan=1, sticky=N, padx=5)

        # 회원등록 버튼
        btnBookRegist=ttk.Button(self, text='회원등록',command=())
        btnBookRegist.grid(row=3, column=0, columnspan=1, rowspan=1, sticky=N, padx=25, pady=3)

        # 회원정보 버튼
        btnBookInformation=ttk.Button(self, text='회원정보', command=lambda: self.userinfo() )
        btnBookInformation.grid(row=3, column=1, columnspan=1, rowspan=1, sticky=W, padx=5, pady=3)

        # 회원수정 버튼
        btnBookEdit=ttk.Button(self, text='회원수정',command=())
        btnBookEdit.grid(row=3, column=2, columnspan=1, rowspan=1, sticky=W, padx=25, pady=3)

        # 회원삭제 버튼
        btnBookDelete=ttk.Button(self, text='회원 삭제',command=() )
        btnBookDelete.grid(row=3, column=4, columnspan=1, rowspan=1, sticky=N, padx=25, pady=3)

    def userinfo(self): # 트리뷰 클릭한 값 넘기기
        try: # 도서 클릭안하고 도서정보 버튼 눌렀을 경우 예외처리 
            bbb = self.Treeview1.focus() # 트리뷰 클릭한 줄
            print(bbb)
            treeviewValues = self.Treeview1.item(bbb).get('values')

            print(treeviewValues)
            for k in self.df2_list:
                print(k)
                print(k[0])
                if treeviewValues[3] == k[0]  :
                    gen = self.gender1(k[3])
                    userinfo.userInfo(k[1], k[2], k[0], gen, k[4], k[3], k[5], k[6])
        except IndexError:
            messagebox.showinfo("알림", "회원를 클릭해주세요.")
            print("회원를 클릭해주세요. ")

    def userSearch(self):  # 회원 검색
        searchText = self.entryValue.get() # 검색창 값 가져오기
        print(searchText)
        cboxText = self.comboBox1.get() # 콤보박스 값 가져오기
        print("콤보박스 : "+cboxText)

        for i in self.Treeview1.get_children(): # 트리뷰의 값들을 다 지워주고 창 새로고침
            self.Treeview1.delete(i)

        if self.comboBox1.get() == '이름':
            c = 1
            for e in self.df2_list:
                if self.entryValue.get() in e[1]: # 이름과 부분일치할 경우 
                    gen = self.gender1(e[3])
                    rent = self.rent1(e[7])
                    cUser = self.currentUser(e[6])
                    # 표에 데이터 삽입
                    TreeviewText=self.Treeview1.insert("", END, text=c, values=(e[1], e[2], gen, e[0], cUser, rent, e[4] ), iid= c-1)
                    c += 1
        elif self.comboBox1.get() == '전화번호':
            c = 1
            for e in self.df2_list:
                if self.entryValue.get() in e[0]: # 전화번호와 부분일치할 경우 
                    gen = self.gender1(e[3])
                    rent = self.rent1(e[7])
                    cUser = self.currentUser(e[6])
                    # 표에 데이터 삽입
                    TreeviewText=self.Treeview1.insert("", END, text=c, values=(e[1], e[2], gen, e[0], cUser, rent, e[4] ), iid= c-1)
                    c += 1 

    def gender1(self, g):
        gen =''
        if g == 0: # 여성

            gen = '여성'

        elif g == 1: # 남성
            gen = '남성'
        return gen

    def rent1(self, r):
        rent =''
        if r == 0: # 대여가능
            rent = '대여가능'

        elif r == 1: # 대여불가
            rent = '대여불가'
        return rent

    def currentUser(self, c):
        print(str(c))
        a = " "
        if a == c : # 회원
            cUser = '회원'

        else : # 탈퇴회원
            cUser = '탈퇴회원'
        return cUser

    def keyEvent(self, event):  # 실시간 검색 기능
        if 8 <= event.keycode <= 105:
            self.userSearch()
            print(event.keycode)   



# 대여하기 시작
##################################################################################################
##################################################################################################
##################################################################################################
##################################################################################################
##################################################################################################
##################################################################################################
##################################################################################################
##################################################################################################
##################################################################################################
##################################################################################################
##################################################################################################
##################################################################################################




class RentPage(tk.Frame):  #### 대여하기 (이름)선택 페이지
    global df2
    
    
    def __init__(self, master):
        df2 = pd.read_csv ('user.csv') ## 회원정보 받아오기

        df2_rent_can_user=df2.groupby('User_out_Date').get_group(" ") # 탈퇴한 회원은 못빌리도록 미리 빼둠
        df2_rent_can_user_list = df2_rent_can_user.values.tolist() 

        tk.Frame.__init__(self, master)
        tk.Frame.configure(self, relief='flat', borderwidth=1, pady=5)
        
        rent_name_frame=Frame(self, relief='flat', borderwidth=1,padx=5,pady=10)
        rent_name_frame.grid(row=1,column=1)

        #이름레이블
        name_Label=Label(rent_name_frame, text='이름') 
        name_Label.grid(row=1, column=0, columnspan=1, rowspan=1, sticky=N)

        # 이름 검색 엔트리창
        rent_name_Entry=ttk.Entry(rent_name_frame,width='17') # 이름검색 Entry
        rent_name_Entry.grid(row=1, column=1, columnspan=1, rowspan=1, sticky=W,pady =1)
        
       

        #이름 검색 버튼 
        search_name_btn=ttk.Button(rent_name_frame,text='검색',command=' ') # 함수 커맨트 빈칸
        search_name_btn.grid(row=1, column=2, columnspan=1, rowspan=1, sticky=W,pady =1)




        #트리뷰 생성
        treeview_frame=tk.Frame(rent_name_frame, relief='flat', borderwidth=1,padx=20,pady=10)
        treeview_frame.grid(row=2, column=0, columnspan=8, rowspan=1, sticky=N)

        self.name_treeview=ttk.Treeview(treeview_frame, height=10, columns=('#1', '#2', '#3', '#4', '#5', '#6','#7'))

        self.name_treeview.column('#0', width=50, minwidth=100, stretch=NO)
        self.name_treeview.heading('#0',text='회원수',anchor=N)
        self.name_treeview.column('#1', width=80, minwidth=120, stretch=NO)
        self.name_treeview.heading('#1',text='이름',anchor=N)
        self.name_treeview.column('#2', width=100, minwidth=100, stretch=NO)
        self.name_treeview.heading('#2',text='생년월일',anchor=N)
        self.name_treeview.column('#3', width=40, minwidth=120, stretch=NO)
        self.name_treeview.heading('#3',text='성별',anchor=N)
        self.name_treeview.column('#4', width=120, minwidth=100, stretch=NO)
        self.name_treeview.heading('#4',text='전화번호',anchor=N)
        self.name_treeview.column('#5', width=80, minwidth=100, stretch=NO)
        self.name_treeview.heading('#5',text='회원현황',anchor=N)
        self.name_treeview.column('#6', width=60, minwidth=120, stretch=NO)
        self.name_treeview.heading('#6',text='대여수',anchor=N)
        self.name_treeview.column('#7', width=140, minwidth=120, stretch=NO)
        self.name_treeview.heading('#7',text='이메일주소',anchor=N)
        c=1
        #m20aa1=self.name_treeview.insert("", END, text='', values=('', '', '', '', '', ''))
        for i in df2_rent_can_user_list:
            gen = self.gender1(i[3])
            #rent = self.i[7]
            cUser = self.currentUser(i[6])
            
            m20aa1=self.name_treeview.insert("", END, text=c, values=(i[1], i[2], gen, i[0], cUser, i[7], i[4] ), iid= c-1)
            c += 1


        
        

        self.name_treeview.grid(row=2, column=0, columnspan=1, rowspan=1, sticky=N)


        #회원선택 버튼
            
        #select_name_btn=ttk.Button(self,text='회원 선택',command=lambda: master.switch_frame(RentBook)) # 도서 선택 나중에 기능추가해서 수정해야함 
        select_name_btn=ttk.Button(rent_name_frame,text='회원 선택',command=lambda:self.userselect()) # 도서 선택 나중에 기능추가해서 수정해야함 
        
        select_name_btn.grid(row=3, column=0, columnspan=1, rowspan=1, sticky=N)
        #tk.Label(self, text="대여하기", font=('Helvetica', 18, "bold")).grid(row=0, column=0)
    
    def switch_frame(self, frame_class):
        new_frame = frame_class
        self._frame= new_frame

    def gender1(self, g):
        gen =''
        if g == 0: # 여성

            gen = '여성'

        elif g == 1: # 남성
            gen = '남성'
        return gen
    
    def userselect(self): # 대여하기 트리뷰 선택후 대여하기 도서로 넘기기
        
        try: # 회원 클릭안하고 회원선택 버튼 눌렀을 경우 예외처리 
            bbb = self.name_treeview.focus() # 트리뷰 클릭한 줄
            print(bbb)
            treeviewValues = self.name_treeview.item(bbb).get('values')
            print(treeviewValues[0])
            rentname=treeviewValues[0]
            self.switch_frame(RentBook(self,rentname)) #  회원선택후 회원이름 가지고 도서대여창으로 넘기는 곳

        except IndexError:
            messagebox.showinfo("알림", "회원를 클릭해주세요\.")
            print("회원를 클릭해주세요. ")

    def currentUser(self, c):
        print(str(c))
        c = " "
        if c == c : # 회원
            cUser = '회원'

        else : # 탈퇴회원
            cUser = '탈퇴회원'
        return cUser

    def userupdate(self): ## 창 정보 최신화
        df12 = pd.read_csv ('user.csv')
        df12_list = df12.values.tolist()
        c = 1
        for i in self.Treeview1.get_children(): # 트리뷰의 값들을 다 지워주고 창 새로고침
            self.Treeview1.delete(i)        
        for e in df12_list:
            # 표에 데이터 삽입
            self.Treeview1.insert("", END, text=c, values=(e[0], e[1], e[2], e[3], e[4], e[5] ), iid= c-1)
            c += 1







df_user = pd.read_csv ('user.csv')
df_book = pd.read_csv ('book3.csv') 
df_rent = pd.read_csv('Rent.csv')

class RentBook(tk.Frame):  #### 대여하기 (도서) 선택 페이지
    global df_book
    global df_user
    global df_rent
    
    
    
    
    
    
    def __init__(self, master, name): ## 선택회원 이름을 가지고옴
        df_book = pd.read_csv ('book3.csv')
        df_user = pd.read_csv ('user.csv')
        df_rent = pd.read_csv('Rent.csv')

        df_rent_can_book=df_book.groupby('Book_pre').get_group(0)
        df_rent_can_book_list = df_rent_can_book.values.tolist()
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self, relief='flat', borderwidth=1, pady=5)
        
        
        self.grid(row=1,column=1)

        #도서레이블
        book_Label=Label(self, text='도서명') 
        book_Label.grid(row=1, column=0, columnspan=1, rowspan=1, sticky=N)

        # 도서 검색 엔트리창
        rent_book_Entry=ttk.Entry(self,width='17') # 이름검색 Entry
        rent_book_Entry.grid(row=1, column=1, columnspan=1, rowspan=1, sticky=W,pady =1)


        #도서 검색 버튼 
        search_book_btn=ttk.Button(self,text='검색',command=' ') # 함수 커맨트 빈칸
        search_book_btn.grid(row=1, column=2, columnspan=1, rowspan=1, sticky=W,pady =1)

        name_Label=Label(self, text='빌리는회원 :'+name) 
        name_Label.grid(row=1, column=3, columnspan=1, rowspan=1, sticky=N)


        #도서 트리뷰 생성
        treeview_frame=tk.Frame(self, relief='flat', borderwidth=1,padx=20,pady=10)
        treeview_frame.grid(row=2, column=0, columnspan=8, rowspan=1, sticky=N)

        self.book_treeview=ttk.Treeview(treeview_frame, height=10, columns=('#1', '#2', '#3', '#4', '#5','#6'))

        self.book_treeview.column('#0', width=40, minwidth=100, stretch=NO)
        self.book_treeview.heading('#0',text='권수',anchor=N)
        self.book_treeview.column('#1', width=100, minwidth=100, stretch=NO)
        self.book_treeview.heading('#1',text='도서명',anchor=N)
        self.book_treeview.column('#2', width=120, minwidth=120, stretch=NO)
        self.book_treeview.heading('#2',text='저자',anchor=N)
        self.book_treeview.column('#3', width=100, minwidth=100, stretch=NO)
        self.book_treeview.heading('#3',text='가격',anchor=N)
        self.book_treeview.column('#4', width=120, minwidth=120, stretch=NO)
        self.book_treeview.heading('#4',text='ISBN',anchor=N)
        self.book_treeview.column('#5', width=100, minwidth=100, stretch=NO)
        self.book_treeview.heading('#5',text='대출여부',anchor=N)
        self.book_treeview.column('#6', width=100, minwidth=100, stretch=NO)
        self.book_treeview.heading('#6',text='URL',anchor=N)
        c=1
        #m20aa1=self.name_treeview.insert("", END, text='', values=('', '', '', '', '', ''))
        for i in df_rent_can_book_list:
            rent=self.rent1(i[4])
            m20aa1=self.book_treeview.insert("", END, text=c, values=(i[0], i[1], i[2], i[3], rent, i[5] ), iid= c-1)
            c += 1

        self.book_treeview.grid(row=2, column=0, columnspan=1, rowspan=1, sticky=N)

        #도서대여 버튼 
            
        select_book_btn=ttk.Button(self,text='도서 대여',command=lambda:self.user_rent_book(name))  # 함수추가 하기
        select_book_btn.grid(row=3, column=0, columnspan=1, rowspan=1, sticky=N)
    def rent1(self, r):
        rent =''
        if r == 0: # 대여가능
            rent = '대여가능'

        elif r == 1: # 대여불가
            rent = '대여불가'
        return rent
    

    def user_rent_book(self,name): # 대여 함수 회원 대여수 증가 책 여부 
        global df_rent
        try: # 도서 클릭안하고 도서대여 눌렀을 경우 예외처리 
            self.name=name
            bbb = self.book_treeview.focus() # 트리뷰 클릭한 줄
            print(bbb)
            treeviewValues = self.book_treeview.item(bbb).get('values')
            rentbook=treeviewValues[0]
            rentname=self.name
            print(rentbook)
            print(rentname)
            rentcount = int(df_user.loc[df_user['User_name'].str.contains(rentname),'User_rent_cnt']) # 선택 회원의 대여권수 뽑아오기
            print(rentcount)
            Name_index=df_user.index[df_user['User_name']==rentname] #랜트 한경우  회원의 대여수 증가 
            df_user.loc[Name_index,'User_rent_cnt']=rentcount+1 


            Title_index=df_book.index[df_book['Book_title']==rentbook]
            df_book.loc[Title_index,'Book_pre']=1
            
           

            ##여기까지 유저와 도서 정보저장

            ##여기서부터 랜트 정보 생성
            RentUser=df_user['User_number'].values[Name_index]     #해당 값의 전화번호
            RentingName=df_user['User_name'].values[Name_index]    #해당 값의 이름
            
            RentBook=df_book['Book_ISBN'].values[Title_index]       #해당 도서의 ISBN
            RentingTitle=df_book['Book_title'].values[Title_index]  #해당 도서의 이름
            
            RentUserNumber=RentUser[0]       # User_number 정보
            RentUserName=RentingName[0]      # User_name 정보
            RentBookISBN=RentBook[0]         # Book_ISBN 정보
            RentBookTitle=RentingTitle[0]    # Book_title 정보
            
            Renttoday = date.today() # 빌리는 날짜     #시간추가
            Returnday = Renttoday+datetime.timedelta(days=14) # 반납예정날짜

            row=[RentBookISBN,RentBookTitle,RentUserNumber,RentUserName,Renttoday,Returnday,0] 
            
            df_rent.set_index('SEQ',inplace=True)
            df_rent=df_rent.append(pd.Series(row, index=df_rent.columns),ignore_index =True)
            df_rent.index.name='SEQ'
            df_rent.reset_index(drop=False, inplace=True)                                    
            
          
            df_rent.to_csv('Rent.csv',index=False,encoding='utf-8-sig') # 랜트 정보 csv 파일로 저장
            df_book.to_csv('book3.csv',index=False,encoding='utf-8-sig') # 도서 랜트여부 여기서 저장
            df_user.to_csv('user.csv',index=False,encoding='utf-8-sig') # 유저 랜트수 여기서 저장
            
        except IndexError:
            messagebox.showinfo("알림", "도서를 클릭해주세요\.")
            print("도서를 클릭해주세요. ")
    














class RentInfo(tk.Frame):  ####  대여 전체 정보 페이지

    def __init__(self, master):
        Rentdf = pd.read_csv ('Rent.csv')
        Rentdf_list = Rentdf.values.tolist()
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self, relief='flat', borderwidth=1, pady=5)
        

        self.grid(row=1,column=1)

        #대여전체 정보 레이블
        rentinfo_Label=Label(self, text='대여 전체 정보') 
        rentinfo_Label.grid(row=1, column=0, columnspan=1, rowspan=1, sticky=N)

     

        #트리뷰 생성
        treeview_frame=tk.Frame(self, relief='flat', borderwidth=1,padx=20,pady=10)
        treeview_frame.grid(row=2, column=0, columnspan=8, rowspan=1, sticky=N)

        self.rentinfo_treeview=ttk.Treeview(treeview_frame, height=10, columns=('#1', '#2', '#3', '#4', '#5','#6','#7'))

        self.rentinfo_treeview.column('#0', width=40, minwidth=100, stretch=NO)
        self.rentinfo_treeview.heading('#0',text='번호',anchor=N)
        self.rentinfo_treeview.column('#1', width=120, minwidth=120, stretch=NO)
        self.rentinfo_treeview.heading('#1',text='ISBN',anchor=N)
        self.rentinfo_treeview.column('#2', width=100, minwidth=100, stretch=NO)
        self.rentinfo_treeview.heading('#2',text='도서명',anchor=N)
        self.rentinfo_treeview.column('#3', width=120, minwidth=120, stretch=NO)
        self.rentinfo_treeview.heading('#3',text='전화번호',anchor=N)
        self.rentinfo_treeview.column('#4', width=100, minwidth=100, stretch=NO)
        self.rentinfo_treeview.heading('#4',text='회원명',anchor=N)
        self.rentinfo_treeview.column('#5', width=100, minwidth=100, stretch=NO)
        self.rentinfo_treeview.heading('#5',text='대여시작',anchor=N)
        self.rentinfo_treeview.column('#6', width=100, minwidth=100, stretch=NO)
        self.rentinfo_treeview.heading('#6',text='반납예정일',anchor=N)
        self.rentinfo_treeview.column('#7', width=100, minwidth=100, stretch=NO)
        self.rentinfo_treeview.heading('#7',text='반납여부',anchor=N)
        c=1
        for i in Rentdf_list:
            m20aa1=self.rentinfo_treeview.insert("", END, text=c, values=(i[1], i[2], i[3], i[4], i[5], i[6] ,i[7]), iid= c-1)
            c += 1
            

       

        self.rentinfo_treeview.grid(row=2, column=0, columnspan=1, rowspan=1, sticky=N)


        #정보 빛 반납 버튼 
        
            
        select_rentinfo_btn=ttk.Button(self,text='정보 및 반납',command=' ' )
        select_rentinfo_btn.grid(row=3, column=0, columnspan=1, rowspan=1, sticky=N)

    

#########################################################################
##########################################################################
##################################################################################################
##################################################################################################
##################################################################################################
##################################################################################################
##################################################################################################




if __name__ == "__main__":
    mk = MainTk()
    mk.mainloop()
