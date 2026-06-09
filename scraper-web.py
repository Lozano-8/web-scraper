###################################################################
# Desarrollado por Lozano https://github.com/Lozano-8/web-scraper #
###################################################################
# Instalar dependencias con "pip install requests" y "pip install beautifulsoup4"
import requests
from bs4 import BeautifulSoup

# Almaceno la url del usuario para hacer web scraping
url = str(input("Dame una url para hacer web scraching: "))
# Hago una peticion get a la pagina introducida por el usuario
request = requests.get(url)
# Almaceno en una variable la codificacion de la pagina solicitada
codificacion = request.apparent_encoding
# Cambiar la codificacion a la codificacion de la pagina
request.encoding = codificacion
# Almaceno el codigo en una variable
html = request.text
# Creo el objeto de BeautifulSoup para luego pasarlo a archivo
html = BeautifulSoup(html, 'html.parser')
# Creo un archivo
with open('codigo.html', 'w', encoding="UTF-8" ) as archivo:
    archivo.write(str(html))