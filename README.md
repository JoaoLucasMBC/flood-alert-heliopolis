# Flood Alert | Heliopolis

## Introdução

Projeto desenvolvido junto à UNAS Heliópolis com a finalidade de alertar a população sobre possíveis enchentes na região.

O projeto consiste em um sistema de alerta de enchentes, que utiliza dados de previsão do tempo para determinar se a região de Heliópolis está em risco de enchentes. Caso esteja, o sistema dispara um alerta em forma de mensagem via WhatsApp para todos os usuários cadastrados.

Esta verificação é feita de duas formas:

- **Durante o dia** - a cada 2 horas, o sistema realiza uma requisição à API de clima utilizada, e verifica os dados de previsão naquele momento. Assim, o sistema avisa as pessoas se existe de fato um risco de enchente neste instante.

- **No final do dia** - às 20h, o sistema realiza a mesma requisição, mas para o dia seguinte. Desta forma, as pessoas são avisadas com antecedência sobre o risco de enchente, e podem se preparar a fim de minimizar as consequências negativas causadas por este evento.

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

<!-- imagem da pasta assets -->
![estrutura](/assets/diagrama.png)

### Explicação

Inicialmente, o usuário se encontrará na Landing Page (feita utilizando a biblioteca React), onde haverá uma breve descrição do projeto, seus integrantes, etc.. Nesta página, também haverá um botão que redireciona o usuário para a página de cadastro, a qual consiste em um formulário.

Nesta página, o usuário informará alguns dados pessoais:

- Nome
- Se mora em Heliópolis (caso sim será perguntada a região em que mora)
- Número de telefone (para receber o alerta via WhatsApp)

Após o cadastro, o usuário será redirecionado para um link em que ele poderá entrar no grupo do WhatsApp, onde os alertas serão enviados. Além disso, já em relação ao back-end, o usuário será cadastrado no banco de dados através de uma rota em Flask (framework web em Python), a qual receberá os dados do formulário e os armazenará no banco de dados (POST).

Com o usuário já cadastrado no sistema, para que este receba os alertas de enchente, são utilizadas duas APIs: uma para a questão do clima e outra para o envio de mensagens via WhatsApp. 

A API de clima é utilizada para verificar a previsão do tempo para a região de Heliópolis, e a partir dos dados coletados, o sistema determina se há risco de enchente ou não. Desta forma, o sistema dispara um alerta para todos os usuários cadastrados, informando-os sobre a situação naquele momento, e também sobre a previsão para o dia seguinte por volta das 20h.

A API relacionada ao envio de mensagens realiza justamente a função do disparo de mensagens via WhatsApp. Para isso, o sistema envia no grupo formado por todos os usuários cadastrados a mensagem com o alerta de enchente.



## Membros

* João Lucas de Moraes Barros Cadorniga  
* Erik Soares  
* Matheus Aguiar  
* Leonardo Scarlato  
* Gustavo Antony  
* Sergio Ramella
