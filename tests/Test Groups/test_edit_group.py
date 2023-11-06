from model.group import Group
import random


def test_edit_group_name_by_id(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group("fsdfsf", "dfsfs", "fsdfs"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    group.name = "New group"
    app.group.edit_group_by_id(group.id, group)
    new_groups = db.get_group_list()
    for i in (0, len(old_groups) - 1):
        if old_groups[i].id == group.id:
            old_groups[i].name = "New group"
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
