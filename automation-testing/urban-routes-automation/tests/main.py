
import data
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
from pages import UrbanRoutesPage   






#APARTADO DE PRUEBAS
class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):


        from selenium import webdriver
        from selenium.webdriver.chrome.options import Options
        options = Options()
        options.set_capability("goog:loggingPrefs", {"performance": "ALL"})

        cls.driver = webdriver.Chrome(options=options)
        cls.driver.implicitly_wait(30)

    #Prueba para introducir las rutas Desde y Hasta
    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route()
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to
    #Prueba para introducir el número de teléfono
    def test_introduce_phone_number(self):
        self.test_set_route()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.introduce_phone_number()
    #Prueba para introducir método de pago
    def test_introduce_payment(self):
        self.test_introduce_phone_number()
        time.sleep(2)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.introduce_payment()
    #Prueba para dejar un mensaje para el conductor
    def test_message_for_the_driver(self):
        self.test_introduce_payment()
        time.sleep(2)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.message_for_the_driver()
    #Prueba para agregar la manta y el helado al servicio
    def test_get_requeriments(self):
        self.test_message_for_the_driver()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.get_manta()
        time.sleep(2)
        routes_page.get_icecream()
    #Prueba para hacer click en el botón y acceder a un taxi
    def test_get_the_taxi(self):
        self.test_get_requeriments()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.get_a_taxi()
        time.sleep(5)
    #Prueba para verificar la información del conductor en la pantalla de espera del viaje
    def test_wait_for_driver_info(self):
        self.test_get_the_taxi()
        routes_page = UrbanRoutesPage(self.driver)
        info = routes_page.wait_for_driver_info()
        assert info is not None

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
