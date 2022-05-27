from tkinter import *

Book_register = Tk()
Book_register.title("도서 등록")
Book_register.geometry("400x450+400+100")

# 도서등록 레이블
Book_name_label = Label(Book_register, text = "제목 :")
Book_author_label = Label(Book_register, text = "저자 :")
Book_publisher_label = Label(Book_register, text = "출판사 :")
Book_price_label = Label(Book_register, text = "가격 :")
Book_link_label = Label(Book_register, text = "관련링크 :")
Book_ISBN_label = Label(Book_register, text = "ISBN :")
Book_photo_label = Label(Book_register, text = "사진 :")
Book_account_label = Label(Book_register, text = "도서 설명 :")

# 도서등록 텍스트
Book_name_entry = Entry(Book_register, width = 30)
Book_author_entry = Entry(Book_register, width = 30)
Book_publisher_entry = Entry(Book_register, width = 30)
Book_price_entry = Entry(Book_register, width = 30)
Book_link_text = Text(Book_register, width = 30, height = 2)
Book_ISBN_entry = Entry(Book_register, width = 30)
Book_photo_entry = Entry(Book_register, width = 30)
Book_account_text = Text(Book_register, width = 40, height = 5)

# 도서등록 버튼
file_open_btn = Button(Book_register, text = "파일 열기")
save_btn = Button(Book_register, text = "저장")

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
Book_photo_entry.place(x=100, y=270)
Book_account_text.place(x=100, y=310)

# 도서등록 버튼 적용
file_open_btn.place(x = 320 ,y = 270)
save_btn.place(x=200, y= 390)

Book_register.mainloop()