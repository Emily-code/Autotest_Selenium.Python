import time

from selenium import webdriver

from pages.basket_page import Basket_page
from pages.cofe_page import Cofe_page
from pages.final_page import Finish_page
from pages.login_page import Login_page
from pages.main_page import Main_page

"""Тест покупки товара"""

def test_buy_item(set_group):
    driver = webdriver.Firefox(executable_path='C:\\Users\\emily\\PycharmProjects\\resource\\geckodriver.exe')
    print('Start Test')

    login = Login_page(driver)
    login.authorization()


    mp = Main_page(driver)
    mp.select_menu_buy()
    mp.cof()

    cp = Cofe_page(driver)
    cp.fb_3()
    cp.click_filter_price()
    cp.by_price_height()
    cp.click_filter_link_3()
    cp.by_roast()
    cp.by_roast_meduim()
    cp.click_buy_product_1079()
    cp.basket_open()

    bp = Basket_page(driver)
    bp.assert_order()

    fp = Finish_page(driver)
    fp.finish()

    print('Оформление заказа почти закончено, осталось ввести данные вашей карты')
    time.sleep(5)
    driver.quit()











