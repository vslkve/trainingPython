# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_first_contact(app):
    app.session.login("admin", "secret")
    app.contact.edit_first_contact(Contact("Kkk", "Aaa", "Ggg", "vvvv", "aaaa", "cccc", "ZZZ", "hhhh", "1111", "222", "em@ma.ru"))
    app.session.logout()
