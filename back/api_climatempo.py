import requests
import datetime

def get_json_from_api(url):
    response = requests.get(url)
    if response.status_code == 200:
        json_data = response.json()
        return json_data
    else:
        return None


def verify_risk_climatempo():
    dict_data = {"today":0, "tomorrow": 0}
    json = get_json_from_api("http://apiadvisor.climatempo.com.br/api/v1/forecast/locale/3679/hours/72?token=b8cbc5c94d430ae14306197f0a396ddc")
    data = json['data']
    today = data[0]['date_br'][:10]
    tomorrow = data[25]['date_br'][:10]
    for hora in data:
        if hora['date_br'][:10] == today:
            dict_data['today'] += hora['rain']['precipitation']
        elif hora['date_br'][:10] == tomorrow:
            dict_data['tomorrow'] += hora['rain']['precipitation']

    #adicionar verificação se tem risco ou nn
    return dict_data

print(verify_risk_climatempo())

