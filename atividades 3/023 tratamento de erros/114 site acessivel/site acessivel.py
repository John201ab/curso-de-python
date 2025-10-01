
import urllib.request

url = "https://www.pudim.com.br/"

try:
    response = urllib.request.urlopen(url)
    print("O site está online! Código:", response.getcode())
except urllib.error.URLError as e:
    print("Erro ao acessar o site:", e.reason)