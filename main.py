import uno
import dos
from time import sleep
if __name__ == '__main__':
    

    print('Primer ejercicio')
    sleep(2)
    uno.scrape_categories()
    
    #URL de categoría-productos por verificar
    url = 'https://super.walmart.com.mx/content/abarrotes/pan-y-tortillas-empacados/120005_630010'

    print('Segundo ejercicio')
    sleep(1)
    print(f'Para url: {url}')
    sleep(1)


    dos.scrape_products(url)