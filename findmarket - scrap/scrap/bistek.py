from selenium import webdriver
import arrow
from time import sleep
import os
import re
import pyautogui as pi
from unidecode import unidecode
from MySQL import CRUD
import requests
from bs4 import BeautifulSoup
from filtros import filtros


def marketBistek():
    banco = CRUD()
    ar = arrow.now().format('DD/MM/YYYY')
    logo = ''
    key_words  = filtros().key_words
    produtos = ['arroz', 'molho de tomate', 'acucar', 'papel higienico', 'feijao',  'sal',  'farinha', 'macarrao', 'cafe', 'detergente' ]

    for p in produtos:
        product_category = p
        continuar = True
        navegador = webdriver.Chrome()
        navegador.get(f'https://www.bistek.com.br/catalogsearch/result/index/?q={p}&product_list_limit=all')
        navegador.fullscreen_window()
        sleep(2)

        xpath_link = '//*[contains(concat( " ", @class, " " ), concat( " ", "product-item-link", " " ))]'
        xpath_image = '//*[contains(concat( " ", @class, " " ), concat( " ", "product-image-photo", " " ))]'
        xpath_price = '//*[@id="maincontent"]/div[3]/div[1]/div[3]/div[2]/ol/li[8]/div/div[2]/div[1]/span[2]/span[1]'
        xpath_name = '//*[contains(concat( " ", @class, " " ), concat( " ", "product-item-link", " " ))]'

        links = []
        names = []
        prices = []
        imgs = []
        weight = []
        bulk = []

        # ---------------------------------------- LINKS ------------------------------------------------ # 

        link_elements = navegador.find_elements('xpath', xpath_link)
        for link_el in link_elements:
            href = link_el.get_attribute('href')
            links.append(href)

        # ------------------------------------- NOMES PRODUTOS ------------------------------------------ #

        name_elements = navegador.find_elements('xpath', xpath_name)
        for name_el in name_elements:
            name = unidecode(name_el.text)
            name = re.sub(r"[^a-zA-Z0-9- ]","",name)
            names.append(name)
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

        for i in range(len(bulk)):
            if bulk[i] > 9999:
                bulk[i] = (bulk[i]/10)
        for i in range(len(weight)):
            if weight[i] > 9999:
                weight[i] = (weight[i]/10)
        # ---------------------------------------- IMAGENS PRODUTOS -------------------------------------- #

        image_elements = navegador.find_elements('xpath', xpath_image)
        for image_el in image_elements:
            href = image_el.get_attribute('src')
            imgs.append(href)

        # --------------------------------------------- Prices ------------------------------------------- #

        alvo = f'https://www.bistek.com.br/catalogsearch/result/index/?q={p}&product_list_limit=all'

        response = requests.get(alvo)
        doc = BeautifulSoup(response.text, 'html.parser')
        tag = doc.find_all(["span"], class_="price-wrapper")
        spans = str(tag).split('</span>')
        spans2 = []

        
        for i in spans:
            x = i
            lista = x.split(' ')
            for k in lista:
                if k == r'data-price-type="finalPrice"':
                    print(i)
                    spans2.append(i)
        
        for i in spans2:
            print(i)
            valor = str(i).split('R$')
            xa = u'\xa0'
            print(valor)
            valor = valor[1].replace(xa, '').replace(',','.')
            print(valor)
            prices.append(valor)

        for i in bulk:
            print(i)
        print('Termino!!!!!!')
        for i in weight:
            print(i)
        # --------------------------------------- INSERÇÃO NO BANCO --------------------------------------- #
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
                        banco.insert_peso('Bistek', product_category, names[i], weight[i], float(prices[i]), imgs[i], links[i], logo, str(ar), price_vol_wei)
                    elif bulk[i] != 0:
                        banco.insert_volume('Bistek', product_category, names[i], bulk[i], float(prices[i]), imgs[i], links[i], logo, str(ar), price_vol_wei)
                    else:
                        banco.insert('Bistek', product_category, names[i], float(prices[i]), imgs[i], links[i], logo, str(ar), price_vol_wei)
                except:
                    pass


        navegador.quit()
    banco.finaliza()
