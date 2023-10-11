# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange


def test_edit_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create_contact(
            Contact("Kat", "Al", "GV", "vs", "ascss", "comp", "Kzn", "hm", "765756765", "5675", "e@m.com"))
    old_contact = app.contact.get_contact_list()
    index = randrange(len(old_contact))
    contact = Contact("Kkk", "Aaa", "Ggg", "vvvv", "aaaa", "cccc", "ZZZ", "hhhh", "1111", "222", "em@ma.ru")
    contact.id = old_contact[index].id
    app.contact.edit_contact_by_index(index, contact)
    assert len(old_contact) == app.contact.count()
    new_contact = app.contact.get_contact_list()
    old_contact[index] = contact
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)


# def test_edit_name_by_first_contact(app):
#     if app.contact.count() == 0:
#         app.contact.create_contact(
#             Contact("Kat", "Al", "GV", "vs", "ascss", "comp", "Kzn", "hm", "765756765", "5675", "e@m.com"))
#     old_contact = app.contact.get_contact_list()
#     app.contact.edit_first_contact(Contact(firstname="New", middlename="New", lastname="New"))
#     new_contact = app.contact.get_contact_list()
#     assert len(old_contact) == len(new_contact)
