import requests
import json

def _get(url):

    headersList = {
    "Accept": "*/*",
    "User-Agent": "Thunder Client (https://www.thunderclient.com)" 
    }

    response = requests.request("GET", url=url, headers=headersList)

    return response.text

def _post(url):

    headersList = {
        "Accept": "*/*",
        "User-Agent": "Thunder Client (https://www.thunderclient.com)",
        "Content-Type": "application/json" 
    }

    payload = json.dumps({
        "titulo": "O código da vinci",
        "genero": "Suspense",
        "ano": 2006
        })

    response = requests.request("POST", url, data=payload,  headers=headersList)

    return response

if __name__ == '__main__':
    url = 'http://localhost:8000/filmes'
    post = _post(url=url)
    print(post)
