from flask import Flask, request
import Database_Connection

app = Flask(__name__)

# "Banco de dados" por enquanto
livros = [{"id": "1", "titulo": "Cem Anos de Solidão", "editora": "Harper & Row", "cidade": "Nova York", "ano": "1967", "pagina": "417", "isbn": "9780060531041", "assunto": ["Realismo mágico", "Ficção latino-americana"]},
          {"id": "2", "titulo": "1984", "editora": "Secker & Warburg", "cidade": "Londres", "ano": "1949", "pagina": "328", "isbn": "9780451524935", "assunto": ["Distopia", "Ficção política"]},
          {"id": "3", "titulo": "O Senhor dos Anéis: A Sociedade do Anel", "editora": "Allen & Unwin", "cidade": "Londres", "ano": "1954", "pagina": "423", "isbn": "9780261103573", "assunto": ["Fantasia épica", "Literatura de aventura"]},
          {"id": "4", "titulo": "O Pequeno Príncipe", "editora": "Reynal & Hitchcock", "cidade": "Nova York", "ano": "1943", "pagina": "96", "isbn": "9780156012195", "assunto": ["Literatura infantojuvenil", "Filosofia"]},
          {"id": "5", "titulo": "Harry Potter e a Pedra Filosofal", "editora": "Bloomsbury Publishing", "cidade": "Londres", "ano": "1997", "pagina": "223", "isbn": "9780747532743", "assunto": ["Fantasia", "Magia", "Aventura infantojuvenil"]}]


# 1.1 Enviar dados de livros de uma biblioteca acadêmica. A aplicação deve permitir enviar ao servidor,
# através de uma requisição http, os dados de referências bibliográficas. Os dados devem ser enviados em formato JSON.
@app.route('/sendbook', methods=['POST'])
def send_book():
    book_data = request.json

    return "Dados inseridos com sucesso no banco de dados!"


# 1.2 Obter dados de todos os livros da blblioteca.  A aplicação deve permitir, através de uma requisição 
# http, obter os dados de todos os livros armazenados pelo servidor web. Os dados devem ser retornados em formato JSON.
@app.route('/getbooks', method=['GET'])
def get_all_books():

    return


# 1.3 Obter os dados de um livro. A aplicação deve permitir, através de uma requisição http, obter os dados 
# do livro partir de ISBN. O código deve ser enviado na requisição http. Os dados devem ser retornados em formato JSON.
@app.route('/getbook/isbn/<int:isbn>')
def get_book_by_isbn():

    return


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port="5000")
