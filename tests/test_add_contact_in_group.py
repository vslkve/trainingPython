from model.contact import Contact
from model.group import Group
import random


def test_add_some_contact_in_group(app, orm):
    # проверка, что существует группа
    if len(orm.get_group_list()) == 0:
        app.group.create(Group("fsdfsf", "dfsfs", "fsdfs"))

    # получаем список групп
    groups = orm.get_group_list()
    group = random.choice(groups)

    # проверяем, существуют ли контакты, не принадлежащие выбранной группе
    if len(orm.get_contacts_not_in_group(group)) == 0:
        app.contact.create_contact(
            Contact(firstname="Kat", middlename="Al", address="Kzn", homephone="66675666", email="e@m.com"))

    # получаем список контактов, которые отсуствуют в выбранной группе
    contacts = orm.get_contacts_not_in_group(group)
    contact = random.choice(contacts)

    app.contact.add_contact_to_group_by_id(contact.id, group.id)
    assert contact in orm.get_contacts_in_group(group)
