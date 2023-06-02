import requests
import os


def sendWSP(message, apikey, gid=0):
    url = "https://whin2.p.rapidapi.com/send"
    headers = {
	    "content-type": "application/json",
	    "X-RapidAPI-Key": apikey,
	    "X-RapidAPI-Host": "whin2.p.rapidapi.com"
    }

    try:
        if gid==0:
            return requests.request("POST", url, json=message, headers=headers)
        else: 
            url = "https://whin2.p.rapidapi.com/send2group"
            querystring = {"gid":gid}
            return requests.request("POST", url, json=message, headers=headers, params=querystring)
    except requests.ConnectionError:
        return("Error: Connection Error")

#################################################################
# Testing Section

if __name__ == "__main__":
    msg2 = {"text":"Teste de mensagem no grupo"}

    myapikey = os.environ.get('WHIN_API_KEY')
    mygroup = os.environ.get('GROUP_ID')

    sendWSP(msg2, myapikey, mygroup)