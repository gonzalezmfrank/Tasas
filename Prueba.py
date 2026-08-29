import json,datetime
from datetime import date, time, datetime, timedelta

with open('Respuesta.json', mode="r", encoding="utf-8") as read_file:
	Tasas_data = json.load(read_file)

#print(f"el resultado es:",Tasas_data)

#print(type(Tasas_data)) # <class 'dict'>

#print("El Index value es ",(Tasas_data["index"]["value"]))

#for rates in Tasas_data:
#	print(rates["base"],rates["mid"])

fecha_alp=Tasas_data["index"]["as_of"]

print("La fecha valor es : ",fecha_alp)

dt = datetime.fromisoformat(fecha_alp)

#print("Fecha es	: ",dt.day," de ",dt.month," de ",dt.year)

print(datetime.strftime(dt, "%d/%m/%Y %H:%M"))



#dt = datetime.strptime(fecha_alp, "%Y-%m-%d %H:%M")

#print("La fecha valor es : ",datetime.datetime(Tasas_data["index"]["as_of"]))

#class Tasas:
#	def __init__(self,currency,base,rates,index,usd,eur,fecha):
#		self.currency = currency
#		self.base = base
#		self.rates = rates
#		self.index = index
#		seif.usd = usd
#		self.eur = eur
#		self.fecha = fecha


#rates = Tasas_data['rates']

#print(type(rates)) ## List

#print("Numero de Valores en el array es ",len(Tasas_data['rates']))

for orden in Tasas_data["rates"]:
	if orden["type"]=="reference":
		if orden["base"]=="USD":
			usd=orden["mid"]
			print("Valor del Dolar : ",orden["mid"])
		elif orden["base"]=="EUR":
			eur=orden["mid"]
			print("Valor del Euro : ",orden["mid"])

nvojs = {

	"fecha" : datetime.strftime(dt,"%d/%m/%Y"),
	"USD" : usd,
	"EUR" :eur

}

print(nvojs)

# 2. Abrir el archivo en modo escritura ('w') y guardar los datos
with open("datos.json", "w", encoding="utf-8") as archivo:
    json.dump(nvojs, archivo, ensure_ascii=False, indent=4)

#print("Valor del ",orden["mid"]," : ",orden["mid"])


#class TasasDecoder(json.JSONDecoder):
#    def __init__(self, object_hook=None, *args, **kwargs):
#        # set the custom object_hook method
#        super().__init__(object_hook=self.object_hook, *args, **kwargs)

    # class method containing the
    # custom parsing logic
#    def object_hook(self, json_dict):
#        new_tasas = Tasas(
#            json_dict.get('currency'),
#            json_dict.get('base'),
#            json_dict.get('rates'),
#            json_dict.get('index'),
#        )

#        return new_tasas

#print(type(Tasas)) # class = Type


#print(new_tasas.currency)

#with open("nvojason.json", mode="w", encoding="utf-8") as write_file:
#    json.dump(Tasas, write_file)
