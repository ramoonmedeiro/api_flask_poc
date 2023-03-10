import requests
import json

def _get(url):
    r = requests.get(url)
    return json.loads(r.text)

def _post(url, d):
    r = requests.post(url, data=d)
    return json.loads(r.text)

def _put():
    pass

def _delete(url):
    r = requests.delete(url)
    return json.loads(r.text)

if __name__ == '__main__':
    
    id_filme = 3
    URL =f'http://localhost:8000/filmes/{id_filme}'

    # GET method
    #print(_get(url=URL))

    # POST Method
    #d = {
    #    'titulo': 'Código Da Vinci',
    #    'genero': 'ação',
    #    'ano': 2003
    #}
    #print(_post(url=URL, d=d))

    # PUT method

    # DELETE method
    print(_delete(url=URL))