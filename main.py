from flask import Flask, request
import Database_Connection

app = Flask(__name__)

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
