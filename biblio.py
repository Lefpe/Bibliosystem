import random
import tkinter as tk
from tkinter import messagebox, simpledialog

# Classe Pessoa com e-mail e senha adicionados
class Pessoa:
    def __init__(self, nome, sobrenome, cpf, endereco, email, senha):
        self.id_pessoa = random.randint(1000, 9999)
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = self.validar_cpf(cpf)
        self.endereco = endereco
        self.email = email
        self.senha = senha

    def validar_cpf(self, cpf):
        if len(cpf) == 11 and cpf.isdigit():
            return cpf
        else:
            raise ValueError("CPF inválido. Deve conter 11 dígitos numéricos.")

    def __str__(self):
        return f"ID: {self.id_pessoa} | {self.nome} {self.sobrenome} | CPF: {self.cpf}"

# Classe Autor
class Autor:
    def __init__(self, nome, sobrenome):
        self.id_autor = random.randint(1000, 9999)
        self.nome = nome
        self.sobrenome = sobrenome
        self.livros = []  # Um autor pode ter múltiplos livros

    def __str__(self):
        return f"ID: {self.id_autor} | {self.nome} {self.sobrenome}"

    def adicionar_livro(self, livro):
        self.livros.append(livro)

# Classe Livro
class Livro:
    def __init__(self, titulo, autor=None):
        self.id_livro = random.randint(1000, 9999)
        self.titulo = titulo
        self.autor = autor

    def __str__(self):
        autor_nome = f"{self.autor.nome} {self.autor.sobrenome}" if self.autor else "Autor desconhecido"
        return f"ID: {self.id_livro} | Título: {self.titulo} | Autor: {autor_nome}"

# Classe Biblioteca para gerenciar autores e livros
class Biblioteca:
    def __init__(self):
        self.autores = []
        self.livros = []

    def adicionar_autor(self, nome, sobrenome):
        novo_autor = Autor(nome, sobrenome)
        self.autores.append(novo_autor)
        return novo_autor

    def adicionar_livro(self, titulo, autor=None):
        novo_livro = Livro(titulo, autor)
        self.livros.append(novo_livro)
        if autor:
            autor.adicionar_livro(novo_livro)
        return novo_livro

# Classe Recursos Humanos
class RecursosHumanos:
    def __init__(self):
        self.pessoas = []

    def adicionar_pessoa(self, nome, sobrenome, cpf, endereco, email, senha):
        nova_pessoa = Pessoa(nome, sobrenome, cpf, endereco, email, senha)
        self.pessoas.append(nova_pessoa)
        return nova_pessoa

    def login(self, email, senha):
        return next((p for p in self.pessoas if p.email == email and p.senha == senha), None)

# Classe principal do sistema com interface gráfica
class SistemaBibliotecaRH:
    def __init__(self, root):
        self.biblioteca = Biblioteca()
        self.rh = RecursosHumanos()

        self.root = root
        self.root.title("Sistema Biblioteca e Recursos Humanos")
        self.root.configure(bg='purple')  # Cor de fundo roxa

        self.menu_principal()

    def limpar_tela(self):
        # Limpa todos os widgets da tela
        for widget in self.root.winfo_children():
            widget.destroy()

    def menu_principal(self):
        self.limpar_tela()

        frame = tk.Frame(self.root, bg='purple')
        frame.pack(pady=20)

        # Botões para menu principal
        tk.Button(frame, text="Gerenciar Autores e Livros", command=self.menu_biblioteca, width=30).pack(pady=10)
        tk.Button(frame, text="Gerenciar Recursos Humanos", command=self.menu_rh, width=30).pack(pady=10)
        tk.Button(frame, text="Sair", command=self.root.quit, width=30).pack(pady=10)

    # Menu Biblioteca
    def menu_biblioteca(self):
        self.limpar_tela()

        frame = tk.Frame(self.root, bg='purple')
        frame.pack(pady=20)

        tk.Label(frame, text="Menu Biblioteca", bg='purple', fg='white').pack(pady=10)
        tk.Button(frame, text="Adicionar Autor", command=self.adicionar_autor, width=30).pack(pady=5)
        tk.Button(frame, text="Adicionar Livro", command=self.adicionar_livro, width=30).pack(pady=5)
        tk.Button(frame, text="Listar Autores", command=self.listar_autores, width=30).pack(pady=5)
        tk.Button(frame, text="Listar Livros", command=self.listar_livros, width=30).pack(pady=5)
        tk.Button(frame, text="Voltar", command=self.voltar, width=30).pack(pady=5)

    # Adicionar Autor
    def adicionar_autor(self):
        nome = simpledialog.askstring("Nome do Autor", "Digite o nome:")
        sobrenome = simpledialog.askstring("Sobrenome do Autor", "Digite o sobrenome:")
        if nome and sobrenome:
            autor = self.biblioteca.adicionar_autor(nome, sobrenome)
            messagebox.showinfo("Sucesso", f"Autor {autor} adicionado com sucesso.")

    # Adicionar Livro
    def adicionar_livro(self):
        titulo = simpledialog.askstring("Título do Livro", "Digite o título do livro:")
        if titulo:
            autores = [str(autor) for autor in self.biblioteca.autores]
            if autores:
                autor_selecionado = simpledialog.askstring("Autor", f"Escolha um autor:\n{', '.join(autores)}")
                autor = next((autor for autor in self.biblioteca.autores if str(autor) == autor_selecionado), None)
                livro = self.biblioteca.adicionar_livro(titulo, autor)
            else:
                livro = self.biblioteca.adicionar_livro(titulo)
            messagebox.showinfo("Sucesso", f"Livro '{livro.titulo}' adicionado com sucesso.")

    # Listar Autores
    def listar_autores(self):
        autores = [str(autor) for autor in self.biblioteca.autores]
        messagebox.showinfo("Autores", "\n".join(autores) if autores else "Nenhum autor cadastrado.")

    # Listar Livros
    def listar_livros(self):
        livros = [str(livro) for livro in self.biblioteca.livros]
        messagebox.showinfo("Livros", "\n".join(livros) if livros else "Nenhum livro cadastrado.")

    # Menu Recursos Humanos
    def menu_rh(self):
        self.limpar_tela()

        frame = tk.Frame(self.root, bg='purple')
        frame.pack(pady=20)

        tk.Label(frame, text="Menu Recursos Humanos", bg='purple', fg='white').pack(pady=10)
        tk.Button(frame, text="Cadastrar Pessoa", command=self.adicionar_pessoa, width=30).pack(pady=5)
        tk.Button(frame, text="Login", command=self.login, width=30).pack(pady=5)
        tk.Button(frame, text="Voltar", command=self.voltar, width=30).pack(pady=5)

    def adicionar_pessoa(self):
        nome = simpledialog.askstring("Nome", "Digite o nome:")
        sobrenome = simpledialog.askstring("Sobrenome", "Digite o sobrenome:")
        cpf = simpledialog.askstring("CPF", "Digite o CPF:")
        endereco = simpledialog.askstring("Endereço", "Digite o endereço:")
        email = simpledialog.askstring("E-mail", "Digite o e-mail:")
        senha = simpledialog.askstring("Senha", "Digite a senha:")
        try:
            nova_pessoa = self.rh.adicionar_pessoa(nome, sobrenome, cpf, endereco, email, senha)
            messagebox.showinfo("Sucesso", f"Pessoa {nova_pessoa.nome} {nova_pessoa.sobrenome} cadastrada com sucesso.")
        except ValueError as e:
            messagebox.showerror("Erro", str(e))

    def login(self):
        email = simpledialog.askstring("E-mail", "Digite seu e-mail:")
        senha = simpledialog.askstring("Senha", "Digite sua senha:", show='*')
        pessoa = self.rh.login(email, senha)
        if pessoa:
            messagebox.showinfo("Sucesso", f"Login realizado com sucesso! Bem-vindo(a), {pessoa.nome}.")
        else:
            messagebox.showerror("Erro", "E-mail ou senha incorretos.")

    def voltar(self):
        self.menu_principal()

# Configuração da janela principal
root = tk.Tk()
app = SistemaBibliotecaRH(root)
root.geometry("400x400")
root.mainloop()
