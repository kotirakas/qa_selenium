from selenium.webdriver.common.alert import Alert
from page_objects import ProductPage
import time
import allure
import mysql.connector

connection = mysql.connector.connect(user='ocuser', password='PASSWORD', host='192.168.0.104', port='3306')
cursor = connection.cursor()
cursor.execute("USE opencart")


def test_add(browser):
    ProductPage(browser).go_site()
    ProductPage(browser).login()
    before = ProductPage(browser).list()
    ProductPage(browser).add()
    ProductPage(browser).add_product_name()
    ProductPage(browser).add_meta_name()
    ProductPage(browser).data_page()
    ProductPage(browser).add_model()
    ProductPage(browser).image_page()
    ProductPage(browser).logo_edit()
    time.sleep(5)
    ProductPage(browser).logo_download()
    time.sleep(5)
    ProductPage(browser).add_logo()
    ProductPage(browser).add_device()
    time.sleep(3)
    after = ProductPage(browser).list()
    with allure.step("сравниваю количество продуктов на странице"):
        assert after == before + 1
    browser.close()
    cursor.execute("SELECT * FROM oc_product_description where name='test_device2'")
    result = cursor.fetchall()
    for row in result:
        if row[2] == 'test_device2':
            print("Устройство добавлено в БД")
        else:
            print("Устройства в БД нет")


def test_change(browser):
    ProductPage(browser).go_site()
    ProductPage(browser).login()
    before = ProductPage(browser).element()
    ProductPage(browser).edit_product()
    ProductPage(browser).add_new_name()
    ProductPage(browser).add_device()
    after = ProductPage(browser).element()
    with allure.step("сравниваю название продукта до и после изменения"):
        assert before != after
    browser.close()
    cursor.execute("SELECT * FROM oc_product_description where name='test_device2'")
    for row in cursor.fetchall():
        if row[2] != 'HTC Touch HD':
            print("Название устройства изменено")
        else:
            print("Название устройства не изменено")


def test_delete(browser):
    ProductPage(browser).go_site()
    ProductPage(browser).login()
    before = ProductPage(browser).list()
    ProductPage(browser).checkbox()
    ProductPage(browser).delete()
    Alert(browser).accept()
    time.sleep(3)
    after = ProductPage(browser).list()
    assert after == before - 1
    browser.close()
    cursor.execute("SELECT * FROM oc_product_description where name='test_device2'")
    result = cursor.fetchall()
    if result == []:
        print("Устройство удалено в БД")
    else:
        print("Устройств не удалено из БД ")

    cursor.close()
    connection.close()
