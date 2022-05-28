from tkinter import *
from tkinter import ttk
def bookInfo(title, author, publisher, price, link, ISBN, rental, bookdescription, photo):  # 나중에 이미지 이름도 인자로 받아와야함!
    win1=Toplevel()
    win1.title('도서 정보')    
    win1.geometry("+650+280")  #
    frame1=Frame(win1, relief='flat', padx=10, pady=10) # relief='flat' : 테두리 없음, padx,y : 외부 패딩값 지정함
    win1.resizable(False, False)
    frame1.grid(row=0, column=0) # 

    # 제목 넣는 곳
    labelTitle=Label(frame1, text='제목 : ')
    labelTitle.grid(row=0, column=0, columnspan=1, rowspan=1, sticky=W) # sticky : 위치 조정(n, e, s, w, nw, ne, sw, se)

    # 제목 넣는 곳
    labelTitleText=Label(frame1, text=title)
    labelTitleText.grid(row=0, column=1, columnspan=1, rowspan=1, sticky=W)

    # 이미지 넣는 곳
    img=PhotoImage(file='GIF/' + photo, master=win1) # 나중에 이미지이름 인자로 받아와야함!
    labelImg=Label(frame1, text='이미지 넣는 곳', image=img)
    labelImg.grid(row=0, column=3, columnspan=1, rowspan=6, sticky=E, padx=5)

    # 저자 넣는 곳
    labelAuthor=Label(frame1, text='저자 : ')
    labelAuthor.grid(row=1, column=0, columnspan=1, rowspan=1, sticky=W)

    # 저자 넣는 곳
    labelAuthorText=Label(frame1, text= author)
    labelAuthorText.grid(row=1, column=1, columnspan=1, rowspan=1, sticky=W)

    # 출판사 넣는 곳
    labelPublisher=Label(frame1, text='출판사 : ')
    labelPublisher.grid(row=2, column=0, columnspan=1, rowspan=1, sticky=W)

    # 출판사 넣는 곳
    labelPublisherText=Label(frame1, text= publisher)
    labelPublisherText.grid(row=2, column=1, columnspan=1, rowspan=1, sticky=W)

    # 가격 넣는 곳
    labelPrice=Label(frame1, text='가격 : ')
    labelPrice.grid(row=3, column=0, columnspan=1, rowspan=1, sticky=W)

    # 가격 넣는 곳
    labelPriceText=Label(frame1, text= price)
    labelPriceText.grid(row=3, column=1, columnspan=1, rowspan=1, sticky=W)

    # 관련 링크 넣는 곳
    labelLink=Label(frame1, text='관련링크 : ')
    labelLink.grid(row=4, column=0, columnspan=1, rowspan=1, sticky=W)

    # 관련 링크 넣는 곳
    labelLinkText=Label(frame1, text= link, wraplength= 250 ) # wraplength : 자동 줄내림 설정
    labelLinkText.grid(row=4, column=1, columnspan=1, rowspan=1, sticky=W)

    # ISBN 넣는 곳
    labelISBN=Label(frame1, text='ISBN : ')
    labelISBN.grid(row=5, column=0, columnspan=1, rowspan=1, sticky=W)

    # ISBN 넣는 곳
    labelISBNText=Label(frame1, text= ISBN)
    labelISBNText.grid(row=5, column=1, columnspan=1, rowspan=1, sticky=W)

    # 대여 여부 넣는 곳
    labelRental=Label(frame1, text='대여 여부 : ')
    labelRental.grid(row=6, column=0, columnspan=1, rowspan=1, sticky=W)

    # 대여 여부 넣는 곳
    labelRentalText=Label(frame1, text= rental)
    labelRentalText.grid(row=6, column=1, columnspan=1, rowspan=1, sticky=W)

    # 도서설명 넣는 곳
    labelBookDescription=Label(frame1, text='도서설명 : ')
    labelBookDescription.grid(row=7, column=0, columnspan=1, rowspan=1, sticky=W)

    # 도서설명 넣는 곳
    labelBookDescriptionText=Label(frame1, text= bookdescription, wraplength= 250 ) # wraplength : 자동 줄내림 설정
    labelBookDescriptionText.grid(row=7, column=1, columnspan=1, rowspan=1, sticky=W)

    win1.mainloop()
