from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QScrollArea, QHBoxLayout  # pylint: disable=no-name-in-module
from PyQt5.QtGui import QFont  # pylint: disable=no-name-in-module
import sys  # pylint: disable=no-name-in-module
import pymysql  # pylint: disable=all

# Configurações de conexão ao banco de dados MySQL
#ATENCAO - MUDE AS CONFIGURACOES ABAIXO PARA RODAR O CÓDIGO - INSIRA AS INFORMACÕES DO SEU BD
DB_CONFIG = {
    'user': 'usuario',   
    'password': 'senha',
    'host': 'hospedagem',
    'database': 'banco de dados'
}

# Criar uma função para estabelecer a conexão ao banco de dados
def create_connection():
    try:
        return pymysql.connect(**DB_CONFIG)
    except pymysql.MySQLError as e:
        print(f"Erro ao conectar ao MySQL: {e}")
        return None
# Função para recuperar livros do banco de dados


def get_livros():
    connection = create_connection()
    if connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM livros")
            return cursor.fetchall()
    return []

# Função para adicionar livros ao banco de dados
def add_livro(titulo, autor, descricao):
    if not titulo or not autor or not descricao:
        return "Todos os campos devem ser preenchidos."
    connection = create_connection()
    if connection:
        with connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO livros (titulo, autor, descricao) VALUES (%s, %s, %s)",
                (titulo, autor, descricao)
            )
            connection.commit()
            return f"Livro '{titulo}' adicionado com sucesso! ID: {cursor.lastrowid}"
    return "Erro ao conectar ao banco de dados."

# Função para excluir livros do banco de dados
def delete_livro(id_livro):
    connection = create_connection()
    if connection:
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM livros WHERE id = %s", (id_livro,))
            connection.commit()
            return f"Livro excluído com sucesso! ID: {id_livro}"
    return "Erro ao conectar ao banco de dados."

# Função para buscar livros no banco de dados
def search_livro(titulo):
    livros = get_livros()
    results = [livro for livro in livros if titulo.lower() in livro[1].lower()]
    if results:
        return '\n'.join([f"ID: {livro[0]} \nTítulo: {livro[1]} \nAutor: {livro[2]} \nDescrição: {livro[3]}" for livro in results])
    return "Nenhum livro encontrado com esse título."


class ChatbotGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.send_welcome_message()

    def initUI(self):
        self.setWindowTitle("Chatbot - Gerenciador de Livros")
        self.setGeometry(300, 300, 400, 600)

        layout = QVBoxLayout()

        # Área de rolagem para as mensagens
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_widget = QWidget()
        self.scroll_layout = QVBoxLayout(self.scroll_widget)
        self.scroll_area.setWidget(self.scroll_widget)
        layout.addWidget(self.scroll_area)

        # Campo de entrada de texto
        self.input_area = QLineEdit()
        self.input_area.setPlaceholderText("Digite sua mensagem...")
        layout.addWidget(self.input_area)

        # Botão para enviar mensagem
        self.send_button = QPushButton("Enviar")
        self.send_button.clicked.connect(self.send_message)
        layout.addWidget(self.send_button)

        self.setLayout(layout)

    def send_welcome_message(self):
        """Envia uma mensagem de boas-vindas ao usuário."""
        self.add_message("Olá! Estou aqui para ajudar. Você pode fazer o seguinte:\n"
                         "1. Adicionar um livro: 'Título, Autor, Descrição'\n"
                         "2. Excluir um livro: 'excluir livro ID'\n"
                         "3. Listar todos os livros: 'listar livros'\n"
                         "4. Buscar um livro: 'buscar livro Título'\n"
                         "5. Pedir ajuda: 'ajuda'", sender='chatbot')
    
    # Método chamado quando o usuário envia uma mensagem
    def send_message(self):
        user_input = self.input_area.text().strip()
        if user_input:
            self.add_message(user_input, sender='user')
            response = self.process_message(user_input)
            self.add_message(response, sender='chatbot')
            self.input_area.clear()
   
    def add_message(self, message, sender):
        """Adiciona uma mensagem à interface com estilo de balão."""
        message_label = QLabel(message)
        message_label.setWordWrap(True)
        message_label.setFont(QFont("Arial", 10))

        if sender == 'user':
            message_label.setStyleSheet(
                "background-color: #dcf8c6; padding: 3px; border-radius: 10px; margin: 3px;")
            layout = QHBoxLayout()
            layout.addStretch()
            layout.addWidget(message_label)
        else:
            message_label.setStyleSheet(
                "background-color: #87ceeb; padding: 3px; border-radius: 10px; margin: 3px;")
            layout = QHBoxLayout()
            layout.addWidget(message_label)
            layout.addStretch()

        self.scroll_layout.addLayout(layout)
        self.scroll_area.verticalScrollBar().setValue(
            self.scroll_area.verticalScrollBar().maximum())

    def process_message(self, user_input):
        if user_input == 'ajuda':
            return ("Olá! Estou aqui para ajudar. Você pode fazer o seguinte:\n"
                    "1. Adicionar um livro: 'Título, Autor, Descrição'\n"
                    "2. Excluir um livro: 'excluir livro ID'\n"
                    "3. Listar todos os livros: 'listar livros'\n"
                    "4. Buscar um livro: 'buscar livro Título'\n"
                    "5. Pedir ajuda: 'ajuda'")
        elif ',' in user_input:
            titulo, autor, descricao = user_input.split(',', 2)
            titulo = titulo.strip()
            autor = autor.strip()
            descricao = descricao.strip()
            return str(add_livro(titulo, autor, descricao))
        elif user_input.startswith('excluir livro '):
            id_livro = user_input.replace('excluir livro ', '').strip()
            return str(delete_livro(id_livro))
        elif user_input.startswith('buscar livro '):
            titulo = user_input.replace('buscar livro ', '').strip()
            return str(search_livro(titulo))
        elif user_input == 'listar livros':
            livros = get_livros()
            return '\n'.join([f"ID: {livro[0]}, Título: {livro[1]}, Autor: {livro[2]}" for livro in livros])
        else:
            return "Desculpe, não entendi. Você pode me dizer o que deseja fazer? Tente usar um dos seguintes comandos:\n" \
                   "1. Adicionar um livro: 'Título, Autor, Descrição'\n" \
                   "2. Excluir um livro: 'excluir livro ID'\n" \
                   "3. Listar todos os livros: 'listar livros'\n" \
                   "4. Buscar um livro: 'buscar livro Título'\n" \
                   "5. Pedir ajuda: 'ajuda'"


if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui = ChatbotGUI()
    gui.show()
    sys.exit(app.exec_())
