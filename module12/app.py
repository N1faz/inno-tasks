#!/usr/bin/env python3
import os
from flask import Flask
from ping3 import ping
import psycopg2

app = Flask(__name__)

# Подключение к БД
DATABASE_URL = os.getenv("DATABASE_URL")

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

@app.route('/db')
def check_db():
    try:
        conn = psycopg2.connect(DATABASE_URL)
        return "Подключение к PostgreSQL успешно!"
    except Exception as e:
        return f"Ошибка подключения к БД: {e}"

@app.route('/app')
def app_route():
    return "Добро пожаловать на /app!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)
