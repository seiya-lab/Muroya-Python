# 室屋がPythonを学ぶファイル
# 1以上100以下の整数のうち、10進数での格桁の和が4以上16以下であるものの総和を出力してください。

total = 0

for i in range(1, 101):
  num = [int(d) for d in str(i)]
  if 4 <= sum(num) <= 16:
    total += i
print(total)

#for文の中、これもあり
# 数値を文字列に変換
# s = str(n)
# １文字ずつ数値化し配列にする。
# array = list(map(int, s))
# 合計値を返す
# return sum(array)