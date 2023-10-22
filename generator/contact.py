import random
import string
from model.contact import Contact
import jsonpickle
import os.path
import getopt
import sys
import random
import string
import re


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contact", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    pattern = r'[`\\/\"<\'>]'
    symbols = string.ascii_letters + string.digits + re.sub(pattern, "", string.punctuation) + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_phone(prefix, maxlen):
    pattern = r'[`\\/\"<\'>]'
    symbols = string.digits + re.sub(pattern, "", string.punctuation) + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname="", middlename="", lastname="", nickname="",
                    address="", homephone="", email="")] + [
    Contact(firstname=random_string("firstname", 15), middlename=random_string("middlename", 15),
            lastname=random_string("lastname", 20), nickname=random_string("nickname", 20),
            address=random_string("address", 20), homephone=random_phone("111", 10),
            mobilephone=random_phone("222", 10), email=random_string("email", 15),
            email2=random_string("email2", 15))
    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
