from flask import Flask, render_template, request
import requests
app = Flask(__name__, template_folder='template')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/weather', methods=['GET', 'POST'])
def weather():
    if request.method == 'POST':
        city_name = request.form['name']
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&APPID=0892de34cf613eef5a90fca243c121f6'
        response = requests.get(url.format(city_name)).json()
        if response.get('cod') != 200:
            error_message = response.get('message', 'City not found')
            return render_template('index.html', error=error_message)
        temp = response['main']['temp']
        country = response['sys']['country']
        icon = response['weather'][0]['icon']
        feels = response['main']['feels_like']
        des_weather = response['weather'][0]['description']
        high_temp = response['main']['temp_max']
        low_temp = response['main']['temp_min']
        return render_template('weather.html', city_name=city_name, country=country,
                               temp=temp, icon=icon, feels=feels, high_temp=high_temp,
                               low_temp=low_temp, des_weather=des_weather)


app.run(debug=True)
