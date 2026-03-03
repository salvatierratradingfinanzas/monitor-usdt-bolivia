# def capturar_precio():
#     url = "https://criptoya.com/api/binancep2p/usdt/bob/1"
#     try:
#         response = requests.get(url)
#         datos = response.json()
#         precio = datos['ask'] # Precio de venta
#         fecha = datetime.now().strftime("%Y-%m-%d %H:%M")
        
#         nuevo_dato = {"fecha": fecha, "precio": precio}
        
#         # Leer datos existentes para no borrar el historial
#         historial = []
#         if os.path.exists("data.json"):
#             with open("data.json", "r") as f:
#                 historial = json.load(f)
        
#         historial.append(nuevo_dato)
        
#         # Guardar historial actualizado
#         with open("data.json", "w") as f:
#             json.dump(historial, f, indent=4)
            
#         print(f"Hexx reporta: Nuevo precio guardado {precio} BOB")
#     except Exception as e:
#         print(f"Error: {e}")

# if __name__ == "__main__":
#     capturar_precio()

# import requests
# import json
# from datetime import datetime, timedelta
# import os

# def obtener_precio():
#     url = "https://criptoya.com/api/binancep2p/usdt/bob/1" 
#     try:
#         response = requests.get(url)
#         data = response.json()
#         precio = float(data['price']) 
        
#         # 3. MANEJO DE LA HORA (La magia para Bolivia)
#         # datetime.utcnow() saca la hora de Londres (UTC) que usa el servidor de GitHub
#         # timedelta(hours=-4) le resta exactamente 4 horas para que sea hora de La Paz
#         hora_bolivia = datetime.utcnow() + timedelta(hours=-4)
        
#         # 4. Formateamos la fecha para que sea legible
#         # %Y-%m-%d %H:%M -> 2026-02-26 11:45
#         fecha_formateada = hora_bolivia.strftime('%Y-%m-%d %H:%M')

#         # 5. CARGAR DATOS EXISTENTES
#         # Intentamos abrir el archivo actual para no borrar lo que el bot ya recolectó
#         try:
#             with open('data.json', 'r') as f:
#                 historial = json.load(f)
#         except FileNotFoundError:
#             # Si el archivo no existe aún, creamos una lista vacía
#             historial = []

#         # 6. AGREGAR EL NUEVO PRECIO
#         nuevo_registro = {
#             "fecha": fecha_formateada,
#             "precio": precio
#         }
#         historial.append(nuevo_registro)

#         # 7. GUARDAR TODO DE NUEVO
#         # Guardamos la lista actualizada para que el archivo siga creciendo
#         with open('data.json', 'w') as f:
#             json.dump(historial, f, indent=4)
            
#         print(f"Éxito: {fecha_formateada} - Precio: {precio}")

#     except Exception as e:
#         print(f"Error: {e}")

# if __name__ == "__main__":
#     obtener_precio()




import requests
import json
from datetime import datetime, timedelta



def obtener_precio_usdt_bolivia():
    # 1. Definimos la URL de la API (CriptoYa es excelente para esto)
    # Buscamos el exchange 'binancep2p' para la moneda 'usdt' en Bolivia 'bob'
    url = "https://criptoya.com/api/binancep2p/usdt/bob/1"

    try:
        # 2. Hacemos la petición a la API
        response = requests.get(url)
        datos = response.json()

        # 3. Extraemos el precio de "puntas" (el promedio de compra/venta)
        # Usamos 'ask' que es el precio al que la gente está vendiendo
        precio = datos['ask']
        
        # 4. Obtenemos la fecha y hora actual
        fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # 5. Creamos el objeto de datos que guardaremos
        registro = {
            "fecha": fecha_actual,
            "precio": precio,
            "moneda": "BOB",
            "fuente": "Binance P2P via CriptoYa"
        }

        print(f"✅ Hexx ha capturado el precio: {precio} BOB a las {fecha_actual}")
        return registro

    except Exception as e:
        print(f"❌ Error al capturar datos: {e}")
        return None

# Ejecutamos la función
dato_obtenido = obtener_precio_usdt_bolivia()

# 6. Simulación de guardado (Aquí podrías mandarlo a una DB o Google Sheets)
if dato_obtenido:
    with open("precios_historial.json", "a") as archivo:
        archivo.write(json.dumps(dato_obtenido) + "\n")




def obtener_precio():
    # 1. Definimos la URL de la API (Binance u otra)
    # Aquí usarías la URL real que ya tenías funcionando
    url = "https://criptoya.com/api/binancep2p/usdt/bob/1"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        # 2. Extraemos el precio (ajusta según la estructura de tu JSON)
        # Ejemplo: 9.03
        precio = float(data['price']) 
        
        # 3. MANEJO DE LA HORA (La magia para Bolivia)
        # datetime.utcnow() saca la hora de Londres (UTC) que usa el servidor de GitHub
        # timedelta(hours=-4) le resta exactamente 4 horas para que sea hora de La Paz
        hora_bolivia = datetime.utcnow() + timedelta(hours=-4)
        
        # 4. Formateamos la fecha para que sea legible
        # %Y-%m-%d %H:%M -> 2026-02-26 11:45
        fecha_formateada = hora_bolivia.strftime('%Y-%m-%d %H:%M')

        # 5. CARGAR DATOS EXISTENTES
        # Intentamos abrir el archivo actual para no borrar lo que el bot ya recolectó
        try:
            with open('data.json', 'r') as f:
                historial = json.load(f)
        except FileNotFoundError:
            # Si el archivo no existe aún, creamos una lista vacía
            historial = []

        # 6. AGREGAR EL NUEVO PRECIO
        nuevo_registro = {
            "fecha": fecha_formateada,
            "precio": precio
        }
        historial.append(nuevo_registro)

        # 7. GUARDAR TODO DE NUEVO
        # Guardamos la lista actualizada para que el archivo siga creciendo
        with open('data.json', 'w') as f:
            json.dump(historial, f, indent=4)
            
        print(f"Éxito: {fecha_formateada} - Precio: {precio}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    obtener_precio()


