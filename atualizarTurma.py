from tkinter import *
from sqlite3 import dbapi2
import sqlite3
from tkinter import *
from tkinter import messagebox

def atualizar_Turma():
    try:
        idturma = id_turma.get()
        codturma = codigo.get()
        nturma = nome.get()
        cx = dbapi2.connect('db3_alunos.db')
        cursor = cx.cursor() 
        cursor.execute('''UPDATE turmas SET codigo_turma = ?, nome_turma = ? where id = ?''', (codturma, nturma, idturma))
        cx.commit()  
        messagebox.showinfo('Cadastro Turma', f'O cadastro da turma {nturma} foi atualizado com sucesso!')
    except sqlite3.DatabaseError as erro:        
        messagebox.showinfo('Cadastro', 'Cadastro da turma não foi atualizado')
        cx.rollback()
    finally:
        cursor.close()
        cx.close()  

Janela_atualizarTurma = Tk()
Janela_atualizarTurma.title('Atualizar dados de Turma')
Janela_atualizarTurma.geometry('400x200')

label = Label(Janela_atualizarTurma, text='Informe o ID da turma')
label.pack()
id_turma = Entry(Janela_atualizarTurma)
id_turma.pack()

label2 = Label(Janela_atualizarTurma, text='Informe o novo código da turma')
label2.pack()
codigo = Entry(Janela_atualizarTurma)
codigo.pack()

label3 = Label(Janela_atualizarTurma, text='Informe o novo nome da turma')
label3.pack()
nome = Entry(Janela_atualizarTurma)
nome.pack()

botao = Button(Janela_atualizarTurma, text= 'Atualizar Turma', command= atualizar_Turma)
botao.pack()

botao2 = Button(Janela_atualizarTurma, text = 'Fechar', command = Janela_atualizarTurma.destroy)
botao2.pack()

Janela_atualizarTurma.mainloop()