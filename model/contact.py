from sys import maxsize


class Contact:

    def __init__(self, firstname=None, middlename=None, lastname=None, id=None, nickname=None, title=None, company=None,
                 address=None, homephone=None, mobilephone=None, workphone=None, secondaryphone=None, email=None,
                 all_phones_from_homepage=None):
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
        self.id = id
        self.all_phones_from_homepage = all_phones_from_homepage

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.lastname, self.firstname)

    def __eq__(self, other):
        return ((self.id is None or other.id is None or self.id == other.id) and
                self.lastname == other.lastname and self.firstname == other.firstname)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

