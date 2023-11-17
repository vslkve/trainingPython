# -*- coding: utf-8 -*-
from model.contact import Contact
import random


def test_edit_contact_lastname_by_id(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create_contact(
            Contact(firstname="Kat", middlename="Al", lastname="GV", nickname="vs", title="ascss",
                    company="comp", address="Kzn", homephone="66675666", mobilephone="765756765", workphone="5675",
                    secondaryphone="321123", email="e@m.com"))
    old_contact = db.get_contact_list()
    contact = random.choice(old_contact)
    contact.lastname = "NewLastname"
    app.contact.edit_contact_by_id(contact.id, contact)
    new_contact = db.get_contact_list()
    for i in (0, len(old_contact) - 1):
        if old_contact[i].id == contact.id:
            old_contact[i].lastname = "NewLastname"
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contact, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)