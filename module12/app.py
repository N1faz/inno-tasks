#!/usr/bin/env python3
import os
from flask import Flask, Response
from ping3 import ping
import psycopg2
from prometheus_client import Counter, generate_latest, REGISTRY

app = Flask(__name__)

DATABASE_URL = os.getenv("DATABASE_URL")

# Создаем счетчик запросов
REQUESTS = Counter('http_requests_total', 'Total HTTP requests', ['endpoint'])

@app.route('/')
def ping_google():
    REQUESTS.labels(endpoint='/').inc()
    try:
        response = ping("google.com", timeout=3)
        if response is not None:
            return f"Пинг google.com успешен! Время: {response:.2f} мс!!!"
        else:
            return "Пинг google.com не удался (нет ответа)!!!"
    except Exception as e:
        return f"Ошибка: {e}!!!"

@app.route('/db')
def check_db():
    REQUESTS.labels(endpoint='/db').inc()
    try:
        conn = psycopg2.connect(DATABASE_URL)
        return "Подключение к PostgreSQL успешно!"
    except Exception as e:
        return f"Ошибка подключения к БД: {e}"

@app.route('/app')
def app_route():
    REQUESTS.labels(endpoint='/app').inc()
    return "Добро пожаловать на /app!"

@app.route('/metrics')
def metrics():
    return Response(generate_latest(REGISTRY), mimetype='text/plain')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)
