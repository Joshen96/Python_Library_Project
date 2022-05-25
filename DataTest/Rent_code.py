import pandas as pd
import csv
from datetime import date
import datetime

#Rentdf = pd.DataFrame(index=range(0,0), columns=['SEQ', 'Book_ISBN','Book_title','User_number','User_name','Rent_date','Rent_retun','Rent_YN'])
#Rentdf.to_csv('Rentdata.csv',index=False,encoding='utf-8-sig') #csv파일 생성 최초실행

Userdf = pd.read_csv('Userdata.csv',encoding='utf-8-sig')
Bookdf = pd.read_csv('Bookdata.csv',encoding='utf-8-sig')
Rentdf = pd.read_csv('Rentdata.csv',encoding='utf-8-sig')


#대여 테스트

def Renting():
    global Rentdf
    global Bookdf
    
    
    print(Userdf['User_number'])

    Rentcandf=Bookdf.groupby('Book_pre').get_group(1) ## 도서여부가 0인책은 고르지못하도록 함  Rentcandf = 도서여부가 1인 도서의데이터프레임
    ISBNck=Rentcandf['Book_ISBN']
    ISBN_val=ISBNck.values
    ISBN_list=ISBN_val.tolist()
    print(ISBN_list)
    
    RentNumber=input("랜트할 전화번호 : ")   #수정하고자 하는 회원전화번호 선택
    if (Userdf['User_number']!=RentNumber).all():       #검색 결과가 없는 경우
        print('검색 결과가 없습니다.')
    else:
        RentISBN=int(input("랜트할 책ISBN : "))   #수정하고자 하는 책 ISBN 선택
        if RentISBN not in ISBN_list:       #검색 결과가 없는 경우
            print('검색 결과가 없습니다.')
        else:
            rentcount = int(Userdf.loc[Userdf['User_number'].str.contains(RentNumber),'User_rent_cnt']) # 선택 회원의 대여권수 뽑아오기
            
            Number_index=Userdf.index[Userdf['User_number']==RentNumber] #랜트 한경우  회원의 대여수 증가 
            Userdf.loc[Number_index,'User_rent_cnt']=rentcount+1 

            ISBN_index=Bookdf.index[Bookdf['Book_ISBN']==RentISBN]
            Bookdf.loc[ISBN_index,'Book_pre']=0       #랜트 한경우 책 여부0

            Bookdf.to_csv('Bookdata.csv',index=False,encoding='utf-8-sig') # 도서 랜트여부 여기서 저장
            Userdf.to_csv('Userdata.csv',index=False,encoding='utf-8-sig') # 유저 랜트수 여기서 저장
         
            RentUser=Userdf['User_number'].values[Number_index]    #Userdf.iat[Number_index,0
            RentingName=Userdf['User_name'].values[Number_index]
            
            RentBook=Bookdf['Book_ISBN'].values[ISBN_index]       #Bookdf.iat[ISBN_index,0]
            RentingTitle=Bookdf['Book_title'].values[ISBN_index]
            
            RentUserNumber=RentUser[0]       # User_number 정보
            RentUserName=RentingName[0]      # User_name 정보
            RentBookISBN=RentBook[0]         # Book_ISBN 정보
            RentBookTitle=RentingTitle[0]    # Book_title 정보
            
            #랜트 데이터프레임 추가
            
            Renttoday = date.today() # 빌리는 날짜
            Returnday = Renttoday+datetime.timedelta(days=14) # 반납예정날짜
            
            row=[RentBookISBN,RentBookTitle,RentUserNumber,RentUserName,Renttoday,Returnday,0] 
            
            Rentdf.set_index('SEQ',inplace=True)
            Rentdf=Rentdf.append(pd.Series(row, index=Rentdf.columns),ignore_index =True)
            Rentdf.index.name='SEQ'
            Rentdf.reset_index(drop=False, inplace=True)                                    
            
          
            Rentdf.to_csv('Rentdata.csv',index=False,encoding='utf-8-sig') # 랜트 정보 csv 파일로 저장
            
        print(Userdf)
        print(Bookdf)
        print(Rentdf)
            


def ReturnBook(): #반납 테스트
    global Rentdf
    global Bookdf
    
    ChoiceSeq=int(input("반납할 번호를 고르세요"))
    
    if (Rentdf['SEQ']!=ChoiceSeq).all():       #검색 결과가 없는 경우
        print('검색 결과가 없습니다.')
    else:
        Rentdf.loc[ChoiceSeq,'Rent_YN']=1
        Rentdf.to_csv('Rentdata.csv',index=False,encoding='utf-8-sig') # 랜트 정보 csv 파일로 저장
        
        RentNumber=Rentdf.loc[ChoiceSeq,'User_number'] # 대여의 number 정보 추출
        
        rentcount = int(Userdf.loc[Userdf['User_number'].str.contains(RentNumber),'User_rent_cnt']) # 선택 회원의 대여권수 뽑아오기
        Number_index=Userdf.index[Userdf['User_number']==RentNumber] #랜트 한경우  회원의 대여수 증가 
        Userdf.loc[Number_index,'User_rent_cnt']=rentcount-1

        RentISBN=Rentdf.loc[ChoiceSeq,'Book_ISBN'] # 대여의 ISBN 정보 추출
        
        ISBN_index=Bookdf.index[Bookdf['Book_ISBN']==RentISBN]
        Bookdf.loc[ISBN_index,'Book_pre']=1      #랜트 한경우 책 여부0

        Bookdf.to_csv('Bookdata.csv',index=False,encoding='utf-8-sig') # 도서 랜트여부 여기서 저장
        Userdf.to_csv('Userdata.csv',index=False,encoding='utf-8-sig') # 유저 랜트수 여기서 저장

        print(Userdf)
        print(Bookdf)
        print(Rentdf)

    
#메인
#Renting()#대여
ReturnBook()# 반납
