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
    print("-------------------------------------")
    print("2. 연락처 출력")
    for contact in contact_list:
        contact.print_info()


def delete_contact(contact_list, name):
    print("3. 연락처 삭제")
    for i, target in enumerate(contact_list):
        if name == target.name:
            del contact_list[i]


def store_contact(contact_list):
    with open("contact_db.txt", mode="wt", encoding='utf-8') as f:
        for contact in contact_list:
            f.write(contact.name + '\n')
            f.write(contact.phone_number + '\n')
            f.write(contact.e_mail + '\n')
            f.write(contact.addr + '\n')


def load_contact(contact_list):
    """
    read contact-file and load into contact_list
    :param contact_list:
    :return: None
    """
    with open("contact_db.txt", mode="rt", encoding="utf-8") as f:
        lines = f.readlines()
        num = len(lines) / 4
        num = int(num)

        for i in range(num):
            # 4줄 단위로 하나의 사람 정보임
            name = lines[4 * i].rstrip('\n')
            phone = lines[4 * i + 1].rstrip('\n')
            email = lines[4 * i + 2].rstrip('\n')
            addr = lines[4 * i + 3].rstrip('\n')
            contact = Contact(name, phone, email, addr)
            contact_list.append(contact)


def run():
    contact_list = []
    load_contact(contact_list)

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
            store_contact(contact_list)
            break
        else:
            print("잘못 입력하였습니다. 메뉴를 다시 입력하세요")


if __name__ == "__main__":
    run()
