#Developer: https://github.com/VegaCenturion
#Special thanks : https://github.com/Ala-R-F
#               : https://github.com/annapss
#               : https://github.com/LuisHTVRS
#=========================================(//||^Progranadores^||\\)=========================================

#print("rodando")                            	# Checa se o programa foi iniciado
#browser = webdriver.Firefox()               	# Recebe drives do nevegador a ser usado || recomenda-se Firefox por ser mais leve
#print("Peguei o Navegador")		    	    # Teste
#browser.get('http://172.16.8.79/monitora')  	# Abre a janela na qual será alvo da captura
#print("Abri a URl")				            # Teste
#print("carregando programa")                	# Teste de carregamento da página
#sleep(5)                                    	# Espera para carregamento das informações da Estação
#while True:                                	# Condição de automação para Screenshot
#print("funcionando")                    	    # Teste
#browser.save_screenshot('Teste.png')        	# Timer para o espaçamento das capturas
#print("A mimir")                            	# Finaliza o progama

#=========================================(//||^Função_Primitiva^||\\)=========================================

#'C:\Users\comet\Downloads\ScreeshotMet\Versao ESP_32_1'

#===========================================(//||^Path_Arquivo^||\\)===========================================

from PIL import Image
import shutil
from PySimpleGUI import PySimpleGUI as sg
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from time import sleep
from threading import Thread

#=====================================(//||^Imports utilizados^||\\)=========================================

winOpen = True
state = False
timeSet = 60
url = 'http://173.16.8.151'
arqNome = 'Teste.png'
browser = webdriver.Firefox()           # Recebe drives do nevegador a ser usado || recomenda-se Firefox por ser mais leve

#=====================================(//||^Variaveis globais^||\\)=========================================


def Rodando():                              #Função de Screenshot do programa
    global winOpen, timeSet, state
    sleep(5)                                # tempo para carregar a pagina
    browser.save_screenshot(arqNome)        # salva a screenshot
    print("printando")                      # Teste
    state = True
    timeSet = int(timeSet)
    sleep(timeSet)                          # Timer para o espaçamento das captura
    print("a mimir")                        # Teste
    


def window():                               # Inteface grafica do programa
    sg.theme('LightGray1')
    global winOpen

    layout = [[sg.Button('Tirar foto agora',button_color=('purple')), sg.Text(size=(15,1), key='-FOTO-')],
                [sg.Text('Tempo entre capturas (Segundos):'),sg.Text(size=(15,1),key='-OUTPUT1-')], 
                [sg.Input(key='-IN1-',default_text='60'),sg.Button('Definir Segundos',button_color=('purple')),],
                [sg.Text('URL completa do alvo para a captura[https://www."site".com]: '), sg.Text(size=(40,1), key='-OUTPUT2-')], 
                [sg.Input(key='-IN2-', default_text='http://172.16.8.79/monitora'), sg.Button('Definir URL',button_color=('purple'))],
                [sg.Text('Nome do Arquivo[.png]: '), sg.Text(size=(40,1),key='-OUTPUT3-')], 
                [sg.Input(key='-IN_ARQ-', default_text='Teste.png'), sg.Button('Definir Nome',button_color=('purple'))],
                [[sg.Button('Iniciar/Pausar Programa', button_color=('purple')), sg.Text(size=(40,1)), sg.Text(size=(15,1), key='-STATE-')], sg.Button('Sair',button_color=('purple'))]]

    window = sg.Window('ScreenShot Esp_32_3', layout)

    try:
        while True: 
            global url, timeSet, winOpen, state, browser, arqNome
            event, values, = window.read() 
            print(event, values) 
            
            if event in  (None, 'Sair'): 
                state = False
                winOpen = False
                browser.close()
                break
            if event == 'Tirar foto agora':
                window['-FOTO-']
                Rodando()
        
            if event == 'Definir Segundos': 
                window['-OUTPUT1-'].update(values['-IN1-']) 
                timeSet = (values['-IN1-'])

            if event == 'Definir URL': 
                window['-OUTPUT2-'].update(values['-IN2-']) 
                url = (values['-IN2-'])

            if event == 'Definir Nome': 
                window['-OUTPUT3-'].update(values['-IN_ARQ-']) 
                arqNome = (values['-IN_ARQ-'])

            if event == 'Iniciar/Pausar Programa':
                if state == False:
                    state = True
                    window['-STATE-'].update('Ligado')
                    browser.get(url)                        # Abre a janela na qual será alvo da captura
                    winOpen = True
                    while(state == True):
                        Rodando()
                        
                else:
                    state = False
                    window['-STATE-'].update('Desligado')  
                    browser.close()               

    except:
        winOpen = False            #pop-up de erro
        sg.popup_error(f'ERRO. Tente novamente.')
        window.close()

#======================================(//||^Botões da Interface^||\\)======================================

a = Thread(target = window())
b = Thread(target = Rodando())

a.start()
b.start()

a.join
b.join
#======================================(//||^Thread dos programas^||\\)======================================

