import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser

engine = pyttsx3.init()


def sayToMe(talk):
    engine.say(talk)
    engine.runAndWait()


sayToMe('Привет всем! У нас всё работает отлично')
sayToMe('Что мне сделать?')

record = sr.Recognizer()
try:
    with sr.Microphone(device_index=0) as source:
        print('Говори...')
        audio = record.listen(source)

        result = record.recognize_google(audio, language='ru-RU')
        result = result.lower()
        print(result)

        if result == 'скажи время':
            now = datetime.datetime.now()
            str_date = f'Сейчас {str(now.hour)}:{str(now.minute)}'
            print(str_date)
            sayToMe(str_date)

        elif result == 'открой сайт':
            webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

except sr.UnknownValueError:
    print('I don`t understand you')
except sr.RequestError:
    print('Something going wrong!')
