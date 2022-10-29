




#1.何をしたいのか?
#1,2,Fizz,4,Buzz,Fizz,7.....を出力したい

# print(1)#1
# print(2)#2
# print(3)#3

# print(1)#1
# print(2)#2
# print("Fizz")#Fizz

#2.何回出力したいのか?
#10回?,100回?,100000000回?....膨大な量を繰り返す

#繰り返す→：for/while
for i in range(3):
    pass#print(1)#111
#print(1)を3回繰り返せ

for i in range(3):
    pass#print(i)#012
#(i)に[0]が入り、[0]がprintされる
#(i)に[1]が入り、[1]がprintされる
#(i)に[2]が入り、[2]がprintされる

#0~9
for i in range(10):
    pass#print(i)#0123456789,(計10)10未満

#1~10
for i in range(1,11):
    pass#print(i)#123456789,10,(計11)11未満


#1~1000
for i in range(1,1001):
    pass#print(i)#123456789,10,(計11)11未満


#3.1,2,3,4,5,6.....ではなく
#→：3の倍数のときはFizz,5の倍数のときはBuzz,3,5の倍数の時はFizzBuzz

#if文の例
#Fizzを付け加える
for i in range(1,11):
    if i==3:#条件式
        pass#print("Fizz")#Fizz


#elseを付け加える
for i in range(1,11):
    if i==3:#条件式
        pass#print("Fizz")
    else:
        pass#print(i)#12Fizz45678910


#elifを付け加える
#Buzzを付け加える
for i in range(1,11):
    if i==3:#条件式,
        pass#print("Fizz")
    elif i==5:#iが5に等しい時
        pass#print("Buzz")
    else:
        pass#print(i)#12Fizz4Buzz678910


#%=余りを割り出すときに使う演算
for i in range(1,11):
    if i %3==0:#条件式,
        pass#print("Fizz")
    elif i %5==0:#iが5に等しい時
        pass#print("Buzz")
    else:
        pass#print(i)#12Fizz4BuzzFizz78FizzBuzz


#3,5の倍数の時はFizzBuzzを表す
for i in range(1,101):
    if i %3==0:#条件式,
        pass#print("Fizz")
    elif i %5==0:#iが5に等しい時
        pass#print("Buzz")
    elif i  % 3==0 and i %5==0:
        pass#print("FizzBuzz")
    else:
        pass#print(i)#FizzBuzzの表示はなかった
#[i]に[1]から数字が入って、回っている
#条件の順番によって"FizzBuzz"は表示されなくなっている状態



#3,5の倍数の時はFizzBuzzを表す
for i in range(1,101):
    if i % 3==0 and i %5==0:#条件式,
        pass#print("FizzBuzz")
    elif i %3==0:#iが3に等しい時
        pass#print("Fizz")
    elif i %5==0:#iが5に等しい時
        pass#print("Buzz")
    else:
        pass#print(i)#FizzBuzzの表示はあった



#表示を横にする
for i in range(1,101):
    if i % 3==0 and i %5==0:#条件式,
        print("FizzBuzz",end=" ")
    elif i %3==0:#iが3に等しい時
        print("Fizz",end=" ")
    elif i %5==0:#iが5に等しい時
        print("Buzz",end=" ")
    else:
        print(i,end=" ")
#1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz 16 17 Fizz 19 Buzz Fizz 22 23 Fizz Buzz 26 Fizz 28 29 FizzBuzz 31 32 Fizz 34 Buzz Fizz 37 38 Fizz Buzz 41 Fizz 43 44 FizzBuzz 46 47 Fizz 49 Buzz Fizz 52 53 Fizz Buzz 56 Fizz 58 59 FizzBuzz 61 62 Fizz 64 Buzz Fizz 67 68 Fizz Buzz 71 Fizz 73 74 FizzBuzz 76 77 Fizz 79 Buzz Fizz 82 83 Fizz Buzz 86 Fizz 88 89 FizzBuzz 91 92 Fizz 94 Buzz Fizz 97 98 Fizz Buzz






# for i in range(1,101):
#     if i % 15==0:#if 15の倍数
#         print("Fizz Buzz",end=" ")
#     elif i % 5==0:#elif 5の倍数
#         print("Buzz",end=" ")
#     elif i % 3==0:#3の倍数
#         print("Fizz",end=" ")
#     else:
#         print(i, end=" ")









