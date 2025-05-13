from flask import Flask, render_template
import weather
import pprint

app = Flask(__name__)

@app.template_filter('pprint')
def pprint_filter(obj):
    return pprint.pformat(obj)

@app.route('/')
def home():
    location = "Minneapolis,MN,US"
    weather_data = weather.get_weather(location)
    
    print("Weather data requested")
    print(f"Type: {type(weather_data)}")
    if weather_data:
        print("Weather data received successfully")
    else:
        print("Weather data is None")
    
    return render_template('index.html', weather=weather_data)

# Add a route to serve static files (just to be sure)
@app.route('/static/<path:filename>')
def static_files(filename):
    return app.send_static_file(filename)

if __name__ == '__main__':
    app.run(debug=True)