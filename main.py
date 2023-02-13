# 室屋がPythonを学ぶファイル
# TODO バブルソートを用いて、数字を昇順に並び替えてください。
# 引数が配列、返すのも配列
def bubble_sort(num_list):
    n = len(num_list)
    for i in range(n):#配列の要素を反復処理
        for j in range(0, n - i - 1): # n - i - 1を内側のループの範囲にすると、既にソートされた要素をスキップすることができる
            if num_list[j] > num_list[j + 1]:#もし次のものより大きかったら
                num_list[j], num_list[j + 1] = num_list[j + 1], num_list[j] #num_list[j], num_list[j + 1]を交換
    return num_list #最終的に並べ終わったやつを返す


num_list = [1, 5, 4, 3, 2, 8, 7, 9, 10]
print("元の配列:", num_list)
print("ソートされた配列:", bubble_sort(num_list))
