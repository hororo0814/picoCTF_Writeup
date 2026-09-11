# 与えられた暗号を入力
text = input("暗号を入力")

# アルファベットの数26回分文字をずらし続ける
for i in range(26):
    flag = ""
    for t in text:
        if "a" <= t <= "z":
            part_flag = chr((ord(t) - ord("a") + i) % 26 + ord("a"))
            flag += part_flag
        elif "A" <= t <= "Z":
            part_flag = chr((ord(t) - ord("A") + i) % 26 + ord("A"))
            flag += part_flag
        else:
            # 今回は記号ならそのまま出力する
            flag += t

    # flagを出力
    print(flag)
