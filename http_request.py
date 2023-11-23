import requests

data = {
    "id": "",
    "titulo": "",
    "editora": "",
    "cidade": "",
    "ano": "",
    "pagina": "",
    "isbn": "",
    "assunto": ""
    }

requests.post('150.162.221.93:5000/sendbook', data=data)