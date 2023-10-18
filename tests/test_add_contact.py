# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contact = app.contact.get_contact_list()
    contact = Contact(firstname="Kat", middlename="Al", lastname="GV", nickname="vs", title="ascss",
                      company="comp", address="Kzn", homephone="66675666", mobilephone="765756765", workphone="5675",
                      secondaryphone="321123", email="e@m.com")
    app.contact.create_contact(contact)
    assert len(old_contact) + 1 == app.contact.count()
    new_contact = app.contact.get_contact_list()
    old_contact.append(contact)
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)


# def test_add_empty_contact(app):
#     old_contact = app.contact.get_contact_list()
#     app.contact.create_contact(Contact("", "", "", "", "", "", "", "", "", "", ""))
#     new_contact = app.contact.get_contact_list()
#     assert len(old_contact) + 1 == len(new_contact)

