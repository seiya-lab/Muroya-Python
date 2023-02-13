# 室屋がPythonを学ぶファイル
# TODO 回文を判定するプログラムを作成してください。
# 引数は文字列、出力はブール値


def is_kaibun(text):
    reverced_text = text[::-1] #文字列のスライス(逆から読む)
    if reverced_text == text:
      return True


texts = ["たけやぶやけた", "a", "わたしはたわし"]

for text in texts:
    if is_kaibun(text):
        print(text, "は回文ですよ")
    else:
        print(text,"は回文じゃないです！！")

#もしスライスを使わない方法だったら、最初の文字と最後の文字を比較していく方法もある
# def is_kaibun(text):
#     left = 0
#     right = len(text) - 1
#     while left < right:
#         if text[left] != text[right]:
#             return False
#         left += 1
#         right -= 1
#     return True