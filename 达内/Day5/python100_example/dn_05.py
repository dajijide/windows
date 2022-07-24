word = input("请输入·单词")
f = open('test.txt')

for line in f:
    w = line.split(' ')[0]
    if w > word:
        print("没有找到单词")
        break
    elif w == word:
        print(line)
        break
else:
    print("没有找到单词")
f.close()