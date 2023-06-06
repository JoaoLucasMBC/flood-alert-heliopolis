import requests
import datetime
import copy

def get_json_from_api(url):
    response = requests.get(url)
    if response.status_code == 200:
        json_data = response.json()
        return json_data
    else:
        return None


def verify_risk_climatempo():
    json = get_json_from_api("http://apiadvisor.climatempo.com.br/api/v1/forecast/locale/3679/hours/72?token=b8cbc5c94d430ae14306197f0a396ddc")
    data = json['data']
    tomorrow_data = data[24:48]
    rain_amount = 0
    list_rain_amount = []
    try:
        #adiciona por hora a quantidade de precipitação na precipitação total e na lista que será utilizada em um dos parâmetros de escolha
        for hora in tomorrow_data:
            rain_amount += hora['rain']['preciptation']
            list_rain_amount += [hora['rain']['preciptation']]
    except:
        print("Error")

    #caso a precipitação total seja maior que 20 mm ou em alguma hora tenha chovido mais que 7.5mm
    if (rain_amount > 20) or not all(x < 7.5 for x in list_rain_amount):
        return True
    return False

print(verify_risk_climatempo())

