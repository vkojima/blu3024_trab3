import requests

book_name = "Os patetinhas"

data = {
    "titulo": "",
    "editora": "",
    "cidade": "",
    "ano": "",
    "pagina": "",
    "isbn": "",
    "assunto": ""
    }

requests.post('150.162.221.93:5000/sendbooks', data=data)