from model.contact import Contact
from random import randrange
import time


def test_delete_some_contact(app):
    if app.contact.count() == 0:
        app.contact.create_contact(
            Contact(firstname="Kat", middlename="Al", lastname="GV", nickname="vs", title="ascss",
                    company="comp", address="Kzn", homephone="66675666", mobilephone="765756765", workphone="5675",
                    secondaryphone="321123", email="e@m.com"))
    old_contact = app.contact.get_contact_list()
    index = randrange(len(old_contact))
    app.contact.delete_contact_by_index(index)
    assert len(old_contact) - 1 == app.contact.count()
    new_contact = app.contact.get_contact_list()
    old_contact[index:index+1] = []
    assert old_contact == new_contact
