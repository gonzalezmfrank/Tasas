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

# print("La fecha valor es : ",fecha_alp)

dt = datetime.fromisoformat(fecha_alp)

for orden in data["rates"]:
	if orden["type"]=="reference":
		if orden["base"]=="USD":
			usd=orden["mid"]
			#print("Valor del Dolar : ",orden["mid"])
		elif orden["base"]=="EUR":
			eur=orden["mid"]
			# print("Valor del Euro : ",orden["mid"])

NVOJSON = {

	"fecha" : datetime.strftime(dt,"%d/%m/%Y"),
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

