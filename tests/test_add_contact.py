# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string
import re


def random_string(prefix, maxlen):
    pattern = r'[`\\/\"<\'>]'
    symbols = string.ascii_letters + string.digits + re.sub(pattern, "", string.punctuation) + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_phone(prefix, maxlen):
    pattern = r'[`\\/\"<\'>]'
    symbols = string.digits + re.sub(pattern, "", string.punctuation) + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname="", middlename="", lastname="", nickname="",
                    address="", homephone="", email="")] + [
    Contact(firstname=random_string("firstname", 15), middlename=random_string("middlename", 15),
            lastname=random_string("lastname", 20), nickname=random_string("nickname", 20),
            address=random_string("address", 20), homephone=random_phone("111", 10),
            mobilephone=random_phone("222", 10), email=random_string("email", 15),
            email2=random_string("email2", 15))
    for i in range(5)
]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contact = app.contact.get_contact_list()
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

