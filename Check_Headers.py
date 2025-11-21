import requests
import sys
import colorama
from colorama import Fore, init

init(autoreset=True)

#Lista com alguns headers de segurança
HEADERS_TO_CHECK = [
    'Strict-Transport-Security',
    'Content-Security-Policy',
    'X-Frame-Options',
    'X-Content-Type-Options',
    'Clear-Site-Data',
    'Permissions-Policy',
    'Cross-Origin-Opener-Policy'
]

#Verifica se o comando pra rodar o script foi inserido corretamente.
if len(sys.argv) != 2:
    print(f"{Fore.YELLOW}Something went wrong with your command. To run the script, please type: 'Python Check_Headers.py (website)")
    sys.exit()

#Tenta fazer a execução da lógica principal do script
try:
    url = sys.argv[1]
    if (not url.startswith("https://") and (not url.startswith("http://"))):
        url = "https://" + url
     
    #Criação de um header de usuário, para enviar a requisição do site como se fosse um usuário comum e não um script.
    user_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36'
    }

    #Faz a requisição ao site e armazena a resposta na variável
    response = requests.get(url, headers=user_headers, timeout=5)
    
    cont = 0
    #Contagem e checagem dos Headers na resposta do site
    for header in HEADERS_TO_CHECK:
        if header in response.headers:
            cont +=1
            print(f"{Fore.GREEN}{header} ✅ {cont}/7")
        else:
            print(f"{Fore.RED}{header} ❌ {cont}/7")


#Erro de conexão com o site
except requests.exceptions.ConnectionError:
    print(f"{Fore.YELLOW}The connection to the website failed.")
    sys.exit()

#Erro de timeout (resposta do site excedeu o tempo limite de 5s)
except requests.exceptions.Timeout:
    print(f"{Fore.YELLOW}The website's response timed out.")
    sys.exit()

#Qualquer outro erro
except Exception:
    print(f"{Fore.YELLOW} Something went wrong, please try again.")
    sys.exit()