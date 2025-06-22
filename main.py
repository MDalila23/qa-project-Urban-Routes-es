import data
import time
from pages import UrbanRoutesPage
from helpers import retrieve_phone_code
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
        time.sleep(10)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

    def test_seleccionar_confort(self):
        routes_page = UrbanRoutesPage(self.driver)
        time.sleep(5)
        routes_page.click_boton_flash()
        routes_page.click_boton_carrito()
        routes_page.click_boton_pedir_un_taxi()
        time.sleep(3)
        routes_page.click_boton_comfort()
        assert  routes_page.leer_boton_comfort() == "Comfort"

    def test_rellenar_telefono(self):
        routes_page = UrbanRoutesPage(self.driver)
        time.sleep(2)
        routes_page.click_boton_numero_de_telefono()
        time.sleep(2)
        numero = data.phone_number
        routes_page.escribir_numero_de_telefono(numero)
        assert routes_page.leer_numero_de_telefono() == numero
        routes_page.click_siguiente_telefono()
        time.sleep(2)
        codigo = retrieve_phone_code(self.driver)
        routes_page.escribe_codigo(codigo)
        assert routes_page.leer_codigo() == codigo
        routes_page.presionar_tecla_tabulador()
        routes_page.click_confirmar_codigo()
        time.sleep(5)

    def test_agregar_tarjeta_de_credito(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_boton_metodo_de_pago()
        time.sleep(2)
        routes_page.click_boton_agregar_tarjeta()
        time.sleep(2)
        tarjeta = data.card_number
        routes_page.escribir_tarjeta(tarjeta)
        assert routes_page.leer_tarjeta() == tarjeta
        time.sleep(2)

    def test_codigo_cvv(self):
        routes_page = UrbanRoutesPage(self.driver)
        cvv = data.card_code
        routes_page.escribir_cvv(cvv)
        assert routes_page.leer_cvv() == cvv
        time.sleep(2)
        routes_page.presionar_tecla_tabulador_cvv()
        time.sleep(2)
        routes_page.click_aceptar_agregar_tarjeta()
        time.sleep(2)
        routes_page.click_boton_salir_agregar_tarjeta()

    def test_escribir_mensaje_controlador(self):
        routes_page = UrbanRoutesPage(self.driver)
        time.sleep(5)
        mensaje = data.message_for_driver
        routes_page.escribir_mensaje_chofer(mensaje)
        assert routes_page.leer_mensaje_chofer() == mensaje
        time.sleep(2)

    def test_pedir_manta_y_panuelos(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_manta()
        assert routes_page.revisar_check_manta() == True
        time.sleep(2)

    def test_pedir_helados(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_agregar_helado()
        time.sleep(2)
        routes_page.click_agregar_helado()
        time.sleep(2)
        assert routes_page.leer_valor_helado() == "2"

    def test_modal_buscar_taxi(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_boton_pedir_taxi_final()
        time.sleep(5)
        texto_leido = routes_page.leer_texto_buscando_automovil()
        assert texto_leido == "Buscar automóvil"

    def test_cambia_modal_buscar_taxi(self):
        routes_page = UrbanRoutesPage(self.driver)
        time.sleep(35)
        texto_leido_despues = routes_page.leer_texto_buscando_automovil()
        assert texto_leido_despues != "Buscar automóvil"

    def test_datos_conductor(self):
        routes_page = UrbanRoutesPage(self.driver)
        assert routes_page.leer_nombre_conductor() != ""


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
