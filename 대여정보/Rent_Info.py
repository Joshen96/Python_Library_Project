from tkinter import*

window = Tk()
window.title("대여")
#window.geometry("")
#window.resizable(0,0)

# 이름 정보
label_title = Label(text="이름 : ")
label_title.grid(row=0, column=0, pady=4)

# 전화번호 정보
label_title = Label(text="전화번호 : ")
label_title.grid(row=1, column=0, pady=4)

# 도서명 정보
label_title = Label(text="도서명 : ")
label_title.grid(row=2, column=0, pady=4)

# ISBN 정보
label_title = Label(text="ISBN : ")
label_title.grid(row=3, column=0, pady=4)

# 대출일 정보
label_title = Label(text="대출일 : ")
label_title.grid(row=4, column=0, pady=4)

# 반납예정일 정보
label_title = Label(text="반납예정일 : ")
label_title.grid(row=5, column=0, pady=4)

btn_rent = Button(window, text="대여", bg="blue", fg="white")
btn_rent.grid(row=6, column=0, pady=4)

window.mainloop()