
from selenium import webdriver, common
import arrow
from time import sleep
import re
import os
from unidecode import unidecode
import pyautogui as pi 
from MySQL import CRUD
from filtros import filtros

def marketSam():
    banco = CRUD()
    logo = r'https://raw.githubusercontent.com/dbentooojj/FindMarket/master/findmarket%20-%20django/static/images/SAMSLOGO.png'
    key_words = filtros().key_words
    produtos = ['arroz', 'feijao', 'acucar', 'sal', 'molho de tomate', 'farinha', 'macarrao', 'cafe', 'detergente', 'papel higienico']
    ar = arrow.now().format('DD/MM/YYYY')

    for p in produtos:
        product_category = p

        # ---------------------------------------------------- ABRIR O SITE ------------------------------------------------- #

        navegador = webdriver.Chrome()
        navegador.get(f'https://www.samsclub.com.br/{p}?_q={p}&map=ft')
        sleep(2)
        while True:
            try:
                navegador.find_element('xpath','//*[contains(concat( " ", @class, " " ), concat( " ", "vtex-cep", " " ))]')
                break
            except:
                pass
        
        # ------------------------------------------------------- COLOCAR CEP ------------------------------------------------ #

        sleep(3)
        navegador.find_element('xpath','//*[contains(concat( " ", @class, " " ), concat( " ", "vtex-cep", " " ))]').send_keys('89052-381')
        sleep(1)
        navegador.find_element('xpath','//*[@id="button"]').click()
        sleep(3)
        navegador.fullscreen_window()
        sleep(3)
        navegador.fullscreen_window()
        for i in range(10):
            pi.hotkey('ctrl','-')
            sleep(0.2)
        sleep(2)
        try:
            navegador.find_element('xpath','//*[contains(concat( " ", @class, " " ), concat( " ", "h-100", " " )) and contains(concat( " ", @class, " " ), concat( " ", "ph5", " " ))]').click()
        except:
            pass

        #  ----------------------------------------------- LINK DAS INFORMAÇÕES ---------------------------------------- #

        sleep(2)
        xpath_link = '//*[contains(concat( " ", @class, " " ), concat( " ", "pa4", " " ))]'
        xpath_image = '//*[contains(concat( " ", @class, " " ), concat( " ", "vtex-product-summary-2-x-image", " " ))]'
        xpath_price = '//*[contains(concat( " ", @class, " " ), concat( " ", "vtex-productShowCasePrice", " " ))]'
        xpath_name = '//*[contains(concat( " ", @class, " " ), concat( " ", "vtex-product-summary-2-x-brandName", " " ))]'

        links = []
        links2 = []
        names = []
        prices = []
        imgs = []
        weight = []
        bulk = []

        cont = 0

        # ---------------------------------------- LINKS -------------------------------------------- # 

        while True:
            link_elements = navegador.find_elements('tag name', 'a')
            for link_el in link_elements:
                try:
                    href = link_el.get_attribute('href')
                    if 'p' in href[-1] and '/' in href[-2] and href not in links:
                        links.append(href)
                            
                except:
                    pass
            navegador.execute_script("window.scrollTo(0,(document.body.scrollHeight/2))")
            link_elements2 = navegador.find_elements('tag name', 'a')
            for link_el in link_elements2:
                try:
                    href = link_el.get_attribute('href')
                    print(href)
                    if 'p' in href[-1] and '/' in href[-2] and href not in links:
                        links2.append(href)
                        
                except:
                    pass
            for i in links2:
                if i not in links:
                    links.append(i)
            for i in links:
                print(i)
            try:
                navegador.find_element('xpath','//*[contains(concat( " ", @class, " " ), concat( " ", "h-100", " " )) and contains(concat( " ", @class, " " ), concat( " ", "ph5", " " ))]').click()
                pass
            except:
                break
        
        # ------------------------------------- NOMES PRODUTOS ------------------------------------------ #

        name_elements = navegador.find_elements('xpath', xpath_name)
        price_elements = navegador.find_elements('xpath', xpath_price)
        image_elements = navegador.find_elements('xpath', xpath_image)
        for name_el in name_elements:
            name = unidecode(name_el.text)
            name = re.sub(r"[^a-zA-Z0-9- ]","",name)
            names.append(name)
            listed_name = name.split(' ')
            check_weight = str(listed_name[-1]).upper()
            print(check_weight)
            try:
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
            except:
                pass
        for i in range(len(bulk)):
            if bulk[i] > 9999:
                bulk[i] = (bulk[i]/10)
        for i in range(len(weight)):
            if weight[i] > 9999:
                weight[i] = (weight[i]/10)
        # ---------------------------------------- PREÇOS PRODUTOS --------------------------------------- #

        price_elements = navegador.find_elements('xpath', xpath_price)
        for price_el in price_elements:
            price = price_el.text
            bkprice = price.split('\n')
            bkprice[0] = bkprice[0].replace('R$', '').replace(' ', '').replace(',', '.')
            prices.append(bkprice[0])
        
        # ---------------------------------------- IMAGENS PRODUTOS -------------------------------------- #

        image_elements = navegador.find_elements('xpath', xpath_image)
        for image_el in image_elements:
            href = image_el.get_attribute('src')
            imgs.append(href)
        
        navegador.quit()

        # --------------------------------------- INSERÇÃO NO BANCO --------------------------------------- #

        print(f'{len(names)} {len(prices)} {len(links)} {len(imgs)}')
        for i in range(len(links)):
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
                        banco.insert_peso('Sams', product_category, names[i], weight[i], float(prices[i]), imgs[i], links[i], logo, str(ar), price_vol_wei)
                    elif bulk[i] != 0:
                        banco.insert_volume('Sams', product_category, names[i], bulk[i], float(prices[i]), imgs[i], links[i], logo, str(ar), price_vol_wei)
                    else:
                        banco.insert('Sams', product_category, names[i], float(prices[i]), imgs[i], links[i], logo, str(ar), price_vol_wei)
                except:
                    pass
        navegador.quit()
    banco.finaliza()