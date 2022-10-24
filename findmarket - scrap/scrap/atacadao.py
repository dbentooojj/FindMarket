
from selenium import webdriver
import arrow
from time import sleep
import re
import pyautogui as pi
from unidecode import unidecode
from MySQL import CRUD
from filtros import filtros

def marketAtacadao():
    banco = CRUD()
    logo = ''
    ar = arrow.now().format('DD/MM/YYYY')
    key_words  = filtros().key_words

    produtos = ['papel higienico', 'molho de tomate', 'acucar', 'arroz', 'feijao',  'sal',  'farinha', 'macarrao', 'cafe', 'detergente' ]

    for p in produtos:
        f = p
        if f == 'papel higienico':
            f = 'papel-higienico'
        if f == 'molho de tomate':
            f = 'molho-de-tomate'
        product_category = p
        navegador = webdriver.Chrome()
        navegador.get(f'https://www.atacadao.com.br/catalogo/?q={p}')
        navegador.fullscreen_window()

        while True:
            try:
                navegador.find_element('xpath','/html/body/div[3]/div/div/div/div/div/div[2]/div')
                print('foi')
                break
            except:
                pass
                print('n foi')

        for i in range(10):
            pi.hotkey('ctrl','-')
            sleep(0.2)
        sleep(8)
        xpath_price = '//*[contains(concat( " ", @class, " " ), concat( " ", "product-box__price--number", " " ))]'
        xpath_name = '//*[contains(concat( " ", @class, " " ), concat( " ", "product-box__name", " " ))]'

        links = []
        names = []
        prices = []
        imgs = []
        weight = []
        bulk = []

        # ------------------------------------------------------ LINKS ------------------------------------------------------------- # 

        link_elements = navegador.find_elements('tag name', 'a')
        for link_el in link_elements:
            try:
                href = link_el.get_attribute('href')
                if f in href and '#' not in href:
                    print(href, 'Passou')
                    links.append(href)  
            except:
                pass     

        # --------------------------------------------------- NOMES PRODUTOS -------------------------------------------------------- #

        name_elements = navegador.find_elements('xpath', xpath_name)
        for name_el in name_elements:
            name = unidecode(name_el.text)
            name = re.sub(r"[^a-zA-Z0-9- ]","",name)
            names.append(name)
            listed_name = name.split(' ')
            check_weight = listed_name[-1]
            check_weight = str(listed_name[-1]).upper()
            print(check_weight)
            if check_weight[0].isnumeric():
                if check_weight[-1] == 'G' or check_weight[-1] == 'L':
                    pass
            else:
                try:
                    for i in listed_name:
                        i = str(i).upper()
                        if i[0].isnumeric():
                            if i[-1] == 'G' or i[-1] == 'L':
                                check_weight = i
                                break
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
        # ----------------------------------------------------- PREÇOS PRODUTOS ----------------------------------------------------- #

        price_elements = navegador.find_elements('xpath', xpath_price)
        for price_el in price_elements:
            price = price_el.text
            bkprice = price.split('\n')
            bkprice[0] = bkprice[0].replace('R$', '').replace(' ', '').replace(',','.')
            prices.append(bkprice[0])

        # ------------------------------------------------------ IMAGENS PRODUTOS --------------------------------------------------- #

        image_elements = navegador.find_elements('tag name', 'img')
        for e in image_elements:
            try:
                img = e.get_attribute('src')
                if 'sku' in img and 'bing' not in img:
                    imgs.append(img)
                    print(img)
            except:
                pass
        

        # --------------------------------------- INSERÇÃO NO BANCO --------------------------------------- #

        print(f'{len(names)} {len(prices)} {len(links)} {len(imgs)}')
        for i in range(len(names)):
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
                        banco.insert_peso('Giassi', product_category, names[i], weight[i], float(prices[i]), imgs[i], links[i], logo, str(ar), price_vol_wei)
                    elif bulk[i] != 0:
                        banco.insert_volume('Giassi', product_category, names[i], bulk[i], float(prices[i]), imgs[i], links[i], logo, str(ar), price_vol_wei)
                    else:
                        banco.insert('Giassi', product_category, names[i], float(prices[i]), imgs[i], links[i], logo, str(ar), price_vol_wei)
                except:
                    pass
        
        
        navegador.quit()
    banco.finaliza()
