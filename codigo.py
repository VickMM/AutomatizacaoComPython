
import pyautogui
import time
import pandas 

# pyautogui.click -> clica em algo
# pyautogui.write -> escreva algo
# pyautogui.press -> pressiona uma tecla
# pyautogui.hotkey -> aperta um atalho (ex: ctrl + c)

pyautogui.PAUSE = 0.5
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
email = "programadoravictoria@outlook.com"
senha = "senha"

#1 - entrar no sistema da empresa

#abrir navegador
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

time.sleep(3)

pyautogui.write(link)
pyautogui.press("enter")

time.sleep(3)

tabela = pandas.read_csv("produtos.csv")
print(tabela)

# fazer login
pyautogui.click(x=779, y=404)
pyautogui.write(email)
pyautogui.press("tab")
pyautogui.write(senha)
pyautogui.press("enter")

time.sleep(3)

for linha in tabela.index:

    # cadastrar um produto

    pyautogui.click(x=753, y=290)

    #codigo
    codigo = str(tabela.loc[linha, "codigo"]) #localizar na linha, no campo chamado código
    pyautogui.write(codigo)
    pyautogui.press("tab")

    #marca
    marca = str(tabela.loc[linha, "marca"]) #localizar na linha, no campo marca e assim por diante
    pyautogui.write(marca)
    pyautogui.press("tab")

    #tipo
    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.write(tipo)
    pyautogui.press("tab")

    #categoria
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")
    
    #preco_unitario
    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)
    pyautogui.press("tab")

    #custo
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")
    
    #obs
    obs = str(tabela.loc[linha, "obs"])
    pyautogui.write(obs)
    pyautogui.click(x=925, y=960)

    pyautogui.scroll(5000)

# repetir até finalizar
