from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create_contact(
            Contact("Kat", "Al", "GV", "vs", "ascss", "comp", "Kzn", "hm", "765756765", "5675", "e@m.com"))
    app.contact.delete_first_contact()
