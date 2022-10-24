#Giassi Supermercados - 

from unicodedata import name
from selenium import webdriver
import arrow
from time import sleep
import requests
from bs4 import BeautifulSoup
import re
import pyautogui as pi
from unidecode import unidecode
from MySQL import CRUD
from filtros import filtros

def marketGiassi():
    banco = CRUD()
    logo = r'https://raw.githubusercontent.com/dbentooojj/FindMarket/master/findmarket%20-%20django/static/images/logoGiassi.png'
    ar = arrow.now().format('DD/MM/YYYY')
    key_words = filtros().key_words
    produtos = ['arroz', 'feijao', 'acucar', 'sal', 'molho de tomate', 'farinha', 'Macarrão', 'cafe', 'detergente', 'papel higiencio']

    # ---------------------------------------------------- ABRIR O SITE ------------------------------------------------- #
    for p in produtos:
        product_category = p
        navegador = webdriver.Chrome()
        navegador.get(f'https://www.giassi.com.br/{p}?_q={p}&map=ft')
        navegador.fullscreen_window()
        sleep(5)
        try:
            navegador.find_element('xpath','//*[@id="cookiescript_accept"]').click()
        except:
            pass
        while True:
            try:
                navegador.find_element('xpath','/html/body/div[2]/div/div[1]/div/div[2]/div/div/section/div[2]/div/div[4]/div/div[2]/div/div[4]/div/div/div/div/div/a').click()
                sleep(5)
            except:
                break
        
    # ---------------------------------------------------- CAMINHO DOS ITENS ------------------------------------------------- #

        xpath_image = '//*[contains(concat( " ", @class, " " ), concat( " ", "vtex-product-summary-2-x-image", " " ))]'
        xpath_price = '//*[contains(concat( " ", @class, " " ), concat( " ", "giassi-apps-custom-0-x-priceUnit", " " ))]'


        links = []
        names = []
        prices = []
        imgs = []
        weight = []
        bulk = []

        link_elements = navegador.find_elements('tag name', 'a')
        name_elements = navegador.find_elements('tag name', 'span')

        for name_el in name_elements:
            name = unidecode(name_el.text)
            name = re.sub(r"[^a-zA-Z0-9- ]","",name)
            if p.upper() in name.upper() and 'ARROZ' != name.upper():
                names.append(name)
                try:
                    listed_name = name.split(' ')
                    check_weight = str(listed_name[-1]).upper()
                    print(check_weight)
                    if check_weight[0].isnumeric():
                        if check_weight[-1] == 'G' or check_weight[-1] == 'L':
                            print('passou!')
                            pass
                    else:
                        for i in listed_name:
                            i = str(i).upper()
                            if i[0].isnumeric():
                                if i[-1] == 'G' or i[-1] == 'L':
                                    check_weight = i
                                    break

                # ------------------------------------- PESO/VOLUME PRODUTOS ------------------------------------------ #

                    check_weight = str(check_weight).replace('KG','')
                    print(check_weight)
                    try:
                        weight.append(float(check_weight)*1000)
                        bulk.append(0)
                    except:
                        try:
                            check_weight = str(check_weight).replace('G','')
                            weight.append(float(check_weight))
                            bulk.append(0)
                        except:
                            try:
                                print(check_weight)
                                check_weight = str(check_weight).replace('L','')
                                bulk.append(float(check_weight)*1000)
                                weight.append(0)
                            except:
                                try:
                                    print(check_weight)
                                    check_weight = str(check_weight).replace('M','')
                                    bulk.append(float(check_weight))
                                    weight.append(0)
                                except:
                                    bulk.append(0)
                                    weight.append(0)
                except:
                    pass
        for i in range(len(bulk)):
            if bulk[i] > 9999:
                bulk[i] = (bulk[i]/10)
        for i in range(len(weight)):
            if weight[i] > 9999:
                weight[i] = (weight[i]/10)

        for li_el in link_elements:
            href = li_el.get_attribute('href')
            if href[-1] == 'p' and href[-2] == '/':
                links.append(href)

        price_elements = navegador.find_elements('xpath', xpath_price)
        for price_el in price_elements:
            price = price_el.text
            bkprice = price.split('\n')
            bkprice[0] = bkprice[0].replace('R$', '').replace(' ', '').replace(',','.')
            prices.append(bkprice[0])

        # ---------------------------------------- IMAGENS PRODUTOS -------------------------------------- #

        image_elements = navegador.find_elements('xpath', xpath_image)
        for image_el in image_elements:
            href = image_el.get_attribute('src')
            imgs.append(href)

        for i in range(len(names)):
            try:
                if weight[i] > 0:
                    price_vol_wei = float(prices[i]) / weight[i]
                elif bulk[i] > 0:
                    price_vol_wei = float(prices[i]) / bulk[i]
            except:
                price_vol_wei = 999

            verify_product = True
            for k in key_words:
                if k.upper() in str(names[i]).upper():
                    verify_product = False
            if verify_product:
                try:
                    if weight[i] != 0:
                        banco.insert_peso('Giassi', product_category, names[i], weight[i], float(prices[i]), imgs[i], links[i], logo, str(ar), price_vol_wei)
                    elif bulk[i] != 0:
                        banco.insert_volume('Giassi', product_category, names[i], bulk[i], float(prices[i]), imgs[i], links[i], logo, str(ar), price_vol_wei)
                    else:
                        banco.insert('Giassi', product_category, names[i], float(prices[i]), imgs[i], links[i], logo, str(ar), price_vol_wei)
                except:
                    pass
        navegador.quit()
    banco.finaliza()
