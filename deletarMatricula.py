from tkinter import *
from sqlite3 import dbapi2
from tkinter import *
from tkinter import messagebox
import sqlite3

def deletar_Matricula():
    try:
        codmat = codigo_Matricula.get()
        cx = dbapi2.connect('db3_alunos.db')
        cursor = cx.cursor() 
        cursor.execute(f'''delete from matriculas where cod_matricula = {codmat};''')
        cx.commit()          
        messagebox.showinfo('Cadastro deletado', f'Cadastro de {codmat} foi deletado com sucesso!!!')
    except sqlite3.DatabaseError as erro:        
        messagebox.showinfo('Cadastro', 'Cadastro do aluno não foi deletado')
        cx.rollback()
    finally:
        cursor.close()       
        cx.close()  

janela_deletarMatricula = Tk()
janela_deletarMatricula.title('Deletar Matrícula')
janela_deletarMatricula.geometry('250x100')
label = Label(janela_deletarMatricula, text='Informe o código da matrícula a deletar')
label.pack()
codigo_Matricula = Entry(janela_deletarMatricula)
codigo_Matricula.pack()

botao = Button(janela_deletarMatricula, text= 'Deletar Matrícula', command= deletar_Matricula)
botao.pack()

botao2 = Button(janela_deletarMatricula, text = 'Fechar', command = janela_deletarMatricula.destroy)
botao2.pack()

janela_deletarMatricula.mainloop()