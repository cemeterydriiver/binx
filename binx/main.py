import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pywhatkit
import webbrowser

# Objeto para reconhecer nosso áudio
audio = sr.Recognizer()
binx = pyttsx3.init()

# Configurações da voz do pyttsx3
vozes = binx.getProperty('voices')
binx.setProperty('voice', vozes[30].id)
binx.setProperty('volume', 0.8)
binx.setProperty('rate', 100)

# Mensagens de boas-vindas
binx.say('Olá, eu sou o Binx')
binx.runAndWait()
binx.say('Como posso te ajudar?')
binx.runAndWait()


def executaComando():
    comando = ""  # Inicializa com um valor padrão
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
        binx.say('Agora são ' + hora)
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
    elif 'abrir documento' in comando:
        webbrowser.open('https://docs.google.com/document/u/0/create')
        binx.say('Abrindo o Google Docs')
        binx.runAndWait()


comandoVozUser()
