# Passo a passo do Projeto
# Passo 1: Entrar no sistema da empresa

import pyautogui
import time
import pandas as pd

# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar uma tecla
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.hotkey("ctrl", "alt", "del")
# abrir o navegador
pyautogui.PAUSE = 0.8
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
# entrar no link
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3)


# Passo 2: fazer login
# selecionar o campo de email
pyautogui.click(x=790, y=359)
# escrever o seu email
pyautogui.write("python@python.py")
pyautogui.press("tab") # passando para o próximo campo
pyautogui.write("senha")
pyautogui.click(x=832, y=522) # click no botao de login
time.sleep(3)
# Passo 3: importar a base de produtos para cadastrar
# certificar-se de importar pandas
tabela = pd.read_csv("produtos.csv")

# Passo 4: Cadastrar um produto
for linha in tabela.index:
    #clicar no campo de codigo
    pyautogui.click(x=734, y=240)
    # pegar da tabela o valor do campo que a gente quer preencher
    codigo = tabela.loc[linha, "codigo"]
    # preencher o campo
    pyautogui.write(str(codigo))
    # passar para o proximo campo
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter")
    # dar o scroll de tudo pra cima
    pyautogui.scroll(5000)

    # Passo 5: Repetir o processo de cadastro até o fim
    # for linha in tabela.index:
