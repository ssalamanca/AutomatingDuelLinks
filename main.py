import pyautogui, time
"""Coordenadas X y Y"""
#689 , 745 -> Para seleccionar la barra de abajo
#711 , 596 -> Para seleccionar la opcion de "Mostrar el  escritorio"
#439 , 124 -> Para cerrar las notificaciones

"""Variables globales"""
global menu_notifications =True

pyautogui.displayMousePosition()

#Para mostrar el escritorio
pyautogui.rightClick(x=689, y=745)
"""btn = pyautogui.locateOnScreen('images/mostrar_escritorio.PNG',grayscale=False,confidence=0.8)
print(btn)
click_x, click_y = pyautogui.center(btn)"""
pyautogui.click(711, 596)

#Para abrir duel links
btn = pyautogui.locateOnScreen('images/duellinks_icon.PNG',grayscale=False,confidence=0.8)
click_x, click_y = pyautogui.center(btn)
pyautogui.doubleClick(click_x, click_y)

#Para iniciar Duel Links
btn_initiate = False
while not btn_initiate:
    btn = pyautogui.locateOnScreen('images/initiate_link.PNG',grayscale=False,confidence=0.8)
    if( btn == None):
        time.sleep(5)
        #print("Pasaron 10 segundos")
    else:
        btn_initiate=True
        click_x,click_y = pyautogui.center(btn)
        pyautogui.click(click_x,click_y)
#exit_menus()

def exit_menus():
    if(menu_notifications):
        btn = pyautogui.locateOnScreen("images/notifications.PNG",grayscale=False,confidence=0.8)
        if(btn !=None):
            menu_notifications=False
            pyautogui.click(439 , 124)

