from model.contact import Contact
import random


def test_delete_some_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create_contact(
            Contact(firstname="Kat", middlename="Al", lastname="GV", nickname="vs", title="ascss",
                    company="comp", address="Kzn", homephone="66675666", mobilephone="765756765", workphone="5675",
                    secondaryphone="321123", email="e@m.com"))
    old_contact = db.get_contact_list()
    contact = random.choice(old_contact)
    app.contact.delete_contact_by_id(contact.id)
    new_contact = db.get_contact_list()
    old_contact.remove(contact)
    assert old_contact == new_contact
    if check_ui:
        assert sorted(new_contact, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
