# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.contact.create_contact(
        Contact("Kat", "Al", "GV", "vs", "ascss", "comp", "Kzn", "hm", "765756765", "5675", "e@m.com"))


def test_add_empty_contact(app):
    app.contact.create_contact(Contact("", "", "", "", "", "", "", "", "", "", ""))

