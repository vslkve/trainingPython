# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.session.login("admin", "secret")
    app.contact.create_contact(Contact("Kat", "Al", "GV", "vs", "ascss", "comp", "Kzn", "hm", "765756765", "5675", "em@ma.com"))
    app.session.logout()


def test_add_empty_contact(app):
    app.session.login("admin", "secret")
    app.contact.create_contact(Contact("", "", "", "", "", "", "", "", "", "", ""))
    app.session.logout()

