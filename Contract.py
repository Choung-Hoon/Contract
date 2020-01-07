# -*- coding: utf-8 -*-


class Contact:
    def __init__(self, name, phone_number, e_mail, addr):
        self.name = name
        self.phone_number = phone_number
        self.e_mail = e_mail
        self.addr = addr

    def print_info(self):
        print("-------------------------------------")
        print("Name : %s" % self.name)
        print("Phone_number : %s" % self.phone_number)
        print("E-mail : %s" % self.e_mail)
        print("Address : %s" % self.addr)


def set_contact():
    print("-------------------------------------")
    print("1. 연락처 입력")
    print("-------------------------------------")
    name = input("Name : ")
    phone_number = input("Phone Number : ")
    e_mail = input("E-mail : ")
    addr = input("Address : ")

    contact = Contact(name, phone_number, e_mail, addr)

    return contact


def print_menu():
    """
    show menu and get input
    :return: returns menu id
    """
    print("-------------------------------------")
    print("1. 연락처 입력")
    print("2. 연락처 출력")
    print("3. 연락서 삭제")
    print("4. 종료")
    print("-------------------------------------")
    menu = input("메뉴선택 : ")
    try:
        menu = int(menu)
    except ValueError:
        print("메뉴 아이디 변환 오류")

    return menu


def print_contact(contact_list):
    """
    prints contact list

    :param contact_list: 
    :return: None
    """

    print("2. 연락처 출력")
    print("-------------------------------------")
    for contact in contact_list:
        contact.print_info()


def delete_contact(contact_list, name):
    print("3. 연락처 삭제")
    for i, target in enumerate(contact_list):
        if name == target:
            del contact_list[i]


def run():
    contact_list = []

    while 1:
        # getting input
        menu = print_menu()
        if menu == 1:
            contact = set_contact()
            contact_list.append(contact)
        elif menu == 2:
            print_contact(contact_list)
        elif menu == 3:
            name = input("Name : ")
            delete_contact(contact_list, name)
        elif menu == 4:
            break
        else:
            print("잘못 입력하였습니다. 메뉴를 다시 입력하세요")


if __name__ == "__main__":
    run()
