import numpy as np
import time
from datetime import datetime
import json
import requests
from sendDatabase import firestore, db
from common_functions import get_next_state, get_state
from value_iteration import optimal_policy
from sendDatabase import sendToFirestoreRecomendationsNState
from serviceMQTT import sendToDB

# PARAMETROS PARA LA CONSULTA A LA API METEOROLOGICA
url = "https://api.openweathermap.org/data/2.5/weather"

querystring = {"lat": "-2.061163", "lon": "-79.905671",
               "appid": "89fc41f21b8e2b4a7561e2acafa082de",
               "units": "metric", "lang": "38"}

headers = {
    'Cache-Control': 'no-cache'
}


previous_state = 0
cold_reset = 0
neutral_reset = 0
warm_reset = 0
while 1:
    try:
        # FECHA ACTUAL
        date_time = firestore.SERVER_TIMESTAMP
        current_time = datetime.now().hour

        # OBTENCION DE RESULTADOS DE LAS VOTACIONES
        comfortDB = db.reference('comfort')
        comfort_get = comfortDB.get()
        comfort_cold_rt = comfort_get.get('cold')
        comfort_neutral_rt = comfort_get.get('neutral')
        comfort_warm_rt = comfort_get.get('warm')
        arr_confort = np.array(
            [comfort_cold_rt, comfort_neutral_rt, comfort_warm_rt])
        lista_comfort = ["cold", "neutral", "warm"]

        # NIVEL DE COMFORT GANADOR EN EL SISTEMA DE VOTACION
        results = lista_comfort[np.argmax(arr_confort)]
        comfort = 0
        if (results == "cold"):
            comfort = 0
        elif (results == "neutral"):
            comfort = 1
        else:
            comfort = 2

        # TEMPERATURA ACTUAL DEL AIRE ACONDICIONADO
        ac_status = db.reference('recomendation/rec').get()

        # PETICION A LA API METEOROLOGICA PARA OBTENER LA TEMEPRATURA EXTERNA
        response = requests.request(
            "GET", url, headers=headers, params=querystring)
        data = json.loads(response.content)
        temp_ext = data['main']['temp']

        # SE DETERMINA EL RESULTADO DE LOS ESTADOS Y ACCIONES EN BASE A LAS VARIABLES
        state = get_state(ac_status, comfort, current_time, temp_ext)
        action = optimal_policy[state]
        new_state = get_next_state(state, action)

        # ENVIO A LA BASE DE DATOS Y SE MUESTRA LOS RESULTADOS POR CONSOLA
        # sendToFirestoreRecomendationsNState(
        #   ac_status, temp_ext, date_time, comfort, state, new_state,action)
        print("Para el analisis de la informacion (determinacion del estado optimo) se consideran 4 variables: ")
        print("")
        print(
            "- Periodo del dia: \nP1: 07h00 a 12h00\nP2: 12h00 a 17h00\nP3: 17h00 a 23h59")
        print("- Nivel de confort: \n1. Frio (cold)\n2. Calor (warm)\n3. Neutral (neutral)")
        print("- Temperatura externa al lugar donde nos encontramos.")
        print("- Estado actual del aire acondicionado del sitio (temperatura del aire acondicionado actualmente)")
        print("")
        print("**************************************************************************************************")
        print("")
        print("Valor actual de las variables: ")
        print("Fecha actual: ", datetime.now())
        print("Periodo del dia (Hora): ", current_time)
        print("Nivel del comfort actual de los usuarios que han votado: ", results)
        print("Estado del AC: ", ac_status)
        print("Temperatura externa: ", temp_ext)
        print("**************************************************************************************************")
        print("Resultados: ")
        print("Estado determinado: ", state)
        print("Accion determinada para el estado: ", action)
        print("Estado siguiente: ", new_state)

        if state == previous_state:
            print("El estado actual es igual al anterior estado")
            time.sleep(60)
        elif state == new_state:
            print("El estado actual es igual al siguiente estado")
            time.sleep(60)
        else:
            # sendToDB(state,action)
            comfortDB.update(
                {
                    'cold': cold_reset,
                    'neutral': neutral_reset,
                    'warm': warm_reset
                }
            )
            print(
                "El estado actual es distinto al anterior y siguiente estado, se realiza la accion pertinente.")
            # sendToDB(state, action)
        previous_state = state
    except Exception as e:
        print("Ocurrio un error pero estamos restableciendo la conexion")
