import time

import allure
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base



class Login_page(Base):
    url = 'https://shop.tastycoffee.ru/'
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    """Locators"""
    login_registration = '//button[@class="greyLink enterOpen"]'
    login_name = '//input[@id="email"]'
    password = '//input[@id="password"]'
    button_log = '//input[@id="sign-in"]'


    """Getters"""
    def get_button_login_registration(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_registration)))
    def get_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_name)))
    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))
    def get_button_log(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_log)))
    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word_login_page)))


    """Actions"""
    def click_button_button_login_registration(self):
        self.get_button_login_registration().click()
        print('Login to your personal account')
    def input_login_name(self, login_name):
        self.get_name().send_keys(login_name)
        print('Enter login')
    def input_password(self, password):
        self.get_password().send_keys(password)
        print('Enter password')
    def click_log(self):
        self.get_button_log().click()
        print('You are logged in')


    """Methods"""
    def authorization(self):
        with allure.step('Authorization'):
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.get_current_url()
            self.click_button_button_login_registration()
            self.input_login_name('emy.vi@mail.ru')
            self.input_password('test1234')
            self.click_log()
            self.assert_word(self.get_main_word(), 'Ваша скидка')












