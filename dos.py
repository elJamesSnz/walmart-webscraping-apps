from time import sleep
from random import randint
import json

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def scrape_products(url): 
    # servicio ChromeDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome()
    driver.maximize_window()
    #url = 'https://super.walmart.com.mx/content/abarrotes/pan-y-tortillas-empacados/120005_630010'
    # get al sitio
    driver.get(url)
    sleep(randint(2,3))

    try:    
        # verificación click & hold
        element = driver.find_element(By.XPATH, "//div[@id='px-captcha']")
        action = ActionChains(driver)
        action.move_to_element_with_offset(element, 0, 0).click_and_hold().perform()
        sleep(10)
        action.release(element)
        action.perform()
        sleep(0.2)
        action.release(element)
        # verificación click & hold
        sleep(1)
        print('Click & hold verificado')
        sleep(5)
    except:
        # no hay hold&click
        print('no hay click and hold')

    # Obtener categorías
    categorias = []
    #data_item_ids_guardados = {}
    contador = 0

    for div_categoria in driver.find_elements(By.CSS_SELECTOR, 'div[class="mv3 mv4-xl ml3 ml0-l bb b--near-white"]'):

        try:
            texts = div_categoria.text.splitlines()
            uno = texts[0]
        
            categoria = {
                'nombre': driver.find_element(By.XPATH, "//h2[text()='" + uno + "']").text,
                'productos': []
            }

            # Obtener productos
            for li_producto in div_categoria.find_elements(By.CSS_SELECTOR, 'li[class="flex flex-column items-center pa1 pr2 pb2"]'):
                aux_producto = li_producto.find_element(By.CSS_SELECTOR, 'div[class="sans-serif mid-gray relative flex flex-column w-100 h-100 hide-child-opacity"]').get_attribute("data-item-id")
                #if  aux_producto not in data_item_ids_guardados:

                producto = {
                    'nombre_producto': li_producto.find_element(By.CSS_SELECTOR, 'span[class="normal dark-gray mb0 mt1 lh-title f6 f5-l"]').text,
                    'img_uri': li_producto.find_element(By.CSS_SELECTOR, 'div[class="relative"]').find_element(By.TAG_NAME, 'img').get_attribute('src')
                }

                # Obtener precios
                precios_div = li_producto.find_element(By.CSS_SELECTOR, 'div[class="flex flex-wrap justify-start items-center lh-title mb2 mb1-m"]')
                
                try:            
                    precio_descuento_div = precios_div.find_element(By.CSS_SELECTOR, 'div[class="mr1 mr2-xl lh-copy b black f5 f4-l"]')
                    producto['precio_actual'] = precio_descuento_div.text if precio_descuento_div.text else 'null'
                except:
                    producto['precio_actual'] = None


                try:            
                    precio_anterior_div = precios_div.find_element(By.CSS_SELECTOR, 'div[class="gray mr1 strike f7 f6-l"]')
                    producto['precio_anterior'] = precio_anterior_div.text if precio_anterior_div.text else 'null'
                except:
                    producto['precio_anterior'] = None

                categoria['productos'].append(producto)
                #data_item_ids_guardados.append(aux_producto)


            categorias.append(categoria)
            contador+=1
        except:
            print('categoria no válida')

    # Generar JSON
    result = {
        'URL': url,
        'categorias': categorias
    }

    categorias_json = json.dumps(result, indent=4, ensure_ascii=False)

    #   encoding='utf-8' para los acentos
    with open('productos.json', 'w', encoding='utf-8') as file:
        file.write(categorias_json)