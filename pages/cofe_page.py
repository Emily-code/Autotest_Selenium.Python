import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.core import driver
from selenium.webdriver import Keys, ActionChains
from base.base_class import Base

class Cofe_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver



    """Locators"""

    ### Фильтр - бокс
    filter_box_1 = '//div[@class="filterBox filterBox-static coffee"]//span[text()="Яркий эспрессо"]'
    filter_box_2 = '//div[@class="filterBox filterBox-static coffee"]//span[text()="Сбалансированный эспрессо"]'
    filter_box_3 = '//div[@class="filterBox filterBox-static coffee"]//span[text()="Яркий фильтр"]'
    filter_box_4 = '//div[@class="filterBox filterBox-static coffee"]//span[text()="Сбалансированный фильтр"]'
    filter_box_5 = '//div[@class="filterBox filterBox-static coffee"]//span[text()="Капсулы"]'
    filter_box_6 = '//div[@class="filterBox filterBox-static coffee"]//span[text()="Дрип-пакеты"]'
    filter_box_7 = '//div[@class="filterBox filterBox-static coffee"]//span[text()="Кофе в банках"]'
    filter_box_8 = '//div[@class="filterBox filterBox-static coffee"]//span[text()="Наборы"]'
    filter_box_9 = '//div[@class="filterBox filterBox-static coffee"]//span[text()="Кофейный концентрат"]'

    ### Фильтр - dropdown
    dropdown_price = '//button[@title="Цена"]'
    dropdown_type_roast = '//button[@title="Степень обжарки"]'

    ### Фильтр - cсылки
    filter_link_1 = '//div[@class="checkBtn-wrap filter-links"]//a[@data-id="1"]'
    filter_link_2 = '//div[@class="checkBtn-wrap filter-links"]//a[@data-id="2"]'
    filter_link_3 = '//div[@class="checkBtn-wrap filter-links"]//a[@data-id="3"]'
    filter_link_4 = '//div[@class="checkBtn-wrap filter-links"]//a[@data-id="4"]'


    ### Checkbox в выпадающем списке цены
    checkbox_price_height = '//span[contains(text(),"По возрастанию цены")]'
    checkbox_price_low = '//span[contains(text(),"По убыванию цены")]'

    ### Checkbox в выпадающем списке степени прожарки
    checkbox_roast_light = '//span[contains(text(),"Светлая")]'
    checkbox_roast_medium = '//span[contains(text(),"Средняя")]'
    checkbox_roast_dark = '//span[contains(text(),"Тёмная")]'

    ### Сброс фильтров
    button_reset_filters = '//div[@class="resultFilter"]//a[@class="lightBtn"]'

    ### Каталог продуктов
    buy_product_1079 = '//div[@class="card-wrap catalogCard"]//span[@class="buyText buyText_1079"]'
    name_item = '//a[text() = "Christmas Blend 2023"]'

    ### Всплывающее окно корзины
    popup_basket = '//div[@class="popupAdded-wrap"]//a[@class="blackBtn"]'


    """Getters"""

    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word_registration_page)))

    def get_name_item(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.name_item)))


    ### Фильтр - бокс

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

    ### Фильтр - dropdown

    def get_filter_by_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.dropdown_price)))
    def get_filter_by_roast(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.dropdown_type_roast)))

    ### Фильтр - cсылки
    def get_filter_link_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_link_1)))
    def get_filter_link_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_link_2)))
    def get_filter_link_3(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_link_3)))
    def get_filter_link_4(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_link_4)))



    ### Checkbox в выпадающем списке
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

    ### Сброс фильтров
    def get_reset_filters(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_reset_filters)))

    ### Каталог продуктов
    def get_buy_product_1079(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.buy_product_1079)))


    ### Перейти в корзину
    def get_basket_open(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.popup_basket)))



    """Actions"""

    ### Фильтр - бокс

    def click_filter_box_1(self):
        self.get_filter_box_1().click()
        print('Выбран фильтр ' + 'Яркий эспрессо')
    def click_filter_box_2(self):
        self.get_filter_box_2().click()
        print('Выбран фильтр ' + 'Сбалансированный эспрессо')
    def click_filter_box_3(self):
        self.get_filter_box_3().click()
        print('Выбран фильтр ' + 'Яркий фильтр')
    def click_filter_box_4(self):
        self.get_filter_box_4().click()
        print('Выбран фильтр ' + 'Сбалансированный фильтр')
    def click_filter_box_5(self):
        self.get_filter_box_5().click()
        print('Выбран фильтр ' + 'Капсулы')
    def click_filter_box_6(self):
        self.get_filter_box_6().click()
        print('Выбран фильтр ' + 'Дрип-пакеты')
    def click_filter_box_7(self):
        self.get_filter_box_7().click()
        print('Выбран фильтр ' + 'Кофе в банках')
    def click_filter_box_8(self):
        self.get_filter_box_8().click()
        print('Выбран фильтр ' + 'Наборы')
    def click_filter_box_9(self):
        self.get_filter_box_9().click()
        print('Выбран фильтр ' + 'Кофейный концентрат')

    ### Фильтр - dropdown

    def click_filter_price(self):
        self.get_filter_by_price().click()
        print('Фильтр по цене выбран')
    def click_filter_roast(self):
        self.get_filter_by_roast().click()
        print('Фильтр по степени обжарки выбран')


    ### Фильтр - cсылки
    def click_filter_link_1(self):
        self.get_filter_link_1().click()
        print('Фильтр = для Молочных напитков выбран')
    def click_filter_link_2(self):
        self.get_filter_link_2().click()
        print('Фильтр = c Низкой кислотностью выбран')
    def click_filter_link_3(self):
        self.get_filter_link_3().click()
        print('Фильтр = для Кофемашины выбран')
    def click_filter_link_4(self):
        self.get_filter_link_4().click()
        print('Фильтр = Крекий кофе выбран')


    ### Checkbox в выпадающем списке

    def click_checkbox_price_height(self):
        self.get_checkbox_price_height().click()
        print('Выбран фильтр - по возрастанию цены')
    def click_checkbox_price_low(self):
        self.get_checkbox_price_low().click()
        print('Выбран фильтр - по убыванию цены')
    def click_checkbox_roast_light(self):
        self.get_checkbox_roast_light().click()
        print('Выбран фильтр степень обжарки - Светлая')
    def click_checkbox_roast_medium(self):
        self.get_checkbox_roast_medium().click()
        print('Выбран фильтр степень обжарки - Средняя')
    def click_checkbox_roast_dark(self):
        self.get_checkbox_roast_dark().click()
        print('Выбран фильтр степень обжарки - Тёмная')

    ### Сброс фильтров
    def click_reset_filters(self):
        self.get_reset_filters().click()
        print('Сбросить Фильтры - выполнено')

    ### Купить продукт
    def click_buy_product_1079(self):
        self.get_name_item()
        self.value_name_1079 = self.get_name_item().text
        print('Выбран товар ' + self.value_name_1079)
        self.get_buy_product_1079().click()
        print('Продукт отправлен в корзину')

    ### Перейти в Корзину
    def click_open_basket(self):
        self.get_basket_open().click()
        print('Корзина с выбранными продуктами открыта')




    """Methods"""
    ### Фильтр - бокс

    def fb_1(self):
        self.click_filter_box_1()
    def fb_2(self):
        self.click_filter_box_2()
    def fb_3(self):
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

    ### Фильтр - dropdown

    def by_price(self):
        self.click_filter_price()
    def by_roast(self):
        self.click_filter_roast()

    ### Фильтр - cсылки
    def by_filter_link_1(self):
        self.click_filter_link_1()
    def by_filter_link_2(self):
        self.click_filter_link_2()
    def by_filter_link_3(self):
        self.click_filter_link_3()
    def by_filter_link_4(self):
        self.click_filter_link_4()



    ### Checkbox в выпадающем списке
    def by_price_height(self):
        self.click_checkbox_price_height()
    def by_price_low(self):
        self.click_checkbox_price_low()
    def by_roast_light(self):
        self.click_checkbox_roast_light()
    def by_roast_meduim(self):
        self.click_checkbox_roast_medium()
    def by_roast_dark(self):
        self.click_checkbox_roast_dark()


    ### Сброс фильтров
    def reset_filters(self):
        self.click_reset_filters()

    ### Купить продукт
    def buy_button(self):
        self.click_buy_product_1079()

    ### Открыть Корзину
    def basket_open(self):
        self.click_open_basket()
        self.assert_word(self.get_main_word(), 'ОФОРМЛЕНИЕ')






















