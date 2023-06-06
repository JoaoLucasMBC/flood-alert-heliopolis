import requests
from environ import GROUP_ID, WHIN_API_KEY

def sendWSP(message, apikey, gid=0):
    '''
    Função para enviar mensagens para o grupo de WhatsApp utilizando a API do Whin

    Parâmetros:
    message: mensagem a ser enviada
    apikey: chave da API do Whin
    gid: id do grupo de WhatsApp

    Retorno:
    resposta da API do Whin
    '''

    url = "https://whin2.p.rapidapi.com/send"
    
    # cria o cabeçalho da requisição
    headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": apikey,
	"X-RapidAPI-Host": "whin2.p.rapidapi.com"}
    try:
        if gid==0: # se não for passado o id do grupo, envia para o grupo padrão
            return requests.request("POST", url, json=message, headers=headers)
        else: 
            # se for passado o id do grupo, envia para o grupo especificado
            url = "https://whin2.p.rapidapi.com/send2group"
            querystring = {"gid":gid}
            return requests.request("POST", url, json=message, headers=headers, params=querystring) 
    except requests.ConnectionError:
        # se der erro de conexão, retorna uma mensagem de erro
        return("Error: Connection Error")



#################################################################
# Testing Section
msg2 = {"text":'''Atenção! Risco de alagamento na sua região, mantenha o cuidado ao sair de casa!'''}

myapikey = WHIN_API_KEY
mygroup = GROUP_ID

sendWSP(msg2, myapikey, mygroup)
