#pyautogui -> fazer automações com python | controlar mouse, teclado e tela

import pyautogui #.click | .press | .write
import time
import pandas

pyautogui.PAUSE = 0.5 #cada comando tem uma pausa de x segundos

#### PASSO 1: entrar no sistema da empresa ###
site = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

# abrir o chrome
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# escolher o usuário chrome
pyautogui.press("tab")
pyautogui.press("enter")

# digitar o site
pyautogui.write(site)
pyautogui.press("enter")
time.sleep(3)


### PASSO 2: fazer login ###

# inserir login
pyautogui.press("tab")
pyautogui.write("login.generico@email.com")
# inserir senha
pyautogui.press("tab")
pyautogui.write("senhagenerica123")
# entrar
pyautogui.press("enter")
time.sleep(3)

### PASSO 3: importar a base de dados ###
## Dados: pandas
tabela = pandas.read_csv("produtos.csv") #variável contendo a base de dados


### PASSO 4: cadastrar 1 produto ###

# rodar o código para cada linha da tabela
for linha in tabela.index: 
    
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.press("tab")
    pyautogui.write(codigo) 

    pyautogui.press("tab")
    marca = tabela.loc[linha, "marca"]    
    pyautogui.write(marca) 

    pyautogui.press("tab")
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(tipo) 

    #necessário transformar números em textos | float/int to string
    pyautogui.press("tab")
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria) 

    pyautogui.press("tab")
    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario) 

    pyautogui.press("tab")
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo) 

    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if obs != "nan":
        pyautogui.write(obs)

    #enviar
    pyautogui.press("tab")
    pyautogui.press("enter")
    #voltar ao início
    pyautogui.scroll(1080)


### PASSO 5: repetir o passo 4 para todos os produtos ###
# feito acima