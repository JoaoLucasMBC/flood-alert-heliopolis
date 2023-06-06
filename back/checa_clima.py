import requests
import datetime
from environ import WEATHER_API_KEY

def get_json_from_api(url):
    '''
    Função que recebe uma url e retorna um json com os dados da api

    @param url: url da api
    @return: json com os dados da api
    '''
    try:
        response = requests.get(url) # faz a requisição
        if response.status_code == 200: # verifica se a requisição foi bem sucedida
            json_data = response.json() # transforma a resposta em json
            return json_data
        else:
            return None
    except:
        return None


def verify_risk_today(date=datetime.datetime.today().strftime('%Y-%m-%d')):
    '''
    Função que verifica se há risco de enchente hoje

    @return: True se há risco, False se não há
    '''
    
    url = f'http://api.weatherapi.com/v1/history.json?key={WEATHER_API_KEY}&q=-23.606820,-46.596861&dt={date}' 
    json = get_json_from_api(url) # pega o json da api
    

    try:
        precipitation = json['forecast']['forecastday'][0]['hour'] # pega a lista de informações sobre o as horas do dia atual
        hora_atual = datetime.datetime.now().time().hour - 1 # pega a hora atual
        
        # pega a precip das duas horas anteriores
        precip = [precipitation[hora_atual], precipitation[hora_atual-1]]
        
        if sum(hour['precip_mm'] for hour in precip)/2 > 7.5 or not all(hour['precip_mm'] < 7.5 for hour in precip) or not all(hour['condition'] ['text'] != "Heavy rain" for hour in precip):
            return True

        return False
    
    except: # se não tiver alguma chave no json por erro da API, retorna False
        return False


def verify_risk_tomorrow(date=datetime.datetime.now()):
    '''
    Função que verifica se há risco de chuva forte no dia seguinte segundo a previsão do tempo

    @return: True se há risco, False se não há
    '''
    #gera json com a previsão do tempo para as próximas 72 horas
    json = get_json_from_api("http://apiadvisor.climatempo.com.br/api/v1/forecast/locale/3679/hours/72?token=b8cbc5c94d430ae14306197f0a396ddc")
    #pega os dados do dia seguinte
    data = json['data']
    tomorrow_data = data[24:48]
    #variável que armazena a quantidade de precipitação por hora
    list_rain_amount = []
    
    #adiciona por hora a quantidade de precipitação na lista que será utilizada nos parâmetros de escolha se há risco ou não
    for hora in tomorrow_data:
        try:
            list_rain_amount.append(hora['rain']['precipitation'])
        except:
            return None

    #caso a precipitação total seja maior que 20 mm ou em alguma hora tenha chovido mais que 7.5mm
    if (sum(list_rain_amount) > 20) or not all(x < 7.5 for x in list_rain_amount):
        return True
    return False


if __name__ == "__main__":
    print(verify_risk_today())
    print(verify_risk_tomorrow())