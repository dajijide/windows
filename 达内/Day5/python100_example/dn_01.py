L = []
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if (i != k)and (k != j) and (i != j):
                L.append([i,j,k])
print("数量", len(L))
print(L)
