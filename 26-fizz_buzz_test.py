




print(True*3)#10
print(True+3)#2


print(False*3)#10
print(False+3)#1


print(False*3)#0




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













