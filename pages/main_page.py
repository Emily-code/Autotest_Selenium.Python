import time
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.core import driver
from selenium.webdriver import Keys, ActionChains
from base.base_class import Base



class Main_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    """Locators"""

    menu_buy = '//div[@class="wrapMlh "]//a[@class="m-no-link menu__link-h menuAc openMob "]'
    select_cof = '//div[@class="wrapMlh "]//*[text()="Кофе"]'
    select_tea = '//div[@class="wrapMlh "]//*[text()="Чай"]'
    select_accessories = '//div[@class="wrapMlh "]//*[text()="Аксессуары"]'
    select_chocolate = '//div[@class="wrapMlh "]//*[text()="Шоколад"]'
    select_subscription = '//div[@class="wrapMlh "]//*[text()="Подписка на кофе"]'
    select_gift_card = '//div[@class="wrapMlh "]//*[text()="Подарочный сертификат"]'


    """Getters"""

    def get_menu_buy(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.menu_buy)))
    def get_select_cof(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_cof)))
    def get_select_tea(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_tea)))
    def get_select_accessories(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_accessories)))
    def get_select_chocolate(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_chocolate)))
    def get_select_subscription(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_subscription)))
    def get_select_gift_card(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_gift_card)))


    """Actions"""

    def click_menu_buy(self):
        self.get_menu_buy().click()
        print('Menu - Купить is open')
    def click_cof(self):
        self.get_select_cof().click()
        print('Category selected - Кофе')
    def click_tea(self):
        self.get_select_tea().click()
        print('Category selected - Чай')
    def click_accessories(self):
        self.get_select_accessories().click()
        print('Category selected - Акссесуары')
    def click_chocolate(self):
        self.get_select_chocolate().click()
        print('Category selected - Шоколад')
    def click_subscription(self):
        self.get_select_subscription().click()
        print('Category selected - Подписка на кофе')
    def click_gift_card(self):
        self.get_select_gift_card().click()
        print('Category selected - Подарочный сертификат')




    """Methods"""
    def select_menu_buy(self):
        with allure.step('Select Menu Buy'):
            self.click_menu_buy()
    def cof(self):
        with allure.step('Coffe'):
            self.click_cof()
    def tea(self):
        self.click_tea()
    def accessories(self):
        self.click_accessories()
    def chocolate(self):
        self.click_chocolate()
    def subscription(self):
        self.click_subscription()
    def gift_card(self):
        self.click_gift_card()














