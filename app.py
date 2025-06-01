from flask import Flask, request, jsonify
from strategies import apply_strategies
from ai_module import ai_filter
from telegram_bot import send_telegram_alert

app = Flask(__name__)

@app.route('/webhook/tradingview', methods=['POST'])
def webhook():
    data = request.json
    signal = apply_strategies(data)
    analysis = ai_filter(signal)
    send_telegram_alert(analysis)
    return jsonify({'status': 'Signal processed', 'analysis': analysis})

@app.route('/status')
def status():
    return jsonify({'status': 'Bot is running'})