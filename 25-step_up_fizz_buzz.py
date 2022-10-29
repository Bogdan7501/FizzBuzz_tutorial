




#for ループを使わずに実装するなど
#行数を制限したりというのもある

#内包表記を使って、FizzBuzzを一行で書く、面白い書き方がある

#print(" ".join(["Fizz"*(num%3==0)+"Buzz"*(num%5==0)or str(num)for num in range(1,101)]))
#1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz 16 17 Fizz 19 Buzz Fizz 22 23 Fizz Buzz 26 Fizz 28 29 FizzBuzz 31 32 Fizz 34 Buzz Fizz 37 38 Fizz Buzz 41 Fizz 43 44 FizzBuzz 46 47 Fizz 49 Buzz Fizz 52 53 Fizz Buzz 56 Fizz 58 59 FizzBuzz 61 62 Fizz 64 Buzz Fizz 67 68 Fizz Buzz 71 Fizz 73 74 FizzBuzz 76 77 Fizz 79 Buzz Fizz 82 83 Fizz Buzz 86 Fizz 88 89 FizzBuzz 91 92 Fizz 94 Buzz Fizz 97 98 Fizz Buzz

#実務や開発においては、上記のようなコードを書く必要はない
#内包表記においても、中身が複雑になったら、複数行に分けて書くべき


#解説：
#21行目：resultという[varible]を作成、" ".join(fizz_buzz_list)で、結果が作成され
#23行目：printする
fizz_buzz_list=["Fizz"*(num%3==0)+"Buzz"*(num%5==0)or str(num)for num in range(1,101)]
result=" ".join(fizz_buzz_list)#21行目のfizz_buzz_list[list]が入ってる
print(result)
#1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz 16 17 Fizz 19 Buzz Fizz 22 23 Fizz Buzz 26 Fizz 28 29 FizzBuzz 31 32 Fizz 34 Buzz Fizz 37 38 Fizz Buzz 41 Fizz 43 44 FizzBuzz 46 47 Fizz 49 Buzz Fizz 52 53 Fizz Buzz 56 Fizz 58 59 FizzBuzz 61 62 Fizz 64 Buzz Fizz 67 68 Fizz Buzz 71 Fizz 73 74 FizzBuzz 76 77 Fizz 79 Buzz Fizz 82 83 Fizz Buzz 86 Fizz 88 89 FizzBuzz 91 92 Fizz 94 Buzz Fizz 97 98 Fizz Buzz

fizz_buzz_list=["Fizz"*(num%3==0)+"Buzz"*(num%5==0)or str(num)for num in range(1,101)]
result=" ".join(fizz_buzz_list)#21行目のfizz_buzz_list[list]が入ってる
print(fizz_buzz_list)
#['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz', '16', '17', 'Fizz', '19', 'Buzz', 'Fizz', '22', '23', 'Fizz', 'Buzz', '26', 'Fizz', '28', '29', 'FizzBuzz', '31', '32', 'Fizz', '34', 'Buzz', 'Fizz', '37', '38', 'Fizz', 'Buzz', '41', 'Fizz', '43', '44', 'FizzBuzz', '46', '47', 'Fizz', '49', 'Buzz', 'Fizz', '52', '53', 'Fizz', 'Buzz', '56', 'Fizz', '58', '59', 'FizzBuzz', '61', '62', 'Fizz', '64', 'Buzz', 'Fizz', '67', '68', 'Fizz', 'Buzz', '71', 'Fizz', '73', '74', 'FizzBuzz', '76', '77', 'Fizz', '79', 'Buzz', 'Fizz', '82', '83', 'Fizz', 'Buzz', '86', 'Fizz', '88', '89', 'FizzBuzz', '91', '92', 'Fizz', '94', 'Buzz', 'Fizz', '97', '98', 'Fizz', 'Buzz']


#True=1
#False=0

#for num in range(1,101)
#numには1~100までの数値が、毎回1つずつ入ってくる　
#これは、for文でも、[list]内包表記でも同様

#numに1が入り、forまでの"Fizz"*(num%3==0)+"Buzz"*(num%5==0)or str(num)の処理が行われる

#numが1ならば、num%3==0は[False]になるから、
#文字列Fizz*False=Fizz*0と評価される

#numが1の最初はFizz*何々が空文字になった

#次は"Buzz"*(num%5==0)
#numが1ならば、num%5==0は[False]になるから、
#文字列Buzz*False=Buzz*0と評価される

#まとめると
#"+"or str(num)になる

#or=
#user_input=input()
#result=user_input or"デフォルト文字列"


#[True],[False]と評価される仕組みと[or]を使っている状況

#今回は、" "+" "or str(num)になったから、
#str(num)が評価され、[1]になった
#[2]も同様

#3の場合、
#numに3が入り、forまでの"Fizz"*(num%3==0)+"Buzz"*(num%5==0)or str(num)の処理が行われる

#numが3ならば、num%3==0は[True]になるから、
#文字列Fizz*True=Fizz*1と評価される

#次は"Buzz"*(num%5==0)
#numが3ならば、num%5==0は[False]になるから、
#文字列Buzz*False=Buzz*0と評価され、空文字列になる


#5の場合、
#numに5が入り、forまでの"Fizz"*(num%3==0)+"Buzz"*(num%5==0)or str(num)の処理が行われる

#numが5ならば、num%3==0は[False]になるから、
#文字列Fizz*False=Fizz*0と評価され、空文字列になる

#次は"Buzz"*(num%5==0)
#numが5ならば、num%5==0は[True]になるから、
#文字列Buzz*True=Buzz*1と評価され、文字列Buzzになる


