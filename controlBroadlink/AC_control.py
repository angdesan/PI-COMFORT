import broadlink
from paho.mqtt import client as mqtt_client
import random
import RL_valueIteration.constantes as constantes

TURN_OFF= constantes.TURN_OFF
TURN_ON = constantes.TURN_ON
TEMP_16 = constantes.TEMP_16
TEMP_17 = constantes.TEMP_17
TEMP_18 = constantes.TEMP_18
TEMP_19 = constantes.TEMP_19
TEMP_20 = constantes.TEMP_20
TEMP_21 = constantes.TEMP_21
TEMP_22 = constantes.TEMP_22
TEMP_23 = constantes.TEMP_23
TEMP_24 = constantes.TEMP_24


devices= broadlink.discover()
while(len(devices)==0):
    print("No existen dispositivos disponibles")
    devices = broadlink.discover()
print("Existe dispositivo broadlink")
device=devices[0]
device.auth()


broker = constantes.BROKER
port = constantes.PORT
topic = constantes.TOPIC_RL
username= constantes.USERNAME
password= constantes.PASSWORD
client_id = constantes.CLIENT

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)
    # Set Connecting Client ID
    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def subscribe(client:mqtt_client):
    def on_message(client, userdata, msg):
        option = int (msg.payload.decode())
        control_AC(option)


    client.subscribe(topic)
    client.on_message = on_message





def turn_on_AC(device):

    device.send_data(TURN_ON)
    print("Se ha encendido el aire acondicionado!")

def turn_off_AC(device):

    device.send_data(TURN_OFF)
    print("Se ha apagado el aire acondicionado!")

def temp_16_AC(device):

    device.send_data(TEMP_16)
    print("Se ha cambiado la temperatura a 16°C")

def temp_17_AC(device):

    device.send_data(TEMP_17)
    print("Se ha cambiado la temperatura a 17°C")

def temp_18_AC(device):

    device.send_data(TEMP_18)
    print("Se ha cambiado la temperatura a 18°C")

def temp_19_AC(device):

    device.send_data(TEMP_19)
    print("Se ha cambiado la temperatura a 19°C")

def temp_20_AC(device):

    device.send_data(TEMP_20)
    print("Se ha cambiado la temperatura a 20°C")

def temp_21_AC(device):

    device.send_data(TEMP_21)
    print("Se ha cambiado la temperatura a 21°C")

def temp_22_AC(device):

    device.send_data(TEMP_22)
    print("Se ha cambiado la temperatura a 22°C")

def temp_23_AC(device):

    device.send_data(TEMP_23)
    print("Se ha cambiado la temperatura a 23°C")

def temp_24_AC(device):

    device.send_data(TEMP_24)
    print("Se ha cambiado la temperatura a 24°C")


def control_AC(code: int):
    ans = True
    
    if code == 1:
        #encender aire
       turn_on_AC(device)
    if code == 2:
         #apagar aire
        turn_off_AC(device)
    if code == 3:
        #setear a 16 la temperatura
        temp_16_AC(device)
    if code == 4:
        #setear a 17 la temperatura
        temp_17_AC(device)
    if code == 5:
        #setear a 18 la temperatura
        temp_18_AC(device)
    if code == 6:
        #setear a 19 la temperatura
        temp_19_AC(device)
    if code == 7:
        #setear a 20 la temperatura
        temp_20_AC(device)
    if code == 8:
        #setear a 21 la temperatura
        temp_21_AC(device)
    if code == 9:
        #setear a 22 temperatura
        temp_22_AC(device)
    if code == 10:
        #setear a 23 la temperatura
        temp_23_AC(device)
    if code == 11:
        #setear a 24 la temperatura
        temp_24_AC(device)
    if code == 12:
        print("Standby")
    
    
def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()
    


if __name__ == '__main__':
    run()
