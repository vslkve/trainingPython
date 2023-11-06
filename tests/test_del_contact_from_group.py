from model.contact import Contact
from model.group import Group
import random


def test_delete_some_contact_from_group(app, orm):
    # проверка, что существует контакт
    if len(orm.get_contact_list()) == 0:
        app.contact.create_contact(
            Contact(firstname="Kat", middlename="Al", lastname="GV", nickname="vs", title="ascss",
                    company="comp", address="Kzn", homephone="66675666", mobilephone="765756765", workphone="5675",
                    secondaryphone="321123", email="e@m.com"))

    # проверка, что существует группа
    if len(orm.get_group_list()) == 0:
        app.group.create(Group("fsdfsf", "dfsfs", "fsdfs"))

    # получаем списки
    groups = orm.get_group_list()
    contacts = orm.get_contact_list()
    group = random.choice(groups)
    contact = random.choice(contacts)

    # проверка, что выбранный контакт присутсвует в группе
    if contact in orm.get_contacts_not_in_group(group):
        app.contact.add_contact_to_group_by_id(contact.id, group.id)

    app.contact.delete_contact_from_group_by_id(contact.id, group.id)
    assert contact in orm.get_contacts_not_in_group(group)
