from flask import Flask, request, render_template
import requests

app = Flask(__name__)

API_KEY = "24a276cf80ecfe4c8e217c41766cc7c8"

@app.route('/', methods=['GET', 'POST'])
def weather():
    weather_data = None
    if request.method == 'POST':
        city = request.form.get('city')
        if city:
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                weather_data = {
                    'city': city,
                    'temperature': data['main']['temp'],
                    'description': data['weather'][0]['description'],
                    'icon': data['weather'][0]['icon']
                }
            else:
                weather_data = {'error': 'City not found!'}
    return render_template('weather.html', weather=weather_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
