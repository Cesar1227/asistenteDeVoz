import webbrowser
import speech_recognition as sr
import pyttsx3 as voz
import pyautogui as gui
from time import sleep
import subprocess as subp
import mysql.connector
import pywhatkit

##configuracion del asistente
name='iris'
asistente=voz.init()
velocidad = asistente.getProperty('rate')
asistente.setProperty('rate', velocidad-20)
asistente.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0')


##objetos
listener = sr.Recognizer()


##Variables globale


def hablar(texto):
    asistente.say(texto)
    asistente.runAndWait()

def reconocer(escribiendo):
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
                interpretar(text)
            #else:
                #print("No reconozco el comando, intenta de nuevo por favor")
        except:
            print('No te he entendido :(')

def interpretar(comando):
    comando = comando.split(' ')
    valido=False
    print("Interpretando")

    try:
        for keyss in array_words:
            print(keyss)
            if keyss in comando:
                print("Encontrado")
                keyswords.get(keyss,error)()
                valido=True       
            else:
                print("No esta")
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
    #auto.write(msgInicio)
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
    except:
        hablar("No te he entendido")
        redactar()

def abrir_youtube():
    music = rec.replace('reproduce', '')
    talk('Reproduciendo ' + music)
    pywhatkit.playonyt(music)

array_words=['escribir','musica','youtube']
keyswords={'escribir':abrir_blocNotas,'musica':abrir_youtube,'youtube':abrir_youtube}
reconocer(False)
print("Terminado")