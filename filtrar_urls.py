import re

def filtrar_urls(archivo):
    # Expresión regular para detectar dominios con 'shop' y URLs que terminan en '.html'
    regex = re.compile(r'https?://[^/]*shop[^/]*.*\.html$')
    
    urls_filtradas = set()  # Utilizamos un set para eliminar duplicados
    total_urls = 0
    
    try:
        # Leer el archivo en bloques
        with open(archivo, 'r', encoding='utf-8') as file:
            for linea in file:
                url = linea.strip()  # Eliminar espacios en blanco y saltos de línea
                if regex.match(url):
                    if url not in urls_filtradas:
                        urls_filtradas.add(url)
                        total_urls += 1
    except FileNotFoundError:
        print(f"Error: El archivo {archivo} no se encuentra.")
        return
    
    # Imprimir resultados
    print(f"Total de URLs válidas: {total_urls}")
    print("Listado de URLs válidas:")
    for url in urls_filtradas:
        print(url)

# Instrucciones para ejecutar el programa:
# 1. Guarda este código en un archivo Python, por ejemplo, 'filtrar_urls.py'.
# 2. Asegúrate de tener el archivo de URLs en el mismo directorio, por ejemplo, 'urls.txt'.
# 3. Ejecuta el programa desde la terminal o línea de comandos usando:
#    python filtrar_urls.py

if __name__ == "__main__":
    # Ruta del archivo de texto con las URLs
    archivo_urls = "urls.txt"
    filtrar_urls(archivo_urls)
