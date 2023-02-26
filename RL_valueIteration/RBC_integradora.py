import time
from datetime import datetime
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import db
import numpy as np
import paho.mqtt.client as mqtt #import the client1
import random

# creacion de la app para firebase
cred = credentials.Certificate(
    'energy-coach-f5270-firebase-adminsdk-o4rki-881d6550e6.json')
app = firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://energy-coach-f5270-default-rtdb.firebaseio.com/'
})
print(app.name)
dbF = firestore.client()

broker_address="127.0.0.1"
port = 1883
topic = "integradora/confort"
client_id = f'python-mqtt-{random.randint(0, 1000)}'
client = mqtt.Client(client_id)
client.username_pw_set("labtelematica", "l4bt3l3m4tic@")
client.connect(broker_address,port)

def sendToFirestoreRecomendations(optionChange, dtm, recomendacion):
    data = {
        u'date': dtm,
        u'option': optionChange,
        u'recomendation': recomendacion
    }
    dbF.collection(u'recomendations2').add(data)
    return None


def sendToFirestoreComfort(comfortCould, comfortNeutral, comfortHold, dtm):
    data = {
        u'cold': comfortCould,
        u'neutral': comfortNeutral,
        u'warm': comfortHold,
        u'date': dtm
    }
    dbF.collection(u'Comfort').add(data)
    return None


# nueva Funcion


def accionRBC(option, confort):
    option_change = 0
    if option == 1:  # ON
        if confort == "cold":
            option_change = 9
        elif confort == "neutral":
            option_change = 9
        elif confort == "warm":
            option_change = 7
    elif option == 2:  # OFF
        if confort == "cold":
            option_change = option
        elif confort == "neutral":
            option_change = option
        elif confort == "warm":
            option_change = 1
    elif option == 3:  # 16°
        if confort == "cold":
            option_change = option+2
        elif confort == "neutral":
            option_change = option
        elif confort == "warm":
            option_change = option
    elif option == 4:  # 17°
        if confort == "cold":
            option_change = option+2
        elif confort == "neutral":
            option_change = option
        elif confort == "warm":
            option_change = option-1
    elif option == 5:  # 18°
        if confort == "cold":
            option_change = option+2
        elif confort == "neutral":
            option_change = option
        elif confort == "warm":
            option_change = option-2
    elif option == 6:  # 19°
        if confort == "cold":
            option_change = option+2
        elif confort == "neutral":
            option_change = option
        elif confort == "warm":
            option_change = option-2
    elif option == 7:  # 20°
        if confort == "cold":
            option_change = option+2
        elif confort == "neutral":
            option_change = option
        elif confort == "warm":
            option_change = option-2
    elif option == 8:  # 21°
        if confort == "cold":
            option_change = option+2
        elif confort == "neutral":
            option_change = option
        elif confort == "warm":
            option_change = option-2
    elif option == 9:  # 22°
        if confort == "cold":
            option_change = option+2
        elif confort == "neutral":
            option_change = option
        elif confort == "warm":
            option_change = option-2
    elif option == 10:  # 23°
        if confort == "cold":
            option_change = option+1
        elif confort == "neutral":
            option_change = option
        elif confort == "warm":
            option_change = option-2
    elif option == 11:  # 24°
        if confort == "cold":
            option_change = option
        elif confort == "neutral":
            option_change = option
        elif confort == "warm":
            option_change = option-2
    print("la opcion dada por las reglas es: ", option_change)
    return option_change


while (1):
    try:
        #variables para encerar la real time
        comfort_cold = 0
        comfort_neutral = 0
        comfort_warm = 0

        # lectura de fecha actual
        dtm = firestore.SERVER_TIMESTAMP   
       
        # temperatura actual del aire acondicionado
        opcion = db.reference('recomendation').child('rec').get()
        print("La opcion actual de temperatura es: ", opcion)

        # valores de comfort (votaciones)
        comfort = db.reference('comfort')
        comfort_get = comfort.get()
        comfort_cold_rt = comfort_get.get('cold')
        comfort_neutral_rt = comfort_get.get('neutral')
        comfort_warm_rt = comfort_get.get('warm')
        print("Cold: %d, Neutral: %d, Calor: %d"%(comfort_cold_rt,comfort_neutral_rt,comfort_warm_rt))

        if (comfort_cold_rt == 0 and comfort_neutral_rt == 0 and comfort_warm_rt == 0):
            print("Sin datos, se mantiene el valor actual de comfort y temperatura en el AC")
            sendToFirestoreComfort(comfort_cold_rt, comfort_neutral_rt, comfort_warm_rt, dtm)

        else:
            print("si hay datos, se procede a validar la votacion.")
            arr_confort = np.array(
                    [comfort_cold_rt, comfort_neutral_rt, comfort_warm_rt])
            lista_comfort = ["cold", "neutral", "warm"]
            #Obtencion del mayor en la votacion, opcion correspondiente y envio por MQTT
            valorComfortMayor = lista_comfort[np.argmax(arr_confort)]
            value_change = accionRBC(opcion, valorComfortMayor)
            client.publish(topic,str(value_change))
            print("Se envio por mqtt el valor: %d"%value_change)
            sendToFirestoreRecomendations(
                value_change, dtm, valorComfortMayor)
            sendToFirestoreComfort(
                comfort_cold_rt, comfort_neutral_rt, comfort_warm_rt, dtm)

        # se encera las votaciones
        comfort.set(
            {'cold': comfort_cold,
            'neutral': comfort_neutral,
            'warm': comfort_warm
            }
        )
        print("Sistemas de votacion en cero nuevamente")
        time.sleep(900)
    except Exception as e:
        print("Ocurrio un error, pero se restablecio la conexion",e)
