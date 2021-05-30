from tkinter import *
from sqlite3 import dbapi2
import sqlite3
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

def lerListaAlunos():
    try:
        cx = dbapi2.connect('db3_alunos.db')
        cursor = cx.cursor() 
        dados_Alunos = cursor.execute('select * from alunos;')
        rows = dados_Alunos.fetchall()
        for row in rows:
            print(row)
            tree.insert('', END, values = row)
    finally:
        cursor.close()
        cx.close()

janela_listar = Tk()
janela_listar.title('Lista dos Alunos Matriculados - Universidade da Felicidade')
tree = ttk.Treeview(janela_listar, column=('c1', 'c2', 'c3', 'c4'), show ='headings')  
tree.column('#1')
tree.heading('#1', text = 'Número Matricula')
tree.column('#2')
tree.heading('#2', text = 'Nome Aluno')
tree.column('#3')
tree.heading('#3', text = 'Data de Nascimento')
tree.column('#4')
tree.heading('#4', text = 'Sexo')

tree.pack()

button = Button(janela_listar, text ='Ver lista alunos', command = lerListaAlunos)
button.pack()
button1 = Button(janela_listar, text='Fechar', command= janela_listar.destroy).pack()
janela_listar.mainloop()

