from selenium import webdriver
from time import sleep

def pesquisarPA(receita, panelinha):
    panelinha.get('https://www.panelinha.com.br')
    panelinha.maximize_window()

    
    panelinha.find_element_by_xpath('/html/body/main-content/app-root/nav/div[2]/div/div[3]/ul/li[1]/a').click()
    procurar_receita = panelinha.find_element_by_xpath('/html/body/main-content/app-root/div[2]/div[1]/search-bar/form-search-bar/div/div/div[1]/div/form/div[1]/input-erasable/div/input')
    procurar_receita.send_keys(receita)
    panelinha.find_element_by_xpath('/html/body/main-content/app-root/div[2]/div[1]/search-bar/form-search-bar/div/div/div[1]/div/form/div[2]/button').click()
    sleep(10)
    panelinha.find_element_by_xpath('/html/body/main-content/app-root/div[2]/div[2]/search/main/section[1]/div/div[1]/ul/li[1]/label').click()
    sleep(10)
    panelinha.find_element_by_xpath('/html/body/main-content/app-root/div[2]/div[2]/search/main/section[2]/div[1]/div/div/div/article/a/div/img').click()
    sleep(10)




def get_panelinha(panelinha):   
    titulo = panelinha.find_element_by_xpath('/html/body/main-content/app-root/div[2]/div[2]/recipe/main/section[1]/div[1]/div[3]/h1[1]').text
    print(titulo.upper())
    print()

    try:
        ingredientes = panelinha.find_element_by_xpath('/html/body/main-content/app-root/div[2]/div[2]/recipe/main/section[2]/div/div[2]/section[1]/div[2]/ul').text
    except:
        ingredientes = panelinha.find_element_by_xpath('/html/body/main-content/app-root/div[2]/div[2]/recipe/main/section[2]/div/div[2]/section/div[1]/ul').text

    print("INGREDIENTES")
    print(ingredientes)
    print()

    
    print("MODO DE PREPARO")
    try:
        mododepreparo = panelinha.find_element_by_xpath('/html/body/main-content/app-root/div[2]/div[2]/recipe/main/section[2]/div/div[2]/section[1]/div[4]/ol').text
        mododepreparo = mododepreparo.splitlines()
        organizarMDP(mododepreparo)
    except:
        try:
            mododepreparo = panelinha.find_element_by_xpath('/html/body/main-content/app-root/div[2]/div[2]/recipe/main/section[2]/div/div[2]/section[1]/div[4]').text
        except:
            mododepreparo = panelinha.find_element_by_xpath('/html/body/main-content/app-root/div[2]/div[2]/recipe/main/section[2]/div/div[2]/section/div[3]/ol').text
        print(mododepreparo)
    print()

    numero=2
    while(True):

        try:
            titulo_de_passo = panelinha.find_element_by_xpath('/html/body/main-content/app-root/div[2]/div[2]/recipe/main/section[2]/div/div[2]/section['+ str(numero) +']/div[1]/h4[1]').text
            ingredientes_de_passo =  panelinha.find_element_by_xpath('/html/body/main-content/app-root/div[2]/div[2]/recipe/main/section[2]/div/div[2]/section['+ str(numero) +']/div[2]/ul').text
            mdp_de_passo =  panelinha.find_element_by_xpath('/html/body/main-content/app-root/div[2]/div[2]/recipe/main/section[2]/div/div[2]/section['+ str(numero) +']/div[4]/ol').text


            print(titulo_de_passo.upper())
            print()

            print("INGREDIENTES")
            print(ingredientes_de_passo)
            print()

            print("MODO DE PREPARO")
            mdp_de_passo=mdp_de_passo.splitlines()
            organizarMDP(mdp_de_passo)
            print()
        except:
            break

        numero+=1


    print(panelinha.current_url)

def organizarMDP(mdp):
    i=1    
    for k in mdp:
        print(i, mdp[i-1])
        i+=1

def pegarReceita(receita):
    panelinha = webdriver.Chrome()
    pesquisarPA(receita, panelinha)
    get_panelinha(panelinha)
    panelinha.close()

