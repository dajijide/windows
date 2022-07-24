list_01 = ["铁扇公主", "铁锤公主", "扳手王子"]

iterator = list_01.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item)
    except StopIteration:
        break

dict_02 = {"铁扇公主": 101, "铁锤公主": 102, "扳手王子": 103}
iterator_01 = dict_02.__iter__()
while True:
    try:
        key = iterator_01.__next__()
        print(key, dict_02[key])
    except StopIteration:
        break
