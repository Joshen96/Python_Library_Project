from tkinter import*

window = Tk()
window.title("도서수정")
#window.geometry("")
#window.resizable(0,0)

# 제목 수정
label_title = Label(text="제목 : ")
label_title.grid(row=0, column=0, pady=4)
e_title = Entry(window, width=30)
e_title.grid(row=0, column=1, pady=4)
e_title.insert(0, "")

# 저자 수정
label_author = Label(text="저자 : ")
label_author.grid(row=1, column=0, pady=4)
e_author = Entry(window, width=30)
e_author.grid(row=1, column=1, pady=4)
e_author.insert(0, "")

# 출판사 수정
label_publish = Label(text="출판사 : ")
label_publish.grid(row=2, column=0, pady=4)
e_publish = Entry(window, width=30)
e_publish.grid(row=2, column=1, pady=4)
e_publish.insert(0, "")

# 가격 수정
label_price = Label(text="가격 : ")
label_price.grid(row=3, column=0, pady=4)
e_price = Entry(window, width=30)
e_price.grid(row=3, column=1, pady=4)
e_price.insert(0, "")

#  관련링크
label_link = Label(text="관련링크 : ")
label_link.grid(row=4, column=0, pady=4)
t_link = Text(window, width=30, height=2)
t_link.grid(row=4, column=1, pady=4)
# t_link.insert(0, "")

# ISBN 수정
label_isbn = Label(text="ISBN : ")
label_isbn.grid(row=5, column=0, pady=4)
e_isbn = Entry(window, width=30)
e_isbn.grid(row=5, column=1, pady=4)
e_isbn.insert(0, "")

# 사진 수정
label_pic = Label(text="사진 : ")
label_pic.grid(row=6, column=0, pady=4)
e_pic = Entry(window, width=30)
e_pic.grid(row=6, column=1, pady=4)
e_pic.insert(0, "")
btn_pic = Button(text="파일 열기", bg="#0099ff", fg="white")
btn_pic.grid(row=6,column=2, padx=8)

label_explain = Label(text="도서설명 : ")
label_explain.grid(row=7, column=0, pady=4)
t_explain = Text(window, width=30, height=2)
t_explain.grid(row=7, column=1, pady=4)
# t_explain.insert(0, "")

btn_edit = Button(text="수정하기", bg="#0099ff", fg="white")
btn_edit.grid(row=8,column=0, pady=4)

btn_cancel = Button(text="취소", bg="#0099ff", fg="white")
btn_cancel.grid(row=8,column=1, pady=4)

window.mainloop()

