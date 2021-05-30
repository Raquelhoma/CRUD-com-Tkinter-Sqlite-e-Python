from tkinter import *
from sqlite3 import dbapi2
import sqlite3
from tkinter import *
from tkinter import messagebox


def atualizarAluno():
    try:
        nid = numero_id.get()
        naluno = nome_aluno.get()
        dnasc = data_nascimento.get()
        saluno = sexo_aluno.get()
        cx = dbapi2.connect('db3_alunos.db')
        cursor = cx.cursor() 
        cursor.execute('''UPDATE alunos SET nome = ?, nascimento = ?, sexo = ? where id = ?''',  (naluno, dnasc, saluno, nid))
        cx.commit()  
        messagebox.showinfo('Atualizar Cadastro', f'O cadastro do(a) aluno(a) {naluno} foi atualizado com sucesso!')
    except sqlite3.DatabaseError as erro:        
        messagebox.showinfo('Cadastro', 'Cadastro do aluno não foi atualizado')
        cx.rollback()
    finally:
        cursor.close()
        cx.close()


janela_atualizar = Tk()
janela_atualizar.title('Cadastro de Novos Alunos - Universidade da Felicidade')
janela_atualizar.geometry('500x300')
label1 = Label(janela_atualizar, text= 'Informe o número do aluno para retificar')
label1.grid(row=0, column=0)
numero_id = Entry(janela_atualizar)
numero_id.grid(row= 1, column=0)
label2 = Label(janela_atualizar, text= 'Informe o novo nome do aluno')
nome_aluno = Entry(janela_atualizar)
label2.grid(row= 2, column=0) 
nome_aluno.grid(row= 3, column=0)

label3 = Label(janela_atualizar, text= 'Informe a nova data de nascimento dd/mm/aaaa')
label3.grid(row= 4, column=0)
data_nascimento = Entry(janela_atualizar)
data_nascimento.grid(row= 5, column=0)    

label4 = Label(janela_atualizar, text= 'Informe o novo sexo do aluno)')
label4.grid(row= 6, column=0)
sexo_aluno = Entry(janela_atualizar)
sexo_aluno.grid(row= 7, column=0)

botao = Button(janela_atualizar, text= 'Atualizar Aluno', command= atualizarAluno)
botao.grid(row= 8, column=1)

botao2 = Button(janela_atualizar, text = 'Fechar', command = janela_atualizar.destroy)
botao2.grid(row=9, column=1)

janela_atualizar.mainloop()