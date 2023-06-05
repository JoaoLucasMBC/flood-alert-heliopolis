import { useState } from 'react'
import './App.css'
import NavBar from './components/NavBar.jsx'
import helipa from './assets/helipa.jpeg'
import insper from './assets/logo-insper.png'
import celular from './assets/celular.png'
import form from './assets/form.png'

function App() {
  return (

    <div>

      <div className='banner'>
        <div className='image-container'>
          <div className='text-overlay'>
            <h1>Alerta de Enchentes - Heliópolis</h1>
            <ul>
              <li><a href='#sobre-nos-text'>Sobre nós</a></li>
              <li><a href='#button-form'> Cadastrar </a></li>
            </ul>
          </div>
        </div>
      </div>

      <div className='corpo'>

        <div className='sobre-nos'>
          <div id='sobre-nos-text'>
            <h1>Sobre nós</h1>
            <p>
              Somos um grupo de estudantes da faculdade Insper do curso de Ciência da Computação e desenvolvemos um sistema de alerta de enchentes para a população
              de Heliópolis. 
              
              <br/>
              <br/>
              
              Este projeto foi desenvolvido junto à UNAS com base no depoimento de diversos moradores da região, os quais relataram que as enchentes são um problema
              recorrente quando chove nesta área, impactando de forma grave a vida de todos que frequentam esta região.
              
              <br/>
              <br/>

              O objetivo deste projeto é alertar a população sobre possíveis
              enchentes para que as pessoas possam se preparar e, consequentemente, minimizar os impactos causados por este problema.
            </p>
          </div>

          <div className='sobre-nos-image'>
            <img src={insper} alt='insper' />
          </div>


        </div>

        <div className='como-funciona'>

          <div id='como-funciona-text'>
            <h1>Como funciona?</h1>
            <p>
              O sistema de alerta de enchentes funciona da seguinte forma: quando a previsão do tempo indica que há uma grande probabilidade de chuva na região de Heliópolis,
              é enviada uma mensagem de texto via WhatsApp para as pessoas cadastradas no sistema, alertando sobre a possibilidade de enchentes. As mensagens são enviadas nos seguintes 
              momentos:

              <br/>
              <br/>

              <ul>
                <li>Durante o dia (a cada 2 horas)</li>
                <li>À noite, mostrando a previsão para o dia seguinte (às 20h)</li>
              </ul>

              <br/>

              Desta forma, todas as pessoas cadastradas serão atualizadas frequentemente sobre a previsão do tempo e poderão se preparar para possíveis enchentes.
            </p>
          </div>

          <div className='como-funciona-image'>
            <img src={celular} alt='celular' />
          </div>

          
        </div>

        <div className='como-cadastrar'>

          <div id='como-cadastrar-text'>
            <h1>Como posso me cadastrar?</h1>
            <p>
              Para se cadastrar no sistema de alerta de enchentes, basta clicar no botão abaixo e preencher o formulário de inscrição. 

              <br/>
              <br/>

              Desta forma, você será redirecionado para um formulário online, onde deverá preencher seus dados requisitados. 

              <br/>
              <br/>

              Após o preenchimento, você será redirecionado para uma página com o convite para o grupo de
              WhatsApp do sistema de alerta de enchentes. Basta clicar no link e você será adicionado ao grupo.
            </p>

            <br/>
            <br/>

            <div id='button-form'>
              <a href='https://forms.gle/jNAtzaL5X5Z8dyBY7'>Formulário de inscrição</a>
            </div>
          </div>

          <div className='como-cadastrar-image'>
            <img src={form} alt='form' />
          </div>



        </div>
      </div>


        

    </div>
    
  )
}

export default App
