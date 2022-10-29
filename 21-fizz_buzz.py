




#Fizz Buzz 問題
#繰り返し処理と条件分岐を組み合わせる必要がある
#ちょっとしたプログラミングの練習にもなる

#Fizz Buzz のルール
#1から、n回まで繰り返し
#3の倍数はFizz、
#5の倍数はBuzz、
#15の倍数で、Fizz Buzz
#それ以外は、数字を出力する

#今回は
#1から、100回まで繰り返し
#3の倍数はFizz、
#5の倍数はBuzz、
#15の倍数で、Fizz Buzz
#それ以外は、数字を出力する





#今回n=100
for i in range(1,101):
    pass#[pass]=Errorにならず、何もしない


#まだ動かないコード
#print functionに[end=" "]を入れる意味=
#デフォルトのprint functionでは、出力後に改行される
#今回は1~100まで出力することから100分の改行が行われてみずらくなる
#print functionに[end=" "]：←をいれることで、指定した引数で出力が繋がれていく
#デフォルトでは[end="\n"]
#※[i % 15==0]※を必ず最初に書く
# for i in range(1,101):
#     if i % 15==0:#if 15の倍数
#         print("Fizz Buzz",end=" ")
#     elif i % 5==0:#elif 5の倍数
#         print("Buzz",end=" ")
#     elif i % 3==0:#3の倍数
#         print("Fizz",end=" ")
#     else:
#         print(i, end=" ")
# 1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 Fizz Buzz 16 17 Fizz 19 Buzz Fizz 22 23 Fizz Buzz 26 Fizz 
# 28 29 Fizz Buzz 31 32 Fizz 34 Buzz Fizz 37 38 Fizz Buzz 41 Fizz 43 44 Fizz Buzz 46 47 Fizz 49 Buzz Fizz 52 
# 53 Fizz Buzz 56 Fizz 58 59 Fizz Buzz 61 62 Fizz 64 Buzz Fizz 67 68 Fizz Buzz 71 Fizz 73 74 Fizz Buzz 76 77 
# Fizz 79 Buzz Fizz 82 83 Fizz Buzz 86 Fizz 88 89 Fizz Buzz 91 92 Fizz 94 Buzz Fizz 97 98 Fizz Buzz


#※[i % 15==0]※を必ず最初に書かなかった場合
# for i in range(1,101):
#     if i % 5==0:
#         print("Buzz",end=" ")
#     elif i % 3==0:
#         print("Fizz",end=" ")
#     elif i % 15==0:
#         print("Fizz Buzz",end=" ")
#     else:
#         print(i, end=" ")
# 1 2 Fizz 
# 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 Buzz 16 17 Fizz 19 Buzz Fizz 22 23 Fizz Buzz 26 Fizz 28 29 Buzz 31 
# 32 Fizz 34 Buzz Fizz 37 38 Fizz Buzz 41 Fizz 43 44 Buzz 46 47 Fizz 49 Buzz Fizz 52 53 Fizz Buzz 56 Fizz 58 
# 59 Buzz 61 62 Fizz 64 Buzz Fizz 67 68 Fizz Buzz 71 Fizz 73 74 Buzz 76 77 Fizz 79 Buzz Fizz 82 83 Fizz Buzz 
# 86 Fizz 88 89 Buzz 91 92 Fizz 94 Buzz Fizz 97 98 Fizz Buzz


#これがFizz Buzzの回答


#他の細かいバージョン
# for i in range(1,101):
#     message=''
#     if i % 15==0:
#         message='Fizz Buzz'
#     elif i % 5==0:
#         message='Buzz'
#     elif i % 3==0:
#         message='Fizz'
#     else:
#         message=i
#     print(message,end=' ')
# 1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 Fizz Buzz 16 17 Fizz 19 Buzz Fizz 22 23 Fizz Buzz 26 Fizz 
# 28 29 Fizz Buzz 31 32 Fizz 34 Buzz Fizz 37 38 Fizz Buzz 41 Fizz 43 44 Fizz Buzz 46 47 Fizz 49 Buzz Fizz 52 
# 53 Fizz Buzz 56 Fizz 58 59 Fizz Buzz 61 62 Fizz 64 Buzz Fizz 67 68 Fizz Buzz 71 Fizz 73 74 Fizz Buzz 76 77 
# Fizz 79 Buzz Fizz 82 83 Fizz Buzz 86 Fizz 88 89 Fizz Buzz 91 92 Fizz 94 Buzz Fizz 97 98 Fizz Buzz


#他の細かいバージョン
# for i in range(1,101):
#     message=''
#     if i % 3==0:
#         message+='Fizz'

#     if i % 5==0:
#         message+='Buzz'
    
#     if message:
#         print(message,end=' ')
#     else:
#         print(i,end=' ')
# 1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz 16 17 Fizz 19 Buzz Fizz 22 23 Fizz Buzz 26 Fizz 28 29 FizzBuzz 31 32 Fizz 34 Buzz Fizz 37 38 Fizz Buzz 41 Fizz 43 44 FizzBuzz 46 47 Fizz 49 Buzz Fizz 52 53 
# Fizz Buzz 56 Fizz 58 59 FizzBuzz 61 62 Fizz 64 Buzz Fizz 67 68 Fizz Buzz 71 Fizz 73 74 FizzBuzz 76 77 Fizz 
# 79 Buzz Fizz 82 83 Fizz Buzz 86 Fizz 88 89 FizzBuzz 91 92 Fizz 94 Buzz Fizz 97 98 Fizz Buzz


#その他のやり方
for i in range(1,101):
    message=''
    if i % 3==0:
        message+='Fizz'

    if i % 5==0:
        message+='Buzz'

    print(message or i,end=' ')
# print(message or i,end=' ')=まずmessageを見る、Trueであれば使えて、空文字(False)であれば[i]に移る、[i]がTrueならば[i]が適応される

# 1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz 16 17 Fizz 19 Buzz Fizz 22 23 Fizz Buzz 26 Fizz 28 29 FizzBuzz 31 32 Fizz 34 Buzz Fizz 37 38 Fizz Buzz 41 Fizz 43 44 FizzBuzz 46 47 Fizz 49 Buzz Fizz 52 53 
# Fizz Buzz 56 Fizz 58 59 FizzBuzz 61 62 Fizz 64 Buzz Fizz 67 68 Fizz Buzz 71 Fizz 73 74 FizzBuzz 76 77 Fizz 
# 79 Buzz Fizz 82 83 Fizz Buzz 86 Fizz 88 89 FizzBuzz 91 92 Fizz 94 Buzz Fizz 97 98 Fizz Buzz

# user_input=""#例えば、ユーザーからの入力が入る
# result=user_input or "デフォルト文字列"
#[or]の使い方
