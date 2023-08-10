import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import webbrowser
import subprocess
import AppOpener #para abrir os apps pip install AppOpener

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

sitesEducacionais = [['geekieOne', 'https://one.geekie.com.br/'], 
                     ['classroom', 'https://classroom.google.com/u/0/h'], 
                     ['espaço do estudante', 'https://estudante.sesisenai.org.br/login']]


def abrirApp(app):
    appsEducacionais = {
        'vscode': 'code',  
        'git': 'git',      
    }
    if app in appsEducacionais:
        try:
            subprocess.Popen(appsEducacionais[app], shell=True)
            binx.say(f'Abrindo {app}')
            binx.runAndWait()
        except Exception as e:
            print(f'Erro ao abrir {app}: {e}')
    else:
        binx.say('Aplicativo não encontrado na lista.')
        binx.runAndWait()


def comandoVozUser():
    comando = executaComando()

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

    elif 'abra o aplicativo' in comando:
        consulta = comando.replace('Abra o aplicativo', '').strip()
        abrirApp(consulta.lower())
    
    elif 'toque' in comando:
        musica = comando.replace('toque', '')
        pywhatkit.playonyt(musica)
        binx.say('Tocando música')
        binx.runAndWait()

    elif 'criar uma tarefa' in comando:
        tarefa = comando.replace('criar uma tarefa', '').strip()
        if tarefa:
            with open('tarefas.txt', 'a') as arquivo:
                arquivo.write(f'{tarefa}\n')
            binx.say('Tarefa adicionada à lista de tarefas.')
            binx.runAndWait()
        else:
            binx.say('Por favor, especifique a tarefa.')
            binx.runAndWait()
    
    elif 'ler minha lista de tarefas' in comando:
        with open('tarefas.txt', 'r') as arquivo:
            lista_tarefas = arquivo.read()
        if lista_tarefas:
            binx.say('Aqui está a sua lista de tarefas:')
            binx.say(lista_tarefas)
            binx.runAndWait()
        else:
            binx.say('Sua lista de tarefas está vazia.')
            binx.runAndWait()

    elif 'definir um lembrete' in comando:
        lembrete = comando.replace('definir um lembrete', '').strip()
        if lembrete:
            agora = datetime.datetime.now()
            horaAtual = agora.strftime('%H:%M')
            with open('tarefas.txt', 'a') as arquivo:
                arquivo.write(f'{lembrete} às {horaAtual}\n')
            binx.say('Lembrete definido.')
            binx.runAndWait()
        else:
            binx.say('Por favor, especifique o lembrete.')
            binx.runAndWait()
   


comandoVozUser()
