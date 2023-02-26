import constantes
import random
from sendDatabase import ref
import paho.mqtt.client as mqtt
import time

broker = constantes.BROKER
port = constantes.PORT
topic = constantes.TOPIC_RL
username = constantes.USERNAME
password = constantes.PASSWORD
client_id = constantes.CLIENT


def sendToDB(state, action):
    print("Estado seleccionado: %d\n Accion a realizar: %d" % (state, action))
    code = 0
    if action == 0:  # apagar
        code = 2
    if action == 1:  # subir
        if (0 <= state <= 8) or (36 <= state <= 44) or (72 <= state <= 80):
            print("hola")
            code = random.randint(9, 11)  # seteamos a T3
        elif 9 <= state <= 17 or 45 <= state <= 53 or 81 <= state <= 89:
            code = random.randint(6, 8)  # seteamos a T2
        elif 18 <= state <= 26 or 54 <= state <= 62 or 90 <= state <= 98:
            code = random.randint(9, 11)  # seteamos a T3
        elif 27 <= state <= 35 or 63 <= state <= 71 or 99 <= state <= 107:
            code = random.randint(9, 11)  # seteamos a T3
        else:
            print("no entra a los otros")
            code = 2  # apagar
    if action == 2:  # bajar
        if 0 <= state <= 8 or 36 <= state <= 44 or 72 <= state <= 80:
            code = 2  # apagar
        elif 9 <= state <= 17 or 45 <= state <= 53 or 81 <= state <= 89:
            code = random.randint(3, 5)  # seteamos a T1
        elif 18 <= state <= 26 or 54 <= state <= 62 or 90 <= state <= 98:
            code = random.randint(3, 5)  # seteamos a T1
        elif 27 <= state <= 35 or 63 <= state <= 71 or 99 <= state <= 107:
            code = random.randint(6, 8)  # seteamos a T2
        else:
            code = 2  # apagar
    print("codigo a  enviar:", code)
    ref.update({"rec": code})
    # enviar al broker con publish
    client = mqtt.Client(client_id)
    client.username_pw_set(username, password)
    client.connect(broker, port)
    client.publish(topic, str(code))
    time.sleep(1800)
    return None
