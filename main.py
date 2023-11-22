from flask import Flask, request
import json
import requests

app = Flask(__name__)


@app.route('/sendbooks', method=['POST'])
def sendbooks():
    response = request.get_json()


    "SELECT * FROM alunos WHERE id = %s", (aluno_id)
    query = "INSERT INTO %s" 

@app.route('/getbooks', method=['GET'])
def getbooks():


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=False)