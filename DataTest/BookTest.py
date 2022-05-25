import pandas as pd
import csv


#Bookdf = pd.DataFrame(index=range(0,0), columns=['Book_ISBN', 'Book_title','Book_author','Book_pub','Book_price','Book_link','Book_description','Book_pre'])
#Bookdf.to_csv('Bookdata.csv',index=False,encoding='utf-8-sig') #csv파일 생성 최초실행

Bookdf = pd.read_csv('Bookdata.csv',encoding='utf-8-sig')


#도서 등록 테스트
def BookSave():  #도서 등록 함수
    global Bookdf
    Title=input("도서 명 : ")
    ISBN=input("ISBN : ")
    Author=input("저자 : ")
    Pub=input("출판사 : ")
    Price=input("가격 : ")
    Link=input("링크 : ")
    Infor=input("도서 설명 : ")
    if '' in [ISBN,Title,Author, Pub, Price, Link, Infor,]:        #입력받은칸이 빈칸인지 검사
        print("올바른 값을 입력세요.")
        return 0
    else:
        in_row=[ISBN,Title,Author,Pub,Price,Link,Infor,1]         # 입력받은 값을 리스트로 
        Bookdf=Bookdf.append(pd.Series(in_row, index=Bookdf.columns),ignore_index =True) # Bookdf에 추가
        Bookdf.to_csv('Bookdata.csv',index=False,encoding='utf-8-sig') # 추가된Bookdf 를 csv로 저장
    print(Bookdf)


#도서 수정 테스트용
def BookAdit():
    AditTitle=input("변경할 도서 명 : ")   # 수정할 도서 검색
    if (Bookdf['Book_title']!=AditTitle).all():       #검색 결과가 없는 경우
        print('검색 결과가 없습니다.')
    else:
        Title=input("도서 명 ")                  #수정할 도서명
        Isbn=input("ISBN ")                      #수정할 ISBN
        Author=input("저자 : ")                  #수정할 저자
        Infor=input("도서 설명 : ")              #수정할 도서정보
        Bookdf.loc[Bookdf['Book_title'].str.contains(AditTitle),('Book_title','Book_ISBN','Book_author','Book_description')]=(Title,Isbn,Author,Infor)      #수정한 정보를 데이터 프레임에 추가
        Bookdf.to_csv('Bookdata.csv',index=False,encoding='utf-8-sig')           #수정된 Bookdf 를 csv로 저장
    print(Bookdf)



#도서 삭제 테스트용
def BookDel():
    Title=input('삭제할 도서 명')  # 삭제할 도서 선택
    Bookdf.loc[Bookdf['Book_title'].str.contains(Title),('Book_pre')]=(0) #선택한 도서의 도서여부 0으로 바꿈
    Bookdf.to_csv('Bookdata.csv',index=False,encoding='utf-8-sig')   #수정된 Bookdf 를 csv로 저장
    print(Bookdf)


def BookFind():

    FindChoice=input("1: 제목, 2:저자 선택 ")
    if FindChoice =='1':
        TitleVal=Bookdf['Book_title'].values  # 데이터프레임의 Book_title의 값을 리스트로 만들어 확인하기위해 만든소스
        TitleList=TitleVal.tolist()
        print(TitleList)
        
        FindTitle=input("찾는 제목 입력:")
        
        filt=Bookdf['Book_title'].str.contains(FindTitle) # 특정 문자를 포함한 제목을 가진 데이터 프레임을 filt
        if Bookdf[filt].empty:                          #데이터 프레임이 비었다면 검색결과가없는것
            print("검색결과가 없습니다.")
        else:                                           #값이 있다면 검색된 데이터프레
            print(Bookdf[filt])
        
       
    elif FindChoice == '2':
        
        AuthorVal=Bookdf['Book_author'].values      #데이터프레임의 Book_author의 값을 리스트로 만들어 확인하기위해 만든소스
        AuthorList=AuthorVal.tolist()
        print(AuthorList)
        
        FindAuthor=input("찾는 저자 입력:")
        
        filt=Bookdf['Book_author'].str.contains(FindAuthor) # 특정 문자를 포함한 저자 을 가진 데이터 프레임을 filt
        if Bookdf[filt].empty:                          #데이터 프레임이 비었다면 검색결과가없는것
            print("검색결과가 없습니다.")
        else:                                           #값이 있다면 검색된 데이터프레임
            print(Bookdf[filt])
        

    
    
#메인 테스트 시작
        
#BookSave() #등록
#BookAdit() #수정
#BookDel() #삭제
BookFind() #검색
