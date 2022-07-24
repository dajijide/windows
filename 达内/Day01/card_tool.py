card_list = []


def show_menu():
    """显示菜单"""
    print("#" * 50)
    print("欢迎使用名片管理系统v1.0")
    print("")
    print("1.新增名片")
    print("2.显示全部")
    print("3.搜索名片")
    print("0.退出系统")
    print("")
    print("#" * 50)


print(show_menu())


def new_card():
    print("-" * 50)
    print("新增名片")

    # 提示用户输入详细信息
    name_str = input("请输入姓名：")
    phone_str = input("请输入电话：")
    qq_str = input("请输入qq：")
    email_str = input("请输入邮件：")

    # 使用用户信息新建一个库
    card_dict = {"name": name_str,
                 "phone": phone_str,
                 "qq": qq_str,
                 "email": email_str}

    # 用列表保存用户信息
    card_list.append(card_dict)
    print(card_list)

    # 通知用户信息保存成功
    print("%s信息保存成功" % name_str)


def show_all():
    print("-" * 50)
    print("显示全部")

    # 判断是否存在名片记录，如果不存在，提示用户创建用户
    if len(card_list) == 0:
        print("没有用户名片，请创建用户")

        # return后面没有任何内容，返回调用函数的位置
        # 不会返回任何值
        return

    # 打印表头
    for name in ["姓名", "电话", "qq", "邮件"]:
        print(name, end="\t\t")
    print("")

    # 打印分割线
    print("-" * 50)

    # 遍历名片列表依次输出字典内容
    for card_dict in card_list:
        print("%s\t\tt%s\t\t%s\t\t%s" % (card_dict["name"],
                                                  card_dict["phone"],
                                                  card_dict["qq"],
                                                  card_dict["email"]))


def search_card():
    print("-" * 50)
    print("搜索名片")

    # 1.提示用户输入要搜索的姓名
    find_name = input("请输入要搜索的姓名")

    # 2.遍历名片列表，查询要搜索的姓名，如果查询不到，需要提示用户

    for card_dict in card_list:
        if card_dict["name"] == find_name:
            print("姓名\t\t\t电话\t\t\tqq\t\t\t邮件")
            print("%s\t\t\t%s\t\t\t%s\t\t\t%s\t\t\t" % (card_dict["name"],
                                                        card_dict["phone"],
                                                        card_dict["qq"],
                                                        card_dict["email"]))
            # 针对找到的名片记录执行修改和删除
            deal_card(card_dict)
            break
    else:
        print("没有找到%s用户" % find_name)


def deal_card(find_card):
    print(find_card)
    action_str = input("请选择要执行的操作"
                       "[1]修改 [2]删除 [0]返回上级菜单")

    if action_str == "1":
        find_card["name"] = input("姓名：")
        find_card["phone"] = input("电话：")
        find_card["qq"] = input("qq：")
        find_card["email"] = input("邮件：")
        print("修改名片")

    elif action_str == "2":
        card_list.remove(find_card)
        print("删除名片")