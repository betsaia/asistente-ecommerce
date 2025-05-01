from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/comparar-producto', methods=['GET'])
def comparar_producto():
    producto = request.args.get('q', '')

    # Buscar en Mercado Libre Chile
    url_ml = f"https://api.mercadolibre.com/sites/MLC/search?q={producto}&limit=5"
    res_ml = requests.get(url_ml)
    datos_ml = res_ml.json()

    resultados = []
    for item in datos_ml.get("results", []):
        resultados.append({
            "titulo": item.get("title", ""),
            "precio": item.get("price", 0),
            "ventas": item.get("sold_quantity", 0),
            "link": item.get("permalink", "")
        })

    return jsonify({
        "producto": producto,
        "mercado_libre_resultados": resultados,
        "alibaba_resultados": "Aquí se agregará Alibaba en el siguiente paso"
    })
