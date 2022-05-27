from tkinter import *
from tkinter import messagebox
import pandas as pd 
class tt():
    def __init__(self):
        self.Book_register = Toplevel()
        self.Book_register.title("도서 등록")
        self.Book_register.geometry("400x400+740+270")

        # 도서등록 레이블
        Book_name_label = Label(self.Book_register, text = "제목 :")
        Book_author_label = Label(self.Book_register, text = "저자 :")
        Book_publisher_label = Label(self.Book_register, text = "출판사 :")
        Book_link_label = Label(self.Book_register, text = "관련링크 :")
        Book_ISBN_label = Label(self.Book_register, text = "ISBN :")
        Book_photo_label = Label(self.Book_register, text = "사진 :")
        Book_account_label = Label(self.Book_register, text = "도서 설명 :")

        # 도서등록 텍스트
        Book_name_entry = Entry(self.Book_register, width = 30)
        Book_author_entry = Entry(self.Book_register, width = 30)
        Book_publisher_entry = Entry(self.Book_register, width = 30)
        Book_link_text = Text(self.Book_register, width = 30, height = 2)
        Book_ISBN_entry = Entry(self.Book_register, width = 30)
        Book_photo_entry = Entry(self.Book_register, width = 30)
        Book_account_text = Text(self.Book_register, width = 40, height = 5)

        # 도서등록 버튼
        file_open_btn = Button(self.Book_register, text = "파일 열기", command=() )
        save_btn = Button(self.Book_register, text = " 저장 ", command = lambda : [self.registbook( Book_name_entry, Book_author_entry, Book_publisher_entry, Book_link_text, 
        Book_ISBN_entry, Book_photo_entry, Book_account_text), self.on_closing() ])

        # 도서등록 레이블 적용
        Book_name_label.place(x=15,y=20)
        Book_author_label.place(x=15,y=60)
        Book_publisher_label.place(x=15,y=100)
        Book_link_label.place(x=15,y=140)
        Book_ISBN_label.place(x=15,y=190)
        Book_photo_label.place(x=15,y=230)
        Book_account_label.place(x=15,y=270)

        # 도서등록 텍스트 적용
        Book_name_entry.place(x=100, y=20)
        Book_author_entry.place(x=100, y=60)
        Book_publisher_entry.place(x=100, y=100)
        Book_link_text.place(x=100, y=140)
        Book_ISBN_entry.place(x=100, y=190)
        Book_photo_entry.place(x=100, y=230)
        Book_account_text.place(x=100, y=270)

        # 도서등록 버튼 적용
        file_open_btn.place(x = 320 ,y = 230)
        save_btn.place(x=200, y= 350)


    def registbook(self, title, author, publisher, link, ISBN, photo, text ):
        #print(photo.get())
        print("@@@@@@@@@@@@@@@@@@@@@")
        print(title.get())
        print(author.get())
        price = "1,000"
        print(ISBN.get())
        rentcheck = 0
        print(link.get("1.0","end"+"-1c"))
        print(publisher.get())
        print(text.get("1.0","end"+"-1c"))
        
        df1 = pd.read_csv ('book3.csv', dtype=str)
        num = int(len(df1))
        print(num)
        df1.loc[num] = [title.get(), author.get(), price, ISBN.get(), rentcheck, link.get("1.0","end"+"-1c"), publisher.get(), text.get("1.0","end"+"-1c")]
        df1.to_csv('book3.csv', mode='w', sep=',', index=False)


    def on_closing(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.Book_register.destroy()
            self.parent.update()
            #self.self.Book_register.protocol("WM_DELETE_WINDOW", on_closing)
        else:
            print("존재")