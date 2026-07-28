import os
import requests
import pandas as pd
import urllib.request
import ssl



def load_AUH_data():
    # 1. Configurar la ruta absoluta del proyecto para guardar en la carpeta global por fuera de src
    ruta_script = os.path.abspath(__file__)
    raiz_proyecto = os.path.dirname(os.path.dirname(os.path.dirname(ruta_script)))
    
    carpeta_destino = os.path.join(raiz_proyecto, "data", "raw", "AUH")
    ruta_guardado = os.path.join(carpeta_destino, "boletin_auh_febrero_2026_raw.xlsx")

    os.makedirs(carpeta_destino, exist_ok=True)

    # 2. URL REAL DEL ARCHIVO EXCEL (No la de la página web principal)
    # Nota: ANSES suele publicar sus series en links específicos de su CDN o servidor de estadísticas.
    # Como ejemplo, usamos la estructura típica de sus archivos editables (.xls/.xlsx)
    url_directa_excel = "https://anses.gob.ar"

    print("Descargando el boletín estadístico real de la AUH...")

    try:
        # Bypassear posibles problemas de certificados estatales
        context = ssl._create_unverified_context()
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
        req = urllib.request.Request(url_directa_excel, headers=headers)

        # Descargamos los bytes del Excel real
        with urllib.request.urlopen(req, context=context) as response:
            contenido_binario = response.read()
        
        # Guardamos en tu disco el archivo verdadero
        with open(ruta_guardado, 'wb') as f:
            f.write(contenido_binario)
            
        print(f"¡Listo! Archivo de Excel real guardado con éxito en:\n--> {ruta_guardado}")

    except Exception as e:
        print(f"\n[AVISO] No se pudo automatizar la descarga directa por restricciones del servidor: {e}")
        print("Los servidores de ANSES suelen cambiar los tokens de sus archivos adjuntos.")
        print("Si falla, te conviene descargarlo manualmente desde la sección oficial:")
        print("--> http://anses.gob.ar")


def load_CBT_CBA():
    # ESPERAR QUE SALGA EN DATOS ARGENTINA
    pass

def load_IPC_NAC():
    # URL del servidor alternativo estable (CSV)
    url_directa = "https://datos.gob.ar"
    ruta_guardado = "../data/raw/IPC/IPC_raw.csv"

    os.makedirs("../data/raw/IPC", exist_ok=True)
    print("Descargando el IPC desde el servidor alternativo simulando navegador...")

    try:
        # 1. Crear el contexto SSL permisivo para certificados inválidos
        context = ssl._create_unverified_context()

        # 2. Configurar el User-Agent para simular un navegador real y evitar el bloqueo 403
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
        
        # 3. Crear la petición formal con los encabezados incluidos
        req = urllib.request.Request(url_directa, headers=headers)

        # 4. Abrir la conexión y leerla con Pandas
        with urllib.request.urlopen(req, context=context) as response:
            df = pd.read_csv(response, sep=None, engine='python', on_bad_lines='skip')
        
        # 5. Guardar el archivo localmente en tu carpeta
        df.to_csv(ruta_guardado, index=False)
        print(f"¡Listo! Archivo CSV descargado y guardado en: {ruta_guardado}")
        
        # Mostramos las últimas filas para verificar que las columnas coincidan
        print("\nEstructura de datos detectada:")
        print(df.tail(3))

    except Exception as e:
        print(f"\n[ERROR] No se pudo procesar: {e}")


#load_IPC_NAC()
#load_AUH_data()