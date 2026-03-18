from selenium.webdriver.common.by import By
from helpers import retrieve_phone_code
import data
import time

class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    taxi_button = (By.XPATH, '//div[@class="results-text"]//button[@class="button round"]')
    comfort_tariff = (By.XPATH, "//div[contains(text(), 'Comfort')]")
    phone_button = (By.CLASS_NAME, 'np-button')
    input_phone = (By.XPATH, "//input[@id='phone']")
    button_next_phone = (By.XPATH, "//button[contains(text(), 'Siguiente')]")
    input_phone_code = (By.XPATH, "//div[@class='input-container']//input[@id='code']")
    confirm_code_button = (By.XPATH, "//button[contains(text(), 'Confirmar')]")
    payment_button = (By.XPATH, "//div[@class='pp-button filled']//div[@class='pp-value']")
    payment_window = (By.CLASS_NAME, 'section active')
    add_card_button = (By.XPATH, "//div[@class='pp-row disabled']//div[@class='pp-checkbox']")
    input_card_number = (By.XPATH, "//div[@class='card-number-input']//input[@id='number']")
    input_card_code = (By.XPATH, "//div[@class='card-code']//div[@class='card-code-input']//input[@id='code']")
    plc_div = (By.XPATH, "//div[@class='plc']")
    finish_add_card = (By.XPATH, "//div[@class='pp-buttons']//button[@class='button full']")
    button_close_payment = (By.XPATH, "//div[@class='payment-picker open']//div[@class='modal']//div[@class='section active']//button[@class='close-button section-close']")
    click_to_send_message = (By.XPATH, "//div[@class='input-container']//label[@for='comment']")
    send_message = (By.ID, 'comment')
    switch_manta = (By.XPATH, "//div[@class='r-sw']//div[@class='switch'][1]")
    counter_plus_icecream = (By.XPATH, "//div[@class='counter-plus'][1]")
    button_get_taxi = (By.XPATH, "//div[@class='smart-button-wrapper']")
    order_number = (By.XPATH, "//div[@class='order-number']")
    def __init__(self, driver):
        self.driver = driver

    def set_from(self, from_address):
        self.driver.find_element(*self.from_field).send_keys(from_address)

    def set_to(self, to_address):
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def click_button_pedir_taxi(self):
        self.driver.find_element(*self.taxi_button).click()
    def set_route(self):
        self.set_from(data.address_from)
        self.set_to(data.address_to)
        self.get_to()
        self.get_from()
        self.click_button_pedir_taxi()
    def seleccionar_tarifa(self):
        self.driver.find_element(*self.comfort_tariff).click()
    def open_phone_window(self):
        self.driver.find_element(*self.phone_button).click()
    def send_phone_number(self):
        self.driver.find_element(*self.input_phone).send_keys(data.phone_number)
    def click_on_next(self):
        self.driver.find_element(*self.button_next_phone).click()
    def send_code(self):
        code = retrieve_phone_code(driver=self.driver)
        self.driver.find_element(*self.input_phone_code).send_keys(code)
    def click_to_save_phone(self):
        self.driver.find_element(*self.confirm_code_button).click()
    def introduce_phone_number(self):
        self.seleccionar_tarifa()
        time.sleep(2)
        self.open_phone_window()
        time.sleep(2)
        self.send_phone_number()
        time.sleep(2)
        self.click_on_next()
        time.sleep(2)
        self.send_code()
        time.sleep(2)
        self.click_to_save_phone()
    def get_into_payment(self):
        element = self.driver.find_element(*self.payment_button)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.driver.find_element(*self.payment_button).click()
    def click_on_add_card(self):
        self.driver.find_element(*self.add_card_button).click()
    def send_card_number(self):
        self.driver.find_element(*self.input_card_number).send_keys(data.card_number)
    def send_card_code(self):
        self.driver.find_element(*self.input_card_code).send_keys(data.card_code)
    def click_to_unlock(self):
        self.driver.find_element(*self.plc_div).click()
    def click_on_finish(self):
        self.driver.find_element(*self.finish_add_card).click()
    def click_on_close(self):
        self.driver.find_element(*self.button_close_payment).click()
    def introduce_payment(self):
        self.get_into_payment()
        time.sleep(2)
        self.click_on_add_card()
        time.sleep(2)
        self.send_card_number()
        time.sleep(2)
        self.send_card_code()
        time.sleep(2)
        self.click_to_unlock()
        time.sleep(2)
        self.click_on_finish()
        time.sleep(2)
        self.click_on_close()
    def click_on_text_driver(self):
        self.driver.find_element(*self.click_to_send_message).click()
    def introduce_message(self):
        self.driver.find_element(*self.send_message).send_keys(data.message_for_driver)
    def message_for_the_driver(self):
        self.click_on_text_driver()
        time.sleep(2)
        self.introduce_message()
    def get_manta(self):
        element = self.driver.find_element(*self.switch_manta)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.driver.find_element(*self.switch_manta).click()
    def get_icecream(self):
        click = self.driver.find_element(*self.counter_plus_icecream)
        for i in range(2):
            click.click()
    def get_a_taxi(self):
        self.driver.find_element(*self.button_get_taxi).click()

    def wait_for_driver_info(self):
        return  self.driver.find_element(*self.order_number)