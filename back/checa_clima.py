import requests
import datetime
from environ import WEATHER_API_KEY

def get_json_from_api(url):
    '''
    Função que recebe uma url e retorna um json com os dados da api

    @param url: url da api
    @return: json com os dados da api
    '''

    response = requests.get(url) # faz a requisição
    if response.status_code == 200: # verifica se a requisição foi bem sucedida
        json_data = response.json() # transforma a resposta em json
        return json_data
    else:
        return None
    

def create_url(date=datetime.datetime.today().strftime('%Y-%m-%d')):
    '''
    Função que cria a url para a api do open-meteo

    @param date: data para a qual se quer a previsão do tempo
    @return: url da api
    '''
    return f"https://api.open-meteo.com/v1/forecast?latitude=-23.6045&longitude=-46.5983&hourly=precipitation_probability,precipitation&daily=precipitation_sum&forecast_days=1&start_date={date}&end_date={date}&timezone=America%2FSao_Paulo"


def verify_risk_today():
    '''
    Função que verifica se há risco de enchente hoje

    @return: True se há risco, False se não há
    '''
    url = create_url() # cria a url
    json = get_json_from_api(url) # pega o json da api

    try:
        precipitation = json['hourly']['precipitation'] # pega a lista de precipitação

        if sum(precipitation) > 25 or sum(precipitation)/datetime.datetime.now().hour > 4: # verifica se a soma da precipitação é maior que 25mm ou se a média de precipitação por hora é maior que 4mm
            return True #Tem risco
        return False
    
    except: # se não tiver alguma chave no json por erro da API, retorna False
        return False


def verify_risk_tomorrow():
    '''
    Função que verifica se há risco de chuva forte no dia seguinte segundo a previsão do tempo

    @return: True se há risco, False se não há
    '''

    # pega o json da api
    url = f'http://api.weatherapi.com/v1/forecast.json?key={WEATHER_API_KEY}&q=-23.606820,-46.596861&days=7'
    json = get_json_from_api(url)

    try:
        tomorrow = json['forecast']['forecastday'][1]['day']['totalprecip_mm'] # pega a precipitação do dia seguinte
    
        if tomorrow > 10: # verifica se a precipitação é maior que 10mm
            return True #Tem risco
        return False
    
    except: # se não tiver alguma chave no json por erro da API, retorna False
        return False



if __name__ == "__main__":
    print(verify_risk_today())
    print(verify_risk_tomorrow())