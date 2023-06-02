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


# Resistente a sistema operacional
FILE = Path(__file__).resolve()
src_folder = FILE.parents[0]
# caminho para a base
rel_arquivo_db = Path('model/db_alert.db')
caminho_arq_db = src_folder / rel_arquivo_db


app = Flask(__name__)
sched = APScheduler()
load_dotenv()


app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{caminho_arq_db.resolve()}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)


def start_tasks():
    print('remarcou')
    sched.add_job(id='check_weather_today', func=check_weather_today, trigger='interval', seconds=10)

def check_weather_today():
    print("Verificando clima...")
    print('checked!')

    
    if verify_risk_today():
        sched.remove_job('check_weather_today')
        print('tá chovendo pa caraio!')
        msg2 = {"text":"Mensagem de que tá chovendo muito hoje"}
        myapikey = "3ef74400e8msh11f3728c6fb249fp112f4fjsnc487dd3c2fbf"
        mygroup = "120363142240766611"
        sendWSP(msg2, myapikey, mygroup)
    else:
        print('não tá chovendo tanto!')

def check_weather_tomorrow():
    print("Verificando clima amanhã...")
    print('checked!')
    if verify_risk_tomorrow():
        print('tá chovendo pa caraio!')
        msg2 = {"text":"Mensagem de que vai chover amanhã cpa"}
        myapikey = "3ef74400e8msh11f3728c6fb249fp112f4fjsnc487dd3c2fbf"
        mygroup = "120363142240766611"
        sendWSP(msg2, myapikey, mygroup)


@app.route("/")
def hello_world():
    return f"<p>Hello, World!</p>"


api.add_resource(ListUsuario, '/usuario')
api.add_resource(Usuario, '/usuario/<int:usuario_id>')


db.init_app(app)
sched.add_job(id='start_tasks', func=start_tasks, trigger='cron', day_of_week='mon-sun', hour=15, minute=7)
sched.add_job(id='check_weather_tomorrow', func=check_weather_tomorrow, trigger='cron', day_of_week='mon-sun', hour=20, minute=0)
sched.add_job(id='check_weather_today', func=check_weather_today, trigger='interval', seconds=10)
sched.start()

if __name__ == '__main__':

    if 'liveconsole' not in gethostname():
        app.run(use_reloader=False, debug=True)