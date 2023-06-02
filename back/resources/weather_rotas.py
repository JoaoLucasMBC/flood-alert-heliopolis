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
            print('tá chovendo pa caraio!')
            msg2 = {"text":"Mensagem de que tá chovendo muito hoje"}
            myapikey = WHIN_API_KEY
            mygroup = GROUP_ID
            sendWSP(msg2, myapikey, mygroup)

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
            print('tá chovendo pa caraio!')
            msg2 = {"text":"Mensagem de que vai chover amanhã cpa"}
            myapikey = WHIN_API_KEY
            mygroup = GROUP_ID
            sendWSP(msg2, myapikey, mygroup)

            return {'message': 'there is risk tomorrow'}, 200
        else:
            print('não tá chovendo tanto!')
            return {'message': 'there is no risk tomorrow'}, 200