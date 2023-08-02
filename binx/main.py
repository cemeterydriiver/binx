import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import webbrowser
import AppOpener#para abrir os apps pip install AppOpener

# Inicializando o objeto para reconhecer o áudio
audio = sr.Recognizer()

# Inicializando o objeto para sintetizar a fala
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
    elif 'Abrir Geekie One' in comando:
        consulta = comando.replace('Abrir Geekie One', '').strip()
        if consulta:
            url = f'https://one.geekie.com.br/'
            webbrowser.open(url)
            binx.say('Bons estudos!')
            binx.runAndWait()
        else:
            binx.say('Por favor, especifique a consulta de pesquisa.')
            binx.runAndWait()

    elif 'Abrir Classroom' in comando:
        consulta = comando.replace('Abrir Classroom', '').strip()
        if consulta:
            url = f'https://classroom.google.com/u/0/h'
            webbrowser.open(url)
            binx.say('Bons estudos!')
            binx.runAndWait()
        else:
            binx.say('Por favor, especifique a consulta de pesquisa.')
            binx.runAndWait()
    elif 'Abrir espaço do estudante' in comando:
        consulta = comando.replace('Abrir Classroom', '').strip()
        if consulta:
            url = f'https://estudante.sesisenai.org.br/login'
            webbrowser.open(url)
            binx.say('Bons estudos!')
            binx.runAndWait()
        else:
            binx.say('Por favor, especifique a consulta de pesquisa.')
            binx.runAndWait()
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
            hora_atual = agora.strftime('%H:%M')
            with open('tarefas.txt', 'a') as arquivo:
                arquivo.write(f'{lembrete} às {hora_atual}\n')
            binx.say('Lembrete definido.')
            binx.runAndWait()
        else:
            binx.say('Por favor, especifique o lembrete.')
            binx.runAndWait()
   


comandoVozUser()
