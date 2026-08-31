import json,datetime
from datetime import date, time, datetime, timedelta

with open('Respuesta.json', mode="r", encoding="utf-8") as read_file:
	Tasas_data = json.load(read_file)

print(f"el resultado es:",Tasas_data)

#print(type(Tasas_data)) # <class 'dict'>
#print(type(Tasas_data["fecha"])) # <class 'str'>
fecha_gen=Tasas_data["fecha"]

print("La fecha valor es : ",fecha_gen)

dt = datetime.strptime(fecha_gen, "%d/%m/%Y")
#print(type(dt)) # <class 'datetime.datetime'>
print ("La fecha valor del registro es : ",dt)

