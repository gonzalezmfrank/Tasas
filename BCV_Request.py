# Ejecuta el script para obtener el valor del dolar y euro en bolivares y lo guarda en un archivo json
# Solo guarda alli la data necesaria fecha, dolar y euro

import os,requests,sys,json,datetime,platform
from zoneinfo import ZoneInfo
from datetime import date, time, datetime, timedelta

from KEY import CLAVE
from KEY import URL
from KEY import ARCHIVO
from KEY import ARCHIVO2

from pathlib import Path
from sys import platform

# Creador de un codificador personalizado para JSON
class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()  # Mantiene los 6 decimales de precisión
        return super().default(obj)

#print("el API Key es :",CLAVE)
##print("el URL es :",URL)

bcv = requests.get(
    URL,
    headers={'X-API-Key': CLAVE},
)

data = bcv.json()

## Selecciona los datos y crea un json con el resultado del dia

fecha_alp=data["index"]["as_of"]

print("La fecha valor es : ",fecha_alp)

dt = datetime.fromisoformat(fecha_alp)

for orden in data["rates"]:
	if orden["type"]=="reference":
		if orden["base"]=="USD":
			usd=orden["mid"]
			#print("Valor del Dolar : ",orden["mid"])
		elif orden["base"]=="EUR":
			eur=orden["mid"]
			# print("Valor del Euro : ",orden["mid"])


# "fecha" : datetime.strftime(dt,"%d/%m/%Y"),
#"fecha" : datetime.strftime(dt,"%d/%m/%Y %H:%M:%S"),
NVOJSON = {

	"fecha" : fecha_alp,
	"USD" : usd,
	"EUR" :eur

}

print("el contenido del JSon seria :",NVOJSON)

# Crea el json con los valores de la fecha

# Toma el Json del scrip BCV_Request.py y su resultado lo evalua con el archivo Tasas.json
# Si valor de Respuesta.json en su ultimo registro no se encuentra (valida dia de ejecucion)
# incluye un registro en Tasas.json con la fecha y el valor del dolar y euro en bolivares y
# y la fecha cuando se ejecuto esa actualizacion
#

# 1. Lee el archivo json historico principal (Tasas.json)
with open("Tasas.json", "r") as main_file:
    main_data = json.load(main_file)  

print("ultimo registro historico: ", main_data[-1])
print("Valor de Fecha del ultimo registro historico: ", main_data[-1]["Fecha_Proceso"])

Last_fecha = datetime.fromisoformat(main_data[-1]["Fecha_Proceso"])

# toma la informacion del nuevo registro a ser evaluado

eur = NVOJSON["EUR"]
usd = NVOJSON["USD"]
fecha = datetime.fromisoformat(NVOJSON["fecha"])
print("Fecha que viene del API del BCV: ", fecha)
Last_fecha = Last_fecha.replace(tzinfo=ZoneInfo("America/Caracas"))
fecha = fecha.replace(tzinfo=ZoneInfo("America/Caracas"))
#fecha = json.dumps(NVOJSON["fecha"], cls=DateTimeEncoder, indent=4)
print("Valor de Fecha del nuevo registro a evaluar: ", fecha)
#fecha = json.dumps(fecha, cls=DateTimeEncoder, indent=4)
#print("fecha el BCV nva: ", fecha)


if fecha > Last_fecha:
    print("Se debe incluir un nuevo registro en el archivo Tasas.json")
    # Crear un nuevo registro con la información de Respuesta.json
    #Last_fecha = Last_fecha.strftime("%x")
    #fecha = fecha.strftime("%x")
    fecha_proceso = datetime.now()
    fecha = fecha.replace(tzinfo=None)
    new_record = {
        "Fecha_Proceso": fecha_proceso.isoformat(),
        "Fecha_Valor": fecha.isoformat(),
        "USD": usd,
        "EUR": eur,
    }

    print("Nuevo registro a agregar: ", new_record)
    
    # Agregar el nuevo registro al historial principal
    main_data.append(new_record)
    
    # Guardar los cambios en el archivo Tasas.json
    with open("Tasas.json", "w") as main_file:
        json.dump(main_data, main_file, indent=4,ensure_ascii=False,default=str)    
    print("Nuevo registro agregado a Tasas.json")