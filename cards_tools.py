# _*_ coding: utf-8 _*_
__author__ = 'xiaozhi'
__date__ = '2017/12/27 21:43'

card_list = []


def show_menu():
    """
    显示菜单
    """
    print("*" * 50)
    print("欢迎使用【名片管理系统】 V1.0")
    print("")
    print("1、新增名片")
    print("2、显示全部")
    print("3、搜索名片")
    print("")
    print("0、退出系统")

    print("*" * 50)


def new_card():
    """
    新增名片
    """
    print("-" * 50)
    print("新增名片")

    # 1、提示用户输入名片信息
    name = raw_input("请输入姓名：")
    phone = raw_input("请输入电话：")
    qq = input("请输入QQ：")
    email = raw_input("请输入邮箱：")

    # 2、使用用户输入的信息建立一个名片字典
    card_dict = {"name": name, "phone": phone, "qq": qq, "email": email}

    # 3、将名片字典添加到列表中
    card_list.append(card_dict)
    # print card_list

    # 4、提示用户添加成功
    print("添加%s的名片成功！" % name)


def show_all():
    """
    显示所有名片
    :return:
    """
    print("-" * 50)
    print("显示所有名片")

    if len(card_list) == 0:
        print("当前没有任何名片记录，请添加名片!")
        return
    else:
        # 遍历名片列表依次输出字典信息
        for card_dict in card_list:
            print("姓名：%s\t电话：%s\tQQ：%s\t\t邮箱%s" %
                  (card_dict["name"], card_dict["phone"], card_dict["qq"], card_dict["email"]))
        print("^" * 50)


def search_card():
    """
    搜索名片
    :return:
    """
    print("-" * 50)
    print("搜索名片")

    find_name = raw_input("请输入要搜索的姓名：")
    for card_dict in card_list:
        if card_dict["name"] == find_name:
            print("姓名：%s\t电话：%s\tQQ：%s\t\t邮箱%s" %
                  (card_dict["name"], card_dict["phone"], card_dict["qq"], card_dict["email"]))
            deal_card(card_dict)
            break
    else:
        print("抱歉，没有找到'%s'" % find_name)


def deal_card(find_dict):
    """
    操作搜索到的名片
    :param find_dict:
    """
    action = input("请选择要执行的操作：【1】修改  【2】删除  【0】返回：")
    if action == 1:
        find_dict["name"] = input_card_info(find_dict["name"], "姓名【回车不修改】：")
        find_dict["phone"] = input_card_info(find_dict["phone"], "电话【回车不修改】：")
        find_dict["qq"] = input_card_info(find_dict["qq"], "QQ【回车不修改】：")
        find_dict["email"] = input_card_info(find_dict["email"], "邮箱【回车不修改】：")

        print("名片修改成功")
    elif action == 2:
        card_list.remove(find_dict)
        print("该名片信息已删除")


def input_card_info(dict_value, tip_message):
    """
    1、提示用户输入内容
    2、针对用户输入的内容进行判断，如果用户输入了内容，直接返回结果
    3、如果用户没有输入内容，返回字典中原有的值
    """
    result_str = raw_input(tip_message)
    if len(result_str) > 0:
        return result_str
    else:
        return dict_value
