from tkinter import *
from sqlite3 import dbapi2
import sqlite3
from tkinter import *
from tkinter import messagebox

def matricular_Aluno():
    try:
        codigoMat = codigo_matricula.get()
        alunoMat = id_aluno.get()
        turmaMat = id_Turma.get()
        anoMat = ano.get()
        periodoMat = periodo.get()
        cx = dbapi2.connect('db3_alunos.db')
        cursor = cx.cursor() 
        cursor.execute('''insert into matriculas (cod_matricula, id_aluno, id_turma, ano, periodo) values (?,?,?,?,?)''',
    (codigoMat, alunoMat, turmaMat, anoMat, periodoMat))
        cx.commit()  
        messagebox.showinfo('Cadastro', f'A matrícula {alunoMat} foi realizado com sucesso na Turma {turmaMat}!')
    except sqlite3.DatabaseError as erro:        
        messagebox.showinfo('Cadastro', 'A matrícula do aluno não foi realizada')
        cx.rollback()
    finally:
        cursor.close()
        cx.close()     
  
janela_cadastrarMatricula = Tk()
janela_cadastrarMatricula.title('Matricular Aluno - Universidade da Felicidade')
janela_cadastrarMatricula.geometry('500x300')

label1 = Label(janela_cadastrarMatricula, text= 'Informe o código de matrícula do aluno')
label1.grid(row=0, column=0)
codigo_matricula = Entry(janela_cadastrarMatricula)
codigo_matricula.grid(row= 1, column=0)

label2 = Label(janela_cadastrarMatricula, text= 'Informe ID do aluno')
label2.grid(row= 2, column=0) 
id_aluno = Entry(janela_cadastrarMatricula)
id_aluno.grid(row= 3, column=0)

label3 = Label(janela_cadastrarMatricula, text= 'Informe ID da Turma')
label3.grid(row= 4, column=0)
id_Turma = Entry(janela_cadastrarMatricula)
id_Turma.grid(row= 5, column=0)    

label4 = Label(janela_cadastrarMatricula, text= 'Informe o ano')
label4.grid(row= 6, column=0)
ano = Entry(janela_cadastrarMatricula)
ano.grid(row= 7, column=0)

label5 = Label(janela_cadastrarMatricula, text= 'Informe o período M, T ou N')
label5.grid(row= 8, column=0)
periodo = Entry(janela_cadastrarMatricula)
periodo.grid(row= 9, column=0)

botao = Button(janela_cadastrarMatricula, text= 'Matricular Aluno', command= matricular_Aluno)
botao.grid(row= 10, column=1)

botao2 = Button(janela_cadastrarMatricula, text = 'Fechar', command = janela_cadastrarMatricula.destroy)
botao2.grid(row=11, column=1)

janela_cadastrarMatricula.mainloop()