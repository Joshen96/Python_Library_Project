from msilib.schema import CheckBox
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

User_add=Tk()
User_add.title('회원 등록')
User_add.geometry("480x350+400+200")
User_add.resizable(False, False)

def User_add_save() : # 저장 버튼 눌렀을 때
    pass

def User_add_file() : # 사진 파일 열기 버튼 눌렀을 때
    User_add_photo = filedialog.askopenfilenames(title = "이미지 파일을 선택하세요",\
    filetypes=(("GIF 파일","*.GIF"), ("모든 파일","*.*")),\
    initialdir="C:/") # 최초의 경로를 c 드라이브로 설정
    User_add_photoEntry.insert(END, User_add_photo) # 사진 파일을 선택 했을 때 엔트리에 주소 넣음

def daychange() : # 생년월일 월에따른 일 수
    pass

# 이름 프레임
User_add_nameFrame=Frame(User_add, relief='flat', borderwidth=1, padx =20 , pady = 20)
User_add_nameFrame.grid(row=0, column=0, sticky=W)
# 이름 레이블
User_add_nameLabel=Label(User_add_nameFrame, text='이 름 :', width= 10)
User_add_nameLabel.grid(row=0, column=0, columnspan=1, rowspan=1, sticky=N, padx=10)
# 이름 엔트리
User_add_nameEntry=ttk.Entry(User_add_nameFrame ,width='30')
User_add_nameEntry.grid(row=0, column=1, columnspan=1, rowspan=1, sticky=N)


# 생년월일 프레임
User_add_birthFrame=Frame(User_add, relief='flat', borderwidth=1, padx =20)
User_add_birthFrame.grid(row=1, column=0, sticky=W)
# 생년월일 레이블 ( 생년월일 : )
User_add_birthLabel=Label(User_add_birthFrame, text='생년월일 :', width= 10)
User_add_birthLabel.grid(row=0, column=0, columnspan=1, rowspan=1, sticky=N, padx=10)
#생년월일 년도 콤보박스 ( OO년 )
years = list(range(1950,2023))
User_add_yearCombobox=ttk.Combobox(User_add_birthFrame, values = years, width=5)
User_add_yearCombobox.current(0)
User_add_yearCombobox.grid(row=0, column=1, sticky=W, padx =2)
# 생년월일 년 레이블 ( OO년 )
User_add_yearLabel=Label(User_add_birthFrame, text='년')
User_add_yearLabel.grid(row=0, column=2, sticky=W, padx =2)
# 생년월일 월 콤보박스 ( OO월 )
month = list(range(1,13))
User_add_monthCombobox=ttk.Combobox(User_add_birthFrame, values = month, width=3)
User_add_monthCombobox.current(0)
User_add_monthCombobox.grid(row=0, column=3, sticky=W, padx =2)
# 생년월일 월 레이블 ( OO월 )
User_add_monthLabel=Label(User_add_birthFrame, text='월')
User_add_monthLabel.grid(row=0, column=4, columnspan=1, rowspan=1, sticky=N, padx =2)
# 생년월일 일 콤보박스 ( OO일 )
days = list(range(1,32))
User_add_dayCombobox=ttk.Combobox(User_add_birthFrame, values = days, width=3)
User_add_dayCombobox.current(0)
User_add_dayCombobox.grid(row=0, column=5, sticky=W, padx =2)
# 생년월일 월 레이블 ( OO월 )
User_add_dayCombobox=Label(User_add_birthFrame, text='일')
User_add_dayCombobox.grid(row=0, column=6, columnspan=1, rowspan=1, sticky=N, padx =2)


# 성별 프레임
User_add_sexFrame=Frame(User_add, relief='flat', borderwidth=1, padx =20, pady=20)
User_add_sexFrame.grid(row=2, column=0, sticky=W)
# 성별 레이블
User_add_sexLabel=Label(User_add_sexFrame, text='성별 :', width= 10)
User_add_sexLabel.grid(row=0, column=0, columnspan=1, rowspan=1, sticky=N, padx=10)
# 성별 라디오 버튼
sexcheck = IntVar()
sexcheck.set('1') # 라디오 버튼 기본값 남자로 설정
User_add_manBtn=Radiobutton(User_add_sexFrame, text='남자', value = '1', variable = sexcheck) # 남자 체크시 sexcheck에 1 저장
User_add_manBtn.grid(row=0, column=1, columnspan=1, rowspan=1, sticky=N)
User_add_womanBtn=Radiobutton(User_add_sexFrame, text='여자', value = '2', variable = sexcheck)# 여자 체크시 sexcheck에 2 저장
User_add_womanBtn.grid(row=0, column=2, columnspan=1, rowspan=1, sticky=N)


# 메인 프레임
User_add_mainFrame=Frame(User_add, relief='flat', borderwidth=1, padx =20)
User_add_mainFrame.grid(row=3, column=0, sticky=W)

# 휴대전화 레이블
User_add_phoneLabel=Label(User_add_mainFrame, text='휴대전화 :', width= 10)
User_add_phoneLabel.grid(row=0, column=0, columnspan=1, rowspan=1, sticky=N, padx=10, pady=10)
# 휴대전화 엔트리
User_add_phoneEntry=ttk.Entry(User_add_mainFrame ,width='30')
User_add_phoneEntry.grid(row=0, column=1, columnspan=1, rowspan=1, sticky=N, padx=10, pady=10)

# 이메일 주소 레이블
User_add_emailLabel=Label(User_add_mainFrame, text='이메일 주소 :', width= 10)
User_add_emailLabel.grid(row=1, column=0, columnspan=1, rowspan=1, sticky=N, padx=10, pady=10)
# 이메일 주소 엔트리
User_add_emailEntry=ttk.Entry(User_add_mainFrame ,width='30')
User_add_emailEntry.grid(row=1, column=1, columnspan=1, rowspan=1, sticky=N, padx=10, pady=10)

# 사진 레이블
User_add_photoLabel=Label(User_add_mainFrame, text='사진', width= 10)
User_add_photoLabel.grid(row=2, column=0, columnspan=1, rowspan=1, sticky=N, padx=10, pady=10)
# 사진 엔트리
User_add_photoEntry=ttk.Entry(User_add_mainFrame ,width='30')
User_add_photoEntry.grid(row=2, column=1, columnspan=1, rowspan=1, sticky=N, padx=10, pady=10)
# 사진 파일 열기 버튼
User_add_fileBtn=ttk.Button(User_add_mainFrame,text='파일 열기', command=User_add_file)
User_add_fileBtn.grid(row=2, column=2, columnspan=1, rowspan=1, sticky=N, padx = 5, pady =6)

# 저장 버튼
User_add_saveBtn=ttk.Button(User_add_mainFrame,text='저장', command=User_add_save)
User_add_saveBtn.grid(row=3, column=1, columnspan=1, rowspan=1, sticky=N, pady =20)

User_add.mainloop()