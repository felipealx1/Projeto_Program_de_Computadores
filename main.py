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