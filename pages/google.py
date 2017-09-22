class Google:
    def __init__(self, driver):
        self.driver = driver
        self.navigation_bar = "lst-ib"
        self.btn_search = "btnK"
        self.btn_luck = "btnI"
        self.url = "https://www.google.com.br"

    def navigate(self):
        self.driver.get(self.url)

    def search(self, text):
        self.driver.find_element_by_id(self.navigation_bar).send_keys(text)
        self.driver.find_element_by_name(self.btn_search).click()

    def search_luck(self, text):
        self.driver.find_element_by_id(self.navigation_bar).send_keys(text)
        self.driver.find_element_by_name(self.btn_luck).click()


class Gmail:
    def __init__ (self, driver):
        self.driver = driver
        self.login = "identifierId"
        self.url = "https://www.gmail.com"
        self.btn_next = "CwaK9"

    def acesso_pagina(self):
        self.driver.get(self.url)

    def execute_login(self, user, passwd):
        self.driver.find_element_by_id(self.login).send_keys(user)
        self.driver.find_element_by_class_name(self.btn_next).click()
        # self.driver.find_element_by_class_name(
        #     "whsOnd zHQkBf").send_keys(passwd)
        # self.driver.find_element_by_class_name(self.btn_next).click()
