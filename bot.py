# import requests
# import json
# import os
# from datetime import datetime, timedelta

# def obtener_precio():
#     url = "https://criptoya.com/api/binancep2p/usdt/bob/1"
#     try:
#         response = requests.get(url)
#         data = response.json()
#         precio = float(data['price']) 
        
#         hora_bolivia = datetime.utcnow() + timedelta(hours=-4)
#         fecha_formateada = hora_bolivia.strftime('%Y-%m-%d %H:%M')

#         archivo_nombre = 'data.json'
        
#         if os.path.exists(archivo_nombre):
#             with open(archivo_nombre, 'r') as f:
#                 try:
#                     historial = json.load(f)
#                 except:
#                     historial = []
#         else:
#             historial = []

#         historial.append({"fecha": fecha_formateada, "precio": precio})

#         with open(archivo_nombre, 'w') as f:
#             json.dump(historial, f, indent=4)
            
#         print(f"Exito: {fecha_formateada} - {precio}")
#     except Exception as e:
#         print(f"Error: {e}")

# if __name__ == "__main__":
#     obtener_precio()


import requests
import json
import os
from datetime import datetime, timedelta

def obtener_precio():
    # URL de CriptoYa para Binance P2P USDT/BOB
    url = "https://criptoya.com/api/binancep2p/usdt/bob/1"
    archivo_nombre = 'data.json'
    
    try:
        # Añadimos un timeout de 10 segundos por seguridad
        response = requests.get(url, timeout=10)
        response.raise_for_status() # Lanza error si la respuesta no es 200
        
        data = response.json()
        precio = float(data['ask']) # 'ask' suele ser más preciso para compra rápida

        # Configuración de hora local Bolivia
        hora_bolivia = datetime.utcnow() - timedelta(hours=4)
        fecha_formateada = hora_bolivia.strftime('%Y-%m-%d %H:%M')

        # Cargar historial existente
        if os.path.exists(archivo_nombre) and os.path.getsize(archivo_nombre) > 0:
            with open(archivo_nombre, 'r') as f:
                try:
                    historial = json.load(f)
                except json.JSONDecodeError:
                    historial = []
        else:
            historial = []

        # Agregar nuevo registro
        historial.append({"fecha": fecha_formateada, "precio": precio})

        # Opcional: Mantener solo los últimos 1000 registros para no saturar el disco
        # historial = historial[-1000:]

        # Guardar en el archivo
        with open(archivo_nombre, 'w') as f:
            json.dump(historial, f, indent=4)
            
        print(f"Éxito: {fecha_formateada} -> Bs. {precio}")

    except requests.exceptions.RequestException as e:
        print(f"Error de conexión: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")

if __name__ == "__main__":
    obtener_precio()
