
from selenium import webdriver
import arrow
from time import sleep
import os
import re
import pyautogui as pi
from unidecode import unidecode
from MySQL import CRUD
from filtros import filtros
def marketRedeTop():
    banco = CRUD()
    logo = ''
    acucar= ''
    sal = ''
    ar = arrow.now().format('DD/MM/YYYY')
    key_words = filtros().key_words
    produtos = [ 'sal', 'arroz', 'feijao', 'acucar', 'Molho de Tomate', 'Farinha', 'Macarrão', 'Café', 'Detergente', 'Papel Higiênico']
    
    # ---------------------------------------------------- ABRIR O SITE ------------------------------------------------- #

    for p in produtos:
        link = f'https://www.sitemercado.com.br/redetop/blumenau-loja-escola-agricola-asilo-r-benjamin-constant/busca/{p}'
        if p == 'sal':
            key_words.append('ACUCAR')
            sal = r'SAL%2520refinado'
            link = f'https://www.sitemercado.com.br/redetop/blumenau-loja-escola-agricola-asilo-r-benjamin-constant/busca/{sal}'

        if p == 'acucar':
            acucar = r'ACUCAR%2520REFINADO'
            key_words.remove('ACUCAR')
            link = f'https://www.sitemercado.com.br/redetop/blumenau-loja-escola-agricola-asilo-r-benjamin-constant/busca/{acucar}'

        product_category = p
        continuar = True
        navegador = webdriver.Chrome()
        navegador.get(link)
        navegador.fullscreen_window()
        sleep(6)
        try:
            navegador.find_element('xpath','/html/body/ngb-modal-window/div/div/app-auth-modal/div[1]/div/i').click()
        except:
            pass


        for i in range(15):
            navegador.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            sleep(0.5)


        xpath_link = '//*[contains(concat( " ", @class, " " ), concat( " ", "txt-desc-product-item", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "list-product-link", " " ))]'
        xpath_image = '//*[contains(concat( " ", @class, " " ), concat( " ", "ng-lazyloaded", " " ))]'
        xpath_price = '//*[contains(concat( " ", @class, " " ), concat( " ", "area-preco", " " ))]'
        xpath_name = '//*[contains(concat( " ", @class, " " ), concat( " ", "txt-desc-product-item", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "list-product-link", " " ))]'

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
            print(name)
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
            bkprice[0] = bkprice[0].replace('R$', '').replace(' ', '').replace(',','.')
            prices.append(bkprice[0])

        # ---------------------------------------- IMAGENS PRODUTOS -------------------------------------- #

        image_elements = navegador.find_elements('xpath', xpath_image)
        for image_el in image_elements:
            href = image_el.get_attribute('src')
            imgs.append(href)

        # --------------------------------------- INSERÇÃO NO BANCO --------------------------------------- #

        for i in range(len(links)):
            if weight[i] > 0:
                price_vol_wei = prices[i] / weight[i]
            elif bulk[i] > 0:
                price_vol_wei = prices[i] / bulk[i]
            else:
                price_vol_wei = 999

            verify_product = True
            for k in key_words:
                if k.upper() in str(names[i]).upper():
                    verify_product = False
            if verify_product:
                try:
                    if weight[i] != 0:
                        banco.insert_peso('Rede Top', product_category, names[i], weight[i], float(prices[i]), imgs[i], links[i], logo, str(ar), price_vol_wei)
                    elif bulk[i] != 0:
                        banco.insert_volume('Rede Top', product_category, names[i], bulk[i], float(prices[i]), imgs[i], links[i], logo, str(ar), price_vol_wei)
                    else:
                        banco.insert('Rede Top', product_category, names[i], float(prices[i]), imgs[i], links[i], logo, str(ar), price_vol_wei)
                except:
                    pass
        navegador.quit()
    banco.finaliza()