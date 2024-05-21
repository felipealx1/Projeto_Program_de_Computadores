import tkinter as tk
from tkinter import messagebox
import json

class Member:
    def _init_(self, name, cpf, plan, value):
        self.name = name
        self.cpf = cpf
        self.plan = plan
        self.value = value

class GymManagement:
    def _init_(self):
        self.members = []

    def add_member(self, member):
        self.members.append(member)

    def remove_member(self, index):
        del self.members[index]

    def get_member_list(self):
        return [f"{member.name} - CPF: {member.cpf} - Plano: {member.plan} - Valor: R${member.value}" for member in self.members]

    def save_data(self, filename):
        with open(filename, 'w') as file:
            json.dump([member._dict_ for member in self.members], file, indent=4)

    def load_data(self, filename):
        with open(filename, 'r') as file:
            data = json.load(file)
            self.members = [Member(member['name'], member['cpf'], member['plan'], member['value']) for member in data]

class AcademiaApp:
    def _init_(self, master):
        self.master = master
        self.master.title("Sistema de Academia")
        self.master.configure(bg="#f0f0f0")

        self.gym_manager = GymManagement()

        self.setup_ui()

    def setup_ui(self):
        # Definindo um estilo para os botões
        button_style = {
            'bg': "#008080",
            'fg': "white",
            'cursor': "hand2",
            'font': ('Arial', 12)
        }

        self.frame_adicionar = tk.Frame(self.master, bg="#f0f0f0")
        self.frame_adicionar.pack(pady=10)

        self.frame_lista = tk.Frame(self.master, bg="#f0f0f0")
        self.frame_lista.pack(padx=10, pady=5)

        self.label_nome = tk.Label(self.frame_adicionar, text="Nome:", bg="#f0f0f0")
        self.label_nome.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.entry_nome = tk.Entry(self.frame_adicionar, width=50)
        self.entry_nome.grid(row=0, column=1, padx=5, pady=5)

        self.label_cpf = tk.Label(self.frame_adicionar, text="CPF:", bg="#f0f0f0")
        self.label_cpf.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.entry_cpf = tk.Entry(self.frame_adicionar, width=30)
        self.entry_cpf.grid(row=1, column=1, padx=5, pady=5)

        self.label_plano = tk.Label(self.frame_adicionar, text="Plano:", bg="#f0f0f0")
        self.label_plano.grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.entry_plano = tk.Entry(self.frame_adicionar, width=30)
        self.entry_plano.grid(row=2, column=1, padx=5, pady=5)

        self.label_valor = tk.Label(self.frame_adicionar, text="Valor:", bg="#f0f0f0")
        self.label_valor.grid(row=3, column=0, padx=5, pady=5, sticky="e")
        self.entry_valor = tk.Entry(self.frame_adicionar, width=30)
        self.entry_valor.grid(row=3, column=1, padx=5, pady=5)

        self.botao_adicionar = tk.Button(self.frame_adicionar, text="Adicionar Membro", command=self.adicionar_membro, **button_style)
        self.botao_adicionar.grid(row=4, columnspan=2, pady=10, sticky="ew")

        self.botao_editar_membro = tk.Button(self.frame_lista, text="Editar Membro", command=self.editar_membro, **button_style)
        self.botao_editar_membro.grid(row=0, column=0, pady=5, padx=5, sticky='ew')

        self.botao_registrar_pagamento = tk.Button(self.frame_lista, text="Registrar Pagamento", command=self.registrar_pagamento, **button_style)
        self.botao_registrar_pagamento.grid(row=1, column=0, pady=5, padx=5, sticky='ew')

        self.botao_gerar_relatorio = tk.Button(self.frame_lista, text="Gerar Relatório", command=self.gerar_relatorio, **button_style)
        self.botao_gerar_relatorio.grid(row=2, column=0, pady=5, padx=5, sticky='ew')

        self.lista_membros = tk.Listbox(self.frame_lista, width=70)
        self.lista_membros.grid(row=0, column=1, rowspan=5)

    def adicionar_membro(self):
        nome = self.entry_nome.get()
        cpf = self.entry_cpf.get()
        plano = self.entry_plano.get()
        valor = self.entry_valor.get()

        if nome and cpf and plano and valor:
            self.gym_manager.add_member(Member(nome, cpf, plano, valor))
            self.refresh_member_list()
            self.clear_entry_fields()
        else:
            messagebox.showwarning("Atenção", "Por favor, preencha todos os campos.")