
class Base():
    def __init__(self, driver):
        self.driver = driver

    """Общие локаторы"""

    main_word_login_page = '//div[@class="discount-h"]//span[text()="Ваша скидка"]'
    main_word_registration_page = '//div[@class="col-v5 col-t10 blackBox"]//h2[text()="Оформление"]'



    """"Method get current url"""
    def get_current_url(self):
        get_url = self.driver.current_url
        print('Текущий адрес сайта ' + get_url)


    """"Method value word"""
    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print('Вы корректно перешли на следующий этап')


    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print('Адрес верный')


    def finish_screenshot(self):
        name_screenshot = 'screenshot' + '.png'
        self.driver.get_screenshot_as_file('C:\\Users\\emily\\PycharmProjects\\Final_Project\\screenshots\\' + name_screenshot)
        print('Скриншот успешно сохранен')

