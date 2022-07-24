import time


def get_week(year, month, day):
    """
    获取星期数
    :param year: 年
    :param month: 月
    :param day: 日
    :return: 星期几的字符串
    """
    tuple_time = time.strptime("%d - %d - %d" % (year, month, day), "%Y - %m - %d")
    dict_week = {
        0: "星期一",
        1: "星期二",
        2: "星期三",
        3: "星期四",
        4: "星期五",
        5: "星期六",
        6: "星期日",
    }
    return dict_week[tuple_time[6]]


re = get_week(2022, 6, 3)
print(re)
tuple_time = time.localtime()
print(time.mktime(tuple_time))
