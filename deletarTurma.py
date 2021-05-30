from tkinter import *
from sqlite3 import dbapi2
from tkinter import *
from tkinter import messagebox
import sqlite3

def deletar_Turma():
    try:
        nid = numero_id.get()
        cx = dbapi2.connect('db3_alunos.db')
        cursor = cx.cursor() 
        cursor.execute(f'''delete from turmas where id = {nid};''')
        cx.commit()          
        messagebox.showinfo('Cadastro deletado', f'Cadastro de {nid} foi deletado com sucesso!!!')
    except sqlite3.DatabaseError as erro:        
        messagebox.showinfo('Cadastro', 'Cadastro do aluno não foi deletado')
        cx.rollback()
    finally:
        cursor.close()       
        cx.close()  

janela_deletarTurma = Tk()
janela_deletarTurma.title('Deletar Turma')
janela_deletarTurma.geometry('250x100')
label = Label(janela_deletarTurma, text='Informe o ID da Turma a deletar')
label.pack()
numero_id = Entry(janela_deletarTurma)
numero_id.pack()

botao = Button(janela_deletarTurma, text= 'Deletar Turma', command= deletar_Turma)
botao.pack()

botao2 = Button(janela_deletarTurma, text = 'Fechar', command = janela_deletarTurma.destroy)
botao2.pack()

janela_deletarTurma.mainloop()