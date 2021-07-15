from selenium import webdriver
from time import sleep


def get_tudo_gostoso(tudogostoso):

    nome =  tudogostoso.find_element_by_xpath('/html/body/div[5]/div[1]/div/div[3]/div[1]/div/div[1]/div[1]/div[1]/h1').text
    ingredientes = tudogostoso.find_element_by_xpath('//*[@id="info-user"]/ul').text
    mododepreparo =  tudogostoso.find_element_by_xpath('/html/body/div[5]/div[1]/div/div[3]/div[5]/div/div[1]/div/ol').text

    nome.upper()
    print(nome)

    print("INGREDIENTES")
    print(ingredientes)

    print("MODO DE PREPARO")
    organizarMDP(mododepreparo)
    print(tudogostoso.current_url)


def organizarMDP(mdp):
    counter = 1
    passo = str(counter) + " "

    mdp = mdp.replace("\n", "｡")

    for k in mdp:
        passo = passo + k
       
        if k == "｡":
            print(passo[0:len(passo)-1])
            
            counter += 1
            passo = str(counter) + " "


def pesquisarTG(receita, tudogostoso):
    
    tudogostoso.get('https://www.tudogostoso.com.br/')
    tudogostoso.maximize_window()

    sleep(15) #evitar o anuncio

    procurar_receita = tudogostoso.find_element_by_xpath('//*[@id="search-query"]')
    procurar_receita.send_keys(receita)

    sleep(15)
    #tudogostoso.find_element_by_xpath('//*[@id="search"]/input[2]').click() paro de funfa o debaixo ainda funfa
    tudogostoso.find_element_by_xpath('/html/body/header/div/div[1]/div/div/div[1]/form/input[2]').click()
    
    #escolher
    sleep(10)
    tudogostoso.find_element_by_xpath('/html/body/div[5]/div[1]/div[2]/div[2]/div/div[1]/a').click()
    sleep(10)


def pegarReceita(receita):
    tudogostoso = webdriver.Chrome()
    pesquisarTG(receita, tudogostoso)
    get_tudo_gostoso(tudogostoso)
    tudogostoso.close()
