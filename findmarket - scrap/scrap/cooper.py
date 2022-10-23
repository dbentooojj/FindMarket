import imp
from selenium import webdriver
import arrow
from time import sleep
import os
import re
from unidecode import unidecode
from filtros import filtros
from MySQL import CRUD

def marketCooper():

    banco = CRUD()
    logo = ''
    ar = arrow.now().format('DD/MM/YYYY')
    mercados = ['a.verde', 'garcia', 'i.norte', 'mafisa', 'v.nova']
    key_words  = filtros().key_words
    for j in mercados:
        #feijao, arroz, açucar, café, >>cerveja, detergente, feijao, macarrao, molho, papel higienico, sal
        produtos_n = ['feijao', 'arroz', 'acucar', 'cafe', 'detergente', 'macarrao', 'molho de tomate', 'papel higienico', 'sal' ]
        produtos = ['busca?q=Feijao+1kg', 'listar/12', 'listar/5',  'listar/43',   'listar/401', 
        'listar/199', 'listar/106', 'busca?q=papel%20higiênico',  'listar/97']
        mercadoa = 'Cooper'
        if j == mercados[0]:
            mercado = 'Cooper Água Verde'

        elif j == mercados[1]:
            mercado = 'Cooper Garcia'

        elif j == mercados[2]:
            mercado = 'Cooper Itoupava Norte'

        elif j == mercados[3]:
            mercado = 'Cooper Mafisa'

        elif j == mercados[4]:
            mercado = 'Cooper Omino'

        elif j == mercados[5]:
            mercado = 'Cooper Vila Nova'

        for i in range(9):
            product_category = produtos_n[i]
            continuar = True
            navegador = webdriver.Chrome()
            navegador.get(f'https://www.minhacooper.com.br/loja/{j}-bnu/produto/{produtos[i]}')
            navegador.fullscreen_window()
            height = navegador.execute_script("return document.body.scrollHeight")
            while True:
                try:
                    navegador.find_element('xpath','//*[@id="variant-list"]/div/div/div/div[4]/div[3]/div[2]/div/a').click()
                    break
                except:
                    pass
            
            while continuar:
                #Scroll down the page to show all the products
                for i in range(5):
                    navegador.execute_script("window.scrollTo(0,document.body.scrollHeight)")
                    sleep(1.5)
                try:
                    navegador.find_element('xpath', '//*[@id="variant-list"]/div/div/div/div[4]/div[3]/div[2]/div/a').click()
                except:
                    continuar = False
                    pass

            xpath_link = '//*[contains(concat( " ", @class, " " ), concat( " ", "product-variation__name", " " ))]'
            xpath_image = '//*[contains(concat( " ", @class, " " ), concat( " ", "product-variation__image", " " ))]'
            xpath_price = '//*[contains(concat( " ", @class, " " ), concat( " ", "product-variation__price", " " ))]'
            xpath_name = '//*[contains(concat( " ", @class, " " ), concat( " ", "product-variation__name", " " ))]'

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
                try:
                    if check_weight[0].isnumeric():
                        if check_weight[-1] == 'G' or check_weight[-1] == 'L':
                            print('passou!')
                            pass
                    else:
                        for i in listed_name:
                            i = str(i).upper()
                            check_weight = '0G'
                            try:
                                if i[0].isnumeric():
                                    if i[-1] == 'G' or i[-1] == 'L':
                                        check_weight = i
                                        break
                            except:
                                pass
                except:
                    pass
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
                bkprice[0] = bkprice[0].replace('R$', '').replace(' ', '').replace(',', '.').replace('De', '')
                prices.append(bkprice[0])

            # ---------------------------------------- IMAGENS PRODUTOS -------------------------------------- #

            image_elements = navegador.find_elements('xpath', xpath_image)
            for image_el in image_elements:
                href = image_el.get_attribute('src')
                imgs.append(href)

            # --------------------------------------- INSERÇÃO NO BANCO --------------------------------------- #

            for i in range(len(links)):
                verify_product = True
                for k in key_words:
                    if k.upper() in str(names[i]).upper():
                        verify_product = False
                if verify_product:
                    if weight[i] != 0:
                        banco.insert_peso(mercadoa, product_category, names[i], weight[i], float(prices[i]), imgs[i], links[i], logo, str(ar))
                    elif bulk[i] != 0:
                        banco.insert_volume(mercadoa, product_category, names[i], bulk[i], float(prices[i]), imgs[i], links[i], logo, str(ar))
                    else:
                        banco.insert(mercadoa, product_category, names[i], float(prices[i]), imgs[i], links[i], logo, str(ar))
            navegador.quit()
    banco.finaliza()
