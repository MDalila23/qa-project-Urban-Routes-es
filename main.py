import data
import time
from pages import UrbanRoutesPage
from selenium import webdriver


class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        #cls.driver = webdriver.Chrome(desired_capabilities=capabilities)
        cls.driver = webdriver.Chrome()
        cls.driver.get(data.urban_routes_url)

    def test_set_route(self):
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

    def test_seleccionar_confort(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_comfort()
        assert  routes_page.leer_boton_comfort() == "Comfort"

    def test_rellenar_telefono(self):
        routes_page = UrbanRoutesPage(self.driver)
        numero = data.phone_number
        routes_page.set_numero_de_telefono(numero)
        assert routes_page.leer_numero_de_telefono()== numero
        codigo = routes_page.set_codigo()
        assert routes_page.leer_codigo() == codigo
        routes_page.salir_de_telefono()

    def test_agregar_tarjeta_de_credito(self):
        routes_page = UrbanRoutesPage(self.driver)
        tarjeta = data.card_number
        routes_page.set_tarjeta_de_credito(tarjeta)
        assert routes_page.leer_tarjeta() == tarjeta

    def test_codigo_cvv(self):
        routes_page = UrbanRoutesPage(self.driver)
        cvv = data.card_code
        routes_page.escribir_cvv(cvv)
        assert routes_page.leer_cvv() == cvv
        routes_page.salir_tarjeta_de_credito()

    def test_escribir_mensaje_controlador(self):
        routes_page = UrbanRoutesPage(self.driver)
        mensaje = data.message_for_driver
        time.sleep(2)
        routes_page.escribir_mensaje_chofer(mensaje)
        assert routes_page.leer_mensaje_chofer() == mensaje

    def test_pedir_manta_y_panuelos(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_manta()
        assert routes_page.revisar_check_manta() == True
        time.sleep(2)

    def test_pedir_helados(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.agregar_dos_helados()
        assert routes_page.leer_valor_helado() == "2"

    def test_modal_buscar_taxi(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_boton_pedir_taxi_final()
        time.sleep(2)
        texto_leido = routes_page.leer_texto_buscando_automovil()
        assert texto_leido == "Buscar automóvil"

    def test_datos_conductor(self):
        routes_page = UrbanRoutesPage(self.driver)
        [conductor, texto] = routes_page.leer_datos_del_conductor()
        assert texto != "Buscar automóvil"
        assert  conductor != ""

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
