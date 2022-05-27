poem = ["昔人已乘黄鹤去,此地空余黄鹤楼。",
        "黄鹤一去不复返,白云千载空悠悠。",
        "晴川历历汉阳树，芳草萋萋鹦鹉洲。",
        "日暮乡关何处是？烟波江上使人愁。"]
print(poem)

for poem_str in poem:
    print("|%s|" % poem_str.strip().center(10, "　"))

# 拆分
poem_list = poem_str.split()
print(poem)
# 合并
print("".join(poem))
