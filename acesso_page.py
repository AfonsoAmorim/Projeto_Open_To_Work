import pyautogui as fc


#excluir fonte de dados antiga

fc.moveTo(x=569,y=1058)
fc.sleep(3)
fc.click(button='left')
fc.sleep(5)
fc.moveTo(x=109,y=863)
fc.sleep(5)
fc.click(button='left')
fc.moveTo(x=1789,y=194)
fc.sleep(5)
fc.click(button='left')
fc.write('Fonte_Dados_Excel')
fc.sleep(5)
fc.press('enter')
fc.sleep(3)
fc.moveTo(x=391,y=249)
fc.doubleClick()
fc.moveTo(x=446,y=267)
fc.sleep(5)
fc.click(button='left')
fc.sleep(3)
fc.press('del')

# iniciar processo de download
fc.press('win')
fc.sleep(3)
fc.write('Edge')
fc.sleep(3)
fc.press('enter')
fc.sleep(6)
fc.moveTo(x=674,y=64)
fc.sleep(5)
fc.click(button='left')
fc.sleep(3)
fc.write('https://docs.google.com/spreadsheets/d/16AMM9LexCfUSZB_1H7uUYSi59tTbcUAVfZ6c3HwHN7I/')
fc.sleep(10)
fc.press('enter')
fc.sleep(15)
fc.moveTo(x=118,y=145)
fc.sleep(5)
fc.click(button='left')
fc.sleep(10)
fc.moveTo(x=118,y=450)
fc.sleep(10)
fc.moveTo(x=602,y=620)
fc.click(button='left')
fc.sleep(3)


#recortar novo download 

fc.moveTo(x=569,y=1058)
fc.click(button='left')
fc.sleep(5)
fc.moveTo(x=112,y=306)
fc.sleep(4)
fc.click(button='left')
fc.moveTo(x=352,y=294)
fc.sleep(3)
fc.click(button='left')
fc.hotkey('ctrl', 'x')

fc.sleep(5)
fc.moveTo(x=109,y=863)
fc.sleep(5)
fc.click(button='left')
fc.moveTo(x=1789,y=194)
fc.sleep(5)
fc.click(button='left')
fc.write('Fonte_Dados_Excel')
fc.sleep(5)
fc.press('enter')
fc.sleep(3)
fc.moveTo(x=391,y=249)
fc.doubleClick()
fc.moveTo(x=446,y=267)
fc.sleep(5)
fc.click(button='left')
fc.sleep(3)
fc.hotkey('ctrl', 'v')