from flask import Flask, jsonify, request
import requests

url_prod = 'http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_02'

app = Flask(__name__)

@app.route('/fetch-data', methods=['GET'])
def fetch_data():
    try:
        response = requests.get(url_prod)
        response.raise_for_status()  # Levanta um erro para códigos de status HTTP 4xx/5xx
        if response.headers.get('Content-Type') == 'application/json':
            data = response.json()  # Assumindo que a resposta é JSON
            return jsonify(data)
        else:
            return jsonify({"error": "Resposta não é um JSON válido", "content": response.text}), 500
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

app.run(debug=True)
