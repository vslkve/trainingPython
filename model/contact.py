from sys import maxsize


class Contact:

    def __init__(self, firstname=None, middlename=None, lastname=None, id=None, nickname=None, title=None, company=None,
                 address=None, homephone=None, mobilephone=None, workphone=None, secondaryphone=None, email=None,
                 email2=None, email3=None, all_phones_from_homepage=None, all_emails_from_homepage=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.secondaryphone = secondaryphone
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.id = id
        self.all_phones_from_homepage = all_phones_from_homepage
        self.all_emails_from_homepage = all_emails_from_homepage

    def __repr__(self):
        return "%s:%s:%s:%s" % (self.id, self.lastname, self.firstname, self.address)

    def __eq__(self, other):
        return ((self.id is None or other.id is None or self.id == other.id) and
                self.lastname == other.lastname and self.firstname == other.firstname and self.address == other.address,
                self.homephone == other.homephone, self.workphone == other.workphone,
                self.mobilephone == other.mobilephone, self.secondaryphone == other.secondaryphone,
                self.email == other.email, self.email2 == other.email2, self.email3 == other.email3)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

