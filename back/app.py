from flask import Flask 
from flask_restful import Api
from flask_apscheduler import APScheduler

from model.sql_alchemy_flask import db
from pathlib import Path

from resources.usuario_rotas import Usuario, ListUsuario

from socket import gethostname


# Resistente a sistema operacional
FILE = Path(__file__).resolve()
src_folder = FILE.parents[0]
# caminho para a base
rel_arquivo_db = Path('model/db_alert.db')
caminho_arq_db = src_folder / rel_arquivo_db


app = Flask(__name__)
sched = APScheduler()


app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{caminho_arq_db.resolve()}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)


def check_weather():
   print('checked!')


@app.route("/")
def hello_world():
    return f"<p>Hello, World!</p>"


api.add_resource(ListUsuario, '/usuario')
api.add_resource(Usuario, '/usuario/<int:usuario_id>')


if __name__ == '__main__':
    db.init_app(app)
    sched.add_job(id='check_weather', func=check_weather, trigger='cron', day_of_week='mon-sun', hour=5, minute=0)
    sched.start()

    if 'liveconsole' not in gethostname():
        app.run(use_reloader=False, debug=True)