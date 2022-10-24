
from tkinter import E
from selenium import webdriver
import arrow
from time import sleep
import os
import re
from unidecode import unidecode
from MySQL import CRUD
from filtros import filtros
def marketFortAtacadista():
    banco = CRUD()
    logo = ''
    ar = arrow.now().format('DD/MM/YYYY')
    #ceps 89052-381 (itoupava norte), 89066-003 (Itoupavazinha), 
    key_words  = filtros().key_words
    produtos = ['arroz', 'feijao', 'açucar', 'sal', 'molho de tomate', 'farinha', 'macarrao', 'cafe', 'detergente', 'papel higienico']

    for p in produtos:
        product_category = p
        pagina = 2
        proceed = True
        navegador = webdriver.Chrome()
        navegador.get(f'https://www.deliveryfort.com.br/buscar?q={p}')
        navegador.fullscreen_window()
        while True:
            try:
                navegador.find_element('xpath','//*[@id="shelf-zipcode"]').send_keys('89052-381')
                break
            except:
                pass
        while True:
            try:
                navegador.find_element('xpath','/html/body/div[3]/div/div[3]/div[2]/a[2]').click()
                break
            except:
                pass
        while True:
            try:
                navegador.find_element('xpath','/html/body/div[5]/div/div[2]/div[4]').click()
                break
            except:
                pass
        while True:
            try:
                navegador.find_element('xpath','/html/body/div[5]/div/div[2]/a').click()
                break
            except:
                pass
        while True:
            try:
                navegador.find_element('xpath','/html/body/div[7]/div/div[3]/a[1]').click()
                break
            except:
                pass
        navegador.fullscreen_window()
        while proceed:
            while True:
                try:
                    navegador.find_element('xpath', '//*[contains(concat( " ", @class, " " ), concat( " ", "pagination-link", " " ))]')
                    break
                except:
                    pass

            xpath_link = '//*[contains(concat( " ", @class, " " ), concat( " ", "shelf-item__title-link", " " ))]'
            xpath_image = '//*[contains(concat( " ", @class, " " ), concat( " ", "shelf-item__image", " " ))]'
            xpath_price = '//*[contains(concat( " ", @class, " " ), concat( " ", "shelf-item__best-price", " " ))]//strong'
            xpath_name = '//*[contains(concat( " ", @class, " " ), concat( " ", "shelf-item__title-link", " " ))]'

            links = []
            names = []
            prices = []
            imgs = []
            weight = []
            bulk = []

            # ---------------------------------------- LINKS -------------------------------------------- # 

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

            # ---------------------------------------- PREÇOS PRODUTOS --------------------------------------- #

            price_elements = navegador.find_elements('xpath', xpath_price)
            for price_el in price_elements:
                price = price_el.text
                split_price = price.split('\n')
                split_price[0] = split_price[0].replace('R$', '').replace(' ', '').replace(',','.')
                prices.append(split_price[0])

            # ---------------------------------------- IMAGENS PRODUTOS -------------------------------------- #

            image_elements = navegador.find_elements('tag name', 'img')
            for e in image_elements:
                if 'ids' in e.get_attribute('src'):
                    imgs.append(e.get_attribute('src'))


            # --------------------------------------- INSERÇÃO NO BANCO --------------------------------------- #

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
                            banco.insert_peso('Fort Atacadista', product_category, names[i], weight[i], float(prices[i]), imgs[i], links[i], logo, str(ar), price_vol_wei)
                        elif bulk[i] != 0:
                            banco.insert_volume('Fort Atacadista', product_category, names[i], bulk[i], float(prices[i]), imgs[i], links[i], logo, str(ar), price_vol_wei)
                        else:
                            banco.insert('Fort Atacadista', product_category, names[i], float(prices[i]), imgs[i], links[i], logo, str(ar), price_vol_wei)
                    except:
                        pass

            navegador.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            sleep(4)
            pagina += 1
            while True:
                try:
                    sleep(1)
                    navegador.find_element('xpath', f'/html/body/main/div[4]/div/div[2]/ul/li[{pagina}]/a').click()
                    sleep(1)
                    navegador.find_element('xpath', f'/html/body/main/div[4]/div/div[2]/ul/li[{pagina}]/a').click()
                    sleep(1)
                    break
                except:
                    proceed = False
                    break
        navegador.quit()
    banco.finaliza()