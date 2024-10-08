Aqui está o README atualizado com a etapa de configuração do ambiente virtual destacada:

---

# Chat Terminal com MongoDB e Criptografia

## Descrição

Este projeto é um chat por terminal desenvolvido para a disciplina de Estudo de Banco de Dados 2. Ele utiliza PyMongo para armazenar mensagens em um banco de dados MongoDB e a biblioteca de criptografia `aes-pkcs5` para garantir a segurança da comunicação. O objetivo é permitir que os usuários troquem mensagens de forma segura e eficiente, com armazenamento persistente das conversas.

## Funcionalidades

- **Comunicação em tempo real:** Envio e recebimento de mensagens instantaneamente.
- **Criptografia de mensagens:** As mensagens são criptografadas usando AES com PKCS#5 antes de serem armazenadas no banco de dados.
- **Armazenamento em MongoDB:** Mensagens são salvas em um banco de dados NoSQL, garantindo persistência.
- **Interface de linha de comando:** A interação ocorre diretamente pelo terminal.

## Tecnologias Utilizadas

- **Python:** Linguagem principal do projeto.
- **PyMongo:** Biblioteca para interação com o MongoDB.
- **aes-pkcs5:** Biblioteca para criptografia AES com preenchimento PKCS#5.
- **MongoDB:** Banco de dados NoSQL utilizado para armazenamento.

## Como Executar o Projeto

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/marcos-do-amaral-miotto/MongoChat.git
   cd MongoChat
   ```

2. **Configuração do Ambiente Virtual:**

   Se você estiver **usando o PyCharm**, esta etapa não é necessária, pois a IDE configura o ambiente virtual automaticamente.

   Caso contrário, siga as etapas abaixo para configurar o ambiente virtual manualmente:

   macOS/Linux
   ```bash
   source .venv/bin/activate
   ```
   Windows
   ```bash
   .venv\bin\Activate.ps1
   ```
   
4. **Execute o chat:**
   ```bash
   python main.py
   ```

5. **Inicie a conversa:** Siga as instruções no terminal para enviar e receber mensagens.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para enviar um pull request ou abrir uma issue para sugestões ou problemas.

## Licença

Este projeto está licenciado sob a MIT License. Consulte o arquivo LICENSE para mais detalhes.

---

Isso adiciona as instruções de configuração do ambiente virtual com a nota específica sobre o PyCharm.

**a.** Deseja adicionar instruções para configurar o MongoDB?  
**b.** Precisa de exemplos de criptografia para as mensagens?
