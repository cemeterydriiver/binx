import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import webbrowser
import subprocess
import os
import time

audio = sr.Recognizer()
binx = pyttsx3.init()
binx.setProperty('volume', 0.8)
binx.setProperty('rate', 150)
binx.say('Olá, eu sou o Binx')
binx.say('Como posso te ajudar?')
binx.runAndWait()

sitesEducacionais = [['geekieOne', 'https://one.geekie.com.br/'], 
                     ['classroom', 'https://classroom.google.com/u/0/h'], 
                     ['espaço do estudante', 'https://estudante.sesisenai.org.br/login']]

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
    while True:
        comando = executaComando()

        if 'sair' in comando:
            binx.say('Até mais!')
            binx.runAndWait()
            break

        if 'horas' in comando:
            hora = datetime.datetime.now().strftime('%H:%M')
            binx.say('Agora são ' + hora)
            binx.runAndWait()

        elif 'pesquisar na web por' in comando:
            consulta = comando.replace('pesquisar na web por', '').strip()
            if consulta:
                url = f'https://www.google.com/search?q={consulta}'
                webbrowser.open(url)
                binx.say('Aqui estão os resultados da pesquisa.')
                binx.runAndWait()
            else:
                binx.say('Por favor, especifique a consulta de pesquisa.')
                binx.runAndWait()

        elif 'abrir' in comando:
            consulta = comando.replace('abrir', '').strip()
            siteEncontrado = False
            for site in sitesEducacionais:
                if site[0].lower() in consulta:
                    webbrowser.open(site[1])
                    binx.say('Bons estudos!')
                    binx.runAndWait()
                    siteEncontrado = True
                    break
            if not siteEncontrado:
                binx.say('Site educacional não encontrado na lista.')
                binx.runAndWait()

        elif 'toque' in comando:
            musica = comando.replace('toque', '')
            pywhatkit.playonyt(musica)
            binx.say('Tocando música')
            binx.runAndWait()

        elif 'desligar computador' in comando and 'uma hora' in comando:
            os.system("shutdown -s -t 3600")
        elif 'desligar computador' in comando and 'meia hora' in comando:
            os.system("shutdown -s -t 1800")
        elif 'desligar computador' in comando and 'agora' in comando:
            for i in range(5, 0, -1):
                binx.say(f'Desligando o pc em {i}...')
                time.sleep(1)  
            os.system("shutdown -s -t 0")
        elif 'cancelar desligamento' in comando:
            os.system("shutdown -a")

if __name__ == "__main__":
    comandoVozUser()
