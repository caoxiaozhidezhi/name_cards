# _*_ coding: utf-8 _*_
__author__ = 'xiaozhi'
__date__ = '2017/12/27 21:42'

import cards_tools

while True:

    cards_tools.show_menu()

    action = int(input("请选择希望执行的操作："))
    print("您选择的操作是【%s】" % action)

    if action in [1, 2, 3]:
        if action == 1:
            cards_tools.new_card()
        elif action == 2:
            cards_tools.show_all()
        elif action == 3:
            cards_tools.search_card()

    elif action == 0:
        print("欢迎再次使用【名片管理系统】")
        break

    else:
        print("您输入的不正确，请重新选择")
