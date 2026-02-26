import requests
import json
from datetime import datetime
import os

def capturar_precio():
    url = "https://criptoya.com/api/binancep2p/usdt/bob/1"
    try:
        response = requests.get(url)
        datos = response.json()
        precio = datos['ask'] # Precio de venta
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M")
        
        nuevo_dato = {"fecha": fecha, "precio": precio}
        
        # Leer datos existentes para no borrar el historial
        historial = []
        if os.path.exists("data.json"):
            with open("data.json", "r") as f:
                historial = json.load(f)
        
        historial.append(nuevo_dato)
        
        # Guardar historial actualizado
        with open("data.json", "w") as f:
            json.dump(historial, f, indent=4)
            
        print(f"Hexx reporta: Nuevo precio guardado {precio} BOB")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    capturar_precio()
