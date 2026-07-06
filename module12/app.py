#!/usr/bin/env python3
from flask import Flask
from ping3 import ping

app = Flask(__name__)

@app.route('/')
def ping_google():
    try:
        response = ping("google.com", timeout=3)
        if response is not None:
            return f"Пинг google.com успешен! Время: {response:.2f} мс!!!"
        else:
            return "Пинг google.com не удался (нет ответа)!!!"
    except Exception as e:
        return f"Ошибка: {e}!!!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)
