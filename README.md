# Flood Alert | Heliopolis

introdução

---

## **Instalação e Uso**

O projeto utiliza 3 frentes para a sua execução completa:

### *Backend* - LOCAL:

Para abrir o servidor localmente, siga os seguinte passos:

1. Clone o repositório na sua máquina:
    
        git clone https://github.com/JoaoLucasMBC/flood-alert-heliopolis.git

2. É recomendado que se crie um *virtual environemnt* para instalar as dependências do projeto nas suas versões adequadas:

        python3 -m venv env
        
        ./env/Scripts/Activate.ps1     (Windows)

3. A partir da pasta raiz do repositório, mude para a localização da aplicação e instale as dependências:

        cd ./back
        
        pip install -r requirements.txt

4. Execute o servidor rest localmente em modo *debug*:

        python3 app.py

5. Acesse o servidor em `https://localhost:8000`

### *Backend* - SERVIDOR:

O servidor também está disponível hosteado no **PythonAnywhere**, que pode ser acessado clicando [AQUI](https://eriksoaress.pythonanywhere.com)

### *Frontend*:

A landing page para testes, desenvolvida em ***React*** pode apenas ser executada localmente com os seguintes passos:

1. Clone o repositório na sua máquina:
    
        git clone https://github.com/JoaoLucasMBC/flood-alert-heliopolis.git

2. A partir da pasta raiz do repositório, mude para a localização da aplicação React:

        cd ./front

3. Com JavaScript e Node instalados na sua máquine, instale as dependências do projeto:

        npm install yarn

4. Execute o servidor localmente:

        yarn dev

5. Acesse o servidor em `https://localhost:5173`

### *Agendador*:

O serviço possui um script agendador, que realiza requests na API Flask a cada 2 horas para checagem da previsão do tempo, e disparo do alarme se necessário. Ele está hospedado em um servidor *AWS*, mas também pode ser executado localmente para testes:

1. Clone o repositório na sua máquina:
    
        git clone https://github.com/JoaoLucasMBC/flood-alert-heliopolis.git

2. É recomendado que se crie um *virtual environemnt* para instalar as dependências do projeto nas suas versões adequadas:

        python3 -m venv env
        
        ./env/Scripts/Activate.ps1     (Windows)

3. A partir da pasta raiz do repositório, mude para a localização da aplicação:

        cd ./back
        
        pip install -r requirements.txt

4. Retorna para a pasta raiz e entre na pasta do `scheduler`:

        cd ..
        
        cd ./scheduler

5. Execute o script:

        python scheduler.py

Você deve receber updates por `print` no terminal sobre os resultados retornados pelas requisições do servidor Flask.

---

## **Rotas API**

Mais informações das rotas e documentação da API podem ser encontradas [AQUI](/back/README.md)

---

## **Estrutura do Projeto**

### *

### Membros

* João Lucas de Moraes Barros Cadorniga  
* Erik Soares  
* Matheus Aguiar  
* Leonardo Scarlato  
* Gustavo Antony  
* Sergio Ramella
