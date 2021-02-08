import requests
import json
import time
import pyttsx3
engine = pyttsx3.init()

while True:
    r = requests.get("https://www.mercadobitcoin.net/api/BTC/ticker/")

    if str(r.status_code) == "200":

        r = json.loads(r.content.decode('utf-8'))
        preco = str(r['ticker']['sell']).split('.')[0]
        print(preco)
        engine.say('Preço do bitcoin: ' + preco )
        engine.runAndWait()
        time.sleep(600)

    else:

        engine.say('Houve um erro em enviar a request, o status code é' + str(r.status_code))
        engine.runAndWait()
        exit(0)