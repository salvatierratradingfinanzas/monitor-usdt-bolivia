import requests
import json
import os
from datetime import datetime, timedelta

def obtener_precio():
    url = "https://criptoya.com/api/binancep2p/usdt/bob/1"
    try:
        response = requests.get(url)
        data = response.json()
        precio = float(data['price']) 
        
        hora_bolivia = datetime.utcnow() + timedelta(hours=-4)
        fecha_formateada = hora_bolivia.strftime('%Y-%m-%d %H:%M')

        archivo_nombre = 'data.json'
        
        if os.path.exists(archivo_nombre):
            with open(archivo_nombre, 'r') as f:
                try:
                    historial = json.load(f)
                except:
                    historial = []
        else:
            historial = []

        historial.append({"fecha": fecha_formateada, "precio": precio})

        with open(archivo_nombre, 'w') as f:
            json.dump(historial, f, indent=4)
            
        print(f"Exito: {fecha_formateada} - {precio}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    obtener_precio()
