# 室屋がPythonを学ぶファイル
# TODO 掛け算の九九を9×9の二次元配列の中に格納するプログラムを書いてください。

# 九九の表を作る
table = [] #table という空のリストを作成
for i in range(1, 10): #外側のforループはiという変数を1から9まで増やす。このiは乗数(かけられる数)として使用
    row = [] #tableにrowを追加、九九の表が作られる
    for j in range(1, 10): #jという変数を1から9まで増やす。このjは被乗数(かける数)として使用
        row.append(i * j) #rowにiとjの積を格納。append = 要素を追加すること
    table.append(row) #tableにrowを追加。九九の表を入れる

# 九九の表を映す
for i in range(9): # 0から8までの値を取るため、9回繰り返される
    for j in range(9):
        print(table[i][j], end="\t")
        #二次元配列 table の i 行 j 列の要素を出力。
        #end="\t" は、同じ行に続けて値を出力するために使用。このとき、各値の間にタブが入る
    print("") #""は改行。このため、次の行に続けて値を出力できる