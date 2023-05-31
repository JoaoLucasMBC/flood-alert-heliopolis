import requests
import datetime

def get_json_from_api(url):
    response = requests.get(url)
    if response.status_code == 200:
        json_data = response.json()
        return json_data
    else:
        return None
    
def create_url(date=None):
    if date is None:
        date = get_date_tomorrow()
    #return f"https://api.open-meteo.com/v1/forecast?latitude=-23.6045&longitude=-46.5983&hourly=precipitation_probability,precipitation&daily=precipitation_sum&forecast_days=1&start_date={date}&end_date={date}&timezone=America%2FSao_Paulo"
    return f'http://api.weatherapi.com/v1/forecast.json?key=52b5fb87e51a4a50ab6134613233005&q=-23.606820,-46.596861&days=7'
    
def get_date_tomorrow():
    tomorrow = datetime.datetime.today() + datetime.timedelta(days=1)
    tomorrow = tomorrow.strftime("%Y/%m/%d").replace("/","-")
    return tomorrow

def verify_risk(date=None):
    url = create_url(date)
    json = get_json_from_api(url)
    try:
        precipitation = json['hourly']['precipitation']
        #return True caso todos sejam menores de 20, caso contrario retorna false
        if not all(x < 20 for x in precipitation) or sum(precipitation) > 25:
            return True #Tem risco
        return False
    except:
        return False


if __name__ == "__main__":
    print(verify_risk(f'2023-05-31'))