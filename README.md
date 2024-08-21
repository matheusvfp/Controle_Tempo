# Controle de Tempo de Uso do Computador

## Descrição

Este projeto é um script em Python desenvolvido para monitorar e controlar o tempo de uso diário do computador. A principal finalidade é ajudar a gerenciar o tempo que usuários (como um irmão adolescente que adora jogar) passam no computador. O script exibe um cronômetro regressivo e permite adicionar um tempo extra no último minuto, garantindo que o computador seja bloqueado automaticamente após o tempo determinado.

## Funcionalidades

- **Bloqueio de Tela:** Usa a API do Windows para bloquear a estação de trabalho.
- **Contagem Regressiva:** Exibe uma janela com uma contagem regressiva até o bloqueio do computador.
- **Tempo Extra:** Permite adicionar 2 minutos de tempo extra apenas no último minuto da contagem.
- **Interface Gráfica:** Apresenta uma interface amigável com uma barra de progresso e a opção de adicionar tempo extra.
- **Segurança:** O botão de fechar a janela do script foi desativado para evitar interrupções não autorizadas 😅.
- **Observação:** A interação de tempo extra foi limitada para evitar o bug do tempo ilimitado.

## Tecnologias Utilizadas

- **Python:** Linguagem de programação para a lógica e automação.
- **Tkinter:** Biblioteca para criar a interface gráfica.
- **ctypes:** Para interagir com a API do Windows.

