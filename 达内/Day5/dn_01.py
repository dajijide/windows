for r in range(4):
    for c in range(r + 1):
        print("*", end="")
    print()

list = [3, 80, 45, 5, 7, 1, 7]
for c in range(len(list) - 1):
    for r in range((c + 1), len(list)):
        if list[c] == list[r]:
            result = True
            print(result)
            break

if result == False:
    print("没有相同")

tuple()
