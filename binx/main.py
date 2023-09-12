import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import webbrowser
import os
import time
import requests
import translate
from bs4 import BeautifulSoup

def binxInit():
    binx = pyttsx3.init()
    binx.setProperty('volume', 0.8)
    binx.setProperty('rate', 150)
    binx.say('Olá, eu sou o Binx')
    binx.say('Como posso te ajudar?')
    binx.runAndWait()
    return binx

def getSchoolSites():
    return [['geekieOne', 'https://one.geekie.com.br/'],
            ['classroom', 'https://classroom.google.com/u/0/h'],
            ['espaço do estudante', 'https://estudante.sesisenai.org.br/login']]

def executeComand(binx, audio):
    audio = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print('Ouvindo...')
            voice = audio.listen(source)
            command = audio.recognize_google(voice, language='pt-BR').lower()
            
            if 'binx' in command:
                command = command.replace('binx', '')
                binx.say(command)
                binx.runAndWait()            
            return command
    except sr.UnknownValueError:
        print('ERRO: Não foi possível entender o áudio.')
        return ""
    except sr.RequestError:
        print('ERRO: Não foi possível acessar o serviço de reconhecimento de fala.')
        return ""
    
def hours(binx):
    hora = datetime.datetime.now().strftime('%H:%M')
    binx.say('Agora são ' + hora)
    binx.runAndWait()

def searchWeb(command, binx):
    query = command.replace('pesquisar na web por', '').strip()
    if query:
        url = f'https://www.google.com/search?q={query}'
        webbrowser.open(url)
        binx.say('Aqui estão os resultados da pesquisa.')
        binx.runAndWait()
    else:
        binx.say('Por favor, especifique a consulta de pesquisa.')
        binx.runAndWait()

def openSchoolSites(command, schoolSites, binx):
    query = command.replace('abrir', '').strip()
    findedSite = False
    for site in schoolSites:
        if site[0].lower() in query:
            webbrowser.open(site[1])
            binx.say('Bons estudos!')
            binx.runAndWait()
            findedSite = True
            break
    if not findedSite:
        binx.say('Site educacional não encontrado na lista.')
        binx.runAndWait()

def playMusic(command, binx):
    music = command.replace('toque', '')
    pywhatkit.playonyt(music)
    binx.say('Tocando música')
    binx.runAndWait()


def shutdownComputer(command, binx):
    if 'uma hora' in command:
        os.system("shutdown -s -t 3600")
    elif 'meia hora' in command:
        os.system("shutdown -s -t 1800")
    elif 'agora' in command:
        for i in range(5, 0, -1):
            binx.say(f'Desligando o pc em {i}...')
            time.sleep(1)
        os.system("shutdown -s -t 0")

def cancelShutdown(binx):
    os.system("shutdown -a")

def news(binx):
    try:
        site = requests.get('https://news.google.com/news/rss?ned=pt_br&gl=BR&hl=pt')
        news = BeautifulSoup(site.text, 'xml')
        
        binx.say('Aqui estão as notícias mais recentes:')
        binx.runAndWait()
        
        for item in news.findAll('item')[:5]:
            message = item.title.text
            binx.say(message)
            binx.runAndWait()
    except Exception as e:
        print(f"Erro ao buscar notícias: {e}")
        binx.say('Desculpe, não foi possível buscar notícias no momento.')
        binx.runAndWait()

def openApplication(command, binx):
    if 'google chrome' in command:
        os.startfile("C:\Program Files\Google\Chrome\Application\chrome.exe")
        binx.say('Abrindo o Google Chrome')
        binx.runAndWait()
    elif 'visual studio' in command:
        os.startfile("")
        binx.say('Abrindo o Visual Studio')
        binx.runAndWait()
    elif 'visual studio code' in command:
        os.startfile("<caminho para o Visual Studio Code na sua máquina>")
        binx.say('Abrindo o Visual Studio Code')
        binx.runAndWait()
    else:
        binx.say('Desculpe, não reconheço esse aplicativo.')
        binx.runAndWait()


def main():
    audio = sr.Recognizer()
    binx = binxInit()
    schoolSites = getSchoolSites()

    while True:
        command = executeComand(audio, binx)
        
        if 'sair' in command:
            binx.say('Até mais!')
            binx.runAndWait()
            break
        if 'horas' in command:
            hours(binx)

        elif 'pesquisar na web por' in command:
            searchWeb(command, binx)

        elif 'abrir' in command:
            openSchoolSites(command, schoolSites, binx)

        elif 'toque' in command:
            playMusic(command, binx)

        elif 'notícias' in command:
             news(binx)

        elif 'abra a aplicação' in command:
            openApplication(command, binx)     

        elif 'desligar computador' in command:
            shutdownComputer(command, binx)
        elif 'cancelar desligamento' in command:
            cancelShutdown(binx)

if __name__ == "__main__":
    main()
