import time
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base



class Basket_page(Base):
    url = 'https://shop.tastycoffee.ru/'
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    """Locators"""
    item_name = '//p[@class="goods__name"]//a[text()="Christmas Blend 2023"]'


    """Getters"""
    def get_item_from_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.item_name)))



    """Actions"""
    def value(self):
        self.value_name_item_from_cart = self.get_item_from_cart().text
        assert self.value_name_item_from_cart == 'Christmas Blend 2023'
        print('Товар в заказе соотвествует выбранному артикулу ' + self.value_name_item_from_cart)


    """Methods"""
    def assert_order(self):
        self.value()













