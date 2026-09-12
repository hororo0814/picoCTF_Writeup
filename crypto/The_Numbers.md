# The Numbers　

## 問題の確認

numbers.phgというファイルが与えられます<br>
中身を見てみると<br>

```python
 16 9 3 15 3 20 6 { 20 8 5
 14 21 13 2 5 18 19 13 1
 19 15 14}
```
と書かれています．<br>
文字数的にも，{}の位置的にも数字の一文字がアルファベットの一文字に対応してpicoCTF{...}となるのでしょう<br>
おそらく，記号はそのままですね<br>

## 実際に解いてみる

The_Numbers.pyに数字をアルファベットに変換するコードを書きます<br>
なんか{}をいれたらエラーはいたので{}は抜いといてあとで空気読んで入れます<br>
```python
text = [16, 9, 3, 15, 3, 20, 6, 20, 8, 5, 14, 21, 13, 2, 5, 18, 19, 13, 1, 19, 15, 14]

flag = ""
for i in text:
    if 1 <= i <= 65:
        part_of_flag = chr(i + 64)
    else:
        part_of_flag = i
    flag += part_of_flag

print(flag)
```
とすると..<br>
PICOCTFTHENUMBERSMASON<br>
あ，全部大文字になっちゃった<br>
chr(i + 64)で64でやったせいですね．小文字にしたいので，96にしてもう一度トライ！<br>

picoctfthenumbersmason<br>

でましたね．これに{}をつけ足して，<br>
picoctf{thenumbersmason}<br>
答えをsubmitして，正解です．<br>

## 最後に

ASCIIコードについて理解しているか問う問題でしたね<br>
私はASCIIコードの対応表として↓のリンクの表を使っています<br>
https://www.rapidtables.com/code/text/ascii-table.html<br>
