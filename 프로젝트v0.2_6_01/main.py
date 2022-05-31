
from tkinter import N, filedialog, font
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

#Rentdf = pd.DataFrame(index=range(0,0), columns=['SEQ', 'Book_ISBN','Book_title','User_number','User_name','Rent_date','Rent_retun','Rent_YN'])
#Rentdf.to_csv('Rent.csv',index=False,encoding='utf-8-sig') #csv파일 생성 최초실행
########################################################################################    

    #win.update()

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
            
            TreeviewText=self.Treeview1.insert("", END, text=c, values=(i[0], i[1], i[2], i[3],rent, i[5] ), iid= c-1)
            c += 1
        self.Treeview1.grid(row=0, column=0, columnspan=1, rowspan=1, sticky=N)

        #tk.Label(self, text="Start page", font=('Helvetica', 18, "bold")).grid(row=0, column=0)
        # 검색 버튼
        btnSearch=ttk.Button(self, text='검색', command=lambda: self.bookSearch() )
        btnSearch.grid(row=1, column=3, columnspan=1, rowspan=1, sticky=N, padx=5)

        # 도서등록 버튼
        btnBookRegist=ttk.Button(self, text='도서등록',command=lambda: self.bookRegisterm())
        btnBookRegist.grid(row=3, column=0, columnspan=1, rowspan=1, sticky=N, padx=25, pady=3)

        # 도서정보 버튼
        btnBookInformation=ttk.Button(self, text='도서정보', command=lambda: self.info_and_edit('info') )
        btnBookInformation.grid(row=3, column=1, columnspan=1, rowspan=1, sticky=W, padx=5, pady=3)

        # 도서수정 버튼
        btnBookEdit=ttk.Button(self, text='도서수정', command=lambda: self.info_and_edit('edit'))
        btnBookEdit.grid(row=3, column=2, columnspan=1, rowspan=1, sticky=W, padx=25, pady=3)

        # 도서 삭제 버튼
        btnBookDelete=ttk.Button(self, text='도서 삭제',command=lambda: self.bookDelete(master) ) 
        btnBookDelete.grid(row=3, column=4, columnspan=1, rowspan=1, sticky=N, padx=25, pady=3)
        ##############대여표시#############
    def rent1(self, r):
            rent =''
            if r == 0: # 대여가능
                rent = '대여가능'

            elif r == 1: # 대여불가
                rent = '대여불가'
            return rent    

    
    ################### 도서 등록 #####################
    def bookRegisterm(self): 
        self.Book_register = Toplevel(self)
        #self.Book_register.attributes('-topmost', 'true')
        self.Book_register.title("도서 등록")
        self.Book_register.geometry("400x450+740+270")
        #self.Book_register.option_add('*Dialog.msg.font', 'Helvetica 40')

        # 도서등록 레이블
        Book_name_label = Label(self.Book_register, text = "제목 :")
        Book_author_label = Label(self.Book_register, text = "저자 :")
        Book_publisher_label = Label(self.Book_register, text = "출판사 :")
        Book_price_label = Label(self.Book_register, text = "가격 :")
        Book_link_label = Label(self.Book_register, text = "관련링크 :")
        Book_ISBN_label = Label(self.Book_register, text = "ISBN :")
        Book_photo_label = Label(self.Book_register, text = "사진 :")
        Book_account_label = Label(self.Book_register, text = "도서 설명 :")


        self.Book_photo_label2 = Label(self.Book_register, text = "파일 열기를 통해 사진을 추가하세요. ", wraplength=350)


        # 도서등록 텍스트
        Book_name_entry = Entry(self.Book_register, width = 30)
        Book_author_entry = Entry(self.Book_register, width = 30)
        Book_publisher_entry = Entry(self.Book_register, width = 30)
        Book_price_entry = Entry(self.Book_register, width = 30)
        Book_link_text = Text(self.Book_register, width = 30, height = 2)
        Book_ISBN_entry = Entry(self.Book_register, width = 30)
        self.Book_photo_entry = Entry(self.Book_register, width = 30)
        
        Book_account_text = Text(self.Book_register, width = 40, height = 5)

        # 도서등록 버튼
        file_open_btn = Button(self.Book_register, text = "파일 열기", command = lambda : self.fileadd('add') )
        save_btn = Button(self.Book_register, text = " 저장 ", command = lambda : self.saveCheck(Book_name_entry, Book_author_entry, Book_publisher_entry, Book_link_text, 
        Book_ISBN_entry, self.Book_photo_label2, Book_account_text, Book_price_entry) )

        # 도서등록 레이블 적용
        Book_name_label.place(x=15,y=20)
        Book_author_label.place(x=15,y=60)
        Book_publisher_label.place(x=15,y=100)
        Book_price_label.place(x=15,y=140)
        Book_link_label.place(x=15,y=190)
        Book_ISBN_label.place(x=15,y=230)
        Book_photo_label.place(x=15,y=270)
        Book_account_label.place(x=15,y=310)

        # 도서등록 텍스트 적용
        Book_name_entry.place(x=100, y=20)
        Book_author_entry.place(x=100, y=60)
        Book_publisher_entry.place(x=100, y=100)
        Book_price_entry.place(x=100, y=140)
        Book_link_text.place(x=100, y=190)
        Book_ISBN_entry.place(x=100, y=230)
        self.Book_photo_label2.place(x=100, y=270)
        Book_account_text.place(x=100, y=310)


        # 도서등록 버튼 적용
        file_open_btn.place(x = 320 ,y = 270)
        save_btn.place(x=200, y= 390)

        self.Book_register.protocol("WM_DELETE_WINDOW", self.on_closing)
        

    ##### 창 닫힐때 메인위도우 새로고침 ##### 
    def on_closing(self):
        df14 = pd.read_csv ('book3.csv', dtype=str)
        df14_list = df14.values.tolist()

        c = 1
        for i in self.Treeview1.get_children(): # 트리뷰의 값들을 다 지워주고 창 새로고침
            self.Treeview1.delete(i)        
        for e in df14_list:
            # 표에 데이터 삽입
            self.Treeview1.insert("", END, text=c, values=(e[0], e[1], e[2], e[3], e[4], e[5] ), iid= c-1)
            c += 1
        self.Book_register.destroy()

    ######################################## 도서 삭제 ########################################## 
    def bookDelete(self, master):
        def rent1(self, r):
            rent =''
            if r == 0: # 대여가능
                rent = '대여가능'

            elif r == 1: # 대여불가
                rent = '대여불가'
            return rent    
        # 도서 클릭안하고 도서정보 버튼 눌렀을 경우 예외처리               
        print("삭제 함수")
        df12 = pd.read_csv ('book3.csv', dtype=str)
        bbb = self.Treeview1.focus()
        treeviewValues = self.Treeview1.item(bbb).get('values')
        if treeviewValues == '':
            messagebox.showinfo("알림", "도서를 클릭해주세요.")
            print("도서를 클릭해주세요. ")
        else :
            if messagebox.askyesno("삭제", "정말 삭제하시겠습니까? "):
                if str(treeviewValues[4]) == '대여가능':
                    isbn = str(treeviewValues[3])  # treeviewValues[3] = <class 'int'>
                    b = df12.index[df12['Book_ISBN'] == isbn].tolist()
                    print(str(treeviewValues[3]) )
                    print(isbn)
                    print(df12['Book_ISBN']== isbn)
                    print(b)
                    df13 = df12.drop(index=b[0], inplace=False)
                    print(df13)
                    df13.to_csv('book3.csv', mode='w', sep=',', index=False, encoding='utf-8-sig')
                    '''
                    isbn = str(treeviewValues[3])  # treeviewValues[3] = <class 'int'>
                    b = df12.index[df12['Book_ISBN'] == isbn].tolist()
                    print(str(treeviewValues[3]) )
                    print(isbn)

                    print(df12['Book_ISBN']== isbn)
                    print(b)
                    print("여기")
                    RentISBN=df12.loc[b[0],'Book_ISBN']
                    ISBN_index=df12.index[df12['Book_ISBN']==RentISBN]
                    df12.loc[ISBN_index,'Book_pre']=1      ######################################삭제하면 도서여부 1로 바꿈
                    print(df12)
                    df12.to_csv('book3.csv', mode='w', sep=',', index=False, encoding='utf-8-sig')
                    '''
                    df14 = pd.read_csv ('book3.csv')
                    df14_list = df14.values.tolist()
                    c = 1
                    for i in self.Treeview1.get_children(): # 트리뷰의 값들을 다 지워주고 창 새로고침
                        self.Treeview1.delete(i)     
                    for e in df14_list:
                        # 표에 데이터 삽입
                        rent = self.rent1(e[4])
                        self.Treeview1.insert("", END, text=c, values=(e[0], e[1], e[2], e[3], rent, e[5] ), iid= c-1) #################삭제하면
                        c += 1
                else :
                    messagebox.showinfo("도서삭제 실패", "반납하지 않은 도서가 있습니다.")

     

    ######################################## 도서 수정 ##########################################
    def bookEdit(self, title, author, publisher, price, link, ISBN, photo, bookdescription):
        self.window = Toplevel()
        self.window.title("도서수정")
        self.window.geometry("400x450+740+270")
        self.window.resizable(0,0)
        
        # 제목 수정
        label_title = Label(self.window, text="제목 : ")
        label_title.grid(row=0, column=0, pady=4)
        e_title = Entry(self.window, width=30)
        e_title.grid(row=0, column=1, pady=4)
        e_title.insert(0, title)

        # 저자 수정
        label_author = Label(self.window, text="저자 : ")
        label_author.grid(row=1, column=0, pady=4)
        e_author = Entry(self.window, width=30)
        e_author.grid(row=1, column=1, pady=4)
        e_author.insert(0, author)

        # 출판사 수정
        label_publish = Label(self.window, text="출판사 : ")
        label_publish.grid(row=2, column=0, pady=4)
        e_publish = Entry(self.window, width=30)
        e_publish.grid(row=2, column=1, pady=4)
        e_publish.insert(0, publisher)

        # 가격 수정
        label_price = Label(self.window, text="가격 : ")
        label_price.grid(row=3, column=0, pady=4)
        e_price = Entry(self.window, width=30)
        e_price.grid(row=3, column=1, pady=4)
        e_price.insert(0, price)

        #  관련링크
        label_link = Label(self.window, text="관련링크 : ")
        label_link.grid(row=4, column=0, pady=4)
        t_link = Text(self.window, width=30, height=2) 
        t_link.grid(row=4, column=1, pady=4)
        t_link.insert(tk.END , link)

        # ISBN 수정
        label_isbn = Label(self.window, text="ISBN : ")
        label_isbn.grid(row=5, column=0, pady=4)
        e_isbn = Entry(self.window, width=30)
        e_isbn.grid(row=5, column=1, pady=4)
        e_isbn.insert(0, ISBN)

        # 사진 수정
        self.label_pic = Label(self.window, text="사진 : ")
        self.label_pic.grid(row=6, column=0, pady=4)

        self.book_photo_label2 = Label(self.window, text = photo, wraplength=350)

        btn_pic = Button(self.window, text="파일 열기", bg="#0099ff", fg="white", command = lambda : self.fileadd('edit'))
        btn_pic.grid(row=6,column=2, padx=8)

        label_explain = Label(self.window, text="도서설명 : ")
        label_explain.grid(row=7, column=0, pady=4)
        t_explain = Text(self.window, width = 40, height = 5)
        t_explain.grid(row=7, column=1, pady=4)
        t_explain.insert(tk.END, bookdescription) 

        btn_edit = Button(self.window, text="수정하기", bg="#0099ff", fg="white", command = lambda :self.edit(e_title, e_author, e_publish,\
        t_link, e_isbn, self.book_photo_label2, t_explain, e_price) )

        btn_edit.grid(row=8,column=0, pady=4) # title, author, publisher, link, ISBN, photo, text, price

        btn_cancel = Button(self.window, text="취소", bg="#0099ff", fg="white", command=())
        btn_cancel.grid(row=8,column=1, pady=4)

        # 도서수정 레이블 적용
        label_title.place(x=15,y=20)
        label_author.place(x=15,y=60)
        label_publish.place(x=15,y=100)
        label_price.place(x=15,y=140)
        label_link.place(x=15,y=190)
        label_isbn.place(x=15,y=230)
        self.label_pic.place(x=15,y=270)
        label_explain.place(x=15,y=310)

        # 도서수정 텍스트 적용
        e_title.place(x=100, y=20)
        e_author.place(x=100, y=60)
        e_publish.place(x=100, y=100)
        e_price.place(x=100, y=140)
        t_link.place(x=100, y=190)
        e_isbn.place(x=100, y=230)
        self.book_photo_label2.place(x=100, y=270)
        t_explain.place(x=100, y=310)


        # 도서수정 버튼 적용
        btn_pic.place(x = 320 ,y = 270)
        btn_edit.place(x=130, y= 390)
        btn_cancel.place(x=230, y= 390)


        self.window.mainloop()



    ### 메인창 새로고침 함수#####
    def reupdate(self):
        df12 = pd.read_csv ('book3.csv')
        df12_list = df12.values.tolist()
        c = 1
        for i in self.Treeview1.get_children(): # 트리뷰의 값들을 다 지워주고 창 새로고침
            self.Treeview1.delete(i)        
        for e in df12_list:
            rent = self.rent1(e[4])
            self.Treeview1.insert("", END, text=c, values=(e[0], e[1], e[2], e[3], rent, e[5] ), iid= c-1)
            c += 1

    def edit(self, title, author, publisher, link, ISBN, photo, text, price):
        df12 = pd.read_csv ('book3.csv',dtype= str)
        df12_list = df12.values.tolist()

        print("@@@@@@@@@@@@@@@@@@@@@")  #### 데이터 확인 소스
        print(title.get())
        print(author.get())
        print(price.get())
        print(ISBN.get())
        rentcheck = 0
        print(link.get("1.0","end"+"-1c"))
        print(publisher.get())
        print(text.get("1.0","end"+"-1c"))
        print(photo.cget('text'))


        aaa = self.Treeview1.focus() # 트리뷰 클릭한 줄
        treeviewValues = self.Treeview1.item(aaa).get('values')
        isbn = []
        for k in df12_list:
            print(f'k : {type(k[3])}') # <class 'str'>
            print(f'k : {type(treeviewValues[3])}') # <class 'int'>
            if k[3] != str(treeviewValues[3]):  # 값은 같은데 일치하지않음
                print("일치")
                isbn.append(k[3])

        print(df12['Book_ISBN'] == '9788975504773111111111111111')

        print("########")
        print(f'csv에 있는 ISBN 목록 : {isbn}')
        print("#########")
        #isbn.remove(str(treeviewValues[3]))

        print(treeviewValues[3])
        print("@@@@@@")
        print(ISBN.get())
        print("@@@@@@")
        print("@@@@@@")

        if ISBN.get() in isbn:
            messagebox.showinfo("중복", "ISBN을 확인해주세요. ")
            print("ISBN중복")
            self.window.lift()
        else :
            a = str(treeviewValues[3])  # <class 'int'>
            print(a)
            print(df12.index[df12['Book_ISBN'] == a].tolist())
            b = df12.index[df12['Book_ISBN'] == a].tolist()
            
            print("b : ")
            print(b[0])
            df12.loc[b[0]] = (title.get(), author.get(), price.get(), ISBN.get(), rentcheck, link.get("1.0","end"+"-1c"), publisher.get(), text.get("1.0","end"+"-1c"), photo.cget('text'))
            df12.to_csv('book3.csv', mode='w', sep=',', index=False, encoding='utf-8-sig')
            print("발견")
            
            self.window.destroy()
            self.reupdate()


            
            
    
    def fileadd(self, key):  # 파일 열기로 이미지 추가 함수  (나중에 예외 처리해야함 )
        if key == 'add':
            self.filename = filedialog.askopenfilename(initialdir='./gif',title='파일선택', filetypes=(('gif files','*.gif'),('jpg files','*.jpg'),('all files','*.*')))
            path = self.filename
            path_list = path.split('/')
            fn = path_list[-1]   # 파일명만 출력하기
            self.Book_photo_label2.configure(text= fn)
            self.Book_register.lift()
        
        elif key == 'edit':
            self.filename = filedialog.askopenfilename(initialdir='./gif',title='파일선택', filetypes=(('gif files','*.gif'),('jpg files','*.jpg'),('all files','*.*')))
            path = self.filename
            path_list = path.split('/')
            fn = path_list[-1]   # 파일명만 출력하기
            self.label_pic.configure(text= fn)
            self.window.lift()

    ######################################## 도서 등록 ##########################################
    def registbook(self, title, author, publisher, link, ISBN, photo, text, price ):
        print("@@@@@@@@@@@@@@@@@@@@@")  #### 데이터 확인 소스
        print(title.get())
        print(author.get())
        print(price.get())
        print(ISBN.get())
        rentcheck = 0
        print(link.get("1.0","end"+"-1c"))
        print(publisher.get())
        print(text.get("1.0","end"+"-1c"))
        print(photo.cget('text'))

        self.addtext = "제목 : " + title.get()+ "\n" + "저자 : " + author.get() + "\n" + "출판사 : " + publisher.get() + "\n"+ "가격 : " + price.get() + "관련링크 : " + link.get("1.0","end"+"-1c")\
                        + "\n" + "ISBN : " + ISBN.get()+ "\n" + "사진 : " + photo.cget('text')+ "\n" + "설명 : " + text.get("1.0","end"+"-1c")+ "\n"
        
        df1 = pd.read_csv ('book3.csv', dtype=str)
        num = int(len(df1))
        print(num)

        df1.loc[num] = [title.get(), author.get(), price.get(), ISBN.get(), rentcheck, link.get("1.0","end"+"-1c"), publisher.get(), text.get("1.0","end"+"-1c"), photo.cget('text')]


        df1.to_csv('book3.csv', mode='w', sep=',', index=False, encoding='utf-8-sig')


    def saveCheck(self, title, author, publisher, link, ISBN, photo, text, price):
        df1 = pd.read_csv ('book3.csv')
        df1_list = df1.values.tolist()
        self.addtext = "제목 : " + title.get()+ "\n" + "저자 : " + author.get() + "\n" + "출판사 : " + publisher.get() + "\n"+ "가격 : " + price.get() + "관련링크 : " + link.get("1.0","end"+"-1c")\
                        + "\n" + "ISBN : " + ISBN.get()+ "\n" + "사진 : " + photo.cget('text')+ "\n" + "설명 : " + text.get("1.0","end"+"-1c")+ "\n"
        if messagebox.askyesno("등록", self.addtext + "정말 등록하시겠습니까? "):
            print("메시지박스 예스 일때 : ")
            print("@@@@@@@@@@@@@@@@@@@@@")  #### 데이터 확인 소스#####
            print(title.get())
            print(author.get())
            print(price.get())
            print(ISBN.get())
            rentcheck = 0
            print(link.get("1.0","end"+"-1c"))
            print(publisher.get())
            print(text.get("1.0","end"+"-1c"))
            print(photo.cget('text'))
            df1 = pd.read_csv ('book3.csv', dtype=str)
            num = int(len(df1))
            print(num)
            df1.loc[num] = [title.get(), author.get(), price.get(), ISBN.get(), rentcheck, link.get("1.0","end"+"-1c"), publisher.get(), text.get("1.0","end"+"-1c"), photo.cget('text')]
            df1.to_csv('book3.csv', mode='w', sep=',', index=False, encoding='utf-8-sig')
            df1 = pd.read_csv ('book3.csv')
            df1_list = df1.values.tolist()
            
            c = 1
            for i in self.Treeview1.get_children(): # 트리뷰의 값들을 다 지워주고 창 새로고침
                self.Treeview1.delete(i)        
            for e in df1_list:
                # 표에 데이터 삽입
                rent =self.rent1(e[4])
                self.Treeview1.insert("", END, text=c, values=(e[0], e[1], e[2], e[3], rent, e[5] ), iid= c-1)
                c += 1
            self.Book_register.destroy()
            #self.self.Book_register.protocol("WM_DELETE_WINDOW", saveCheck)
        else:
            #self.Book_register.deiconify()
            self.Book_register.lift()
            print("존재")

    def rent1(self, r):
            rent =''
            if r == 0: # 대여가능
                rent = '대여가능'

            elif r == 1: # 대여불가
                rent = '대여불가'
            return rent 
    ######## 도서정보, 수정 함수 ########
    def info_and_edit(self, key):
        df1 = pd.read_csv ('book3.csv')
        df1_list = df1.values.tolist()
        print(key)
        if key == 'info':
            try: # 도서 클릭안하고 도서정보 버튼 눌렀을 경우 예외처리 
                aaa = self.Treeview1.focus() # 트리뷰 클릭한 줄
                treeviewValues = self.Treeview1.item(aaa).get('values')
                
                for k in df1_list:
                    if treeviewValues[0] == k[0]  :
                        rent=self.rent1(k[4])
                        bookinfo.bookInfo(k[0], k[1], k[6], k[2], k[5], k[3],rent, k[7], k[8])
            except IndexError:
                messagebox.showinfo("알림", "도서를 클릭해주세요.")
                print("도서를 클릭해주세요. ")

        elif key == 'edit': ## 대여불가 
            try: # 도서 클릭안하고 도서수정 버튼 눌렀을 경우 예외처리
                aaa = self.Treeview1.focus() # 트리뷰 클릭한 줄
                treeviewValues = self.Treeview1.item(aaa).get('values')
                if treeviewValues[4] =='대여불가':
                    messagebox.showinfo("알림", "대여중인책은 수정이 불가합니다.")
                else:
                    for k in df1_list:
                        if treeviewValues[0] == k[0]  : # treeviewValues[0]은 도서명
                            self.bookEdit(k[0], k[1], k[6], k[2], k[5], k[3], k[8], k[7])
            except IndexError:
                messagebox.showinfo("알림", "도서를 클릭해주세요.")
                print("도서를 클릭해주세요. ")

    def rent1(self, r):
            rent =''
            if r == 0: # 대여가능
                rent = '대여가능'

            elif r == 1: # 대여불가
                rent = '대여불가'
            return rent    

    def bookSearch(self):  # 도서 검색
        df1 = pd.read_csv ('book3.csv')
        df1_list = df1.values.tolist()
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

class Userpage(tk.Frame):   #### 전체 회원 페이지 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def __init__(self, master):
        df2 = pd.read_csv ('user.csv')
        df2_list = df2.values.tolist()
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
            cUser = self.currentUser(i[6])
            TreeviewText=self.Treeview1.insert("", END, text=c, values=(i[1], i[2], gen, i[0], cUser, i[7], i[4] ), iid= c-1)
            c += 1
        self.Treeview1.grid(row=0, column=0, columnspan=1, rowspan=1, sticky=N)

        #tk.Label(self, text="Start page", font=('Helvetica', 18, "bold")).grid(row=0, column=0)

        # 회원검색 버튼
        btnSearch=ttk.Button(self, text='검색', command=lambda: self.userSearch() )
        btnSearch.grid(row=1, column=3, columnspan=1, rowspan=1, sticky=N, padx=5)

        # 회원등록 버튼
        btnBookRegist=ttk.Button(self, text='회원등록',command=lambda: self.useradd())
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

    

    def User_add_file(self) : # 사진 파일 열기 버튼 눌렀을 때
        self.User_add_photo = filedialog.askopenfilename(initialdir="./gif", title = "이미지 파일을 선택하세요",\
        filetypes=(('gif files','*.gif'), ("모든 파일","*.*"))) # 최초의 경로를 c 드라이브로 설정
        #self.User_add_photoEntry.insert(END, self.self.User_add_photo) # 사진 파일을 선택 했을 때 엔트리에 주소 넣음
        path = self.User_add_photo
        print(path)
        path_list = path.split('/')
        fn = path_list[-1]   # 파일명만 출력하기
        self.User_add_photoLabel2.configure(text=fn)
        print(fn)
        self.User_add.lift()

    def User_add_save(self, phone_number, name, birth_year, birth_month, birth_day, gender, email, photo): ### 유저등록 여기부터 시작 
        print("년도")
        print(self.User_add_yearCombobox.get())
        print(birth_year.get())
        birth = self.User_add_yearCombobox.get() + "-" + self.User_add_monthCombobox.get() + "-" + self.User_add_dayCombobox.get()
        gen = '남성'
        if gender == 0 : 
            gen = '여성'
        self.addtext = "이름 : " + self.User_add_nameEntry.get()+ "\n" + "생년월일 : " + birth + "\n" + "성별 : " + gen + "\n"+ "전화번호 : " + phone_number.get() + "이메일 주소 : " + email.get()\
                        + "\n" + "사진 : " + photo.cget('text')+ "\n"
        print(self.addtext)
        if messagebox.askyesno("등록", self.addtext + "정말 등록하시겠습니까? "):
            print("메시지박스 예스 일때 : ")
            print("@@@@@@@@@@@@@@@@@@@@@")  #### 데이터 확인 소스#####
            #print(phone_number.get())
            #print(name.get())
            #print(birth)
            #print(gen)
            #rentcheck = 0
            #print(link.get("1.0","end"+"-1c"))
            #print(publisher.get())
            #print(text.get("1.0","end"+"-1c"))
            print(photo.cget('text'))
           # df1 = pd.read_csv ('book3.csv', dtype=str)
            #num = int(len(df1))
            #print(num)
            #df1.loc[num] = [title.get(), author.get(), price.get(), ISBN.get(), rentcheck, link.get("1.0","end"+"-1c"), publisher.get(), text.get("1.0","end"+"-1c"), photo.cget('text')]
            #df1.to_csv('book3.csv', mode='w', sep=',', index=False, encoding='utf-8-sig')
            
            #df1_list = df1.values.tolist()
            c = 1
            #for i in self.Treeview1.get_children(): # 트리뷰의 값들을 다 지워주고 창 새로고침
            #    self.Treeview1.delete(i)        
            #for e in df1_list:
            #    # 표에 데이터 삽입
            #    self.Treeview1.insert("", END, text=c, values=(e[0], e[1], e[2], e[3], e[4], e[5] ), iid= c-1)
            #    c += 1
            #self.User_add.destroy()
            #self.self.User_add.protocol("WM_DELETE_WINDOW", saveCheck)
        #else:
            #self.User_add.deiconify()
            #self.User_add.lift()
            #print("존재")

    def daychange() : # 생년월일 월에따른 일 수
        pass

    def useradd(self):
        self.User_add=Toplevel()
        self.User_add.title('회원 등록')
        self.User_add.geometry("460x350+720+290")
        self.User_add.resizable(False, False)

        # 이름 프레임
        self.User_add_nameFrame=Frame(self.User_add, relief='flat', borderwidth=1, padx =20 , pady = 20)
        self.User_add_nameFrame.grid(row=0, column=0, sticky=W)
        # 이름 레이블
        self.User_add_nameLabel=Label(self.User_add_nameFrame, text='이 름 :', width= 10)
        self.User_add_nameLabel.grid(row=0, column=0, columnspan=1, rowspan=1, sticky=N, padx=10)
        # 이름 엔트리
        self.User_add_nameEntry=ttk.Entry(self.User_add_nameFrame ,width='30')
        self.User_add_nameEntry.grid(row=0, column=1, columnspan=1, rowspan=1, sticky=N)


        # 생년월일 프레임
        self.User_add_birthFrame=Frame(self.User_add, relief='flat', borderwidth=1, padx =20)
        self.User_add_birthFrame.grid(row=1, column=0, sticky=W)
        # 생년월일 레이블 ( 생년월일 : )
        self.User_add_birthLabel=Label(self.User_add_birthFrame, text='생년월일 :', width= 10)
        self.User_add_birthLabel.grid(row=0, column=0, columnspan=1, rowspan=1, sticky=N, padx=10)
        #생년월일 년도 콤보박스 ( OO년 )
        years = list(range(1950,2023))
        self.User_add_yearCombobox=ttk.Combobox(self.User_add_birthFrame, values = years, width=5)
        self.User_add_yearCombobox.current(0)
        self.User_add_yearCombobox.grid(row=0, column=1, sticky=W, padx =2)
        # 생년월일 년 레이블 ( OO년 )
        self.User_add_yearLabel=Label(self.User_add_birthFrame, text='년')
        self.User_add_yearLabel.grid(row=0, column=2, sticky=W, padx =2)
        # 생년월일 월 콤보박스 ( OO월 )
        month = list(range(1,13))
        self.User_add_monthCombobox=ttk.Combobox(self.User_add_birthFrame, values = month, width=3)
        self.User_add_monthCombobox.current(0)
        self.User_add_monthCombobox.grid(row=0, column=3, sticky=W, padx =2)
        # 생년월일 월 레이블 ( OO월 )
        self.User_add_monthLabel=Label(self.User_add_birthFrame, text='월')
        self.User_add_monthLabel.grid(row=0, column=4, columnspan=1, rowspan=1, sticky=N, padx =2)
        # 생년월일 일 콤보박스 ( OO일 )
        days = list(range(1,32))
        self.User_add_dayCombobox=ttk.Combobox(self.User_add_birthFrame, values = days, width=3)
        self.User_add_dayCombobox.current(0)
        self.User_add_dayCombobox.grid(row=0, column=5, sticky=W, padx =2)
        # 생년월일 월 레이블 ( OO월 )
        self.User_add_dayCombobox2=Label(self.User_add_birthFrame, text='일')
        self.User_add_dayCombobox2.grid(row=0, column=6, columnspan=1, rowspan=1, sticky=N, padx =2)

        # 성별 프레임
        self.User_add_sexFrame=Frame(self.User_add, relief='flat', borderwidth=1, padx =20, pady=20)
        self.User_add_sexFrame.grid(row=2, column=0, sticky=W)
        # 성별 레이블
        self.User_add_sexLabel=Label(self.User_add_sexFrame, text='성별 :', width= 10)
        self.User_add_sexLabel.grid(row=0, column=0, columnspan=1, rowspan=1, sticky=N, padx=10)
        # 성별 라디오 버튼
        sexcheck = IntVar()
        sexcheck.set('1') # 라디오 버튼 기본값 남자로 설정
        self.User_add_manBtn=Radiobutton(self.User_add_sexFrame, text='남자', value = '1', variable = sexcheck) # 남자 체크시 sexcheck에 1 저장
        self.User_add_manBtn.grid(row=0, column=1, columnspan=1, rowspan=1, sticky=N)
        self.User_add_womanBtn=Radiobutton(self.User_add_sexFrame, text='여자', value = '2', variable = sexcheck)# 여자 체크시 sexcheck에 2 저장
        self.User_add_womanBtn.grid(row=0, column=2, columnspan=1, rowspan=1, sticky=N)


        # 메인 프레임
        self.User_add_mainFrame=Frame(self.User_add, relief='flat', borderwidth=1, padx =20)
        self.User_add_mainFrame.grid(row=3, column=0, sticky=W)

        # 휴대전화 레이블
        self.User_add_phoneLabel=Label(self.User_add_mainFrame, text='휴대전화 :', width= 10)
        self.User_add_phoneLabel.grid(row=0, column=0, columnspan=1, rowspan=1, sticky=N, padx=10, pady=10)
        # 휴대전화 엔트리
        self.User_add_phoneEntry=ttk.Entry(self.User_add_mainFrame ,width='30')
        self.User_add_phoneEntry.grid(row=0, column=1, columnspan=1, rowspan=1, sticky=N, padx=10, pady=10)

        # 이메일 주소 레이블
        self.User_add_emailLabel=Label(self.User_add_mainFrame, text='이메일 주소 :', width= 10)
        self.User_add_emailLabel.grid(row=1, column=0, columnspan=1, rowspan=1, sticky=N, padx=10, pady=10)
        # 이메일 주소 엔트리
        self.User_add_emailEntry=ttk.Entry(self.User_add_mainFrame ,width='30')
        self.User_add_emailEntry.grid(row=1, column=1, columnspan=1, rowspan=1, sticky=N, padx=10, pady=10)

        # 사진 레이블
        self.User_add_photoLabel=Label(self.User_add_mainFrame, text='사진', width= 10)
        self.User_add_photoLabel.grid(row=2, column=0, columnspan=1, rowspan=1, sticky=N, padx=10, pady=10)

        self.User_add_photoLabel2=Label(self.User_add_mainFrame, text=' ', width= 10)
        self.User_add_photoLabel2.grid(row=2, column=1, columnspan=1, rowspan=1, sticky=N, padx=10, pady=10)

        # 사진 엔트리
        #self.User_add_photoEntry=ttk.Entry(self.User_add_mainFrame ,width='30')
       # self.User_add_photoEntry.grid(row=2, column=1, columnspan=1, rowspan=1, sticky=N, padx=10, pady=10)

        # 사진 파일 열기 버튼
        self.User_add_fileBtn=ttk.Button(self.User_add_mainFrame,text='파일 열기', command=lambda: self.User_add_file() )
        self.User_add_fileBtn.grid(row=2, column=2, columnspan=1, rowspan=1, sticky=N, padx = 5, pady =6)

        # 저장 버튼
        self.User_add_saveBtn=ttk.Button(self.User_add_mainFrame,text='저장', command = lambda : self.User_add_save(self.User_add_phoneEntry, self.User_add_nameEntry, self.User_add_yearCombobox, \
            self.User_add_monthCombobox, self.User_add_dayCombobox, sexcheck, self.User_add_emailEntry, self.User_add_photoLabel2))
        self.User_add_saveBtn.grid(row=3, column=1, columnspan=1, rowspan=1, sticky=N, pady =20)


    ######################################## 유저 삭제 ##########################################
    def bookDelete(self, master):
        print("유저 삭제 함수")
        df12 = pd.read_csv ('user.csv', dtype=str)
        bbb = self.Treeview1.focus()
        treeviewValues = self.Treeview1.item(bbb).get('values')
        if messagebox.askyesno("삭제", "정말 삭제하시겠습니까? "):
            if str(treeviewValues[4]) == '0':
                isbn = str(treeviewValues[3])  # treeviewValues[3] = <class 'int'>
                b = df12.index[df12['Book_ISBN'] == isbn].tolist()
                print(str(treeviewValues[3]) )
                print(isbn)
                print(df12['Book_ISBN']== isbn)
                print(b)
                df13 = df12.drop(index=b[0], inplace=False)
                print(df13)
                df13.to_csv('book3.csv', mode='w', sep=',', index=False, encoding='utf-8-sig')

                df14 = pd.read_csv ('book3.csv', dtype=str)
                df14_list = df14.values.tolist()
                c = 1
                for i in self.Treeview1.get_children(): # 트리뷰의 값들을 다 지워주고 창 새로고침
                    self.Treeview1.delete(i)        
                for e in df14_list:
                    # 표에 데이터 삽입
                    self.Treeview1.insert("", END, text=c, values=(e[0], e[1], e[2], e[3], e[4], e[5] ), iid= c-1)
                    c += 1
            else :
                messagebox.showinfo("유저삭제 실패", "반납하지 않은 유저가 있습니다.")

    ### 메인창 새로고침 함수#####
    def userupdate(self):
        df12 = pd.read_csv ('user.csv', dtype=str)
        df12_list = df12.values.tolist()
        c = 1
        for i in self.Treeview1.get_children(): # 트리뷰의 값들을 다 지워주고 창 새로고침
            self.Treeview1.delete(i)        
        for e in df12_list:
            # 표에 데이터 삽입
            self.Treeview1.insert("", END, text=c, values=(e[0], e[1], e[2], e[3], e[4], e[5] ), iid= c-1)
            c += 1

    def userinfo(self): # 트리뷰 클릭한 값 넘기기
        try: # 도서 클릭안하고 도서정보 버튼 눌렀을 경우 예외처리
            df2 = pd.read_csv ('user.csv', dtype=str)
            df2_list = df2.values.tolist()
            bbb = self.Treeview1.focus() # 트리뷰 클릭한 줄
            print(bbb)
            treeviewValues = self.Treeview1.item(bbb).get('values')
            print(treeviewValues)
            for k in df2_list:
                print(k)
                print(k[0])
                if treeviewValues[3] == k[0]  :
                    gen = self.gender1(k[3])
                    userinfo.userInfo(k[1], k[2], k[0], gen, k[4], k[7], k[5], k[6], k[8])
        except IndexError:
            messagebox.showinfo("알림", "회원를 클릭해주세요.")
            print("회원를 클릭해주세요. ")

    def userSearch(self):  # 회원 검색
        df2 = pd.read_csv ('user.csv', dtype=str)
        df2_list = df2.values.tolist()
        searchText = self.entryValue.get() # 검색창 값 가져오기
        print(searchText)
        cboxText = self.comboBox1.get() # 콤보박스 값 가져오기
        print("콤보박스 : "+cboxText)

        for i in self.Treeview1.get_children(): # 트리뷰의 값들을 다 지워주고 창 새로고침
            self.Treeview1.delete(i)

        if self.comboBox1.get() == '이름':
            c = 1
            for e in df2_list:
                if self.entryValue.get() in e[1]: # 이름과 부분일치할 경우 
                    gen = self.gender1(e[3])
                    cUser = self.currentUser(e[6])
                    # 표에 데이터 삽입
                    TreeviewText=self.Treeview1.insert("", END, text=c, values=(e[1], e[2], gen, e[0], cUser, e[7], e[4] ), iid= c-1)
                    c += 1
        elif self.comboBox1.get() == '전화번호':
            c = 1
            for e in df2_list:
                if self.entryValue.get() in e[0]: # 전화번호와 부분일치할 경우 
                    gen = self.gender1(e[3])
                    cUser = self.currentUser(e[6])
                    # 표에 데이터 삽입
                    TreeviewText=self.Treeview1.insert("", END, text=c, values=(e[1], e[2], gen, e[0], cUser, e[7], e[4] ), iid= c-1)
                    c += 1 

    def gender1(self, g):
        gen =''
        if g == 0: # 여성

            gen = '여성'

        elif g == 1: # 남성
            gen = '남성'
        return gen

    def currentUser(self, c):
        print(str(c))
        cUser = ''
        if c == ' ' : # 회원
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
    
    
    
    def __init__(self, master):
    
        
        df2 = pd.read_csv ('user.csv') ## 회원정보 받아오기

        df2_rent_can_user=df2.groupby('User_out_Date').get_group(" ") # 탈퇴한 회원은 못빌리도록 미리 빼둠
        df2_rent_can_user_list = df2_rent_can_user.values.tolist() 

        tk.Frame.__init__(self, master)
        tk.Frame.configure(self, relief='flat', borderwidth=1, pady=5)
        
        frame_r=Frame(self, relief='flat', borderwidth=1,padx=5,pady=10)
        frame_r.grid(row=1,column=1)

        #이름레이블
        name_Label=Label(frame_r, text='이름') 
        name_Label.grid(row=1, column=0, columnspan=1, rowspan=1, sticky=N)

        # 이름 검색 엔트리창
        rent_name_Entry=ttk.Entry(frame_r,width='17') # 이름검색 Entry
        rent_name_Entry.grid(row=1, column=1, columnspan=1, rowspan=1, sticky=W,pady =1)
        
       

        #이름 검색 버튼 
        search_name_btn=ttk.Button(frame_r,text='검색',command=' ') # 함수 커맨트 빈칸
        search_name_btn.grid(row=1, column=2, columnspan=1, rowspan=1, sticky=W,pady =1)




        #트리뷰 생성
        treeview_frame=tk.Frame(frame_r, relief='flat', borderwidth=1,padx=20,pady=10)
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
        select_name_btn=ttk.Button(frame_r,text='회원 선택',command=lambda: [self.userselect(),frame_r.destroy()]) # 도서 선택 나중에 기능추가해서 수정해야함 
        
        select_name_btn.grid(row=3, column=0, columnspan=1, rowspan=1, sticky=N)
        #tk.Label(self, text="대여하기", font=('Helvetica', 18, "bold")).grid(row=0, column=0)
        
    def switch_frame(self, frame_class):
        new_frame = frame_class
        self = new_frame
        
        

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
            rentnumber=treeviewValues[3]
            self.switch_frame(RentBook(self,rentname,rentnumber)) #  회원선택후 회원이름 가지고 도서대여창으로 넘기는 곳

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

########################################################################################################################################


df_user = pd.read_csv ('user.csv')
df_book = pd.read_csv ('book3.csv') 
df_rent = pd.read_csv('Rent.csv')

class RentBook(tk.Frame):  #### 대여하기 (도서) 선택 페이지
    
    
    
    def __init__(self, master, name, number): ## 선택회원 이름을 가지고옴
        
        df_book = pd.read_csv ('book3.csv')
        df_user = pd.read_csv ('user.csv')
        df_rent = pd.read_csv('Rent.csv')

        df_rent_can_book=df_book.groupby('Book_pre').get_group(0)
        
        df_rent_can_book_list = df_rent_can_book.values.tolist()
        
         
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self, relief='flat', borderwidth=1, pady=5)
        
        #frame_rb=Frame(self, relief='flat', borderwidth=1,padx=5,pady=10)
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

        name_Label=Label(self, text='빌리는회원 :'+name + number) 
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
            
        select_book_btn=ttk.Button(self,text='도서 대여',command=lambda:[self.user_rent_book(number)])  # 함수추가 하기
        select_book_btn.grid(row=3, column=0, columnspan=1, rowspan=1, sticky=N)

    def rent1(self, r):
        rent =''
        if r == 0: # 대여가능
            rent = '대여가능'

        elif r == 1: # 대여불가
            rent = '대여불가'
        return rent
    def successRent(self):
        messagebox.showinfo("알림", "대여완료.")

    def switch_frame(self, frame_class):
        new_frame = frame_class
        self= new_frame

    def user_rent_book(self,number): # 대여 함수 회원 대여수 증가 책 여부 
        
        try: # 도서 클릭안하고 도서대여 눌렀을 경우 예외처리 
            self.number=number
            bbb = self.book_treeview.focus() # 트리뷰 클릭한 줄
            print(bbb)
            treeviewValues = self.book_treeview.item(bbb).get('values')
            rentisbn=treeviewValues[3]
            df_user = pd.read_csv ('user.csv')
            df_book =pd.read_csv('book3.csv')
            rentnumber=self.number
            print(rentisbn)
            print(rentnumber)
            rentcount = int(df_user.loc[df_user['User_number'].str.contains(rentnumber),'User_rent_cnt']) # 선택 회원의 대여권수 뽑아오기
            print(rentcount)
            Number_index=df_user.index[df_user['User_number']==rentnumber] #랜트 한경우  회원의 대여수 증가 
            df_user.loc[Number_index,'User_rent_cnt']=rentcount+1 


            ISBN_index=df_book.index[df_book['Book_ISBN']==rentisbn]
            df_book.loc[ISBN_index,'Book_pre']=1

            df_book.to_csv('book3.csv',index=False,encoding='utf-8-sig') # 도서 랜트여부 여기서 저장
            df_user.to_csv('user.csv',index=False,encoding='utf-8-sig') # 유저 랜트수 여기서 저장

            ##여기까지 유저와 도서 정보저장

            ##여기서부터 랜트 정보 생성
            df_rent = pd.read_csv('Rent.csv')
            RentUser=df_user['User_number'].values[Number_index]     #해당 값의 전화번호
            RentingName=df_user['User_name'].values[Number_index]    #해당 값의 이름
            
            RentBook=df_book['Book_ISBN'].values[ISBN_index]       #해당 도서의 ISBN
            RentingTitle=df_book['Book_title'].values[ISBN_index]  #해당 도서의 이름
            
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
            
            #self.switch_frame(Userpage(self)) #  회원선택후 회원이름 가지고 도서대여창으로 넘기는 곳
            self.destroy()
            self.successRent()
            
        except IndexError:
            messagebox.showinfo("알림", "도서를 클릭해주세요\.")
            print("도서를 클릭해주세요. ")
    




####################################################################################################################################################





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
        treeview_frame.grid(row=2, column=0, columnspan=7, rowspan=1, sticky=N)

        self.rentinfo_treeview=ttk.Treeview(treeview_frame, height=10, columns=('#1', '#2', '#3', '#4', '#5','#6','#7','#8'))

        self.rentinfo_treeview.column('#0', width=0, minwidth=100, stretch=NO)
        self.rentinfo_treeview.heading('#0',text=' ',anchor=N)
        self.rentinfo_treeview.column('#1', width=40, minwidth=100, stretch=NO)
        self.rentinfo_treeview.heading('#1',text='번호',anchor=N)
        self.rentinfo_treeview.column('#2', width=120, minwidth=120, stretch=NO)
        self.rentinfo_treeview.heading('#2',text='ISBN',anchor=N)
        self.rentinfo_treeview.column('#3', width=100, minwidth=100, stretch=NO)
        self.rentinfo_treeview.heading('#3',text='도서명',anchor=N)
        self.rentinfo_treeview.column('#4', width=120, minwidth=120, stretch=NO)
        self.rentinfo_treeview.heading('#4',text='전화번호',anchor=N)
        self.rentinfo_treeview.column('#5', width=100, minwidth=100, stretch=NO)
        self.rentinfo_treeview.heading('#5',text='회원명',anchor=N)
        self.rentinfo_treeview.column('#6', width=100, minwidth=100, stretch=NO)
        self.rentinfo_treeview.heading('#6',text='대여시작',anchor=N)
        self.rentinfo_treeview.column('#7', width=100, minwidth=100, stretch=NO)
        self.rentinfo_treeview.heading('#7',text='반납예정일',anchor=N)
        self.rentinfo_treeview.column('#8', width=100, minwidth=100, stretch=NO)
        self.rentinfo_treeview.heading('#8',text='반납여부',anchor=N)
        c=1
        for i in Rentdf_list:
            YN=self.returnYN(i[7])
            SEQ=int(i[0])+1
            m20aa1=self.rentinfo_treeview.insert("", END,  values=(SEQ,i[1], i[2], i[3], i[4], i[5], i[6] ,YN), iid=i)
            
            
        self.rentinfo_treeview.grid(row=2, column=0, columnspan=1, rowspan=1, sticky=N)


        #정보 빛 반납 버튼 
        
        
            
        select_rentinfo_btn=ttk.Button(self,text='대여 정보 보기',command=lambda : self.rentinfoframe())
        select_rentinfo_btn.grid(row=3, column=0, columnspan=1, rowspan=1, sticky=N)
        
        select_rentreturn_btn=ttk.Button(self,text='대여 반납 ',command=lambda : self.returnbook())
        select_rentreturn_btn.grid(row=3, column=1, columnspan=1, rowspan=1, sticky=N)
    def returnYN(self, r):
            rentyn =''
            if r == 1: 
                rentyn = '반납완료'

            elif r == 0: 
                rentyn = '대여중'
            return rentyn  
    def returnbook(self):
        if messagebox.askokcancel("대여반납", "도서 반납 하시겠습니까?"):
            Rentdf = pd.read_csv("Rent.csv")
            print("반납시작")
            aaa = self.rentinfo_treeview.focus() # 트리뷰 클릭한 줄
            treeviewValues = self.rentinfo_treeview.item(aaa).get('values')
            if str(treeviewValues[7])=="대여중":
                
                ReturnSEQ=int(treeviewValues[0])-1

                Returnisbn=treeviewValues[1]
                Returnnumber=treeviewValues[3]
                

                Rentdfindex=Rentdf.index[Rentdf['SEQ']==ReturnSEQ]
                Rentdf.loc[Rentdfindex,'Rent_YN']=1
                Rentdf.to_csv('Rent.csv',index=False,encoding='utf-8-sig') ##내보내기
                
                Rentdf_after = pd.read_csv("Rent.csv")
                Rentdf_after_list=Rentdf_after.values.tolist()
                
                for e in self.rentinfo_treeview.get_children():
                    self.rentinfo_treeview.delete(e)

                for i in Rentdf_after_list:
                    YN=self.returnYN(i[7])
                    SEQ=int(i[0])+1
                    self.rentinfo_treeview.insert("", END,  values=(SEQ,i[1], i[2], i[3], i[4], i[5], i[6] ,YN), iid=i)
                    
                


                #####유저와 도서 정보 바꾸기####
                Bookdf = pd.read_csv('book3.csv',encoding='utf-8-sig')
                Userdf = pd.read_csv('user.csv',encoding='utf-8-sig')
                
                rentcount = int(Userdf.loc[Userdf['User_number'].str.contains(Returnnumber),'User_rent_cnt']) # 선택 회원의 대여권수 뽑아오기
                Number_index=Userdf.index[Userdf['User_number']==Returnnumber] #랜트 한경우  회원의 대여수 증가 
                Userdf.loc[Number_index,'User_rent_cnt']=rentcount-1
                ISBN_index=Bookdf.index[Bookdf['Book_ISBN']==Returnisbn]
                Bookdf.loc[ISBN_index,'Book_pre']=0      #반납 한경우 책 여부0
                messagebox.showinfo("반납완료","반납이 완료되었습니다.")
                Bookdf.to_csv('book3.csv',index=False,encoding='utf-8-sig') # 도서 랜트여부 여기서 저장
                Userdf.to_csv('user.csv',index=False,encoding='utf-8-sig') # 유저 랜트수 여기서 저장

            else:
                messagebox.showinfo("이미반납", "이미반납처리된 내역입니다.")
        else:
            print("반납취소")
    
    
    
    def rentinfoframe(self):
            try: # 도서 클릭안하고 도서정보 버튼 눌렀을 경우 예외처리 
                aaa = self.rentinfo_treeview.focus() # 트리뷰 클릭한 줄
                treeviewValues = self.rentinfo_treeview.item(aaa).get('values')
                self.rentInfo(treeviewValues[4],treeviewValues[3],treeviewValues[2],treeviewValues[1],treeviewValues[5],treeviewValues[6],treeviewValues[7])
                
            except IndexError:
                messagebox.showinfo("알림", "대여내역을 클릭해주세요.")
                print("대여내역를 클릭해주세요. ")

    

    
    def rentInfo(self, name, number, title, isbn, rentday, returnday, returnYN):
            self.window = Tk()
            self.window.title("대여 정보")
            self.window.geometry("300x300+740+270")
            self.window.resizable(0,0)
            

                # 이름 넣는 곳
            labelName=Label(self.window, text='이름 : ')
            labelName.grid(row=1, column=0, columnspan=1, rowspan=2, pady=5,padx=5, sticky=W) # sticky : 위치 조정(n, e, s, w, nw, ne, sw, se)

            # 이름 넣는 곳
            labelTitleText=Label(self.window, text=name)
            labelTitleText.grid(row=1, column=1, columnspan=1, rowspan=2, pady=5 ,padx=5, sticky=W)

        

            # 전화번호 넣는 곳
            labelNumber=Label(self.window, text='전화번호')
            labelNumber.grid(row=3, column=0, columnspan=1, rowspan=2,pady=5, padx=5,sticky=W)

            # 전화번호 넣는 곳
            labelNumberText=Label(self.window, text= number)
            labelNumberText.grid(row=3, column=1, columnspan=1, rowspan=2, pady=5, padx=5,sticky=W)

            # 도서명 넣는 곳
            labelTitle=Label(self.window, text='도서명 : ')
            labelTitle.grid(row=5, column=0, columnspan=1, rowspan=2,pady=5, padx=5,sticky=W)

            # 도서명 넣는 곳
            labelTitleText=Label(self.window, text= title)
            labelTitleText.grid(row=5, column=1, columnspan=1, rowspan=2, pady=5,padx=5, sticky=W)

            # ISBN 넣는 곳
            labelISBN=Label(self.window, text='ISBN : ')
            labelISBN.grid(row=7, column=0, columnspan=1, rowspan=2,pady=5, padx=5, sticky=W)

            # ISBN 넣는 곳
            labelISBNText=Label(self.window, text= isbn)
            labelISBNText.grid(row=7, column=1, columnspan=1, rowspan=2,pady=5, padx=5, sticky=W)

            # 대출일  넣는 곳
            labelRentday=Label(self.window, text='대출일 : ')
            labelRentday.grid(row=9, column=0, columnspan=1, rowspan=2, pady=5, padx=5, sticky=W)

            # 대출일 넣는 곳
            labelRentdayText=Label(self.window, text= rentday) # wraplength : 자동 줄내림 설정
            labelRentdayText.grid(row=9, column=1, columnspan=1, rowspan=2,pady=5, padx=5, sticky=W)
            

            # 예정일 넣는 곳
            labelBackday=Label(self.window, text='반납예정일 : ')
            labelBackday.grid(row=11, column=0, columnspan=1, rowspan=2, pady=5, padx=5, sticky=W)

            # 예정일 넣는 곳
            labelBackdayText=Label(self.window, text= returnday)
            labelBackdayText.grid(row=11, column=1, columnspan=1, rowspan=2,pady=5, padx=5, sticky=W)

            # 반납 여부 넣는 곳
            labelReturnYN=Label(self.window, text='대여 여부 : ')
            labelReturnYN.grid(row=13, column=0, columnspan=1, rowspan=2, pady=5, padx=5, sticky=W)

            # 반납 여부 넣는 곳
            labelReturnYNText=Label(self.window, text= returnYN)
            labelReturnYNText.grid(row=13, column=1, columnspan=1, rowspan=2,pady=5, padx=5, sticky=W)

        
            btn_exit = Button(self.window, text="확인완료", bg="blue", fg="white",command =self.quit)
            btn_exit.grid(row=15, column=1, pady=4)


            self.window.mainloop()

    def quit(self):
       self.window.destroy()
    
    

###################################################################################################################################################

if __name__ == "__main__":
    mk = MainTk()
    mk.mainloop()
