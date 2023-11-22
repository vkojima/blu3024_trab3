import mysql.connector
 
def insert(data):

    db_connection = mysql.connector.connect(
        host="seu_host",
        user="seu_usuario",
        password="sua_senha",
        database="seu_banco_de_dados"
    )

    cursor = db_connection.cursor()

    cursor.execute("INSERT INTO livros (titulo, editora, cidade, ano, pagina, isbn, assunto) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", 
                   (data.get("id"),
                    data.get("titulo"),
                    data.get("editora"),
                    data.get("cidade"),
                    data.get("ano"),
                    data.get("pagina"),
                    data.get("isbn"),
                    data.get("assunto")))

    db_connection.commit()
    cursor.close()
    db_connection.close()