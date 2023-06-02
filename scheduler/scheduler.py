from apscheduler.schedulers.blocking import BlockingScheduler
import requests


def start_tasks():
    '''
    Função que re-inicializa as tarefas agendadas todo dia no começo do dia
    '''
    print('remarcou')
    sched.add_job(id='check_weather_today', func=check_weather_today, trigger='interval', hours=2)


def check_weather_today():
    url = f'http://eriksoaress.pythonanywhere.com/weather/today'

    try:
        res = requests.get(url)

        if res.status_code == 200:
            json_data = res.json()
            if json_data['message'] == 'there is risk today':
                sched.remove_job('check_weather_today')

    except requests.ConnectionError:
        print('Erro de conexão')


def check_weather_tomorrow():
    url = f'http://eriksoaress.pythonanywhere.com/weather/tomorrow'
    
    try:
        requests.get(url)
    except requests.ConnectionError:
        print('Erro de conexão')


# inicializa o agendador de tarefas
sched = BlockingScheduler()

# inicializa as taerfas e os horários
sched.add_job(id='start_tasks', func=start_tasks, trigger='cron', day_of_week='mon-sun', hour=0, minute=0)
sched.add_job(id='check_weather_tomorrow', func=check_weather_tomorrow, trigger='cron', day_of_week='mon-sun', hour=20, minute=0)
sched.add_job(id='check_weather_today', func=check_weather_today, trigger='interval', hours=2)
sched.start()