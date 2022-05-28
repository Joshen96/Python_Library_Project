from tkinter import*
import tkinter as tk
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
    label_pic = Label(self.window, text="사진 : ")
    label_pic.grid(row=6, column=0, pady=4)
    e_pic = Entry(self.window, width=30)
    e_pic.grid(row=6, column=1, pady=4)
    e_pic.insert(0, photo)

    btn_pic = Button(self.window, text="파일 열기", bg="#0099ff", fg="white")
    btn_pic.grid(row=6,column=2, padx=8)

    label_explain = Label(self.window, text="도서설명 : ")
    label_explain.grid(row=7, column=0, pady=4)
    t_explain = Text(self.window, width = 40, height = 5)
    t_explain.grid(row=7, column=1, pady=4)
    t_explain.insert(tk.END, bookdescription) 

    btn_edit = Button(self.window, text="수정하기", bg="#0099ff", fg="white")
    btn_edit.grid(row=8,column=0, pady=4)

    btn_cancel = Button(self.window, text="취소", bg="#0099ff", fg="white")
    btn_cancel.grid(row=8,column=1, pady=4)

    # 도서등록 레이블 적용
    label_title.place(x=15,y=20)
    label_author.place(x=15,y=60)
    label_publish.place(x=15,y=100)
    label_price.place(x=15,y=140)
    label_link.place(x=15,y=190)
    label_isbn.place(x=15,y=230)
    label_pic.place(x=15,y=270)
    label_explain.place(x=15,y=310)

    # 도서등록 텍스트 적용
    e_title.place(x=100, y=20)
    e_author.place(x=100, y=60)
    e_publish.place(x=100, y=100)
    e_price.place(x=100, y=140)
    t_link.place(x=100, y=190)
    e_isbn.place(x=100, y=230)
    e_pic.place(x=100, y=270)
    t_explain.place(x=100, y=310)


    # 도서등록 버튼 적용
    btn_pic.place(x = 320 ,y = 270)
    btn_edit.place(x=130, y= 390)
    btn_cancel.place(x=230, y= 390)


    self.window.mainloop()

