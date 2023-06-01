import requests
def sendWSP(message, apikey,gid=0):
    url = "https://whin2.p.rapidapi.com/send"
    headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": apikey,
	"X-RapidAPI-Host": "whin2.p.rapidapi.com"}
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
msg2 = {"text":"Teste de mensagem no grupo"}

myapikey = "77976d3475msh4020c0569dd11dap121e22jsn7815e2cd58ef"
mygroup = "120363142392509038"

sendWSP(msg2, myapikey,mygroup)