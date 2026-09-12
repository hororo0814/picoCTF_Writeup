text = [16, 9, 3, 15, 3, 20, 6, 20, 8, 5, 14, 21, 13, 2, 5, 18, 19, 13, 1, 19, 15, 14]

flag = ""
for i in text:
    if 1 <= i <= 65:
        part_of_flag = chr(i + 96)
    else:
        part_of_flag = i
    flag += part_of_flag

print(flag)
