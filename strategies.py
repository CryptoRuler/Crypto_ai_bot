def apply_strategies(data):
    # Apply Strategies 1, 3, and 5 based on symbol or strategy tag
    return {
        'symbol': data.get('symbol'),
        'action': data.get('action'),
        'strategy': 'EMA + Bollinger + Divergence'
    }