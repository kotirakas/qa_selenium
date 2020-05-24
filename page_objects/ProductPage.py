import allure
import os
import time
from selenium.webdriver.common.alert import Alert

class ProductPage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "http://192.168.0.102/opencart/admin/index.php?route=catalog/product"

    def go_site(self):
        with allure.step(F"перехожу на адрес {self.base_url}"):
            return self.driver.get(self.base_url)

    ELEMENT = "//*[@id='form-product']/div/table/tbody/tr[4]/td[3]"
    ADD = " //*[@id='content']/div[1]/div/div/a"
    PRODUCT_NAME = "input#input-name1"
    NAME = "test_device2"
    META_NAME = "input#input-meta-title1"
    DATA_PAGE = "//*[@id='form-product']/ul/li[2]/a"
    MODEL = "TEST MODEL2"
    MODEL_NAME = "input#input-model"
    ADD_DEVICE = "button[type='submit']"
    LIST = "//*[@id='form-product']/div/table/tbody/tr/td[3]"
    EDIT = "//*[@id='form-product']/div/table/tbody/tr[4]/td[8]"
    NEW_NAME = "111"
    CHECKBOX = "//*[@id='form-product']/div/table/tbody/tr[20]/td[1]"
    DELETE = "//*[@id='content']/div[1]/div/div/button[3]"
    IMAGE_PAGE = "//*[@id='form-product']/ul/li[9]/a"
    LOGO_ICON = "a#thumb-image"
    LOGO_EDIT_BUTTON ="button#button-image"
    BUTTON_UPLOAD = "#button-upload"
    LOGO_UPLOAD_BUTTON = "input[type='file']"
    ADD_LOGO = "//*[@id='filemanager']/div/div[2]/div[2]/div[3]//img"


    def login(self):
        with allure.step("Произвожу логин на страницу каталога"):
            self.driver.find_element_by_id("input-username").send_keys("admin")
            self.driver.find_element_by_id("input-password").send_keys("admin")
            self.driver.find_element_by_tag_name("button").click()

    def list(self):
        with allure.step("Получаю данные по списку устройств"):
            lenq = len(self.driver.find_elements_by_xpath(self.LIST))
            return lenq

    def add(self):
        with allure.step("Нажимаю на кнопку Добавить"):
            self.driver.find_element_by_xpath(self.ADD).click()

    def add_product_name(self):
        with allure.step("Ввожу название продукта"):
            self.driver.find_element_by_css_selector(self.PRODUCT_NAME).send_keys(self.NAME)

    def add_meta_name(self):
        with allure.step("Ввожу метаданные"):
            self.driver.find_element_by_css_selector(self.META_NAME).send_keys(self.NAME)

    def data_page(self):
        with allure.step("Перехожу на вкладку Дата"):
            self.driver.find_element_by_xpath(self.DATA_PAGE).click()

    def add_model(self):
        with allure.step("ввожу название модели"):
            self.driver.find_element_by_css_selector(self.MODEL_NAME).send_keys(self.MODEL)

    def add_device(self):
        with allure.step("Нажимаю кнопку Добавить устройство"):
            self.driver.find_element_by_css_selector(self.ADD_DEVICE).click()

    def element(self):
        with allure.step("Получаю название элемента"):
            name = self.driver.find_element_by_xpath(self.ELEMENT).text
            return name

    def edit_product(self):
        with allure.step("Нажимаю кнопку редактировать"):
            self.driver.find_element_by_xpath(self.EDIT).click()

    def add_new_name(self):
        with allure.step("ввожу новое название продукта"):
            self.driver.find_element_by_css_selector(self.PRODUCT_NAME).send_keys(self.NEW_NAME)

    def checkbox(self):
        with allure.step("кликаю на чекбокс"):
            self.driver.find_element_by_xpath(self.CHECKBOX).click()

    def delete(self):
        with allure.step("удаляю элемент"):
            self.driver.find_element_by_xpath(self.DELETE).click()

    def image_page(self):
        with allure.step("Перехожу на страницу с логотипами"):
            self.driver.find_element_by_xpath(self.IMAGE_PAGE).click()

    def logo_edit(self):
        with allure.step("вызываю окно доступных лого"):
            self.driver.find_element_by_css_selector(self.LOGO_ICON).click()
            self.driver.find_element_by_css_selector(self.LOGO_EDIT_BUTTON).click()

    def logo_download(self):
        with allure.step("произвожу загрузку нового логотипа"):
            dirname = os.path.dirname(os.path.abspath(__file__))
            filename = os.path.join(dirname, 'fotos.png')
            self.driver.execute_script("$('#button-upload').click()")
            time.sleep(3)
            self.driver.find_element_by_css_selector(self.LOGO_UPLOAD_BUTTON).send_keys(filename)
            time.sleep(3)
            Alert(self.driver).accept()

    def add_logo(self):
        with allure.step("добавляю новы логотип к продукту"):
            self.driver.find_element_by_xpath(self.ADD_LOGO).click()

