from cmath import nan
from tkinter import * 
from tkinter import ttk
from tkinter import messagebox
import pandas as pd 
import userinfo # 도서정보 py 불러오기

#### 데이터프레임, csv 부분  (data, data2 는 실험 후 삭제하면 됨)
data = {'도서명' : ['따라하면 배우는 파이썬', '따라하면 배우는 파이썬2'], # 전체도서확인용 데이터
        '저자' : ['천인국', '천인국2'],
        '가격' : ['26,000', '26,0002'],
        'ISBN' : ['9788975504773', '12321323123'],
        '대출여부' : ['대여가능', '대여불가'],
        'URL' : ['http://kyo.co.kr/product/dsdfsfsfsssfsfsfsfdsfdsf','http://kyo.co.ㄴㅇㄹㄴㅇㄹ15']
        }
data2 = {'도서명' : ['따라하면 배우는 파이썬', '따라하면 배우는 파이썬2'], # 도서정보용 데이터(나중에 이미지도 추가할 예정)
        '저자' : ['천인국', '천인국2'],
        '출판사' :['생능출판', '생능출판2'],
        '가격' : ['26,000', '26,0002'],
        '관련링크' : ['http://kyo.co.kr/product/dsdfsfsfsssfsfsfsfdsfdsf','http://kyo.co.ㄴㅇㄹㄴㅇㄹ15'],
        'ISBN' : ['9788975504773', '12321323123'],
        '대출여부' : ['대여가능', '대여불가'],
        '도서설명' : ['ㄴㄹㅇㄴㅇㄴㄹㄴㅇㄹㅇㄴㄹㅇㄴㄹㅇㄴㄹㅇㄴㄹㅇㄴㄹㅇㄴ','ㄴㄹㅇㄴㄹㄴㅇㄹㄴㅇㄹㅇㄴㄹㄴㅇㄹㄴㅇㄹㄴㅇㄴㅇㄹ']
        }

#df2 = pd.DataFrame(data2)  @@@@ 23-25행 초기 csv 생성 소스코드
#print(df2)
#df2.to_csv("bookinfo.csv", mode="w", encoding='utf-8-sig', index=False)

df1 = pd.read_csv ('user.csv')
df1_list = df1.values.tolist()

#### 함수 부분
def info(): # 트리뷰 클릭한 값 넘기기
    try: # 회원 클릭안하고 회원정보 버튼 눌렀을 경우 예외처리 
        aaa = Treeview1.focus() # 트리뷰 클릭한 줄
        treeviewValues = Treeview1.item(aaa).get('values')
        for k in df1_list:
          if treeviewValues[0] == k[0]  :
              userinfo.userInfo(k[0], k[1], k[6], k[2], k[5], k[3], k[7], k[8])
    except IndexError:
        messagebox.showinfo("알림", "회원을 클릭해주세요.")
        print("회원을 클릭해주세요. ")

def bookSearch():  # 회원 검색
    for i in Treeview1.get_children(): # 트리뷰의 값들을 다 지워주고 창 새로고침
        Treeview1.delete(i)

    searchText = entry1.get() # 검색창 값 가져오기
    print(searchText)
    cboxText = comboBox1.get() # 콤보박스 값 가져오기
    print(cboxText)

    if cboxText == '이름':
        c = 1
        for e in df1_list:
            if searchText in e[1]: # 이름과 부분일치할 경우 
                gen = gender1(i[3])
                rent = rent1(i[7])
                cUser = currentUser(i[6])
                # 표에 데이터 삽입
                TreeviewText=Treeview1.insert("", END, text=c, values=(e[1], e[2], gen, e[0], cUser, rent, e[4] ), iid= c-1)
                c += 1
    elif cboxText == '전화번호':
        c = 1
        for e in df1_list:
            if searchText in e[0]: # 전화번호와 부분일치할 경우 
                gen = gender1(i[3])
                rent = rent1(i[7])
                cUser = currentUser(i[6])
                # 표에 데이터 삽입
                TreeviewText=Treeview1.insert("", END, text=c, values=(e[1], e[2], gen, e[0], cUser, rent, e[4] ), iid= c-1)
                c += 1

    #win.update()

def keyEvent(event):  # 실시간 검색 기능
    print(event.keycode)
    if 8 <= event.keycode <= 105:
        bookSearch()

def gender1(g):
    gen =''
    if g == 0: # 여성
        gen = '여성'

    elif g == 1: # 남성
        gen = '남성'
    return gen

def rent1(r):
    rent =''
    if r == 0: # 대여가능
        rent = '대여가능'

    elif r == 1: # 대여불가
        rent = '대여불가'
    return rent

def currentUser(c):
    print(str(c))
    cUser = ''
    if c != c : # 회원
        cUser = '회원'

    else : # 탈퇴회원
        cUser = '탈퇴회원'
    return cUser

#### 메인 소스 부분
if __name__ == "__main__":
    win=Tk()
    win.title('도서 관리 프로그램')  
    Frame1=Frame(win, relief='flat', borderwidth=1, pady=5)
    win.geometry("+600+300")    #### 나중에 화면 중앙에 생성되게 해야함@@@@@@@@@@@@@@@@@@(현재는 임시)
    win.resizable(False, False)
    Frame1.grid(row=0, column=0)

    # 실시간 검색 실험
    win.bind("<Key>", keyEvent )

    # 빈칸 부분
    entry1=ttk.Entry(Frame1, width='35')
    entry1.grid(row=1, column=2, columnspan=1, rowspan=1, sticky=N, pady=1) # 위치 N, 외부 패딩 1

    # 메뉴바 부분
    menubar1= Menu(Frame1)
    submenu1=Menu(menubar1, tearoff=0)
    menubar1.add_cascade(label='회원', menu=submenu1)
    submenu1.add_command(label='전체 회원', command=() )
    submenu2=Menu(menubar1, tearoff=0)
    menubar1.add_cascade(label='도서', menu=submenu2)
    submenu2.add_command(label='전체 도서', command=() )
    submenu3=Menu(menubar1, tearoff=0)
    menubar1.add_cascade(label='대여', menu=submenu3)
    submenu3.add_command(label='대여하기', command=() )
    submenu3.add_command(label='대여정보,반납', command=() )
    win.config(menu=menubar1)

    # 콤보 박스 부분
    frameCombo=Frame(Frame1, relief='flat')
    frameCombo.grid(row=1, column=1, columnspan=1, rowspan=1, sticky=N)

    comboBox1=ttk.Combobox(frameCombo, width=7, state='readonly')
    comboBox1['values']=('이름', '전화번호')
    comboBox1.current(0)
    comboBox1.grid(row=0, column=1,sticky=N)
    labelCombo=Label(frameCombo, text='')
    labelCombo.grid(row=0, column=0,sticky=N)

    # 트리뷰 부분
    frame2=Frame(Frame1, relief='flat', borderwidth=1, padx=20, pady=10)
    frame2.grid(row=2, column=0, columnspan=5, rowspan=1, sticky=N)
    Treeview1=ttk.Treeview(frame2, height=10, columns=('#1', '#2', '#3', '#4', '#5', '#6', '#7'))
    Treeview1.column('#0', width=50, minwidth=40, stretch=NO) # stretch : 열의 너비 조정 설정 여부
    Treeview1.heading('#0',text='회원수',anchor=N)
    Treeview1.column('#1', width=80, minwidth=70, stretch=NO) # stretch : 열의 너비 조정 설정 여부
    Treeview1.heading('#1',text='이름',anchor=N)
    Treeview1.column('#2', width=100, minwidth=100, stretch=NO)
    Treeview1.heading('#2',text='생년월일',anchor=N)
    Treeview1.column('#3', width=50, minwidth=40, stretch=NO)
    Treeview1.heading('#3',text='성별',anchor=N)
    Treeview1.column('#4', width=130, minwidth=120, stretch=NO)
    Treeview1.heading('#4',text='전화번호',anchor=N)
    Treeview1.column('#5', width=60, minwidth=50, stretch=NO)
    Treeview1.heading('#5',text='회원현황',anchor=N)
    Treeview1.column('#6', width=60, minwidth=40, stretch=NO)
    Treeview1.heading('#6',text='대여',anchor=N) 
    Treeview1.column('#7', width=140, minwidth=120, stretch=NO)
    Treeview1.heading('#7',text='이메일주소',anchor=N) 

    c = 1
    # 표에 데이터 삽입
    for i in df1_list:
        gen = gender1(i[3])
        rent = rent1(i[7])
        cUser = currentUser(i[6])
        TreeviewText=Treeview1.insert("", END, text=c, values=(i[1], i[2], gen, i[0], cUser, rent, i[4] ), iid= c-1)
        c += 1
    #TreeviewText=Treeview1.insert("", END, text='1', values=('2','d', 's', 'a', 'q', 'q'), iid="1") 
    Treeview1.grid(row=0, column=0, columnspan=1, rowspan=1, sticky=N)

    # 검색 버튼
    btnSearch=ttk.Button(Frame1,text='검색',command=bookSearch )
    btnSearch.grid(row=1, column=3, columnspan=1, rowspan=1, sticky=N, padx=5)

    # 도서등록 버튼
    btnBookRegist=ttk.Button(Frame1,text='회원등록',command=())
    btnBookRegist.grid(row=3, column=0, columnspan=1, rowspan=1, sticky=N, padx=25, pady=3)

    # 도서정보 버튼
    btnBookInformation=ttk.Button(Frame1,text='회원정보', command=info )
    btnBookInformation.grid(row=3, column=1, columnspan=1, rowspan=1, sticky=W, padx=5, pady=3)

    # 도서수정 버튼
    btnBookEdit=ttk.Button(Frame1,text='회원수정',command=())
    btnBookEdit.grid(row=3, column=2, columnspan=1, rowspan=1, sticky=W, padx=25, pady=3)

    # 도서 삭제 버튼
    btnBookDelete=ttk.Button(Frame1,text='회원 삭제',command=() )
    btnBookDelete.grid(row=3, column=4, columnspan=1, rowspan=1, sticky=N, padx=25, pady=3)


    #labelTitle=Label(Frame1, text='ㄴㅇㄹ')  @@ 값 들어가는지 확인하는 용도!!!!
    #labelTitle.grid(row=0, column=0, columnspan=1, rowspan=1, sticky=W)


    win.mainloop()
