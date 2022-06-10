import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pywhatkit
import os
import yfinance as yf
import pyjokes
import wikipedia


# transformamos el audio en texto

# ver los idiomas y voces posibles para tu voice asistent
#engine = pyttsx3.init()
# for voice in engine.getProperty('voices'):
#    print(voice)

# probar los asistentes
#id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
#engine.setProperty('voice', id)
#engine.say("hellow daniel how are you i hop taht you are fine")
# engine.runAndWait()


def transform():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.5
        r.adjust_for_ambient_noise(source)
        said = r.listen(source)
        try:
            print("Te Escucho")
            q = r.recognize_google(said, language='es')

            return q
        except sr.UnknownValueError:
            print("Lo siento no entendi lo que dijiste")
            return "Esperando"
        except sr.RequestError:
            print("Lo sentimos el servicio a caido")
            return "Esperando"
        except:
            return "Esperando"


def speaking(message):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1.0)
    engine.say(message)
    engine.setProperty("rate", 10)
    engine.runAndWait()


def entrada():
    speaking("Bienvenido señor Grajales..."
             "..."
             "Iniciando todos los sistemas..."
             "..."

             "en que puedo servirle"
             )


def query_day():
    day = datetime.date.today()
    print(day)
    weekday = day.weekday()
    print(weekday)
    mapping = {
        0: 'lunes',
        1: 'martes',
        2: 'miercoles',
        3: 'jueves',
        4: 'viernes',
        5: 'sabado',
        6: 'domingo'

    }
    try:
        speaking(f'hoy es...{mapping[weekday]} {day}')
    except:
        print("no se que dia es hoy")


def query_time():
    time = datetime.datetime.now().strftime("%I:%M %p")
    try:
        if time[0] == '0':
            speaking(f'Son las {time[1]} y {time[3:5]} {time[6:8]}')
        else:
            speaking(f'Son las {time[0:2]} y {time[3:5]} {time[6:8]}')
    except:
        print('Error al hablar')


def ultron():

    ult = sr.AudioFile("frasesult.wav")
    speaking(ult)


def repetir():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speaking("dime algo....... lo escribire por ti")
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio)
            print(f"digiste {text}")
        except:
            speaking("no pude escuchar bien")


def ultron_query():

    entrada()
    start = True
    while start:
        q = transform().lower()
        if 'fecha' in q:
            speaking("A la orden señor")
            query_day()
            continue
        elif 'hola ultron' in q:
            speaking("¿Hola como estas?")
            continue
        elif 'estoy bien' in q:
            speaking("Me alegra... espero que tu dia siga asi")
            continue
        elif 'estoy mal' in q:
            speaking("¿quieres escuchar musica?")
            continue
        elif 'dame la hora' in q:
            speaking("A la orden señor")
            query_time()
            continue
        elif 'abre youtube' in q:
            speaking("A la orden señor")
            speaking("abrire youtube...")
            webbrowser.open('https://www.youtube.com')
            continue
        elif 'abre google' in q:
            speaking("A la orden señor")
            speaking("abrire gugol...")
            webbrowser.open('https://www.google.com')
            continue
        elif 'tu nombre' in q:
            speaking("yo soy ultron..."
                     "Una maquina creada para la destruccion"
                     )
            ultron()
            continue
        elif 'de wikipedia' in q:
            speaking("A la orden señor")
            speaking('Revisando wikipedia')
            q = q.replace('Wikipedia', '')
            result = wikipedia.summary(q, sentences=3)
            speaking('Encontré esto en wikipedia')
            speaking(result)
            continue
        elif 'estatus' in q:
            speaking(
                "Tengo la carga al 100%... mis servidores estan perfectos...")
        elif 'buscar' in q:
            speaking("A la orden señor")
            pywhatkit.search(q)
            speaking("esto es lo que encontre")
            continue
        elif 'pon' in q:
            speaking("A la orden señor")
            speaking(f'pondre{q}')
            pywhatkit.playonyt(q)
            continue
        elif 'chiste' in q:
            speaking("A la orden señor")
            speaking(pyjokes.get_joke())
            continue

        elif 'precio de' in q:
            speaking("A la orden señor")
            search = q.split("de")[-1].strip()
            lookup = {
                'apple': 'AAPPL',
                'amazon': 'AMZN',
                'google': 'GOOGL'
            }
            try:
                stock = lookup[search]
                stock = yf.Ticker(stock)
                price = stock.info["Precio regular"]
                speaking(f'el precio encontrado para{search}... es {price}')
            except:
                speaking(f'no encontre el articulo{search}')
        elif 'escribe esto' in q:
            speaking("A la orden señor")
            repetir()
        elif 'gracias' in q:
            speaking("Para usted señor... siempre")
        elif 'buenas noches' in q:
            speaking("buenas noches señor....")
            speaking("mi carga disminuyo a un 5%... apagando todos los sistemas")
            query_time()
            break
        elif 'creando proyecto' in q:
            speaking("¿trabajando en un proyecto secreto señor?")
            continue
        elif 'descargado' in q:
            speaking("...Implementando las reservas de energia")
            continue
        elif 'apaga los sistemas' in q:
            speaking("Hasta pronto señor.....apagando ")
            break
        elif 'se lo dije' in q:
            speaking(
                "En que estaba pensando señor.......... usted es siempre tan discreto")
        elif 'abrir lol' in q:
            speaking("a la orden señor")
            os.system("C:/Riot Games/League of Legends/LeagueClient.exe")


ultron_query()
