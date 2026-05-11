from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from paciente import Paciente
from heapsort import heap_sort


pacientes = []


# =====================================
# Função cadastrar paciente
# =====================================
def cadastrar_paciente():

    nome = entrada_nome.get()
    idade = entrada_idade.get()
    gravidade = entrada_gravidade.get()
    sintomas = entrada_sintomas.get()

    # Validação
    if nome == "" or idade == "" or gravidade == "" or sintomas == "":
        messagebox.showerror(
            "Erro",
            "Preencha todos os os campos."
        )
        return

    gravidade = int(gravidade)

    if gravidade < 1 or gravidade > 10:
        messagebox.showerror(
            "Erro",
            "A gravidade deve estar entre 1 e 10."
        )
        return

    # Cria paciente
    paciente = Paciente(
        nome,
        idade,
        gravidade,
        sintomas
    )

    pacientes.append(paciente)

    atualizar_tabela()

    limpar_campos()

    messagebox.showinfo(
        "Sucesso",
        "Paciente cadastrado com sucesso!"
    )


# =====================================
# Atualiza tabela
# =====================================
def atualizar_tabela():

    tabela.delete(*tabela.get_children())

    # Organiza usando Heap Sort
    heap_sort(pacientes)

    prioridade = 1

    for paciente in reversed(pacientes):

        tabela.insert(
            "",
            END,
            values=(
                prioridade,
                paciente.nome,
                paciente.idade,
                paciente.gravidade,
                paciente.sintomas
            )
        )

        prioridade += 1


# =====================================
# Limpa campos
# =====================================
def limpar_campos():

    entrada_nome.delete(0, END)
    entrada_idade.delete(0, END)
    entrada_gravidade.delete(0, END)
    entrada_sintomas.delete(0, END)


# =====================================
# Janela principal
# =====================================
janela = Tk()

janela.title("Sistema Hospitalar - Heap Sort")

janela.geometry("1000x600")

janela.configure(bg="#f0f4f7")


# =====================================
# Título
# =====================================
titulo = Label(
    janela,
    text="Sistema de Prioridade Hospitalar",
    font=("Arial", 22, "bold"),
    bg="#f0f4f7",
    fg="#003049"
)

titulo.pack(pady=20)


# =====================================
# Frame formulário
# =====================================
frame_formulario = Frame(
    janela,
    bg="white",
    padx=20,
    pady=20,
    relief=RIDGE,
    bd=2
)

frame_formulario.pack(
    padx=20,
    pady=10,
    fill=X
)


# =====================================
# Nome
# =====================================
Label(
    frame_formulario,
    text="Nome",
    font=("Arial", 11, "bold"),
    bg="white"
).grid(row=0, column=0, padx=10, pady=10)

entrada_nome = Entry(frame_formulario, width=30)

entrada_nome.grid(row=0, column=1)


# =====================================
# Idade
# =====================================
Label(
    frame_formulario,
    text="Idade",
    font=("Arial", 11, "bold"),
    bg="white"
).grid(row=0, column=2, padx=10)

entrada_idade = Entry(frame_formulario, width=10)

entrada_idade.grid(row=0, column=3)


# =====================================
# Gravidade
# =====================================
Label(
    frame_formulario,
    text="Gravidade (1-10)",
    font=("Arial", 11, "bold"),
    bg="white"
).grid(row=1, column=0, padx=10, pady=10)

entrada_gravidade = Entry(frame_formulario, width=10)

entrada_gravidade.grid(row=1, column=1)


# =====================================
# Sintomas
# =====================================
Label(
    frame_formulario,
    text="Sintomas",
    font=("Arial", 11, "bold"),
    bg="white"
).grid(row=1, column=2, padx=10)

entrada_sintomas = Entry(frame_formulario, width=30)

entrada_sintomas.grid(row=1, column=3)


# =====================================
# Botão cadastrar
# =====================================
botao_cadastrar = Button(
    frame_formulario,
    text="Cadastrar Paciente",
    font=("Arial", 11, "bold"),
    bg="#0077b6",
    fg="white",
    padx=20,
    pady=10,
    command=cadastrar_paciente
)

botao_cadastrar.grid(
    row=2,
    column=0,
    columnspan=4,
    pady=20
)


# =====================================
# Tabela
# =====================================
frame_tabela = Frame(janela)

frame_tabela.pack(
    fill=BOTH,
    expand=True,
    padx=20,
    pady=20
)


colunas = (
    "Prioridade",
    "Nome",
    "Idade",
    "Gravidade",
    "Sintomas"
)


tabela = ttk.Treeview(
    frame_tabela,
    columns=colunas,
    show="headings"
)


# Cabeçalhos
for coluna in colunas:

    tabela.heading(coluna, text=coluna)

    tabela.column(coluna, width=180)


# Scroll
scroll = Scrollbar(
    frame_tabela,
    orient=VERTICAL,
    command=tabela.yview
)

tabela.configure(yscroll=scroll.set)

scroll.pack(side=RIGHT, fill=Y)

tabela.pack(fill=BOTH, expand=True)


# =====================================
# Executa sistema
# =====================================
janela.mainloop()