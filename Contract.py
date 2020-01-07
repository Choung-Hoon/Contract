# -*- coding: utf-8 -*-

class Contract:
    def __init__(self, name, phone_number, e_mail, addr):
        self.name = name
        self.phone_number = phone_number
        self.e_mail = e_mail
        self.addr = addr

    def print_info(self):
        print("Name : %s" % self.name)
        print("Phone_number : %s" % self.phone_number)
        print("E-mail : %s" % self.e_mail)
        print("Address : %s" % self.addr)


def run():
    kim = Contract("김정훈", "010-2755-1607", "nobel77@naver.com", "SEOUL")
    kim.print_info()


if __name__ == "__main__":
    run()
