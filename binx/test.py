
import openai
import pyttsx3
import speech_recognition as sr

openai.api_key = "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"
engine = pyttsx3.init()

voices = engine.getProperty('voices')
ptVoice = None
for voice in voices:
    if 'portuguese' in voice.languages:
        ptVoice = voice
        break
if ptVoice is not None:
    engine.setProperty('voice', ptVoice.id)
else:
    print('nao foi encontrada uma voz em pt')

def audioToText (filename):
    recognizer = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio = recognizer.record(source)
    try:
        return recognizer.recognize_google(audio)
    except:
        print('skipping unknow error')

def generateResponse (prompt):
    response = openai.Completion.create(
        engine = "text-davinci-003",
        prompt=prompt,
        max_tokens=4000,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response['choices'][0]['text']

def speakText (text):
    engine.say(text)
    engine.runAndWait()

def main():
    while True:
        print("digite 'genius' para começar a gravar sua pergunta")
        with sr.Microphone() as source:
            recognizer = sr.Recognizer()
            audio = recognizer.listen(source)
            try:
                transcriprion = recognizer.recognize_google(audio, language="pt-BR")
                if transcriprion.lower() == 'genius':
                    filename = "input.wav"
                    print("faça sua pergunta....")
                    with sr.Microphone() as source:
                        recognizer = sr.Recognizer()
                        source.pause_threshold = 1
                        audio = recognizer.listen(source, phrase_time_limit=None, timeout=None)
                        with open(filename, "wb") as f:
                            f.write(audio.get_wav_data())

                    text = audioToText(filename)
                    if text:
                        print(f"voce disse {text}")

                        response = generateResponse(text)
                        print(f"gpt disse {response}")

                        speakText(response)
            except Exception as e:
                print("ocorreu um erro: {}".format(e))

if __name__ == "__test__":
    test()            


