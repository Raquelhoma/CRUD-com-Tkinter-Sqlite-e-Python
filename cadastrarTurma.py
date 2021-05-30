from tkinter import *
from sqlite3 import dbapi2
import sqlite3
from tkinter import *
from tkinter import messagebox

def criar_Turma():
    try:
        idturma = id_turma.get()
        codturma = codigo.get()
        nturma = nome.get()
        cx = dbapi2.connect('db3_alunos.db')
        cursor = cx.cursor() 
        cursor.execute('''insert into turmas (id, codigo_turma, nome_turma) values (?,?,?)''',(idturma, codturma, nturma))
        cx.commit()  
        messagebox.showinfo('Cadastro Turma', f'O cadastro da turma {nturma} foi realizado com sucesso!')
    except sqlite3.DatabaseError as erro:        
        messagebox.showinfo('Cadastro', 'Cadastro da turma não foi realizado')
        cx.rollback()
    finally:
        cursor.close()
        cx.close()  


Janela_criarTurma = Tk()
Janela_criarTurma.title('Criar Nova Turma')
Janela_criarTurma.geometry('400x200')

label = Label(Janela_criarTurma, text='Informe o ID da turma')
label.pack()
id_turma = Entry(Janela_criarTurma)
id_turma.pack()

label2 = Label(Janela_criarTurma, text='Informe o código da turma')
label2.pack()
codigo = Entry(Janela_criarTurma)
codigo.pack()

label3 = Label(Janela_criarTurma, text='Informe o nome da turma')
label3.pack()
nome = Entry(Janela_criarTurma)
nome.pack()

botao = Button(Janela_criarTurma, text= 'Criar Nova Turma', command= criar_Turma)
botao.pack()

botao2 = Button(Janela_criarTurma, text = 'Fechar', command = Janela_criarTurma.destroy)
botao2.pack()

Janela_criarTurma.mainloop()


