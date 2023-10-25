import pandas as pd
import random
import tkinter as tk
from tkinter import Entry, Button, Label

# Carregando os dados a partir de um arquivo Excel (.xlsx)
lotofacil_data = pd.read_excel('Lotofácil.xlsx')

# Especifique o dia da semana desejado (0 = segunda-feira, 1 = terça-feira, ..., 6 = domingo)
dia_semana_desejado = 2  # 3 representa quinta-feira

# Converta a coluna 'Data Sorteio' para o formato de data (dd/mm/yyyy)
lotofacil_data['Data Sorteio'] = pd.to_datetime(lotofacil_data['Data Sorteio'], format='%d/%m/%Y')

# Passo 1: Filtrar os resultados com base no dia da semana desejado
sorteios_no_dia_desejado = lotofacil_data[lotofacil_data['Data Sorteio'].dt.dayofweek == dia_semana_desejado]

# Passo 2: Obter os números que foram sorteados nesse dia da semana
numeros_sorteados_no_dia = []
for coluna in sorteios_no_dia_desejado.columns[2:]:
    numeros_sorteados_no_dia.extend(sorteios_no_dia_desejado[coluna].tolist())

# Passo 3: Gerar palpites baseados nos números do dia da semana
num_novos_palpites = 10  # Substitua pelo número de palpites que deseja gerar
novos_palpites = []

for _ in range(num_novos_palpites):
    novo_palpite = random.sample(numeros_sorteados_no_dia, 15)  # Gere uma combinação aleatória com base nos números
    # do dia da semana
    novos_palpites.append(novo_palpite)

# Passo 4: Exibir os novos palpites
for i, palpite in enumerate(novos_palpites, start=1):
    print(f"Novo Palpite {i}: {palpite}")


# Função para gerar palpites com base na data inserida
def gerar_palpites():
    data_entrada.get()
    data_entrada.delete(0, "end")  # Limpe o campo de entrada

    # O restante do código para gerar palpites baseados na data do próximo sorteio
    # ... (o código que mostrei anteriormente)

    # Exiba os palpites gerados em uma janela pop-up
    popup = tk.Toplevel()
    popup.title("Palpites Gerados")
    novos_palpites = []  # Defina a variável novos_palpites com base na data inserida
    for i, palpite in enumerate(novos_palpites, start=1):
        label = Label(popup, text=f"Palpite {i}: {palpite}")
        label.pack()


# Crie a janela principal
janela = tk.Tk()
janela.title("Gerador de Palpites Lotofácil")

# Crie um rótulo e um campo de entrada para a data
data_label = Label(janela, text="Data do Próximo Sorteio (dd/mm/yyyy):")
data_label.pack()
data_entrada = Entry(janela)
data_entrada.pack()

# Crie um botão para gerar os palpites
gerar_botao = Button(janela, text="Gerar Palpites", command=gerar_palpites)
gerar_botao.pack()

# Inicie a interface gráfica
janela.mainloop()
