from tkinter import *

# Lista para armazenar as tarefas
lista_tarefas = []

# Criar a janela principal
root = Tk()
root.title("Lista de Tarefas")
root.geometry("500x300")
root.configure(bg="#CCCCCC")

# Criar um contêiner para a Label e a Entry
frame_Tarefa = Frame(root, pady=15)
frame_Tarefa.pack(side=TOP)

# Criar uma Label e uma Entry dentro do contêiner
label = Label(frame_Tarefa, text="Tarefa:")
label.pack(side=LEFT, padx=5)

entry = Entry(frame_Tarefa, width=30)
entry.pack(side=LEFT, padx=5)

# Função para adicionar uma tarefa à lista


def add_task():
    task = entry.get()
    if task != "":
        lista_tarefas.append(task)
        listbox.insert(END, task)
        entry.delete(0, END)

# Função para completar uma tarefa


def complete_task():
    selection = listbox.curselection()
    if selection:
        task_index = selection[0]
        task_text = listbox.get(task_index)
        lista_tarefas.remove(task_text)
        listbox.delete(task_index)
        listboxCompleta.insert(END, task_text)


# Função para retornar uma tarefa completa
def return_task_completa():
    selection = listboxCompleta.curselection()
    if selection:
        task_index = selection[0]
        task_text = listboxCompleta.get(task_index)
        lista_tarefas.append(task_text)
        listboxCompleta.delete(task_index)
        listbox.insert(END, task_text)


# Criar um contêiner para a Label e a Lista
frame_Lista = Frame(root, pady=5)
frame_Lista.pack(side=LEFT)

# Criar uma caixa de lista para exibir as tarefas e Label
label = Label(frame_Lista, text="Lista:")
label.pack(side=TOP, padx=5)

listbox = Listbox(frame_Lista, width=40)
listbox.pack(side=TOP, pady=5)

# Criar um contêiner para a Label e a Lista de completa
frame_ListCompleta = Frame(root, pady=5)
frame_ListCompleta.pack(side=RIGHT)

# Criar uma caixa de lista para exibir as tarefas completas e Label
label = Label(frame_ListCompleta, text="Completo:")
label.pack(side=TOP, padx=5)

listboxCompleta = Listbox(frame_ListCompleta, width=50)
listboxCompleta.pack(side=TOP, pady=5)

# Criar botões para adicionar, completar e retornar tarefas
button_add = Button(frame_Tarefa, text="Adicionar", width=10, command=add_task)
button_add.pack(side=RIGHT, padx=5)

button_complete = Button(frame_Lista, text="Completar", width=10, command=complete_task)
button_complete.pack(side=LEFT, padx=5)

# button_remove = Button(frame_Lista, text="Remover", width=10, command=remove_task)
# button_remove.pack(side=RIGHT, padx=5)

button_return = Button(frame_ListCompleta, text="Retornar", width=10, command=return_task_completa)
button_return.pack(side=RIGHT, padx=5)

root.mainloop()
