from flask_restful import Resource

from disparo import sendWSP
from checa_clima import verify_risk_today, verify_risk_tomorrow

from environ import GROUP_ID, WHIN_API_KEY


class WeatherToday(Resource):

    def get(self):
        '''
        Rota GET para verificar se há risco de enchente hoje

        Return:
            json: mensagem de que há risco de enchente hoje
        '''
        if verify_risk_today():
            msg_risk_today = {"text":'''Atenção! Risco de alagamento na sua região, mantenha o cuidado ao sair de casa!'''}
            myapikey = WHIN_API_KEY
            mygroup = GROUP_ID
            sendWSP(msg_risk_today, myapikey, mygroup)

            return {'message': 'there is risk today'}, 200
        else:
            print('não tá chovendo tanto!')
            return {'message': 'there is no risk today'}, 200


class WeatherTomorrow(Resource):

    def get(self):
        '''
        Rota GET para verificar se há risco de enchente amanhã

        Return:
            json: mensagem de que há risco de enchente amanhã
        '''
        if verify_risk_tomorrow():
            msg_risk_tomorrow = {"text":'''E aí, morador de Heliópolis!
Tô passando pra te avisar que a previsão tá indicando possibilidade de chuva forte amanhã e risco de enchente. Pode não ser 100% certeza, mas é melhor se precaver, né?
Até mais, galera!'''}
            myapikey = WHIN_API_KEY
            mygroup = GROUP_ID
            sendWSP(msg_risk_tomorrow, myapikey, mygroup)

            return {'message': 'there is risk tomorrow'}, 200
        else:
            print('não tá chovendo tanto!')
            return {'message': 'there is no risk tomorrow'}, 200
