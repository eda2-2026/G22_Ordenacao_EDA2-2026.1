class Paciente:
    def __init__(self, nome, idade, gravidade, sintomas):
        self.nome = nome
        self.idade = idade
        self.gravidade = gravidade
        self.sintomas = sintomas

    def __str__(self):
        return (
            f"{self.nome} | "
            f"Idade: {self.idade} | "
            f"Gravidade: {self.gravidade} | "
            f"Sintomas: {self.sintomas}"
        )