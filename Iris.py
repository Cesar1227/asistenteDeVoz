import sys
import webbrowser
import speech_recognition as sr
import pyttsx3 as voz
import pyautogui as gui
import datetime
import subprocess as subp
import mysql.connector
import pywhatkit
import urllib.request
import json

from time import sleep


##configuracion del asistente
name='iris'
asistente=voz.init()
velocidad = asistente.getProperty('rate')
asistente.setProperty('rate', velocidad-20)
asistente.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0')

##objetos
listener = sr.Recognizer()

##Variables globale

##Comandos
salir='finaliza'
lastComand=''

def hablar(texto):
    asistente.say(texto)
    asistente.runAndWait()

def reconocer(escribiendo):
    text=""
    while text!=salir:
        with sr.Microphone() as source:
            print('Hola, soy tu asistente por voz: ')
            audio = listener.listen(source)
            try:
                text = listener.recognize_google(audio, language='es-ES')
                #if name in text:
                text=text.lower()
                if escribiendo==True:
                    return text
                else:
                    print('Has dicho: {}'.format(text))
                    lastComand=text
                    interpretar(text)
                #else:
                    #print("No reconozco el comando, intenta de nuevo por favor")
            except:
                print('No te he entendido :(')

def interpretar(comando):
    comando = comando.split(' ')
    valido=False
    print("Interpretando")

    if 'abre' in comando:
        abrir_pagWeb(lastComand)

    if 'ejecuta' in comando:
        for i in programsDefect.keys():
            if i in comando:
                print('ejecutando '+i)
                ejecutarPrograma(i)
    else:        
        try:
            for keys in array_words:
                if keys in comando:
                    keyswords.get(keys,error)()
                    valido=True       
        except:
            print("Hubo un problema")


    #if valido==False:

    #ver_video = ('vídeo' or 'video') in comando_de_audio
    #escribir = ('escribir' or 'texto') in comando_de_audio

    #if "Amazon" in text:
    #    webbrowser.open('http://amazon.es')
    #if "noticias" in text:
    #    webbrowser.open('http://noticiasfinancieras.info')
    #if "que tal" in text:
    #    print("Bien y tu?")

    #if ver_video is True:
    #    abrir_youtube()
    #elif escribir is True:
    #    abrir_blocNotas()

#def ejecutar(accion):


#### Definición de acciones

def error():
    hablar('Lo siento no me es posible realizar esta tarea')

def abrir_blocNotas():
    print("A escribir")
    msgInicio="Estoy lista para escribir";
    subp.call('start notepad.exe', shell=True)
    sleep(2.5)
    hablar(msgInicio)
    redactar()
    hablar("TERMINANDO ESCRITURA EN BLOC DE NOTAS") 

def redactar():
    try:
        escribiendo=True
        with sr.Microphone() as source:
            while(escribiendo==True):
                audio = listener.listen(source)
                textU = listener.recognize_google(audio, language='es-ES')
                print(textU)
                textU = textU.lower()

                if 'terminar escritura' not in textU :
                    gui.write(textU+ " ") 
                else:
                    escribiendo=False
    except Exception as e:
        print("Ha ocurrido un error :"+e)
        hablar("No te he entendido")
        redactar()

def abrir_youtube():
    try:
        music = lastComand.replace('reproduce', '')
        print(music)
        hablar('Reproduciendo ' + music)
        #music = music.replace(' ','+')
        #webbrowser.open('https://www.youtube.com/results?search_query='+music)
        pywhatkit.playonyt(music)
    except:
        hablar("A ocurrido un problema al reproducir "+music)
        print("Error abriendo youtube "+music)

def abrir_pagWeb(pag):
    try:
        pagina=pag.replace('abre','')
        pagina=pagina.replace(' ','')
        hablar('abriendo '+pagina)
        webbrowser.open('www.'+pagina+'.com')

    except Exception as e:
        print("Ha ocurrido un error :"+e)
    finally:
        pass

def hora_fecha(comand):
    if comand=='hora':
        hora = datetime.datetime.now().strftime('%I:%M %p')
        hablar("Son las " + hora)
    elif comand=='fecha':
        fecha = datetime.datetime.now().strftime('%d/%m/%Y')
        hablar("Hoy es " + fecha) 

def consultar(consulta):
    orden = consulta.replace('busca', '')
    wikipedia.set_lang("es")
    info = wikipedia.summary(orden, 1)
    hablar(info)

def ejecutarPrograma(program):
    programa = programsDefect.get(program)
    hablar('Ejecutando '+program.replace('.exe',''))
    sleep(1)
    subp.call('start '+programa, shell=True)    

programsDefect={'calculadora':'calc.exe','excel':'EXCEL.exe',
'word':'winword.exe','power point':'POWERPNT.exe',
'paint':'mspaint.exe','dibujar':'mspaint.exe','control':'control'}

array_words=['escribir','reproduce','youtube','amazon','hora']
keyswords={'escribir':abrir_blocNotas,'reproduce':abrir_youtube,'youtube':abrir_youtube,'pagina web':abrir_pagWeb,'hora':hora_fecha}
#reconocer(False)

lastComand='abre facebook'
interpretar('abre facebook')
print("Programa Terminado")