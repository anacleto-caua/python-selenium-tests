from selenium import webdriver
from time import sleep

def pesquisarRH(receita, receitadahora):
    receitadahora.get('https://www.receitadahora.com')
    receitadahora.maximize_window()
    
    receitadahora.find_element_by_xpath('/html/body/header/div[1]/div[1]/button').click()

    enviar_receita = receitadahora.find_element_by_xpath('/html/body/header/div[2]/div[1]/form/div[1]/div/input')
    enviar_receita.send_keys(receita)

    receitadahora.find_element_by_xpath('/html/body/header/div[2]/div[1]/form/div[1]/div/button').click()

    receitadahora.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[1]/div').click()
    

def get_receitadahora(receitadahora):   
    titulo = receitadahora.find_element_by_xpath('//*[@id="meio-conteudo"]/div[1]/div[1]/h1').text
    print(titulo.upper())
    print()

    print("INGREDIENTES")
    try:
        ingredientes = receitadahora.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[1]/p[4]').text
    except:
        ingredientes = receitadahora.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[3]/ul').text
    print(ingredientes)
    print()

    print("MODO DE PREPARO")
    try:
        mododepreparo = receitadahora.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[1]/p[6]').text
    except:
        mododepreparo = receitadahora.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[3]/ol').text
    print(mododepreparo)
    print()

    print(receitadahora.current_url)

def pegarReceita(receita):
    receitadahora = webdriver.Chrome()
    pesquisarRH(receita, receitadahora)
    get_receitadahora(receitadahora)
    receitadahora.close()