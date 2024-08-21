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

## Como Usar

# Guia de Configuração

1. **Clone o Repositório:**

   Primeiro, clone o repositório e navegue para o diretório do projeto:

   ```bash
   git clone https://github.com/seu-usuario/controle-tempo-uso-computador.git
   cd controle-tempo-uso-computador

2. **Instale as Dependências**

   Certifique-se de ter o Python instalado em sua máquina. Em seguida, siga os passos abaixo para configurar o ambiente virtual e instalar as dependências necessárias:

   2.1 **Crie e ative um ambiente virtual:**

      No Windows:

      ```bash
      python -m venv venv
      venv\Scripts\activate
      ```

      No macOS ou Linux:

      ```bash
      python -m venv venv
      source venv/bin/activate
      ```

   2.2 **Instale as dependências necessárias:**

      Com o ambiente virtual ativado, execute o seguinte comando para instalar as dependências listadas no arquivo `requirements.txt`:

      ```bash
      pip install -r requirements.txt
      ```

3. **Execute o Script**


Para iniciar o controle de tempo, basta executar o script principal:
```bash
   python main.py
   ```

4. **Configuração do Tempo:**

O tempo padrão para o uso do computador está configurado dentro do código. Se desejar alterar o tempo, modifique o valor na linha correspondente no script `main.py`.

5. **Adicionar Tempo Extra:**

No último minuto da contagem regressiva, você pode clicar no botão "Adicionar Tempo Extra" para ganhar 2 minutos adicionais.


## Apoie o Projeto 🙌
Se você quiser apoiar o projeto, deixe uma ⭐.

______

Made with ❤️ by [Matheus Vinícius](https://www.linkedin.com/in/matheusviniciusfp/).


