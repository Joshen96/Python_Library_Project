import pandas as pd
import csv
from datetime import date

#Userdf = pd.DataFrame(index=range(0,0), columns=['User_number', 'User_name','User_birth','User_sex','User_E-mail','User_Reg_Date','User_out_Date','User_rent_cnt'])
#Userdf.to_csv('Userdata.csv',index=False,encoding='utf-8-sig') #csv파일 생성 최초실행

Userdf = pd.read_csv('Userdata.csv',encoding='utf-8-sig')


#회원 등록 테스트
def UserSave():
    global Userdf
    name=input("이름 : ")
    number=input("휴대번호 : ")
    birth=input("생년월일 : ")
    sex=input("성별 : ")
    email=input("이메일 : ")

    
    if '' in [name,number,birth, sex, email]:        #공백인지 체크
        print("값을 입력세요.")
        return 0
    else:
        usertoday = date.today()   # 가입날짜 오늘 
        in_row=[number,name,birth,sex,email,date.isoformat(usertoday),'',0]  # 등록할정보 리스트
        Userdf=Userdf.append(pd.Series(in_row, index=Userdf.columns),ignore_index =True)  # 등록 Userdf 추가
        
        Userdf.to_csv('Userdata.csv',index=False,encoding='utf-8-sig')     #csv 파일에 등록 정보 추가
    print(Userdf)

    


#회원 수정 테스트용
def UserAdit():
    AditName=input("변경할 회원 명 : ")   #수정하고자 하는 도서 선택
    if (Userdf['User_name']!=AditName).all():       #검색 결과가 없는 경우
        print('검색 결과가 없습니다.')
    else:
        Name=input("회원 명 :")                  #수정할 회원 테스트
        Number=input("전화번호 :")                     
        Birth=input("생년월일 :")
        Sex=input("성별 :")
        Email=input("이메일 :")
        Userdf.loc[Userdf['User_name'].str.contains(AditName),('User_number', 'User_name','User_birth','User_sex','User_E-mail')]=(Number,Name,Birth,Sex,Email)      #수정한 정보를 데이터 프레임에 추가
        Userdf.to_csv('Userdata.csv',index=False,encoding='utf-8-sig')           #csv 파일에 수정 정보 추가
    print(Userdf)



#회원 삭제 테스트용
def UserDel():
    Name=input('삭제할 회원 명 : ')
    userdelday = date.today()
    Userdf.loc[Userdf['User_name'].str.contains(Name),('User_out_Date')]=(date.isoformat(userdelday))    #삭제 시 해당회원의 User_out_Date 에 탈퇴날짜 삽입 
    Userdf.to_csv('Userdata.csv',index=False,encoding='utf-8-sig') # csv 파일로 저장
    print(Userdf)




def UserFind():

    FindChoice=input("1: 이름, 2: 전화번호")
    if FindChoice =='1':
        NameVal=Userdf['User_name'].values  # 데이터프레임의 User_name의 값을 리스트로 만들어 확인하기위해 만든소스
        NameList=NameVal.tolist()
        print(NameList)
        
        FindName=input("찾는 이름 입력:")
        
        filt=Userdf['User_name'].str.contains(FindName) # 특정 문자를 포함한 이름을 가진 데이터 프레임을 filt
        if Userdf[filt].empty:                          #데이터 프레임이 비었다면 검색결과가없는것
            print("검색결과가 없습니다.")
        else:                                           #값이 있다면 검색된 데이터프레
            print(Userdf[filt])
        
       
    elif FindChoice == '2':
        
        NumderVal=Userdf['User_number'].values      #데이터프레임의 User_number 의 값을 리스트로 만들어 확인하기위해 만든소스
        NumberList=NumderVal.tolist()
        print(NumberList)
        
        FindNumber=input("찾는 휴대번호 입력:")
        
        filt=Userdf['User_number'].str.contains(FindNumber) # 특정 문자를 포함한 번호을 가진 데이터 프레임을 filt
        if Userdf[filt].empty:                          #데이터 프레임이 비었다면 검색결과가없는것
            print("검색결과가 없습니다.")
        else:                                           #값이 있다면 검색된 데이터프레임
            print(Userdf[filt])
        

    
    
#메인
        
#UserSave() #등록
#UserAdit() #수정
#UserDel() #삭제
UserFind() #검색
