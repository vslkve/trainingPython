# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.login("admin", "secret")
    app.create_group(Group("fsdfsf", "dfsfs", "fsdfs"))
    app.logout()


def test_add_empty_group(app):
    app.login("admin", "secret")
    app.create_group(Group("", "", ""))
    app.logout()

