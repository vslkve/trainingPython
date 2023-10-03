from selenium.webdriver.common.by import By


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "home page").click()

    def delete_first_contact(self):
        wd = self.app.wd
        self.open_contact_page()
        wd.find_element(By.NAME, 'selected[]').click()
        wd.find_element(By.XPATH, "//input[@value='Delete']").click()
        # confirm_deletion
        wd.switch_to.alert.accept()
        self.open_contact_page()

    def edit_first_contact(self, contact):
        wd = self.app.wd
        self.open_contact_page()
        # init_contact_edition
        wd.find_element(By.XPATH, "//img[@alt='Edit']").click()
        self.fill_contact_form(contact)
        # submit_contact_edition
        wd.find_element(By.XPATH, "//div[@id='content']/form/input[22]").click()
        self.return_to_home_page()

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

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.home)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("work", contact.work)
        self.change_field_value("email", contact.email)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element(By.NAME, field_name).click()
            wd.find_element(By.NAME, field_name).clear()
            wd.find_element(By.NAME, field_name).send_keys(text)

    def open_contact_page(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "home").click()
