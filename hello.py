from flask import Flask, render_template
from suds.client import Client

app = Flask(__name__)


@app.route('/')
def index():
    # Création d'une instance du client SOAP
    client = Client('http://localhost:8000/soap/hello?wsdl')

    # Appel de la méthode say_hello du serveur SOAP
    response = client.service.say_hello("John")

    # Renvoi de la réponse à la page web
    return render_template('index.html', response=response)


if __name__ == '__main__':
    app.run(debug=True)
