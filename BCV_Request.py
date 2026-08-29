import os,requests,sys,json

from KEY import CLAVE
from KEY import URL
from KEY import ARCHIVO
from KEY import ARCHIVO2

from pathlib import Path

print("el API Key es :",CLAVE)
##print("el URL es :",URL)

bcv = requests.get(
    URL,
    headers={'X-API-Key': CLAVE},
)
#print(bcv.status)
data = bcv.json()

##ARCHIVO = os.getcwd()+ARCHIVO
ARCHIVO2 =str(Path.cwd())+"\\" + ARCHIVO2

print("el directorio es :",ARCHIVO2)

ARCHIVO = ARCHIVO2

try:
	with open(ARCHIVO,"r+", encoding="utf-8") as f:
     #		datos = json.load(f)
		f.seek(0)
		f.truncate() 
		json.dump(data, f, indent=4, ensure_ascii=False)
except FileNotFoundError:
	with open(ARCHIVO,"w",encoding="utf-8") as f:
		print("archivo no existia ... fue creado")
		json.dump(data, f, indent=4, ensure_ascii=False)
else:
	print("el resultado es:",data)
	print(f"Total de rates: {len(data['rates'])}")

# Crea el json con los valores de la fecha

