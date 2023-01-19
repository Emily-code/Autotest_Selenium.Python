import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.core import driver
from selenium.webdriver import Keys, ActionChains
from base.base_class import Base
import allure
class Cofe_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver



    """Locators"""

    ### Filter - BOX
    filter_box_1 = '//div[@class="filterBox filterBox-static coffee"]//span[text()="Яркий эспрессо"]'
    filter_box_2 = '//div[@class="filterBox filterBox-static coffee"]//span[text()="Сбалансированный эспрессо"]'
    filter_box_3 = '//div[@class="filterBox filterBox-static coffee"]//span[text()="Яркий фильтр"]'
    filter_box_4 = '//div[@class="filterBox filterBox-static coffee"]//span[text()="Сбалансированный фильтр"]'
    filter_box_5 = '//div[@class="filterBox filterBox-static coffee"]//span[text()="Капсулы"]'
    filter_box_6 = '//div[@class="filterBox filterBox-static coffee"]//span[text()="Дрип-пакеты"]'
    filter_box_7 = '//div[@class="filterBox filterBox-static coffee"]//span[text()="Кофе в банках"]'
    filter_box_8 = '//div[@class="filterBox filterBox-static coffee"]//span[text()="Наборы"]'
    filter_box_9 = '//div[@class="filterBox filterBox-static coffee"]//span[text()="Кофейный концентрат"]'

    ### Filter - DROPDOWN
    dropdown_price = '//button[@title="Цена"]'
    dropdown_type_roast = '//button[@title="Степень обжарки"]'

    ### Filter - LINKS
    filter_link_1 = '//div[@class="checkBtn-wrap filter-links"]//a[@data-id="1"]'
    filter_link_2 = '//div[@class="checkBtn-wrap filter-links"]//a[@data-id="2"]'
    filter_link_3 = '//div[@class="checkBtn-wrap filter-links"]//a[@data-id="3"]'
    filter_link_4 = '//div[@class="checkBtn-wrap filter-links"]//a[@data-id="4"]'


    ### Checkbox in the price drop down list
    checkbox_price_height = '//span[contains(text(),"По возрастанию цены")]'
    checkbox_price_low = '//span[contains(text(),"По убыванию цены")]'

    ### Checkbox in the drop-down list of roasting
    checkbox_roast_light = '//span[contains(text(),"Светлая")]'
    checkbox_roast_medium = '//span[contains(text(),"Средняя")]'
    checkbox_roast_dark = '//span[contains(text(),"Тёмная")]'

    ### Reset filters
    button_reset_filters = '//div[@class="resultFilter"]//a[@class="lightBtn"]'

    ### Product catalog
    buy_product_1079 = '//div[@class="card-wrap catalogCard"]//span[@class="buyText buyText_1079"]'
    buy_product_54 = '//div[@class="card-wrap catalogCard"]//span[@class="buyText buyText_54"]'
    name_item_1079 = '//a[text() = "Christmas Blend 2023"]'
    name_item_54 = '//a[text() = "Колумбия Декаф"]'

    ### Cart Popup
    popup_basket = '//div[@class="popupAdded-wrap"]//a[@class="blackBtn"]'


    """Getters"""

    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word_registration_page)))

    def get_name_item_1079(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.name_item_1079)))

    def get_name_item_54(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.name_item_54)))


    ### Filter - BOX

    def get_filter_box_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_box_1)))
    def get_filter_box_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_box_2)))
    def get_filter_box_3(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_box_3)))
    def get_filter_box_4(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_box_4)))
    def get_filter_box_5(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_box_5)))
    def get_filter_box_6(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_box_6)))
    def get_filter_box_7(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_box_7)))
    def get_filter_box_8(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_box_8)))
    def get_filter_box_9(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_box_9)))

    ### Filter - DROPDOWN

    def get_filter_by_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.dropdown_price)))
    def get_filter_by_roast(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.dropdown_type_roast)))

    ### Filter - LINKS
    def get_filter_link_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_link_1)))
    def get_filter_link_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_link_2)))
    def get_filter_link_3(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_link_3)))
    def get_filter_link_4(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_link_4)))



    ### Checkbox in the drop down list
    def get_checkbox_price_height(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkbox_price_height)))
    def get_checkbox_price_low(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkbox_price_low)))
    def get_checkbox_roast_light(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkbox_roast_light)))
    def get_checkbox_roast_medium(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkbox_roast_medium)))
    def get_checkbox_roast_dark(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkbox_roast_dark)))

    ### Reset filters
    def get_reset_filters(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_reset_filters)))

    ### Product catalog
    def get_buy_product_1079(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.buy_product_1079)))
    def get_buy_product_54(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.buy_product_54)))


    ### Go to cart
    def get_basket_open(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.popup_basket)))



    """Actions"""


    ### Filter - BOX

    def click_filter_box_1(self):
        self.get_filter_box_1().click()
        print('Selected filter ' + 'Яркий эспрессо')
    def click_filter_box_2(self):
        self.get_filter_box_2().click()
        print('Selected filter ' + 'Сбалансированный эспрессо')
    def click_filter_box_3(self):
        self.get_filter_box_3().click()
        print('Selected filter ' + 'Яркий фильтр')
    def click_filter_box_4(self):
        self.get_filter_box_4().click()
        print('Selected filter ' + 'Сбалансированный фильтр')
    def click_filter_box_5(self):
        self.get_filter_box_5().click()
        print('Selected filter ' + 'Капсулы')
    def click_filter_box_6(self):
        self.get_filter_box_6().click()
        print('Selected filter ' + 'Дрип-пакеты')
    def click_filter_box_7(self):
        self.get_filter_box_7().click()
        print('Selected filter ' + 'Кофе в банках')
    def click_filter_box_8(self):
        self.get_filter_box_8().click()
        print('Selected filter ' + 'Наборы')
    def click_filter_box_9(self):
        self.get_filter_box_9().click()
        print('Selected filter ' + 'Кофейный концентрат')

    ### Filter - DROPDOWN

    def click_filter_price(self):
        with allure.step('Click filter price'):
            self.get_filter_by_price().click()
            print('Price filter selected')
    def click_filter_roast(self):
        self.get_filter_by_roast().click()
        print('Roast filter selected')


    ### Filter - LINKS
    def click_filter_link_1(self):
        self.get_filter_link_1().click()
        print('Filter = для Молочных напитков selected')
    def click_filter_link_2(self):
        self.get_filter_link_2().click()
        print('Filter = c Низкой кислотностью selected')
    def click_filter_link_3(self):
        with allure.step('Click filter link 3'):
            self.get_filter_link_3().click()
            print('Filter = для Кофемашины selected')
            time.sleep(5)
    def click_filter_link_4(self):
        self.get_filter_link_4().click()
        print('Filter = Крекий кофе selected')


    ### Checkbox in the drop down list

    def click_checkbox_price_height(self):
        self.get_checkbox_price_height().click()
        print('Selected filter - по возрастанию цены')
    def click_checkbox_price_low(self):
        self.get_checkbox_price_low().click()
        print('Selected filter - по убыванию цены')
    def click_checkbox_roast_light(self):
        self.get_checkbox_roast_light().click()
        print('Roast filter selected - Светлая')
    def click_checkbox_roast_medium(self):
        self.get_checkbox_roast_medium().click()
        print('Roast filter selected - Средняя')
    def click_checkbox_roast_dark(self):
        self.get_checkbox_roast_dark().click()
        print('Roast filter selected - Тёмная')

    ### Reset Filters
    def click_reset_filters(self):
        self.get_reset_filters().click()
        print('Reset Filters - Done')

    ### Buy product
    def click_buy_product_1079(self):
        with allure.step('Click buy product 1079'):
            self.get_name_item_1079()
            self.value_name_1079 = self.get_name_item_1079().text
            print('Selected item ' + self.value_name_1079)
            self.get_buy_product_1079().click()
            print('Product sent to cart')

    def click_buy_product_54(self):
        with allure.step('Click buy product 54'):
            self.get_name_item_54()
            self.value_name_54 = self.get_name_item_54().text
            print('Selected item ' + self.value_name_54)
            self.get_buy_product_54().click()
            print('Product sent to cart')


    ### Go to Cart
    def click_open_basket(self):
        self.get_basket_open().click()
        print('Shopping cart with selected products is open')



    """Methods"""
    ### Filter - BOX

    def fb_1(self):
        self.click_filter_box_1()
    def fb_2(self):
        self.click_filter_box_2()
    def fb_3(self):
        with allure.step('Fb3'):
            self.click_filter_box_3()
    def fb_4(self):
        self.click_filter_box_4()
    def fb_5(self):
        self.click_filter_box_5()
    def fb_6(self):
        self.click_filter_box_6()
    def fb_7(self):
        self.click_filter_box_7()
    def fb_8(self):
        self.click_filter_box_8()
    def fb_9(self):
        self.click_filter_box_9()

    ### Filter - dropdown

    def by_price(self):
        self.click_filter_price()
    def by_roast(self):
        with allure.step('By roast'):
            self.click_filter_roast()

    ### Filter - cсылки
    def by_filter_link_1(self):
        self.click_filter_link_1()
    def by_filter_link_2(self):
        self.click_filter_link_2()
    def by_filter_link_3(self):
        self.click_filter_link_3()
    def by_filter_link_4(self):
        self.click_filter_link_4()



    ### Checkbox in the drop down list
    def by_price_height(self):
        with allure.step('By price height'):
            self.click_checkbox_price_height()
    def by_price_low(self):
        self.click_checkbox_price_low()
    def by_roast_light(self):
        self.click_checkbox_roast_light()
    def by_roast_meduim(self):
        with allure.step('By roast meduim'):
            self.click_checkbox_roast_medium()
    def by_roast_dark(self):
        self.click_checkbox_roast_dark()


    ### Reset filters
    def reset_filters(self):
        self.click_reset_filters()

    ### Buy product
    def buy_button_1079(self):
        self.click_buy_product_1079()

    def buy_button_54(self):
        self.click_buy_product_54()



    ### Open Cart
    def basket_open(self):
        with allure.step('Basket open'):
            self.click_open_basket()
            self.assert_word(self.get_main_word(), 'ОФОРМЛЕНИЕ')























