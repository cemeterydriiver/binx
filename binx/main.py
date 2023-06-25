#importando bibliotecas (a do audio já vem quando é baixada)

import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pywhatkit

#objeto para reconhecer o audio

audio = sr.Recognizer()
binx = pyttsx3.init()
binx.setProperty('volume', 0.8)
binx.setProperty('rate', 150)
binx.say('Olá, eu sou o Binx')
binx.say('Como posso te ajudar?')
binx.runAndWait()


def executaComando():
    comando = "" 
    try:
        with sr.Microphone() as source:
            print('Ouvindo...')
            voz = audio.listen(source)
            comando = audio.recognize_google(voz, language='pt-BR')
            comando = comando.lower()
            if 'binx' in comando:
                comando = comando.replace('binx', '')
                binx.say(comando)
                binx.runAndWait()
    except:
        print('ERRO: Microfone não está funcionando.')
    return comando


def comandoVozUser():
    comando = executaComando()
    if 'horas' in comando:
        hora = datetime.datetime.now().strftime('%H:%M')
        binx.say('Agora são' +hora)
        binx.runAndWait()
    elif 'procure por' in comando:
        procurar = comando.replace('procure por', '')
        wikipedia.set_lang('pt')
        result = wikipedia.summary(procurar, 2)
        print(result)
        binx.say(result)
        binx.runAndWait()
    elif 'toque' in comando:
        musica = comando.replace('toque', '')
        result = pywhatkit.playonyt(musica)
        binx.say('Tocando música')
        binx.runAndWait()
comandoVozUser()
