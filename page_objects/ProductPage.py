class ProductPage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "http://192.168.0.104/opencart/admin/index.php?route=catalog/product"

    def go_site(self):
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

    def login(self):
        self.driver.find_element_by_id("input-username").send_keys("admin")
        self.driver.find_element_by_id("input-password").send_keys("admin")
        self.driver.find_element_by_tag_name("button").click()

    def list(self):
        lenq = len(self.driver.find_elements_by_xpath(self.LIST))
        return lenq

    def add(self):
        self.driver.find_element_by_xpath(self.ADD).click()

    def add_product_name(self):
        self.driver.find_element_by_css_selector(self.PRODUCT_NAME).send_keys(self.NAME)

    def add_meta_name(self):
        self.driver.find_element_by_css_selector(self.META_NAME).send_keys(self.NAME)

    def data_page(self):
        self.driver.find_element_by_xpath(self.DATA_PAGE).click()

    def add_model(self):
        self.driver.find_element_by_css_selector(self.MODEL_NAME).send_keys(self.MODEL)

    def add_device(self):
        self.driver.find_element_by_css_selector(self.ADD_DEVICE).click()

    def element(self):
        name = self.driver.find_element_by_xpath(self.ELEMENT).text
        return name

    def edit_product(self):
        self.driver.find_element_by_xpath(self.EDIT).click()

    def add_new_name(self):
        self.driver.find_element_by_css_selector(self.PRODUCT_NAME).send_keys(self.NEW_NAME)

    def checkbox(self):
        self.driver.find_element_by_xpath(self.CHECKBOX).click()

    def delete(self):
        self.driver.find_element_by_xpath(self.DELETE).click()
