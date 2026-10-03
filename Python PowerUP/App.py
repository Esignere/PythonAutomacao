import  pyautogui
import time
import  pandas

pyautogui.PAUSE = 0.5

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

#Pressiona a tecla win
pyautogui.press('win')
#Escreve chrome
pyautogui.write('chrome')
#Acessa o chrome
pyautogui.press('enter')

pyautogui.write(link)
pyautogui.press('Enter')
time.sleep(2)


# FAZER LOGIN
## Email Falso para teste
pyautogui.click(747, 376)
pyautogui.write('pythonimpressionador@gmail.com')
# Senha falsa para testes
pyautogui.press('tab')
pyautogui.write('senhaaleatoria')

pyautogui.click(954, 541)
pyautogui.press('enter')

time.sleep(2)

##Adicionar os produtos

table = pandas.read_csv('./CSV/produtos.csv')

for linha in table.index:
    
    pyautogui.click(x=696, y=262)
    
    code =   table.loc[linha, 'codigo']
    pyautogui.write(code)
    pyautogui.press('tab')
    
    
    marca =  table.loc[linha, 'marca']
    pyautogui.write(marca)
    pyautogui.press('tab')
    
    type = str(table.loc[linha, 'tipo'])
    pyautogui.write(type)
    pyautogui.press('tab')
    
    categoria = str(table.loc[linha, 'categoria'])
    pyautogui.write(categoria)
    pyautogui.press('tab')
    
    preco = str(table.loc[linha, 'preco_unitario'])
    pyautogui.write(preco)
    pyautogui.press('tab')
    
    custo = str(table.loc[linha, 'custo'])
    pyautogui.write(custo)
    pyautogui.press('tab')
    
    obs = str(table.loc[linha, 'obs'])
    if obs != 'nan':
        pyautogui.write(obs)
    pyautogui.press('tab')
    pyautogui.press('enter')
    
    pyautogui.scroll(5000)

    
    