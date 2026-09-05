import json, datetime, platform

from datetime import date, time, datetime, timedelta
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
