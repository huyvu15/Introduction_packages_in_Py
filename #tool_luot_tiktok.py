import pyautogui as pag
from time import sleep
from random import randrange

sleep(3)
pag.press('win')
pag.typewrite('google chrome')
pag.press('enter')


sleep(4)
pag.typewrite('tiktok.com')
pag.press('enter')
sleep(4)

pag.press('enter')
sleep(5)
for i in range(0,30):
    pag.press('down')
    sleep(randrange(15,30))