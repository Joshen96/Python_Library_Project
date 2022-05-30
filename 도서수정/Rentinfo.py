from tkinter import*
import pandas as pd
import numpy as np
from tkinter import filedialog
import tkinter.messagebox as msgbox


# def edit():
#     try:  # 도서 클릭안하고 도서정보 버튼 눌렀을 경우 예외처리
#         aaa = Treeview1.focus()  # 트리뷰 클릭한 줄
#         l = df1_list[int(aaa)]
#         treeviewValues = Treeview1.item(aaa).get('values')
#         for k in df1_list:
#             if treeviewValues[0] == k[0]:
#                 bookedithwang.Book_Edit(
#                     l[4], l[3], l[2], l[1], l[5], l[6], l[7], aaa)
#     except IndexError:
#         messagebox.showinfo("알림", "도서를 클릭해주세요.")
#         print("도서를 클릭해주세요. ")


def rentinfo(name, num, title, ISBN, rentdate, retdate, yesno, line):
    #wininfo = Toplevel()
    global wininfo
    wininfo = Tk()
    wininfo.title("대여정보")
    wininfo.geometry("300x270+600+230")
    wininfo.resizable(0, 0)
    infoframe = Frame(wininfo, relief='flat', padx=10, pady=10)
    infoframe.grid(row=0, column=0)

    # 이름 정보4
    label_name = Label(infoframe, text="이름  ", anchor=W, width=8)
    label_name.grid(row=0, column=0, pady=4)
    label_name = Label(infoframe, text=":", anchor=W)
    label_name.grid(row=0, column=1, pady=4)
    label_name = Label(infoframe, text=name, anchor=W, width=20)
    label_name.grid(row=0, column=2, pady=4)

    # 전화번호 정보3
    label_phonenum = Label(infoframe, text="전화번호  ", anchor=W, width=8)
    label_phonenum.grid(row=1, column=0, pady=4)
    label_phonenum = Label(infoframe, text=":", anchor=W)
    label_phonenum.grid(row=1, column=1, pady=4)
    label_phonenum = Label(infoframe, text=num, anchor=W, width=20)
    label_phonenum.grid(row=1, column=2, pady=4)

    # 도서명 정보2
    label_booktit = Label(infoframe, text="도서명  ", anchor=W, width=8)
    label_booktit.grid(row=2, column=0, pady=4)
    label_booktit = Label(infoframe, text=":", anchor=W)
    label_booktit.grid(row=2, column=1, pady=4)
    label_booktit = Label(infoframe, text=title, anchor=W, width=20)
    label_booktit.grid(row=2, column=2, pady=4)

    # ISBN 정보1
    label_ISBN = Label(infoframe, text="ISBN  ", anchor=W, width=8)
    label_ISBN.grid(row=3, column=0, pady=4)
    label_ISBN = Label(infoframe, text=":", anchor=W)
    label_ISBN.grid(row=3, column=1, pady=4)
    label_ISBN = Label(infoframe, text=ISBN, anchor=W, width=20)
    label_ISBN.grid(row=3, column=2, pady=4)

    # 대출일 정보8
    label_borrow = Label(infoframe, text="대출일  ", anchor=W, width=8)
    label_borrow.grid(row=4, column=0, pady=4)
    label_borrow = Label(infoframe, text=":", anchor=W)
    label_borrow.grid(row=4, column=1, pady=4)
    label_borrow = Label(infoframe, text=rentdate, anchor=W, width=20)
    label_borrow.grid(row=4, column=2, pady=4)

    # 반납예정일 정보6
    label_return = Label(infoframe, text="반납예정일  ", anchor=W, width=8)
    label_return.grid(row=5, column=0, pady=4)
    label_return = Label(infoframe, text=":", anchor=W)
    label_return.grid(row=5, column=1, pady=4)
    label_return = Label(infoframe, text=retdate, anchor=W, width=20)
    label_return.grid(row=5, column=2, pady=4)

    # 반납여부7
    label_returnchk = Label(infoframe, text="반납여부  ", anchor=W, width=8)
    label_returnchk.grid(row=6, column=0, pady=4)
    label_returnchk = Label(infoframe, text=":", anchor=W)
    label_returnchk.grid(row=6, column=1, pady=4)

    if yesno == "1":
        yesnotext = "x"
    else:
        yesnotext = "o"

    label_returnchk = Label(infoframe, text=yesnotext, anchor=W, width=20)
    label_returnchk.grid(row=6, column=2, pady=4)

    btn_return = Button(infoframe, text="반납", bg="#0d47a1", fg="white", width=8, overrelief="solid",
                        highlightcolor="#ede7f6", command=lambda: returnbook(line, label_borrow,
                                                                             label_return, label_returnchk))
    btn_return.grid(row=7, column=2, pady=8)
    wininfo.protocol("WM_DELETE_WINDOW", on_closing)

    wininfo.mainloop()

# 반납 함수


def returnbook(line, label_borrow, label_return, label_returnchk):
    if msgbox.askokcancel("edit", "정말 수정하시겠습니까?"):
        df1 = pd.read_csv('rent.csv', dtype=str)
        df1.iloc[int(line), 5] = "반납완료"  # 예쁘게 나타내기위해
        # df1.iloc[int(line), 5] = np.nan 위의 방법 쓰면 안되면 이 방법
        df1.iloc[int(line), 6] = "반납완료"
        df1.iloc[int(line), 7] = "0"
        df1.to_csv('rent.csv', mode='w', index=False, encoding='utf-8-sig')
        label_borrow.config(text="반납완료")
        label_return.config(text="반납완료")
        label_returnchk.config(text="o")


def on_closing():
    if msgbox.askokcancel("Quit", "창을 닫으시겠습니까?"):
        wininfo.destroy()


# 연결안된상태여서 함수호출 테스트 지워야함
df1 = pd.read_csv('rent.csv', dtype=str)
df1_list = df1.values.tolist()
l = df1_list[1]
rentinfo(l[4], l[3], l[2], l[1], l[5], l[6], l[7], 1)
