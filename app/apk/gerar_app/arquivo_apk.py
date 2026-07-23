import tkinter as tk
from tkinter import ttk, messagebox
import datetime

# Código do app

janela = tk.Tk()
janela.title("Agenda semanal")
janela.geometry("700x500")

# Tratando as informações da lista
def editar_dic():
    horarios = {}
    
    with open("horarios.csv", "r", encoding="utf-8-sig") as h:
        lista = h.read()
        lista = lista.splitlines()
        lista.pop(0)
        
        # Separando os itens em um dicionário com uma lista de listas para hora e atividade
        for item in lista:
            item_dia = item.split(";")
            var = tk.BooleanVar(value=(item_dia[3] == "True"))

            if item_dia[0].capitalize() in horarios:
                horarios[item_dia[0].capitalize()][0].append(item_dia[1])
                horarios[item_dia[0].capitalize()][1].append(item_dia[2])
                horarios[item_dia[0].capitalize()][2].append(var)
            else:
                horarios[item_dia[0].capitalize()] = [[item_dia[1]], [item_dia[2]], [var]]
    
    return horarios

horario = editar_dic()

# Criando espaços para posicionar os itens na janela
frame_principal = ttk.Frame(janela)
frame_principal.place(relx=0.5, rely=0, relheight = 1, anchor="n")

canvas = tk.Canvas(frame_principal)

frame = ttk.Frame(canvas)

frame2 = ttk.Frame(frame_principal)
frame2.grid(row=0, column=2, padx=10, sticky="n")

# Coloca o frame dentro do canvas
canvas.create_window((0, 0), window=frame, anchor="nw")

# Atualiza a área rolável
frame.bind( "<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")) )

# Cria barra de rolagem com o comando de movimento vertical docanvas
barra_rolagem = ttk.Scrollbar( frame_principal, orient="vertical", command=canvas.yview )

# Liga a barra ao canvas
canvas.configure(yscrollcommand=barra_rolagem.set)

frame_principal.grid_rowconfigure(0, weight=1)
canvas.grid(row=0, column=0, sticky="nsew")

barra_rolagem.grid(row=0, column=1, sticky="nsew")

# Passando os parametros para as funções
def salvar_progresso():
    global horario
    lista = ["Dia;Hora;Atividade;Estado"]

    for chave in horario:

        for num in range(len(horario[chave][0])):
            if horario[chave][2][num].get() == True:
                print("verdadeiro")
                lista.append(chave + ";" + horario[chave][0][num] + ";" + horario[chave][1][num] + ";" + "True")
            else:
                print("falso")
                lista.append(chave + ";" + horario[chave][0][num] + ";" + horario[chave][1][num] + ";" + "False")     

    try:
        with open("horarios.csv", "w", encoding="utf-8-sig") as a:
            a.write("\n".join(lista))
        messagebox.showinfo("Alerta", "Progresso salvo")
    except Exception as e:
        messagebox.showerror(
        "Erro",
        f"Não foi possível salvar o progresso.\n\n{e}")

def verificar_hora_save():
    hora = datetime.datetime.now()
    if (hora.hour == 0) and (hora.minute == 0):
        salvar_progresso()

    janela.after(60000, verificar_hora_save)

# Frame 2
def atualiza_frame2(i):
        lista_dias = []
        for dia in horario:
            lista_dias.append(dia)

        if i:
            
            tk.Button(frame2, text="Editar", command=janela_edicao).grid(row=0, column=2, padx=10, pady=10)
            
            view_dia = ttk.Combobox( frame2, values=lista_dias, state="readonly" )
            view_dia.grid(row=0, column=0, pady=10)
            
            view_dia.bind("<<ComboboxSelected>>", seleciona_dia_frame2)
            i = False

        # Limpando os itens do frame 2
        for texto in frame2.winfo_children():
            if isinstance(texto, ttk.Label):
                texto.destroy()
            elif isinstance(texto, ttk.Checkbutton):
                texto.destroy()


def seleciona_dia_frame2(event):
    atualiza_frame2(False)
    view_dia = event.widget.get()

    ttk.Label(frame2, text=view_dia).grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
    linha = 2
    col = 0
    
    for lista_dia_select in horario[view_dia]:        
        for hora_atv in lista_dia_select:
            # Escreve hora e atividade
            if lista_dia_select == horario[view_dia][1]:
                ttk.Label(frame2, text=hora_atv).grid(row=(linha - (len(lista_dia_select))) , column=col, padx=1, pady=5, sticky="nsew")
            elif lista_dia_select == horario[view_dia][2]:
                ttk.Checkbutton(frame2, variable=hora_atv).grid(row=(linha - (len(lista_dia_select * 2))), column=col+1, padx=1, pady=5, sticky="nsew")
            else:
                ttk.Label(frame2, text=hora_atv).grid(row=linha, column=col, padx=1, pady=5, sticky="nsew")    
            linha +=1
            
        col += 1

# Criando os itens mostrados no frame1
def atualiza_frame():
    for texto in frame.winfo_children():
        
        if isinstance(texto, ttk.Label):
            texto.destroy()
        elif isinstance(texto, ttk.Checkbutton):
            texto.destroy()
    
    num_linha = 0
    global horario
    horario = editar_dic()
    atualiza_frame2(True)

    for dia_semana in horario:
        # Escreve dia da semana
        num_col = 0
        ttk.Label(frame, text=dia_semana).grid(row=num_linha, column=num_col, padx=5, pady=5, sticky="nsew")

        for lista in horario[dia_semana]: 
            num_linha += 1

            for hora_atv in lista:
                # Escreve hora e atividade
                if lista == horario[dia_semana][1]:
                    ttk.Label(frame, text=hora_atv).grid(row=num_linha - (len(lista) + 1), column=num_col, padx=5, pady=5, sticky="nsew")
                elif lista == horario[dia_semana][2]:
                    ttk.Checkbutton(frame, variable=hora_atv).grid(row=num_linha - ((len(lista)*2) + 2), column=num_col+1, padx=5, pady=5, sticky="nsew")
                else:
                    ttk.Label(frame, text=hora_atv).grid(row=num_linha, column=num_col, padx=5, pady=5, sticky="nsew")    
                num_linha +=1
            num_col += 2

# Modificar tabela
def add_item(dia, hora, atividade):
    
    with open("horarios.csv", "r+", encoding="utf-8-sig") as ed:
        lista_agenda = ed.read()
        lista_agenda = lista_agenda.splitlines()
        tem = False
        
        for item in lista_agenda:
            if (dia in item) and (hora in item) and (atividade.lower() in item.lower()):
                tem = True
        
        if tem:
            messagebox.showinfo("Nenhuma ação executada:", "Item já existe na lista!")
        else:
            ed.write("\n"+ dia.capitalize() + ";"+ hora+ ";"+ atividade.capitalize() + ";" + "False")
            messagebox.showinfo("Ação executada:", "Item adicionado a lista!") 
    
    atualiza_frame()
            
def excluir_item(dia, hora, atividade):
    
    with open("horarios.csv", "r+", encoding="utf-8") as ed:
        lista_agenda = ed.read()
        lista_agenda = lista_agenda.splitlines()
        
        for linha in lista_agenda:
            i = True
            if (dia.lower() in linha.lower()) and (hora in linha) and (atividade.lower() in linha.lower()):
                i = False
                lista_agenda.remove(linha)
                ed.seek(0)
                ed.truncate(0)
                ed.write("\n".join(lista_agenda))
                messagebox.showinfo("Ação executada:", "Item excluído da lista!")
                break
        
        if i:
            messagebox.showinfo("Nenhuma ação executada:", "O item não foi encontrado na lista!")
    
    atualiza_frame()
    

def janela_edicao():
    horarios = editar_dic()
    lista_dias = []
    
    for dia in horarios:
        lista_dias.append(dia)

    edit = tk.Toplevel(janela)
    edit.title("Edição da agenda")
    edit.geometry("400x200")

    frame_edit = tk.Frame(edit)
    frame_edit.place(relx=0.5,rely=0.5, anchor="center")

    container_hora = tk.Frame(frame_edit)
    container_hora.grid(row=3, column=1, columnspan=2)

    tk.Label(frame_edit, text="Dia da semana:").grid(row=0, column=0)
    dia_edit = ttk.Combobox(frame_edit, values=lista_dias, state="normal")
    dia_edit.grid(row=1, column=0)

    tk.Label(frame_edit, text="Atividade que será realizada:").grid(row=2, column=0)
    atividade = tk.Entry(frame_edit)
    atividade.grid(row=3, column=0)

    tk.Label(frame_edit, text="Hora que será realizada:").grid(row=2, column=1)
    hora = ttk.Combobox(container_hora, values=list(range(0, 24)), state="readonly", width=3)
    hora.grid(row=0, column=0)
    tk.Label(container_hora, text=":").grid(row=0, column=1)
    min = ttk.Combobox(container_hora, values=list(range(0, 60)), state="readonly", width=3)
    min.grid(row=0, column=2)

    tk.Label(container_hora, text="-").grid(row=0, column=3)

    hora2 = ttk.Combobox(container_hora, values=list(range(0, 24)), state="readonly", width=3)
    hora2.grid(row=0, column=4)
    tk.Label(container_hora, text=":").grid(row=0, column=5)
    min2 = ttk.Combobox(container_hora, values=list(range(0, 60)), state="readonly", width=3)
    min2.grid(row=0, column=6)

    def pegar_hora():
        hora_inicial = f"{hora.get().zfill(2)}:{min.get().zfill(2)}"
        hora_final = f"{hora2.get().zfill(2)}:{min2.get().zfill(2)}"
        return hora_inicial+"-"+hora_final

    tk.Button(frame_edit, text="Adicionar", command=lambda: add_item(dia_edit.get(), pegar_hora(), atividade.get())).grid(row=4, column= 0, padx=10, pady=10, sticky="nsew")
    tk.Button(frame_edit, text="Excluir", command=lambda: excluir_item(dia_edit.get(), pegar_hora(), atividade.get())).grid(row=4, column= 1, padx=10, pady=10, sticky="nsew")

atualiza_frame()

def salvar_progresso_fechar():
    try:
        salvar_progresso()
    except:
        pass
    janela.destroy()

verificar_hora_save()

tk.Button(frame_principal, text="Salvar Progesso", command=salvar_progresso).place(relx=0.9, rely=0.9, anchor="n")

janela.protocol("WM_DELETE_WINDOW", salvar_progresso_fechar)

janela.mainloop()