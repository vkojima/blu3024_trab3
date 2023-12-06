import requests

headers = {
    'Content-Type': 'application/json',
}

data = '{"id": "16", "titulo": "Novo Livro2", "editora": "Editora A", "cidade": "São Paulo2", "ano": "2023", "pagina": "300", "isbn": "9781234567890", "assunto": ["Fic\xE7\xE3o", "Aventura"] }'

## Envio de novo livro
response_post = requests.post('http://localhost:3000/books', headers=headers, data=data)

if (response_post.status_code == 201):
    print("Livro adicionado com sucesso.\n\n")


## Busca de livro por ISBN
ISBN = '9780060531041'
http_response_isbn = requests.get('http://localhost:3000/books/' + ISBN)

content_isbn = http_response_isbn.json()

print(f"Busca por ISBN: {ISBN}")
print(f"Título: {content_isbn['titulo']}")
print(f"Editora: {content_isbn['editora']}")
print(f"Cidade: {content_isbn['cidade']}")
print(f"Ano: {content_isbn['ano']}")
print(f"Páginas: {content_isbn['pagina']}")
print(f"ISBN: {content_isbn['isbn']}")
print(f"Assunto: {', '.join(content_isbn['assunto'])}\n\n")

## Busca de todos os livros
http_response_all_books = requests.get('http://localhost:3000/books')

content = http_response_all_books.json()

print("Buscar todos os livros:\n")

for livro in content:
    print(f"Título: {livro['titulo']}")
    print(f"Editora: {livro['editora']}")
    print(f"Cidade: {livro['cidade']}")
    print(f"Ano: {livro['ano']}")
    print(f"Páginas: {livro['pagina']}")
    print(f"ISBN: {livro['isbn']}")
    print(f"Assunto: {', '.join(livro['assunto'])}\n")

