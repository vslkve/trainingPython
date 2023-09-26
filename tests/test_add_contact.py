# -*- coding: utf-8 -*-
from model.contact import Contact
from fixture.application import Application
import pytest


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.login("admin", "secret")
    app.create_contact(Contact("Kat", "Al", "GV", "vs", "ascss", "comp", "Kzn", "hm", "765756765", "5675", "em@ma.com"))
    app.logout()


def test_add_empty_contact(app):
    app.login("admin", "secret")
    app.create_contact(Contact("", "", "", "", "", "", "", "", "", "", ""))
    app.logout()

