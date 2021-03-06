#1. 아래 문자열의 길이를 구해보세요.
q1 = "15"
print(len(q1))  # len(): 해당 데이터의 길이를 구하는 함수


# 2. print 함수를 사용해서 아래와 같이 출력해보세요.
#    apple;orange;banana;lemon
print("apple;orange;banana;lemon")


# 3. 화면에 * 기호 100개를 표시하세요.
print('*'*100)


# 4. 문자열 "30" 을 각각 정수형, 실수형, 복소수형, 문자형으로 변환해보세요.
a='30'
print(int(a))
print(float(a))
print(complex(a))
print(str(a))


# 5. 다음 문자열 "Niceman" 에서 "man" 문자열만 추출해보세요.
a="Niceman"
print(a[4:7])   # 4번째 인덱스부터 7번째 인덱스 전까지 슬라이싱


# 6. 다음 문자열을 거꾸로 출력해보세요. : "Strawberry"
a="Strawberry"
print(a[8:8:-1])  #


# 7. 다음 문자열에서 '-'를 제거 후 출력하세요. : "010-7777-9999"
import re
a="010-7777-9999"
print(re.sub('[^0-9]','',a))


# 8. 다음 문자열(URL)에서 "http://" 부분을 제거 후 출력하세요. : "http://daum.net/"
a="http://daum.net/"
print(a.replace('http://',''))


# 9. 다음 문자열을 모두 대문자, 소문자로 각각 출력해보세요. : "NiceMan"
a="Niceman"
print(a.upper())
print(a.lower())


# 10. 다음 문자열을 슬라이싱을 이용해서 "cde"만 출력하세요. : "abcdefghijklmn"
a="abcdefghijklmn"
print(a[2:5])


# 11. 다음 리스트에서 "Apple" 항목만 삭제하세요. : ["Banana", "Apple", "Orange"]
a=["Banana", "Apple", "Orange"]
del a[1]
print(a)


# 12. 다음 튜플을 리스트로 변환하세요. : (1,2,3,4)
a=(1,2,3,4)
a=list(a)
print(type(a))


# 13. 다음 항목을 딕셔너리(dict)으로 선언해보세요. : <성인 - 100000 , 청소년 - 70000 , 아동 - 30000>
a={'성인':100000, '청소년':70000 , '아동':30000}
print(type(a))


# 14. 13번 에서 선언한 dict 항목에 <소아 - 0> 항목을 추가해보세요.
a['소아']=0


# 15. 13번에서 선언한 딕셔너리(dict)에서 Key 항목만 출력해보세요.
print(list(a.keys()))


# 16. 13번에서 선언한 딕셔너리(dict)에서 value 항목만 출력해보세요.
print(list(a.values()))


print('\n\n\n\n')


# 132
a,b,c,d=1,2,3,4
print(1**3+b*c)
print(d/b%c)
print(c%b**b-a)
print(d//b*a%a**d)
print()


# 133
a,b,c=2,3,5
a+=a+a+b/1
b//=a**3-b
c*=c+b-2
print(a)
print(b)
print(c)


# 134
a=0b1101001
b=0b1011111
print(bin(a&b),a&b)