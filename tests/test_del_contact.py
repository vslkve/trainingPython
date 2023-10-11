from model.contact import Contact
from random import randrange
import time


def test_delete_some_contact(app):
    if app.contact.count() == 0:
        app.contact.create_contact(
            Contact("Kat", "Al", "GV", "vs", "ascss", "comp", "Kzn", "hm", "765756765", "5675", "e@m.com"))
    old_contact = app.contact.get_contact_list()
    index = randrange(len(old_contact))
    app.contact.delete_contact_by_index(index)
    assert len(old_contact) - 1 == app.contact.count()
    new_contact = app.contact.get_contact_list()
    old_contact[index:index+1] = []
    assert old_contact == new_contact
