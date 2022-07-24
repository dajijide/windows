import card_tool


while True:

    #  显示功能菜单
    card_tool.show_menu()

    action_str = input("您希望输入的操作是:")
    print("您选择的操作是【%s】" % action_str)

    if action_str in ["1", "2", "3"]:

        if action_str in ["1"]:
            card_tool.new_card()

        elif action_str == "2":
            card_tool.show_all()

        elif action_str == "3":
            card_tool.search_card()

    elif action_str == "0":
        print("退出程序")
        break

    else:
        print("您输入的不正确，请重新输入")