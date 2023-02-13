# 室屋がPythonを学ぶファイル
# TODO 素数を判定するプログラムを作成してください。
# 引数が正の整数で、出力がbooleanで返してください

from re import I

#数字が素数かどうか判断
def isPrime(num):
    for i in range(2,num):
      if num % i == 0:
        return False
    return True

#2から100までの数字を列挙するforループ
for i in range(2, 100):
    if isPrime(i):
        print(str(i) + "は素数です。文句あるか")


# def isPrime(num): もし5が入ったら
#     for i in range(2,num): 2-4までの数字を繰り返す(2,3,4) rangeはnum-1となるため
#       if num % i == 0: 5が4以下の数字(1は除く)で割り切れたら
#         return False 動作終わり
#     return True そうじゃなかったらTRUEで返す