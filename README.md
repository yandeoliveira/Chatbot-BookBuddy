# Chatbot-BookBuddy
BookBuddy é um chatbot interativo desenvolvido em Python que ajuda os usuários a gerenciar suas coleções de livros de forma simples e eficiente. Com funcionalidades como adicionar, excluir, listar e buscar livros, o BookBuddy se torna um assistente pessoal para amantes da leitura.

# Gerenciador de Livros - Chatbot

Este projeto é um gerenciador de livros simples desenvolvido em Python utilizando a biblioteca PyQt5 para a interface gráfica e pymysql para a conexão com um banco de dados MySQL. O chatbot permite que os usuários adicionem, excluam, busquem e listem livros em um banco de dados.

## Funcionalidades

- **Adicionar um livro**: O usuário pode adicionar um livro informando o título, autor e descrição.
- **Excluir um livro**: O usuário pode excluir um livro pelo seu ID.
- **Buscar um livro**: O usuário pode buscar livros pelo título.
- **Listar todos os livros**: O usuário pode listar todos os livros armazenados no banco de dados.
- **Ajuda**: O chatbot fornece instruções sobre como usar as funcionalidades.

## Pré-requisitos

Antes de executar o projeto, você precisa ter o Python e o MySQL instalados em sua máquina. Além disso, você deve instalar as bibliotecas necessárias. Você pode fazer isso usando o `pip`:

```
pip install PyQt5 pymysql
```

# Configuração do Banco de Dados
## Configurar o Banco de Dados

Antes de executar o código, você deve configurar as informações de conexão ao banco de dados MySQL. No arquivo, localize a variável DB_CONFIG e insira suas credenciais:
```
Copy code
DB_CONFIG = {
    'user': 'usuario',   
    'password': 'senha',
    'host': 'hospedagem',
    'database': 'banco de dados'
}
```
## Criar a Tabela

Certifique-se de que a tabela livros existe no seu banco de dados. Você pode criar a tabela com o seguinte comando SQL:

```
CREATE TABLE livros (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL,
    autor VARCHAR(255) NOT NULL,
    descricao TEXT NOT NULL
);
```

# Executando o Projeto
Para executar o projeto, use o seguinte comando no terminal:

```
python nome_do_seu_arquivo.py
```
Substitua nome_do_seu_arquivo.py pelo nome do arquivo que contém o código.

# Uso
Ao iniciar o aplicativo, você verá uma interface onde pode interagir com o chatbot.
Siga as instruções fornecidas pelo chatbot para adicionar, excluir, buscar ou listar livros.
Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir um problema ou enviar um pull request.

# Licença
Este projeto está licenciado sob a MIT License. Veja o arquivo LICENSE para mais detalhes.

# Contato
Para dúvidas ou sugestões, entre em contato com [yansantos2410@gmail.com].
