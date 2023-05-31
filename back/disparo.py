import requests


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

    myapikey = "3ef74400e8msh11f3728c6fb249fp112f4fjsnc487dd3c2fbf"
    mygroup = "120363142240766611"

    sendWSP(msg2, myapikey, mygroup)