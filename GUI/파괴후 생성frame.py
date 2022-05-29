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
        submenu3.add_command(label='대여정보,반납', command=() )
        self.config(menu=menubar1)
        self._frame.grid(row=0, column=0)


class BookPage(tk.Frame):  #### 전체 도서 페이지 
    def __init__(self, master):
        self.df1 = pd.read_csv ('book3.csv')
        self.df1_list = self.df1.values.tolist()

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
        for i in self.df1_list:
            TreeviewText=self.Treeview1.insert("", END, text=c, values=(i[0], i[1], i[2], i[3], i[4], i[5] ), iid= c-1)
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
        btnBookDelete=ttk.Button(self, text='도서 삭제',command=() ) 
        btnBookDelete.grid(row=3, column=4, columnspan=1, rowspan=1, sticky=N, padx=25, pady=3)

        

    
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


    def edit(self, title, author, publisher, link, ISBN, photo, text, price):
        df12 = pd.read_csv ('book3.csv', dtype=str)
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

        print(df12['ISBN'] == '9788975504773111111111111111')

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
            print(df12.index[df12['ISBN'] == a].tolist())
            b = df12.index[df12['ISBN'] == a].tolist()
            
            print("b : ")
            print(b[0])
            df12.loc[b[0]] = (title.get(), author.get(), price.get(), ISBN.get(), rentcheck, link.get("1.0","end"+"-1c"), publisher.get(), text.get("1.0","end"+"-1c"), photo.cget('text'))
            df12.to_csv('book3.csv', mode='w', sep=',', index=False, encoding='utf-8-sig')
            print("발견")
            
    
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
            
            df1_list = df1.values.tolist()
            c = 1
            for i in self.Treeview1.get_children(): # 트리뷰의 값들을 다 지워주고 창 새로고침
                self.Treeview1.delete(i)        
            for e in df1_list:
                # 표에 데이터 삽입
                self.Treeview1.insert("", END, text=c, values=(e[0], e[1], e[2], e[3], e[4], e[5] ), iid= c-1)
                c += 1
            self.Book_register.destroy()
            #self.self.Book_register.protocol("WM_DELETE_WINDOW", saveCheck)
        else:
            #self.Book_register.deiconify()
            self.Book_register.lift()
            print("존재")

    
    ######## 도서정보, 수정 함수 ########
    def info_and_edit(self, key): 
        print(key)
        if key == 'info':
            try: # 도서 클릭안하고 도서정보 버튼 눌렀을 경우 예외처리 
                aaa = self.Treeview1.focus() # 트리뷰 클릭한 줄
                treeviewValues = self.Treeview1.item(aaa).get('values')
                for k in self.df1_list:
                    if treeviewValues[0] == k[0]  :
                        bookinfo.bookInfo(k[0], k[1], k[6], k[2], k[5], k[3], k[4], k[7], k[8])
            except IndexError:
                messagebox.showinfo("알림", "도서를 클릭해주세요.")
                print("도서를 클릭해주세요. ")

        elif key == 'edit':
            try: # 도서 클릭안하고 도서수정 버튼 눌렀을 경우 예외처리
                aaa = self.Treeview1.focus() # 트리뷰 클릭한 줄
                treeviewValues = self.Treeview1.item(aaa).get('values')
                for k in self.df1_list:
                    if treeviewValues[0] == k[0]  : # treeviewValues[0]은 도서명
                        self.bookEdit(k[0], k[1], k[6], k[2], k[5], k[3], k[8], k[7])
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
            for e in self.df1_list:
                if self.entryValue.get() in e[0]: # 제목과 부분일치할 경우 
                    # 표에 데이터 삽입
                    TreeviewText=self.Treeview1.insert("", END, text=c, values=(e[0], e[1], e[2], e[3], e[4], e[5] ), iid= c-1)
                    c += 1
        elif self.comboBox1.get() == '저자':
            c = 1
            for e in self.df1_list:
                if self.entryValue.get() in e[1]: # 저자와 부분일치할 경우 
                    # 표에 데이터 삽입
                    TreeviewText=self.Treeview1.insert("", END, text=c, values=(e[0], e[1], e[2], e[3], e[4], e[5] ), iid= c-1)
                    c += 1

    def keyEvent(self, event):  # 실시간 검색 기능
        if 8 <= event.keycode <= 105:
            self.bookSearch()
            print(event.keycode)

class Userpage(tk.Frame):   #### 전체 회원 페이지 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    df2 = pd.read_csv ('user.csv')
    df2_list = df2.values.tolist()
    def __init__(self, master):
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
        for i in self.df2_list:
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
                    userinfo.userInfo(k[1], k[2], k[0], gen, k[4], k[3], k[5], k[6], k[8])
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
                    cUser = self.currentUser(e[6])
                    # 표에 데이터 삽입
                    TreeviewText=self.Treeview1.insert("", END, text=c, values=(e[1], e[2], gen, e[0], cUser, e[7], e[4] ), iid= c-1)
                    c += 1
        elif self.comboBox1.get() == '전화번호':
            c = 1
            for e in self.df2_list:
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
        if c != c : # 회원
            cUser = '회원'

        else : # 탈퇴회원
            cUser = '탈퇴회원'
        return cUser

    def keyEvent(self, event):  # 실시간 검색 기능
        if 8 <= event.keycode <= 105:
            self.userSearch()
            print(event.keycode)   

class RentPage(tk.Frame):  #### 전체 대여 페이지
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self, relief='flat', borderwidth=1, pady=5)
        tk.Label(self, text="대여하기", font=('Helvetica', 18, "bold")).grid(row=0, column=0)

if __name__ == "__main__":
    mk = MainTk()
    mk.mainloop()
