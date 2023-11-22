from flask import Flask, request
import mysql.connector
import json

app = Flask(__name__)

@app.route('/sendbooks', methods=['POST'])
def sendbooks():
    book_data = request.json

    db_connection = mysql.connector.connect(
        host="seu_host",
        user="seu_usuario",
        password="sua_senha",
        database="seu_banco_de_dados"
    )

    cursor = db_connection.cursor()

    cursor.execute("INSERT INTO livros (titulo, editora, cidade, ano, pagina, isbn, assunto) VALUES (%s, %s, %s, %s, %s, %s, %s)", 
                   (book_data.get("titulo"),
                    book_data.get("editora"),
                    book_data.get("cidade"),
                    book_data.get("ano"),
                    book_data.get("pagina"),
                    book_data.get("isbn"),
                    book_data.get("assunto")))

    db_connection.commit()
    cursor.close()
    db_connection.close()

    return "Dados inseridos com sucesso no banco de dados!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port="5000")
