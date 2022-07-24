import time


def live_day(year, month, day):
    """
    计算活了多少天了
    :param year: 年
    :param month: 月
    :param day: 日
    :return: 活得天数
    """
    tuple_time = time.strptime("%d-%d-%d" % (year, month, day), "%Y-%m-%d")
    days = time.time() - time.mktime(tuple_time)
    return int(days / 60 / 60 // 24)


re = live_day(2002,3,24)
print(re)
