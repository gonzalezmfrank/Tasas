# Ejecuta el script para obtener el valor del dolar y euro en bolivares y lo guarda en un archivo json
# Solo guarda alli la data necesaria fecha, dolar y euro

import os,requests,sys,json,datetime,platform
from datetime import date, time, datetime, timedelta

from KEY import CLAVE
from KEY import URL
from KEY import ARCHIVO
from KEY import ARCHIVO2

from pathlib import Path
from sys import platform

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

NVOJSON = {

	"fecha" : dt.strftime("%d/%m/%Y"),
	"USD" : usd,
	"EUR" :eur

}

print("el contenido del JSon seria :",NVOJSON)

if platform == "linux" or platform == "linux2":
    # linux
	ARCHIVO ="/opt/SanLucas/Tasas/" + ARCHIVO2
elif platform == "darwin":
    # OS X
    ARCHIVO =str(Path.cwd())+"\\" + ARCHIVO2
elif platform == "win32":
	# Para Windows
    ARCHIVO =str(Path.cwd())+"\\" + ARCHIVO2

# ARCHIVO =str(Path.cwd())+"\\" + ARCHIVO2
print("Y se va a guardar en la ruta :",Path.cwd(),"Para el sistema operativo :",platform)

try:
	with open(ARCHIVO,"r+", encoding="utf-8") as f:
		f.seek(0)
		f.truncate() 
		json.dump(NVOJSON, f, indent=4, ensure_ascii=False)
except FileNotFoundError:
	with open(ARCHIVO,"w",encoding="utf-8") as f:
		print("archivo no existia ... fue creado")
		json.dump(NVOJSON, f, indent=4, ensure_ascii=False)
else:
	print("archivo ya existia ... fue actualizado")

# Crea el json con los valores de la fecha

# Toma el Json del scrip BCV_Request.py y su resultado lo evalua con el archivo Tasas.json
# Si valor de Respuesta.json en su ultimo registro no se encuentra (valida dia de ejecucion)
# incluye un registro en Tasas.json con la fecha y el valor del dolar y euro en bolivares y
# y la fecha cuando se ejecuto esa actualizacion
#

# 1. Lee el archivo json historico principal (Tasas.json)
with open("Tasas.json", "r") as main_file:
    main_data = json.load(main_file)  

# 2. Lee el archivo json de respuesta del script BCV_Request.py (Respuesta.json)
with open("Respuesta.json", "r") as other_file:
    other_data = json.load(other_file)

print("ultimo registro historico: ", main_data[-1])
print("Valor de Fecha del ultimo registro historico: ", main_data[-1]["Fecha_Proceso"])

Last_fecha = datetime.fromisoformat(main_data[-1]["Fecha_Proceso"])

# toma la informacion del nuevo registro a ser evaluado

eur = other_data["EUR"]
usd = other_data["USD"]
fecha = datetime.strptime(other_data["fecha"],"%d/%m/%Y")

if fecha > Last_fecha:
    print("Se debe incluir un nuevo registro en el archivo Tasas.json")
    # Crear un nuevo registro con la información de Respuesta.json
    #Last_fecha = Last_fecha.strftime("%x")
    #fecha = fecha.strftime("%x")
    fecha_proceso = datetime.now()
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