from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    weather = None
    error = None
    if request.method == 'POST':
        city = request.form['city']
        weather, error = get_weather(city)
    return render_template("index.html", weather=weather, error=error)

def get_weather(city):
    api_key = "3fef74ee2c56c7e1881a503252d7ceaf"  # Замените "ваш_ключ" на ваш реальный API ключ
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json(), None
    else:
        return None, "Ошибка получения данных о погоде. Пожалуйста, проверьте название города и попробуйте снова."

if __name__ == '__main__':
    app.run(debug=True)
