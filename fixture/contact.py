from selenium.webdriver.common.by import By
from model.contact import Contact
import time
import re


class ContactHelper:

    def __init__(self, app):
        self.app = app

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            time.sleep(1)
            self.open_contact_page()
            self.contact_cache = []
            for element in wd.find_elements(By.NAME, "entry"):
                dom = element.find_elements(By.TAG_NAME, "td")
                lastname = dom[1].text
                firstname = dom[2].text
                id = dom[0].find_element(By.TAG_NAME, "input").get_attribute("value")
                all_phones = dom[5].text
                address = dom[3].text
                all_emails = dom[4].text
                self.contact_cache.append(Contact(lastname=lastname, firstname=firstname, id=id,
                                                  all_phones_from_homepage=all_phones, address=address,
                                                  all_emails_from_homepage=all_emails))
        return list(self.contact_cache)

    def add_contact_to_group_by_id(self, contact, group):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_id(contact)
        wd.find_element(By.NAME, "to_group").click()
        wd.find_element(By.XPATH, "//div[@id='content']/form[2]/div[4]/select/option[@value='%s']" % group).click()
        wd.find_element(By.NAME, "add").click()
        # переходим на страницу контактов, которые относятся к выбранно группе
        wd.find_element(By.XPATH, "//i/a").click()
        self.contact_cache = None

    def delete_contact_from_group_by_id(self, contact, group):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element(By.NAME, "group").click()
        wd.find_element(By.XPATH, "//option[@value='%s']" % group).click()
        self.select_contact_by_id(contact)
        wd.find_element(By.NAME, "remove").click()
        # переходим на страницу контактов, которые относятся к выбранно группе
        wd.find_element(By.XPATH, "//i/a").click()
        self.contact_cache = None

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element(By.NAME, "firstname").get_attribute("value")
        lastname = wd.find_element(By.NAME, "lastname").get_attribute("value")
        id = wd.find_element(By.NAME, "id").get_attribute("value")
        homephone = wd.find_element(By.NAME, "home").get_attribute("value")
        mobilephone = wd.find_element(By.NAME, "mobile").get_attribute("value")
        workphone = wd.find_element(By.NAME, "work").get_attribute("value")
        secondaryphone = wd.find_element(By.NAME, "phone2").get_attribute("value")
        address = wd.find_element(By.NAME, "address").text
        email1 = wd.find_element(By.NAME, "email").get_attribute("value")
        email2 = wd.find_element(By.NAME, "email2").get_attribute("value")
        email3 = wd.find_element(By.NAME, "email3").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id, homephone=homephone, mobilephone=mobilephone,
                       workphone=workphone, secondaryphone=secondaryphone, address=address,
                       email=email1, email2=email2, email3=email3)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element(By.ID, "content").text
        homephone = re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        secondaryphone = re.search("P: (.*)", text).group(1)
        return Contact(homephone=homephone, mobilephone=mobilephone,
                       workphone=workphone, secondaryphone=secondaryphone)

    def count(self):
        wd = self.app.wd
        self.open_contact_page()
        return len(wd.find_elements(By.NAME, 'selected[]'))

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "home page").click()

    def delete_first_contact(self):
        wd = self.app.wd
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_contact_page()
        # select contact by index
        wd.find_elements(By.NAME, "selected[]")[index].click()
        wd.find_element(By.XPATH, "//input[@value='Delete']").click()
        # confirm_deletion
        wd.switch_to.alert.accept()
        self.open_contact_page()
        time.sleep(1)
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.open_contact_page()
        # select contact by index
        self.select_contact_by_id(id)
        wd.find_element(By.XPATH, "//input[@value='Delete']").click()
        # confirm_deletion
        wd.switch_to.alert.accept()
        self.open_contact_page()
        time.sleep(1)
        self.contact_cache = None

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element(By.CSS_SELECTOR, "input[value='%s']" % id).click()

    def edit_contact_by_index(self, index, contact):
        wd = self.app.wd
        self.open_contact_page()
        # select contact by index
        self.open_contact_to_edit_by_index(index)
        self.fill_contact_form(contact)
        # submit_contact_edition
        wd.find_element(By.XPATH, "//div[@id='content']/form/input[22]").click()
        self.return_to_home_page()
        self.contact_cache = None

    def edit_contact_by_id(self, id, contact):
        wd = self.app.wd
        self.open_contact_page()
        self.open_contact_to_edit_by_id(id)
        self.fill_contact_form(contact)
        # submit_contact_edition
        wd.find_element(By.XPATH, "//div[@id='content']/form/input[22]").click()
        self.return_to_home_page()
        self.contact_cache = None

    def create_contact(self, contact):
        wd = self.app.wd
        self.open_contact_page()
        # init_contact_creation
        wd.find_element(By.LINK_TEXT, "add new").click()
        # fill_contact_form
        self.fill_contact_form(contact)
        # submit_contact_creation
        wd.find_element(By.XPATH, "//div[@id='content']/form/input[21]").click()
        self.return_to_home_page()
        self.contact_cache = None

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.open_contact_page()
        row = wd.find_elements(By.NAME, "entry")[index]
        dom = row.find_elements(By.TAG_NAME, "td")[6]
        dom.find_element(By.TAG_NAME, "a").click()

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.open_contact_page()
        wd.find_elements(By.XPATH, "//img[@alt='Edit']")[index].click()

    def open_contact_to_edit_by_id(self, id):
        wd = self.app.wd
        wd.find_element(By.CSS_SELECTOR, "a[href='edit.php?id=%s']" % id).click()

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.homephone)
        self.change_field_value("mobile", contact.mobilephone)
        self.change_field_value("work", contact.workphone)
        self.change_field_value("phone2", contact.secondaryphone)
        self.change_field_value("email", contact.email)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element(By.NAME, field_name).click()
            wd.find_element(By.NAME, field_name).clear()
            wd.find_element(By.NAME, field_name).send_keys(text)

    def open_contact_page(self):
        wd = self.app.wd
        if wd.current_url.endswith("/addressbook/"):
            return
        wd.find_element(By.LINK_TEXT, "home").click()
