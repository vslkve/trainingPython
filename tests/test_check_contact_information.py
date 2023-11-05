import re
from random import randrange
from model.contact import Contact


# def test_info_of_random_contact_on_homepage(app):
#     contact_list = app.contact.get_contact_list()
#     index = randrange(len(contact_list))
#     contact_from_home_page = app.contact.get_contact_list()[index]
#     contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
#     assert contact_from_home_page.lastname == contact_from_edit_page.lastname
#     assert contact_from_home_page.firstname == contact_from_edit_page.firstname
#     assert contact_from_home_page.address == contact_from_edit_page.address
#     assert contact_from_home_page.all_emails_from_homepage == merge_emails_like_on_homepage(contact_from_edit_page)
#     assert contact_from_home_page.all_phones_from_homepage == merge_phones_like_on_homepage(contact_from_edit_page)

def test_info_of_contacts_on_homepage(app, db):
    contact_list_from_homepage = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    contact_list_from_db = sorted(db.get_contact_list(), key=Contact.id_or_max)
    # print(contact_list_from_homepage)
    # print(contact_list_from_db)
    for i in range(len(contact_list_from_homepage)):
        assert contact_list_from_homepage[i].id == contact_list_from_db[i].id
        assert contact_list_from_homepage[i].lastname == contact_list_from_db[i].lastname
        assert contact_list_from_homepage[i].firstname == contact_list_from_db[i].firstname
        assert contact_list_from_homepage[i].address == contact_list_from_db[i].address
        assert contact_list_from_homepage[i].all_emails_from_homepage == merge_emails_like_on_homepage(contact_list_from_db[i])
        assert contact_list_from_homepage[i].all_phones_from_homepage == merge_phones_like_on_homepage(contact_list_from_db[i])


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_homepage(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None, [contact.homephone, contact.mobilephone,
                                                                 contact.workphone, contact.secondaryphone]))))


def merge_emails_like_on_homepage(contact):
    return "\n".join(filter(lambda x: x != "", [contact.email, contact.email2, contact.email3]))


