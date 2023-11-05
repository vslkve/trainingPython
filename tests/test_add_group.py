# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app, db, json_groups):
    groups = json_groups
    old_groups = db.get_group_list()
    app.group.create(groups)
    new_groups = db.get_group_list()
    old_groups.append(groups)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


# def test_add_empty_group(app):
#     old_groups = app.group.get_group_list()
#     group = Group("", "", "")
#     app.group.create(group)
#     assert len(old_groups) + 1 == len(app.group.count())
#     new_groups = app.group.get_group_list()
#     old_groups.append(group)
#     assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
