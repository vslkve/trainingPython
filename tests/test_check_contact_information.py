import re
from random import randrange


def test_info_of_random_contact_on_homepage(app):
    contact_list = app.contact.get_contact_list()
    index = randrange(len(contact_list))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_emails_from_homepage == merge_emails_like_on_homepage(contact_from_edit_page)
    assert contact_from_home_page.all_phones_from_homepage == merge_phones_like_on_homepage(contact_from_edit_page)


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_homepage(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None, [contact.homephone, contact.mobilephone,
                                                                 contact.workphone, contact.secondaryphone]))))


def merge_emails_like_on_homepage(contact):
    return "\n".join(filter(lambda x: x != "", [contact.email, contact.email2, contact.email3]))

