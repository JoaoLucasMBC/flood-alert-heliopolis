import requests
import datetime
import os

def get_json_from_api(url):
    response = requests.get(url)
    if response.status_code == 200:
        json_data = response.json()
        return json_data
    else:
        return None
    

def create_url(date=datetime.datetime.today().strftime('%Y-%m-%d')):
    return f"https://api.open-meteo.com/v1/forecast?latitude=-23.6045&longitude=-46.5983&hourly=precipitation_probability,precipitation&daily=precipitation_sum&forecast_days=1&start_date={date}&end_date={date}&timezone=America%2FSao_Paulo"


def verify_risk_today():
    url = create_url()
    json = get_json_from_api(url)
    try:
        precipitation = json['hourly']['precipitation']

        if sum(precipitation) > 25 or sum(precipitation)/datetime.datetime.now().hour > 4:
            return True #Tem risco
        return False
    
    except:
        return False


def verify_risk_tomorrow():
    url = f'http://api.weatherapi.com/v1/forecast.json?key={os.environ.get("WEATHER_API_KEY")}&q=-23.606820,-46.596861&days=7'
    json = get_json_from_api(url)

    try:
        tomorrow = json['forecast']['forecastday'][1]['day']['totalprecip_mm']
    
        if tomorrow > 10:
            return True #Tem risco
        return False
    
    except:
        return False



if __name__ == "__main__":
    print(verify_risk_today())
    print(verify_risk_tomorrow())