# Chat Terminal com MongoDB e Criptografia

## Descrição

Este projeto é um chat por terminal desenvolvido para a disciplina de Estudo de Banco de Dados 2. Ele utiliza PyMongo para armazenar mensagens em um banco de dados MongoDB e uma biblioteca de criptografia para garantir a segurança da comunicação. O objetivo é permitir que os usuários troquem mensagens de forma segura e eficiente, com armazenamento persistente das conversas.

## Funcionalidades

- **Comunicação em tempo real:** Envio e recebimento de mensagens instantaneamente.
- **Criptografia de mensagens:** As mensagens são criptografadas antes de serem armazenadas no banco de dados.
- **Armazenamento em MongoDB:** Mensagens são salvas em um banco de dados NoSQL, garantindo persistência.
- **Interface de linha de comando:** A interação ocorre diretamente pelo terminal.

## Tecnologias Utilizadas

- **Python:** Linguagem principal do projeto.
- **PyMongo:** Biblioteca para interação com o MongoDB.
- **Biblioteca de Criptografia:** Como `cryptography` ou `PyCryptodome` para a criptografia das mensagens.
- **MongoDB:** Banco de dados NoSQL utilizado para armazenamento.

## Como Executar o Projeto

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/usuario/chat-terminal.git
   cd chat-terminal
   ```

2. **Instale as dependências:**
   ```bash
   pip install pymongo cryptography
   ```

3. **Configure o MongoDB:**
   - Certifique-se de que o MongoDB esteja em execução.
   - Ajuste as credenciais de acesso no arquivo de configuração, se necessário.

4. **Execute o chat:**
   ```bash
   python chat.py
   ```

5. **Inicie a conversa:** Siga as instruções no terminal para enviar e receber mensagens.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para enviar um pull request ou abrir uma issue para sugestões ou problemas.

## Licença

Este projeto está licenciado sob a MIT License. Consulte o arquivo LICENSE para mais detalhes.
