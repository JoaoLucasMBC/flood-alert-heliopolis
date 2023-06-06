## Rotas da API

A API Restful possui algumas rotas para envio e recebimento de dados:

### **GET** - `/usuario`

Lista todos os usuários da plataforma. Resposta esperada de código 200:

        {
            "usuarios": [
                  {
                      "id": 3, 
                      "nome": "Leonardo", 
                      "regiao": "COAB", 
                      "numero": "11444444444"}, 
                  {
                      "id": 4, 
                      "nome": "Leonardo", 
                      "regiao": "COAB", 
                      "numero": "11444444444"}
            ]
        }

### **POST** - `/usuario`

Cria um usuário novo na plataforma. Corpo da requisição:

        {
            "nome": "João Lucas",
            "regiao": "COAB",
            "numero": "11123123123"d
        }

***OBS: essa rota é protegida por um token de autenticação enviado pelo header da requisição na chave `Secret`***

### **GET** - `/usuario/<id:int>`

Busca o usuário de id específico na base de dados. Resposta esperada de código 200:

        {
            "nome": "João Lucas",
            "regiao": "COAB",
            "numero": "11123123123"d
        }

### **DELETE** - `/usuario/<int:id>`

Deleta o usuário de id específico na base de dados.

### **GET** - `/weather/today`

Checa se há risco de chuva forte com alagamento hoje e apenas retorna mensagem que informa o resultado encontrado. Resposta esperada de código 200:

        {
            "message": "there is risk today"
        }

        {
            "message": "there is no risk today"
        }

### **GET** - `/weather/tomorrow`

Checa se há risco de chuva forte com alagamento na previsão do dia seguinte e apenas retorna mensagem que informa o resultado encontrado. Resposta esperada de código 200:

        {
            "message": "there is risk tomorrow"
        }

        {
            "message": "there is no risk tomorrow"
        }
