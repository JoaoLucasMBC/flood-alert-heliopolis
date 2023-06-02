from flask import Flask 
from flask_restful import Api
from flask_apscheduler import APScheduler

from model.sql_alchemy_flask import db
from pathlib import Path

from resources.usuario_rotas import Usuario, ListUsuario
from disparo import sendWSP
from checa_clima import verify_risk_today, verify_risk_tomorrow

from socket import gethostname
from dotenv import load_dotenv
import os


# Resistente a sistema operacional
FILE = Path(__file__).resolve()
src_folder = FILE.parents[0]
# caminho para a base de dados
rel_arquivo_db = Path('model/db_alert.db')
caminho_arq_db = src_folder / rel_arquivo_db


# inicializa a aplicação
app = Flask(__name__)
# inicializa o agendador de tarefas
sched = APScheduler()
# inicializa o environment
load_dotenv()


# configura o caminho para a base de dados
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{caminho_arq_db.resolve()}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)


def start_tasks():
    '''
    Função que re-inicializa as tarefas agendadas todo dia no começo do dia
    '''
    print('remarcou')
    sched.add_job(id='check_weather_today', func=check_weather_today, trigger='interval', seconds=10)

def check_weather_today():
    '''
    Função que verifica se há risco de enchente hoje
    '''
    print("Verificando clima...")
    print('checked!')

    if verify_risk_today():
        sched.remove_job('check_weather_today') # remove a tarefa de verificar o clima a cada 2 horas se ela já deu resultado positivo
        print('tá chovendo pa caraio!')
        msg2 = {"text":"Mensagem de que tá chovendo muito hoje"}
        myapikey = os.environ.get('WHIN_API_KEY')
        mygroup = os.environ.get('GROUP_ID')
        sendWSP(msg2, myapikey, mygroup) # envia mensagem para o grupo
    else:
        print('não tá chovendo tanto!')


def check_weather_tomorrow():
    '''
    Função que verifica se há risco de chuva forte no dia seguinte segundo a previsão do tempo
    '''
    print("Verificando clima amanhã...")
    print('checked!')

    if verify_risk_tomorrow():
        print('tá chovendo pa caraio!')
        msg2 = {"text":"Mensagem de que vai chover amanhã cpa"}
        myapikey = os.environ.get('WHIN_API_KEY')
        mygroup = os.environ.get('GROUP_ID')
        sendWSP(msg2, myapikey, mygroup) # envia mensagem para o grupo


@app.route("/")
def hello_world():
    return f"<p>Hello, World!</p>"


# adiciona as rotas
api.add_resource(ListUsuario, '/usuario')
api.add_resource(Usuario, '/usuario/<int:usuario_id>')


db.init_app(app)

# inicializa as taerfas e os horários
#sched.add_job(id='start_tasks', func=start_tasks, trigger='cron', day_of_week='mon-sun', hour=0, minute=0)
#sched.add_job(id='check_weather_tomorrow', func=check_weather_tomorrow, trigger='cron', day_of_week='mon-sun', hour=20, minute=0)
#sched.add_job(id='check_weather_today', func=check_weather_today, trigger='interval', hours=2)
#sched.start()

if __name__ == '__main__':

    # se não estiver rodando no servidor oficial, roda em modo debug
    if 'liveconsole' not in gethostname():
        app.run(use_reloader=False, debug=True)