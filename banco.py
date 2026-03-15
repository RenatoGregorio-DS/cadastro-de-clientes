import _sqlite3
import re as re

class Banco:
    def __init__(self, nome_banco):
        self.conexao = _sqlite3.connect(nome_banco, check_same_thread=False)
        self.cursor = self.conexao.cursor()
        self.criar_tabela()

    def criar_tabela(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS clientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT NOT NULL,
                telefone TEXT NOT NULL
            )
        ''')
        self.conexao.commit()

    def adicionar_cliente(self, nome, email, telefone):
        self.cursor.execute('''
            INSERT INTO clientes (nome, email, telefone) 
            VALUES (?, ?, ?)
        ''', (nome, email, telefone))
        self.conexao.commit()

    def listar_clientes(self):
        self.cursor.execute('SELECT * FROM clientes')
        return self.cursor.fetchall()

    def fechar_conexao(self):
        self.conexao.close()
    def excluir_cliente(self, cliente_id):
        self.cursor.execute('DELETE FROM clientes WHERE id = ?', (cliente_id,))
        self.conexao.commit()
    
    def validar_email(self, email):
    # Verifica se o e-mail tem o formato nome@dominio.com
        padrao = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(padrao, email) is not None



    def validar_telefone(self, telefone):
    # O segredo é o re.sub: ele remove tudo que NÃO é número
        apenas_numeros = re.sub(r'\D', '', str(telefone))
    # Verifica se sobraram 10 (fixo) ou 11 (celular) dígitos
        return 10 <= len(apenas_numeros) <= 11
banco = Banco('clientes.db')
banco.criar_tabela()