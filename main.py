from tkinter import *
import pyodbc

# Estabelece a conexão com o banco de dados
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=KONSSUP20\\SQLEXPRESS;'
                      'Database=Teste;'
                      'Trusted_Connection=yes;')

# criar a janela principal
root = Tk()
root.title("Lista de Tarefas")
root.geometry("500x300")
root.configure(bg="#CCCCCC")

# criar um contêiner para a Label e a Entry
frame_Tarefa = Frame(root, pady=15)
frame_Tarefa.pack(side=TOP)

# criar uma Label e uma Entry dentro do contêiner
label = Label(frame_Tarefa, text="Tarefa:")
label.pack(side=LEFT, padx=5)

entry = Entry(frame_Tarefa, width=30)
entry.pack(side=LEFT, padx=5)


def add_task():
    global conn
    task = entry.get()
    if task != "":
        # Criar a conexão com o banco de dados
        conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=KONSSUP20\\SQLEXPRESS;'
                              'Database=Teste;'
                              'Trusted_Connection=yes;')
        # Definir a query SQL para inserir os dados na tabela
        sql = "INSERT INTO Tarefa (Tarefa_ListBox, Tarefa_Completa) VALUES (?, 0)"

        # Executar a query com os dados obtidos na entrada
        cursor_2 = conn.cursor()
        cursor_2.execute(sql, (task,))
        conn.commit()
        # Fechar a conexão com o banco de dados
        conn.close()
        # Inserir a tarefa na lista
        listbox.insert(END, task)
        # Limpar a entrada
        entry.delete(0, END)


button_add = Button(frame_Tarefa, text="Adicionar", width=10, command=add_task)
button_add.pack(side=RIGHT, padx=5)


# criar um contêiner para a Label e a Lista
frame_Lista = Frame(root, pady=5)
frame_Lista.pack(side=LEFT)


# criar uma caixa de lista para exibir as tarefas e Label
label = Label(frame_Lista, text="Lista:")
label.pack(side=TOP, padx=5)

listbox = Listbox(frame_Lista, width=40)
listbox.pack(side=TOP, pady=5)

# carregar as tarefas da tabela do banco de dados na Listbox
cursor_6 = conn.cursor()
cursor_6.execute('SELECT * FROM Tarefa WHERE Tarefa_Completa = 0 OR Tarefa_Completa IS NULL;')
rows = cursor_6.fetchall()
for row in rows:
    listbox.insert(END, row[0])
cursor_6.close()


# criar um contêiner para a Label e a Lista de completa
frame_ListCompleta = Frame(root, pady=5)
frame_ListCompleta.pack(side=RIGHT)


# criar uma caixa de lista para exibir as tarefas e Label
label = Label(frame_ListCompleta, text="Completo:")
label.pack(side=TOP, padx=5)

listboxCompleta = Listbox(frame_ListCompleta, width=50)
listboxCompleta.pack(side=TOP, pady=5)

# carregar as tarefas da tabela do banco de dados na ListboxCompleta
cursor = conn.cursor()
cursor.execute('SELECT * FROM Tarefa WHERE Tarefa_Completa = 1')
rows = cursor.fetchall()
for row in rows:
    listboxCompleta.insert(END, row[0])
cursor.close()


def update_completed_tasks():
    cursor_7 = conn.cursor()
    cursor_7.execute("SELECT * FROM Tarefa WHERE Tarefa_Completa = 1, null")
    completed_tasks = cursor_7.fetchall()
    conn.commit()
    cursor_7.close()

    # Limpa a lista de tarefas completas
    listboxCompleta.delete(0, END)

    # Adiciona as tarefas completas na lista
    for task in completed_tasks:
        listboxCompleta.insert(END, task[1])


def complete_task():
    global conn
    selection = listbox.curselection()
    if selection:
        # Get the task ID and text
        task_id, task_text = listbox.get(selection[0]), listbox.get(selection[0])[0]

        # Connect to the database
        conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=KONSSUP20\\SQLEXPRESS;'
                              'Database=Teste;'
                              'Trusted_Connection=yes;')

        # Update the task status in the database
        cursor_4 = conn.cursor()
        cursor_4.execute("UPDATE Tarefa SET Tarefa_Completa = 1 WHERE Tarefa_ListBox = ?", task_id)
        conn.commit()
        cursor_4.close()

        # Remove the task from the listbox
        listbox.delete(selection)

        # Add the task to the completed task list
        listboxCompleta.insert(END, task_text)


button_complete = Button(frame_Lista, text="Completar", width=10, command=complete_task)
button_complete.pack(side=LEFT, padx=5)


def remove_task():
    global conn
    # Obter a seleção atual da listbox
    selection = listbox.curselection()

    if selection:
        # Obter o valor da linha selecionada
        task = listbox.get(selection[0])

        # Conectar ao banco de dados
        conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=KONSSUP20\\SQLEXPRESS;'
                              'Database=Teste;'
                              'Trusted_Connection=yes;')

        # Executar a query de exclusão
        cursor_3 = conn.cursor()
        cursor_3.execute('DELETE FROM Tarefa WHERE Tarefa_ListBox = ?', task)
        conn.commit()

        # Fechar a conexão com o banco de dados
        conn.close()

        # Remover a linha selecionada da listbox
        listbox.delete(selection)


button_remove = Button(frame_Lista, text="Remover", width=10, command=remove_task)
button_remove.pack(side=RIGHT, padx=5)


def return_task_completa():
    global conn
    # Obter a seleção atual da listbox
    selection = listboxCompleta.curselection()

    if selection:
        # Obter o valor da linha selecionada
        task = listboxCompleta.get(selection[0])

        # Conectar ao banco de dados
        conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=KONSSUP20\\SQLEXPRESS;'
                              'Database=Teste;'
                              'Trusted_Connection=yes;')

        # Executar a query de atualização
        cursor_5 = conn.cursor()
        cursor_5.execute('UPDATE Tarefa SET Tarefa_Completa = ? WHERE Tarefa_ListBox = ?', (0, task))
        conn.commit()

        # Fechar a conexão com o banco de dados
        conn.close()

        # Adicionar a tarefa na listbox principal
        listbox.insert(END, task)

        # Remover a linha selecionada da listbox completa
        listboxCompleta.delete(selection)


button_add = Button(frame_ListCompleta, text="Retornar", width=10, command=return_task_completa)
button_add.pack(side=RIGHT, padx=5)


root.mainloop()
