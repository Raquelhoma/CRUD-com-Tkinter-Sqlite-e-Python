from tkinter import *
from sqlite3 import dbapi2
import sqlite3
from tkinter import messagebox
from tkinter import ttk

def lerListaMatriculas():
    try:
        cx = dbapi2.connect('db3_alunos.db')
        cursor = cx.cursor() 
        dados_Alunos = cursor.execute('select * from matriculas;')
        rows = dados_Alunos.fetchall()
        for row in rows:
            tree.insert('', END, values = row)
    finally:
        cursor.close()
        cx.close()

janela_listarMatricula = Tk()
janela_listarMatricula.title('Lista das Matrículas realizadas - Universidade da Felicidade')
tree = ttk.Treeview(janela_listarMatricula, column=('c1', 'c2', 'c3', 'c4','c5'), show ='headings')  
tree.column('#1')
tree.heading('#1', text = 'Código Matrícula')
tree.column('#2')
tree.heading('#2', text = 'Código do Aluno')
tree.column('#3')
tree.heading('#3', text = 'Código da Turma')
tree.column('#4')
tree.heading('#4', text = 'Ano')
tree.column('#5')
tree.heading('#5', text = 'Período')

tree.pack()

button = Button(janela_listarMatricula, text ='Ver lista de Matrículas', command = lerListaMatriculas)
button.pack()
button1 = Button(janela_listarMatricula, text='Fechar', command= janela_listarMatricula.destroy).pack()
janela_listarMatricula.mainloop()
