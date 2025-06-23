import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers import retrieve_phone_code


class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    boton_flash = (By.XPATH,'//*[@id="root"]/div/div[3]/div[3]/div[1]/div[1]/div[2]')
    boton_carrito = (By.XPATH,'//*[@id="root"]/div/div[3]/div[3]/div[1]/div[2]/div[3]/img')
    boton_pedir_un_taxi = (By.XPATH,'// *[ @ id = "root"] / div / div[3] / div[3] / div[1] / div[3] / div[1] / button')
    boton_comfort = (By.XPATH,'//*[@id="root"]/div/div[3]/div[3]/div[2]/div[1]/div[5]/div[1]/img')
    texto_boton_comfort = (By.XPATH,'//*[@id="root"]/div/div[3]/div[3]/div[2]/div[1]/div[5]/div[2]')
    boton_numero_de_telefono = (By.XPATH,'//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[1]/div')
    input_telefono = (By.ID,'phone')
    boton_siguiente_telefono = (By.XPATH,'//*[@id="root"]/div/div[1]/div[2]/div[1]/form/div[2]/button')
    code = (By.ID,'code')
    boton_confirmar_codigo = (By.XPATH,'//*[@id="root"]/div/div[1]/div[2]/div[2]/form/div[2]/button[1]')
    boton_metodo_de_pago = (By.XPATH,'//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[2]')
    boton_agregar_tarjeta = (By.XPATH,'//*[@id="root"]/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[2]')
    input_tarjeta = (By.ID,'number')
    input_cvv = (By.NAME,'code')
    boton_aceptar_agregar_tarjeta = (By.XPATH,'//*[@id="root"]/div/div[2]/div[2]/div[2]/form/div[3]/button[1]')
    boton_salir_agregar_tarjeta = (By.XPATH,'//*[@id="root"]/div/div[2]/div[2]/div[1]/button')
    input_mensaje_chofer = (By.NAME,'comment')
    boton_manta = (By.XPATH,'//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[1]/div/div[2]/div/span')
    check_manta = (By.XPATH,'//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[1]/div/div[2]/div/input')
    boton_agregar_helado = (By.XPATH,'//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[3]/div/div[2]/div[1]/div/div[2]/div/div[3]')
    valor_helado = (By.XPATH,'//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[3]/div/div[2]/div[1]/div/div[2]/div/div[2]')
    boton_pedir_taxi_final = (By.XPATH,'//*[@id="root"]/div/div[3]/div[4]/button')
    texto_buscando_automovil = (By.XPATH,'//*[@id="root"]/div/div[5]/div[2]/div[1]/div/div[1]')
    nombre_conductor = (By.XPATH,'//*[@id="root"]/div/div[5]/div[2]/div[2]/div[1]/div[1]/div[2]')


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

    def click_boton_flash(self):
        self.driver.find_element(*self.boton_flash).click()

    def click_boton_carrito(self):
        self.driver.find_element(*self.boton_carrito).click()

    def click_boton_pedir_un_taxi(self):
        self.driver.find_element(*self.boton_pedir_un_taxi).click()

    def leer_boton_comfort(self):
        return self.driver.find_element(*self.texto_boton_comfort).text

    def click_boton_comfort(self):
        self.driver.find_element(*self.boton_comfort).click()

    def click_boton_numero_de_telefono(self):
        self.driver.find_element(*self.boton_numero_de_telefono).click()

    def escribir_numero_de_telefono(self,numero):
        self.driver.find_element(*self.input_telefono).send_keys(numero)

    def leer_numero_de_telefono(self):
        return self.driver.find_element(*self.input_telefono).get_property('value')

    def click_siguiente_telefono(self):
        self.driver.find_element(*self.boton_siguiente_telefono).click()

    def escribe_codigo(self,codigo):
        self.driver.find_element(*self.code).send_keys(codigo)

    def leer_codigo(self):
        return self.driver.find_element(*self.code).get_property('value')

    def presionar_tecla_tabulador(self):
        self.driver.find_element(*self.code).send_keys(Keys.TAB)

    def click_confirmar_codigo(self):
        self.driver.find_element(*self.boton_confirmar_codigo).click()

    def click_boton_metodo_de_pago(self):
        self.driver.find_element(*self.boton_metodo_de_pago).click()

    def click_boton_agregar_tarjeta(self):
        self.driver.find_element(*self.boton_agregar_tarjeta).click()

    def escribir_tarjeta(self,tarjeta):
        self.driver.find_element(*self.input_tarjeta).send_keys(tarjeta)

    def leer_tarjeta(self):
        return self.driver.find_element(*self.input_tarjeta).get_property('value')

    def escribir_cvv(self,cvv):
       self.driver.find_element(*self.input_cvv).send_keys(cvv)

    def leer_cvv(self):
       return self.driver.find_element(*self.input_cvv).get_property('value')

    def presionar_tecla_tabulador_cvv(self):
        self.driver.find_element(*self.input_cvv).send_keys(Keys.TAB)

    def click_aceptar_agregar_tarjeta(self):
        self.driver.find_element(*self.boton_aceptar_agregar_tarjeta).click()

    def click_boton_salir_agregar_tarjeta(self):
        self.driver.find_element(*self.boton_salir_agregar_tarjeta).click()

    def escribir_mensaje_chofer(self,mensaje):
        self.driver.find_element(*self.input_mensaje_chofer).send_keys(mensaje)

    def leer_mensaje_chofer(self):
        return self.driver.find_element(*self.input_mensaje_chofer).get_property('value')

    def click_manta(self):
        self.driver.find_element(*self.boton_manta).click()

    def revisar_check_manta(self):
        return self.driver.find_element(*self.check_manta).get_property('checked')

    def click_agregar_helado(self):
        self.driver.find_element(*self.boton_agregar_helado).click()

    def leer_valor_helado(self):
        return self.driver.find_element(*self.valor_helado).text


    def click_boton_pedir_taxi_final(self):
        self.driver.find_element(*self.boton_pedir_taxi_final).click()

    def leer_texto_buscando_automovil(self):
        return self.driver.find_element(*self.texto_buscando_automovil).text

    def leer_nombre_conductor(self):
        return self.driver.find_element(*self.nombre_conductor).text

    def set_route(self,from_address,to_address):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.from_field))
        self.set_from(from_address)
        self.set_to(to_address)

    def set_comfort(self):
        self.click_boton_flash()
        self.click_boton_carrito()
        self.click_boton_pedir_un_taxi()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.boton_comfort))
        self.click_boton_comfort()

    def set_numero_de_telefono(self,numero):
        self.click_boton_numero_de_telefono()
        self.escribir_numero_de_telefono(numero)

    def set_codigo(self):
        self.click_siguiente_telefono()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.code))
        codigo = retrieve_phone_code(self.driver)
        self.escribe_codigo(codigo)
        return codigo

    def salir_de_telefono(self):
        self.presionar_tecla_tabulador()
        self.click_confirmar_codigo()

    def set_tarjeta_de_credito(self,tarjeta):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.boton_metodo_de_pago))
        self.click_boton_metodo_de_pago()
        self.click_boton_agregar_tarjeta()
        self.escribir_tarjeta(tarjeta)

    def salir_tarjeta_de_credito(self):
        time.sleep(2)
        self.presionar_tecla_tabulador_cvv()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.boton_aceptar_agregar_tarjeta))
        self.click_aceptar_agregar_tarjeta()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.boton_salir_agregar_tarjeta))
        self.click_boton_salir_agregar_tarjeta()

    def agregar_dos_helados(self):
        time.sleep(1)
        self.click_agregar_helado()
        time.sleep(1)
        self.click_agregar_helado()

    def leer_datos_del_conductor(self):
        WebDriverWait(self.driver, 45).until(EC.visibility_of_element_located(self.nombre_conductor))
        conductor = self.leer_nombre_conductor()
        texto = self.leer_texto_buscando_automovil()
        return [conductor,texto]