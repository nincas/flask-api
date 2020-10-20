import flask
from flask import request, jsonify
from src.Redis import Redis

app = flask.Flask(__name__)
app.config["DEBUG"] = True

redis = Redis()

# Error handler
@app.errorhandler(404)
def page_not_found(e):
    return jsonify({
        'error': 0,
        'message': 'Request resource not found.'
    }), 404

# Landing route
@app.route('/', methods=['GET'])
def home():
    return "<h1>API</h1><p>...</p>"


# Main routes below:
@app.route('/get/binance', methods=['GET'])
def binance():
    val = redis.getValue('btc-value-binance')
    if val != None:
        val = val.decode('utf-8')
    else:
        val = False

    arguments = request.args
    
    return jsonify({
        'currency': 'USD',
        'price': float(val) if val else 0.00
    })

@app.route('/get/bitmex', methods=['GET'])
def bitmex():
    val = redis.getValue('btc-value-bitmex')
    if val != None:
        val = val.decode('utf-8')
    else:
        val = False

    arguments = request.args
    
    return jsonify({
        'currency': 'USD',
        'price': float(val) if val else float(0.0)
    })

@app.route('/get/blockchain', methods=['GET'])
def blockchain():
    val = redis.getValue('btc-value-blockchain')
    if val != None:
        val = val.decode('utf-8')
    else:
        val = False

    arguments = request.args
    
    return jsonify({
        'currency': 'USD',
        'price': float(val) if val else float(0.0)
    })

app.register_error_handler(404, page_not_found)
app.run()