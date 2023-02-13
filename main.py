# 室屋がPythonを学ぶファイル
# じゃんけんをするアプリを作ってください
#0:グー, 1:チョキ, 2:パーとして、プレイヤーに入力させてください。
#CPUは、それぞれの手をランダムに出すようにしてください。
#勝ち、負け、あいこを出力させてください。

import random #CPがランダムで出す用

hands=['グー', 'チョキ', 'パー']
input_str=input('0:グー 1:チョキ 2:パーで、入力してください>>> ')
hand_num=int(input_str)

computer_hand_num=random.randrange(3)
# ランダムで作った数字から、コンピュータがどの手なのかを出して、computer_handに覚えておいてもらう
computer_hand=hands[computer_hand_num]

# 入力された数字から、どの手なのかを出して、player_handに覚えておいてもらう
player_hand=hands[hand_num]

# player_handに覚えておいてもらった手を表示する
print('あなたは'+player_hand+'を出しました')
# computer_handに覚えておいてもらった手を表示する
print('相手は'+computer_hand+'を出しました')

if player_hand == computer_hand:
    print("引き分けです")
elif (player_hand == "グー" and computer_hand == "チョキ") or (player_hand == "チョキ" and computer_hand == "パー") or (player_hand == "パー" and computer_hand == "グー"):
    print("あなたの勝ちです！")
else:
    print("あなたの負けです。ガキ！")